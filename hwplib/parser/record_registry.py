from typing import Callable, Optional

from hwplib.models.common.enum import RecordTag
from hwplib.models.common.record import Record


class RecordParserRegistry:
    _registry: dict[int, Callable[[bytes], object]] = {}

    @classmethod
    def register(cls, tag_id: int | RecordTag):
        """Decorator to register a record parser for a specific
        tag_id."""

        def wrapper(func: Callable[[bytes], object]):
            cls._registry[int(tag_id)] = func
            return func

        return wrapper

    @classmethod
    def parse(cls, record: Record) -> Optional[object]:
        """If a parser is registered for the record's tag_id,
        call it with the record's data."""
        parser = cls._registry.get(record.header.tag_id)
        if not parser:
            return None  # Fallback to None if no parser is found.

        from hwplib.utils.binary import BinaryReader
        reader = BinaryReader(record.data)

        result = parser(reader)

        if not reader.eof():
            raise ValueError(
                f"Parser for tag_id {record.header.tag_id} did not consume all data: "
                f"{reader.tell()} / {len(record.data)} bytes read")

        return result
