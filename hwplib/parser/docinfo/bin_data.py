from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.bin_data import BinData, BinDataProperty
from hwplib.models.docinfo.enum import BinDataType
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.binary import BinaryReader


@RecordParserRegistry.register(RecordTag.BIN_DATA)
def parse_bin_data(reader: BinaryReader) -> BinData:
    property_raw = reader.read_uint16()
    prop = BinDataProperty.from_value(property_raw)

    bin_data = BinData(property=prop)

    if prop.type == BinDataType.LINK:
        len1 = reader.read_uint16()
        bin_data.absolute_path = reader.read_string(len1)

        len2 = reader.read_uint16()
        bin_data.relative_path = reader.read_string(len2)

    elif prop.type in (BinDataType.EMBEDDING, BinDataType.STORAGE):
        bin_data.storage_id = reader.read_uint16()

        if prop.type == BinDataType.EMBEDDING:
            len3 = reader.read_uint16()
            bin_data.extension = reader.read_string(len3)

    return bin_data
