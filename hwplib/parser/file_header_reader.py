from hwplib.models.file_header import FileHeader
from hwplib.models.file_header.bitfield import (FileHeaderAdditionalProperties,
                                                FileHeaderProperties)
from hwplib.models.file_header.enum import EncryptVersion, KoglCountry
from hwplib.utils.binary import BinaryReader


def parse_file_header(data: bytes) -> FileHeader:
    reader = BinaryReader(data)

    signature = reader.read_bytes(32).rstrip(b'\x00').decode('ascii',
                                                             errors='ignore')
    version_raw = reader.read_uint32()
    properties_raw = reader.read_uint32()
    additional_raw = reader.read_uint32()
    encrypt_ver = EncryptVersion(reader.read_uint32())
    kogl_country = KoglCountry(reader.read_uint8())
    reader.read_bytes(207)  # Reserved

    # Check if the signature matches the expected value.
    if signature != "HWP Document File":
        raise ValueError(f"Invalid HWP file signature: {signature}")

    # Check whether the reader is at the end of the header.
    if not reader.eof():
        raise ValueError("Extra data found after FileHeader parsing.")

    return FileHeader(
        signature=signature,
        version_raw=version_raw,
        properties=FileHeaderProperties.from_value(properties_raw),
        additional_properties=FileHeaderAdditionalProperties.from_value(
            additional_raw),
        encrypt_version=encrypt_ver,
        kogl_country=kogl_country)
