from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.para_shape import (ParaShape, ParaShapeProperty1,
                                              ParaShapeProperty2,
                                              ParaShapeProperty3)
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.binary import BinaryReader


@RecordParserRegistry.register(RecordTag.PARA_SHAPE)
def parse_para_shape(reader: BinaryReader) -> ParaShape:
    property1 = ParaShapeProperty1.from_value(reader.read_uint32())

    left_margin = reader.read_int32()
    right_margin = reader.read_int32()
    indent = reader.read_int32()
    top_para_space = reader.read_int32()
    bottom_para_space = reader.read_int32()
    line_space_old = reader.read_int32()

    tab_definition_id = reader.read_uint16()
    numbering_bullet_id = reader.read_uint16()
    border_fill_id = reader.read_uint16()

    left_border_space = reader.read_int16()
    right_border_space = reader.read_int16()
    top_border_space = reader.read_int16()
    bottom_border_space = reader.read_int16()

    # property2 (4 bytes)
    # TODO (dukim): Branch this logic using version check.
    property2 = (
        ParaShapeProperty2.from_value(reader.read_uint32())
        if reader.remaining_bytes() >= 4
        else None
    )

    # property3 (4 bytes) + line_spacing (4 bytes)
    # TODO (dukim): Branch this logic using version check.
    property3 = None
    line_spacing = None
    if reader.remaining_bytes() >= 8:
        property3 = ParaShapeProperty3.from_value(reader.read_uint32())
        line_spacing = reader.read_uint32()

    return ParaShape(
        property1=property1,
        left_margin=left_margin,
        right_margin=right_margin,
        indent=indent,
        top_para_space=top_para_space,
        bottom_para_space=bottom_para_space,
        line_space_old=line_space_old,
        tab_definition_id=tab_definition_id,
        numbering_bullet_id=numbering_bullet_id,
        border_fill_id=border_fill_id,
        left_border_space=left_border_space,
        right_border_space=right_border_space,
        top_border_space=top_border_space,
        bottom_border_space=bottom_border_space,
        property2=property2,
        property3=property3,
        line_spacing=line_spacing,
    )
