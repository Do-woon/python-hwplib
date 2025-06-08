from .binary import BinaryReader
from ..models.common.record import Record, RecordHeader


class RecordReader:

    def __init__(self, data: bytes):
        self.reader = BinaryReader(data)
        self.records: list[Record] = []

    def read_next(self) -> Record | None:
        if self.reader.eof():
            return None

        header_value = self.reader.read_uint32()
        tag_id = header_value & 0x3FF  # 10 bits for tag ID
        level = (header_value >> 10) & 0x3FF  # 10 bits for level
        size = (header_value >> 20) & 0xFFF  # 12 bits for size
        has_ext = (size == 0xFFF)  # Check if size is extended

        if has_ext:
            size = self.reader.read_uint32()

        data = self.reader.read_bytes(size)
        header = RecordHeader(tag_id, level, size, has_ext)
        return Record(header, data)

    def read_all(self) -> list[Record]:
        while not self.reader.eof():
            rec = self.read_next()
            if rec:
                self.records.append(rec)
        return self.records
