from dataclasses import dataclass
from hwplib.models.docinfo.numbering import ParagraphHeadInfo


@dataclass
class PictureBullet:
    contrast: int  # 이미지 글머리 대비
    brightness: int  # 이미지 글머리 밝기
    effect: int  # 이미지 글머리 효과
    picture_index: int  # 이미지 글머리 ID


@dataclass
class Bullet:
    paragraph_head_info: ParagraphHeadInfo  # 문단 머리 정보
    bullet_char: str  # 글머리 기호 문자
    image_bullet: int  # 이미지 글머리 인덱스 (0이면 그냥 글머리표)
    picture_bullet: PictureBullet  # 이미지 글머리 정보
    check_bullet_char: str  # 체크 글머리 기호 문자
