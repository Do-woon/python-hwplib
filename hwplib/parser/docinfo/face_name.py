from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.face_name import (FaceName, FaceNameProperty,
                                             FontTypeInfo, SubstituteFontType)
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.binary import BinaryReader


@RecordParserRegistry.register(RecordTag.FACE_NAME)
def parse_face_name(reader: BinaryReader) -> FaceName:
    # 1. 속성
    prop_raw = reader.read_uint8()
    prop = FaceNameProperty.from_value(prop_raw)

    # 2. 글꼴 이름
    len1 = reader.read_uint16()
    name = reader.read_string(len1)

    # 3~4. 대체 글꼴 유형 및 이름 (조건부)
    substitute_font_type = None
    substitute_font_name = None
    if prop.has_substitute_font:
        sub_type_val = reader.read_uint8()
        substitute_font_type = SubstituteFontType(sub_type_val)

        len2 = reader.read_uint16()
        substitute_font_name = reader.read_string(len2)

    # 5. 글꼴 유형 정보 (조건부)
    font_type_info = None
    if prop.has_font_type_info:
        raw = reader.read_bytes(10)
        value = int.from_bytes(raw, byteorder='little')
        font_type_info = FontTypeInfo.from_value(value)

    # 6. 기본 글꼴 이름 (조건부)
    base_font_name = None
    if prop.has_base_font:
        len3 = reader.read_uint16()
        base_font_name = reader.read_string(len3)

    return FaceName(property=prop,
                    name=name,
                    substitute_font_type=substitute_font_type,
                    substitute_font_name=substitute_font_name,
                    font_type_info=font_type_info,
                    base_font_name=base_font_name)
