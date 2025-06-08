from dataclasses import dataclass


@dataclass
class RecordHeader:
    tag_id: int
    level: int
    size: int
    has_extended_size: bool


@dataclass
class Record:
    header: RecordHeader
    data: bytes
