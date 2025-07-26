import struct


class BinaryReader:

    def __init__(self, data: bytes):
        self.data = data
        self.offset = 0

    def __len__(self):
        return len(self.data)

    def read_uint8(self):
        (val,) = struct.unpack_from("<B", self.data, self.offset)
        self.offset += 1
        return val

    def read_int8(self):
        (val,) = struct.unpack_from("<b", self.data, self.offset)
        self.offset += 1
        return val

    def read_uint16(self):
        (val,) = struct.unpack_from("<H", self.data, self.offset)
        self.offset += 2
        return val

    def read_int16(self):
        (val,) = struct.unpack_from("<h", self.data, self.offset)
        self.offset += 2
        return val

    def read_uint32(self):
        (val,) = struct.unpack_from("<I", self.data, self.offset)
        self.offset += 4
        return val

    def read_int32(self):
        (val,) = struct.unpack_from("<i", self.data, self.offset)
        self.offset += 4
        return val

    def read_bytes(self, length):
        val = self.data[self.offset : self.offset + length]
        self.offset += length
        return val

    def read_string(self, str_length):
        raw = self.read_bytes(str_length * 2)  # Read bytes for UTF-16LE.
        return raw.decode("utf-16le", errors="ignore").rstrip("\x00")

    def skip(self, length):
        self.offset += length

    def seek(self, offset):
        self.offset = offset

    def tell(self):
        return self.offset

    def remaining_bytes(self):
        return self.__len__() - self.offset

    def eof(self) -> bool:
        return self.offset >= len(self.data)
