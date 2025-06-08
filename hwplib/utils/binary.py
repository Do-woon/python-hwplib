import struct

class BinaryReader:
    def __init__(self, data: bytes):
        self.data = data
        self.offset = 0

    def read_uint8(self):
        val = self.data[self.offset]
        self.offset += 1
        return val

    def read_uint16(self):
        val, = struct.unpack_from('<H', self.data, self.offset)
        self.offset += 2
        return val

    def read_uint32(self):
        val, = struct.unpack_from('<I', self.data, self.offset)
        self.offset += 4
        return val

    def read_bytes(self, length):
        val = self.data[self.offset:self.offset+length]
        self.offset += length
        return val

    def read_string(self, length):
        raw = self.read_bytes(length)
        return raw.decode('utf-16le', errors='ignore').rstrip('\x00')

    def seek(self, offset):
        self.offset = offset

    def tell(self):
        return self.offset

    def eof(self) -> bool:
        return self.offset >= len(self.data)