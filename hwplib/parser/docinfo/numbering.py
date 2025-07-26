from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.numbering import (
    LevelNumbering,
    Numbering,
    ParagraphHeadInfo,
    ParagraphHeadProperty,
)
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.binary import BinaryReader


@RecordParserRegistry.register(RecordTag.NUMBERING)
def parse_numbering(reader: BinaryReader) -> Numbering:
    levels = []

    # 기본 7 levels.
    for _ in range(7):
        # ParagraphHeadInfo (12 bytes)
        prop_raw = reader.read_uint32()
        width_adjustment = reader.read_uint16()
        distance_from_body = reader.read_uint16()
        char_shape_id = reader.read_uint32()
        if char_shape_id == 0xFFFFFFFF:
            char_shape_id = None

        prop = ParagraphHeadProperty.from_value(prop_raw)
        para_head = ParagraphHeadInfo(
            property=prop,
            width_adjustment=width_adjustment,
            distance_from_body=distance_from_body,
            char_shape_id=char_shape_id,
        )

        # Format 문자열
        fmt_len = reader.read_uint16()
        fmt = reader.read_string(fmt_len)

        levels.append(LevelNumbering(paragraph_head_info=para_head, number_format=fmt))

    # 기본 시작 번호
    base_start_number = reader.read_uint16()

    # level 1~7 개별 시작 번호 (5.0.2.5 이상)
    level_start_numbers = []
    # TODO (dukim): Branch this logic using version check.
    if reader.remaining_bytes() >= 4 * 7:
        for i in range(7):
            start = reader.read_uint32()
            level_start_numbers.append(start)
            levels[i].start_number = start

    # 확장 레벨 8~10 (5.1.0.0 이상)
    # TODO (dukim): Branch this logic using version check.
    while reader.remaining_bytes() >= 12 + 2:
        prop_raw = reader.read_uint32()
        width_adjustment = reader.read_uint16()
        distance_from_body = reader.read_uint16()
        char_shape_id = reader.read_uint32()
        if char_shape_id == 0xFFFFFFFF:
            char_shape_id = None

        prop = ParagraphHeadProperty.from_value(prop_raw)
        para_head = ParagraphHeadInfo(
            property=prop,
            width_adjustment=width_adjustment,
            distance_from_body=distance_from_body,
            char_shape_id=char_shape_id,
        )

        fmt_len = reader.read_uint16()
        fmt = reader.read_string(fmt_len)

        levels.append(LevelNumbering(paragraph_head_info=para_head, number_format=fmt))

    # 확장 시작 번호 8~10
    if reader.remaining_bytes() >= 4 * 3:
        for i in range(7, 10):
            start = reader.read_uint32()
            levels[i].start_number = start

    return Numbering(base_start_number=base_start_number, levels=levels)
