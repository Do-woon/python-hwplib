from hwplib.models.common.colorref import ColorRef
from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.border_fill import (
    BorderDirection, BorderFill, BorderFillProperty, BorderThickness,
    BorderType, DiagonalLineType, FillInfo, FillPatternType, FillTypeFlag,
    GradationType, GradientFill, ImageEffect, ImageFill, ImageFillInfo,
    ImageFillType, PatternFill)
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.binary import BinaryReader


@RecordParserRegistry.register(RecordTag.BORDER_FILL)
def parse_border_fill(reader: BinaryReader) -> BorderFill:
    # 1. 속성 비트 필드
    prop_raw = reader.read_uint16()
    prop = BorderFillProperty.from_value(prop_raw)

    # 2. 선 종류/굵기/색상
    border_types = {}
    border_thicknesses = {}
    border_colors = {}
    for dir in BorderDirection:
        border_types[dir] = BorderType(reader.read_uint8())
        border_thicknesses[dir] = BorderThickness(reader.read_uint8())
        border_colors[dir] = ColorRef.from_uint32(reader.read_uint32())

    # 3. 대각선 종류 및 굵기
    diagonal_type = DiagonalLineType(reader.read_uint8())
    diagonal_thickness = BorderThickness(reader.read_uint8())
    diagonal_color = ColorRef.from_uint32(reader.read_uint32())

    # 4. FillInfo
    type_value = reader.read_uint32()
    fill_type = FillTypeFlag(type_value)

    # Pattern Fill
    pattern = None
    if fill_type & FillTypeFlag.PATTERN:
        background_color = ColorRef.from_uint32(reader.read_uint32())
        pattern_color = ColorRef.from_uint32(reader.read_uint32())
        pattern_type = FillPatternType(reader.read_int32())
        pattern = PatternFill(background_color=background_color,
                              pattern_color=pattern_color,
                              pattern_type=pattern_type)

    # Image Fill
    image = None
    if fill_type & FillTypeFlag.IMAGE:
        image_fill_type = ImageFillType(reader.read_uint8())
        brightness = reader.read_int8()
        contrast = reader.read_int8()
        effect = ImageEffect(reader.read_uint8())
        bin_data_id = reader.read_uint16()
        image_info = ImageFillInfo(brightness=brightness,
                                   contrast=contrast,
                                   effect=effect,
                                   bin_data_id=bin_data_id)
        image = ImageFill(fill_type=image_fill_type, info=image_info)

    # Gradient Fill
    gradient = None
    if fill_type & FillTypeFlag.GRADATION:
        gradation_type = GradationType(reader.read_int8())
        angle = reader.read_int32()
        center_x = reader.read_int32()
        center_y = reader.read_int32()
        blur = reader.read_int32()

        color_count = reader.read_int32()
        if color_count > 2:
            positions = [reader.read_int32() for _ in range(color_count)]
        else:
            positions = []
        colors = [
            ColorRef.from_uint32(reader.read_uint32())
            for _ in range(color_count)
        ]

        gradation_center = None
        extra_size = reader.read_uint32()
        if extra_size == 1:
            gradation_center = reader.read_uint8()
        else:
            assert extra_size == 0, "Extra size should be either 0 or 1" \
                " for gradient fill."

        gradient = GradientFill(gradation_type=gradation_type,
                                angle=angle,
                                center_x=center_x,
                                center_y=center_y,
                                blur=blur,
                                gradation_center=gradation_center,
                                positions=positions,
                                colors=colors)
    else:
        extra_size = reader.read_uint32()
        # 추가 채우기 속성 (명세에서는 확인할 수 없음)
        for _ in range(extra_size):
            reader.read_uint8()  # Drop all data

    fill_info = FillInfo(type=fill_type,
                         pattern=pattern,
                         gradient=gradient,
                         image=image)

    # Sometimes one unknown byte comes...
    if not reader.eof():
        reader.read_uint8()  # Drop one byte

    return BorderFill(property=prop,
                      border_types=border_types,
                      border_thicknesses=border_thicknesses,
                      border_colors=border_colors,
                      diagonal_type=diagonal_type,
                      diagonal_thickness=diagonal_thickness,
                      diagonal_color=diagonal_color,
                      fill_info=fill_info)
