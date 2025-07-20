from hwplib.models.common.colorref import ColorRef
from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.char_shape import CharShape, CharShapeProperty
from hwplib.models.docinfo.id_mappings import FaceNameType
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.binary import BinaryReader


def map_by_lang(values: list[int]) -> dict[FaceNameType, int]:
    return {lang: values[i] for i, lang in enumerate(FaceNameType)}


@RecordParserRegistry.register(RecordTag.CHAR_SHAPE)
def parse_char_shape(reader: BinaryReader) -> CharShape:
    # 언어별 글꼴 ID, 장평, 자간, 상대 크기, 글자 위치
    font_ids_raw = [reader.read_uint16() for _ in range(7)]
    font_ids = map_by_lang(font_ids_raw)

    ratios_raw = [reader.read_uint8() for _ in range(7)]
    ratios = map_by_lang(ratios_raw)

    char_spacings_raw = [reader.read_int8() for _ in range(7)]
    char_spacings = map_by_lang(char_spacings_raw)

    relative_sizes_raw = [reader.read_uint8() for _ in range(7)]
    relative_sizes = map_by_lang(relative_sizes_raw)

    char_positions_raw = [reader.read_int8() for _ in range(7)]
    char_positions = map_by_lang(char_positions_raw)

    # 기준 크기
    base_size = reader.read_int32()

    # 속성 비트필드
    prop_raw = reader.read_uint32()
    prop = CharShapeProperty.from_value(prop_raw)

    # 그림자 간격 X, Y
    shadow_gap_x = reader.read_int8()
    shadow_gap_y = reader.read_int8()

    # 글자/밑줄/음영/그림자 색상
    text_color = ColorRef.from_uint32(reader.read_uint32())
    underline_color = ColorRef.from_uint32(reader.read_uint32())
    shade_color = ColorRef.from_uint32(reader.read_uint32())
    shadow_color = ColorRef.from_uint32(reader.read_uint32())

    # 테두리/배경 ID
    border_fill_id = reader.read_uint16()

    # 취소선 색상
    strikeout_color = ColorRef.from_uint32(reader.read_uint32())

    return CharShape(
        font_ids=font_ids,
        ratios=ratios,
        char_spacings=char_spacings,
        relative_sizes=relative_sizes,
        char_positions=char_positions,
        base_size=base_size,
        property=prop,
        shadow_gap_x=shadow_gap_x,
        shadow_gap_y=shadow_gap_y,
        text_color=text_color,
        underline_color=underline_color,
        shade_color=shade_color,
        shadow_color=shadow_color,
        border_fill_id=border_fill_id,
        strikeout_color=strikeout_color,
    )
