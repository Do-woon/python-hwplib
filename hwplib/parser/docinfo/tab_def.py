from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.border_fill import BorderType
from hwplib.models.docinfo.tab_def import (TabDef, TabDefProperty, TabInfo,
                                           TabType)
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.binary import BinaryReader


@RecordParserRegistry.register(RecordTag.TAB_DEF)
def parse_tab_def(reader: BinaryReader) -> TabDef:
    prop_raw = reader.read_uint32()
    prop = TabDefProperty.from_value(prop_raw)

    # Assigned 4 bytes but uses only 2 bytes.
    tab_count = reader.read_int16()
    reader.skip(2)

    # Read tab infos of length `tab_count`.
    tab_infos = []
    for _ in range(tab_count):
        position = reader.read_uint32()
        tab_type = TabType(reader.read_uint8())
        fill_type = BorderType(reader.read_uint8())
        reader.skip(2)  # reserved 2 bytes.

        tab_infos.append(
            TabInfo(position=position, tap_type=tab_type, fill_type=fill_type)
        )

    return TabDef(property=prop, tab_infos=tab_infos)
