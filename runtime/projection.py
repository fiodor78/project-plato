from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ProjectionError(Exception):
    message: str

    def __str__(self) -> str:
        return self.message


def project_entity(entity: dict[str, Any], config: dict[str, Any]) -> dict[str, Any] | None:
    """Return only model-visible allow-listed fields for one raw entity."""
    entity_type = entity.get("entity_type")
    rule = config.get("entity_rules", {}).get(entity_type)
    if not rule:
        return None

    required_visibility = rule["required_visibility"]
    if entity.get("runtime_visibility") != required_visibility:
        return None

    return {key: entity[key] for key in rule["model_fields"] if key in entity}


def _visible_title(work: dict[str, Any]) -> str | None:
    titles = work.get("titles") or {}
    return (
        titles.get("original")
        or titles.get("english")
        or titles.get("polish")
        or titles.get("latin")
    )


def build_corpus_model_payload(
    corpus_objects: list[dict[str, Any]],
    config: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Build the only corpus representation that may be serialized into model context.

    Raw identifiers are used internally for joins, then intentionally discarded.
    Source-edition and CUSTODIAN-only entities are never model payloads.
    """
    works = {
        x["work_id"]: x
        for x in corpus_objects
        if x.get("entity_type") == "work"
    }
    segments = {
        x["segment_id"]: x
        for x in corpus_objects
        if x.get("entity_type") == "segment"
    }
    speakers: dict[str, list[dict[str, Any]]] = {}
    for x in corpus_objects:
        if x.get("entity_type") == "speaker_assertion":
            speakers.setdefault(x["segment_id"], []).append(x)

    payload: list[dict[str, Any]] = []

    for raw_text in corpus_objects:
        if raw_text.get("entity_type") not in {"textual_witness", "translation"}:
            continue

        text_view = project_entity(raw_text, config)
        if text_view is None:
            continue

        segment = segments.get(raw_text.get("segment_id"))
        if segment is None:
            raise ProjectionError("Visible text has no registered logical segment.")

        segment_view = project_entity(segment, config)
        if segment_view is None:
            raise ProjectionError("Visible text points to a segment not visible to the thinker.")

        work = works.get(segment.get("work_id"))
        if work is None:
            raise ProjectionError("Visible segment has no registered work.")

        work_view = project_entity(work, config)
        if work_view is None:
            raise ProjectionError("Visible segment points to a work not visible to the thinker.")

        speaker_view = None
        for speaker in speakers.get(segment["segment_id"], []):
            speaker_view = project_entity(speaker, config)
            if speaker_view is not None:
                break

        item: dict[str, Any] = {
            "kind": "original_text" if raw_text["entity_type"] == "textual_witness" else "translation",
            "work_title": _visible_title(work_view),
            "locator": segment_view.get("locator"),
            "end_locator": segment_view.get("end_locator"),
            "language": text_view.get("language"),
            "text": text_view.get("text"),
        }

        if speaker_view:
            item["speaker"] = {
                "label": speaker_view.get("speaker_label"),
                "status": speaker_view.get("assertion_status"),
            }

        payload.append(item)

    return payload
