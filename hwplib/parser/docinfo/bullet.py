from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.bullet import Bullet, PictureBullet
from hwplib.models.docinfo.numbering import (ParagraphHeadInfo,
                                             ParagraphHeadProperty)
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.binary import BinaryReader


@RecordParserRegistry.register(RecordTag.BULLET)
def parse_bullet(reader: BinaryReader) -> Bullet:
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

    bullet_char = reader.read_string(1)
    image_bullet = reader.read_int32()

    picture_bullet = PictureBullet(
        contrast=reader.read_uint8(),
        brightness=reader.read_uint8(),
        effect=reader.read_uint8(),
        picture_index=reader.read_uint8()
    )

    check_bullet_char = reader.read_string(1)

    return Bullet(
        paragraph_head_info=para_head,
        bullet_char=bullet_char,
        image_bullet=image_bullet,
        picture_bullet=picture_bullet,
        check_bullet_char=check_bullet_char
    )
