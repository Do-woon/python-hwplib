import zlib

def decompress_stream(data: bytes) -> bytes:
    return zlib.decompress(data, wbits=-15)