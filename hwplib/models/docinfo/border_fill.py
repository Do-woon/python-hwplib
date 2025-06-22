from dataclasses import dataclass
from enum import IntEnum, IntFlag
from typing import Dict, List, Optional

from hwplib.models.common.bitfield import BitFieldObject
from hwplib.models.common.colorref import ColorRef


# Table 24
class DiagonalShape(IntFlag):
    NONE = 0b000  # None
    STANDARD = 0b010  # Slash/Backslash
    TO_BOTTOM_EDGE = 0b011  # LeftTop -> Bottom Edge (Slash) / RightTop -> Bottom Edge (Backslash)
    TO_OTHER_EDGE = 0b110  # LeftTop -> Right Edge (Slash) / RightTop -> Left Edge (Backslash)
    TO_BOTH_EDGES = 0b111  # LeftTop -> Bottom & Right Edge (Slash) / RightTop -> Bottom & Left Edge (Backslash)


# Table 24
@dataclass
class BorderFillProperty(BitFieldObject):
    has_3d_effect: bool  # 3D 효과의 유무
    has_shadow: bool  # 그림자 효과의 유무
    slash_type: DiagonalShape  # Slash 대각선 모양 (시계 방향으로 각각의 대각선 유무를 나타냄)
    backslash_type: DiagonalShape  # Backslash 대각선 모양 (반시계 방향으로 각각의 대각선 유무를 나타냄)
    slash_crooked: bool  # Slash 대각선 꺽은선
    backslash_crooked: bool  # Backslash 대각선 꺽선
    slash_reverse: bool  # Slash 대각선 모양 180도 회전 여부
    backslash_reverse: bool  # Backslash 대각선 모양 180도 회전 여부
    has_center_line: bool  # 중심선 유무

    _spec = {
        "has_3d_effect": (0, 0, {
            0: False,
            1: True
        }),
        "has_shadow": (1, 1, {
            0: False,
            1: True
        }),
        "slash_type": (2, 4, DiagonalShape),
        "backslash_type": (5, 7, DiagonalShape),
        "slash_crooked": (8, 9, {
            0: False,
            1: True
        }),  # 명세상 2 bit integer.
        "backslash_crooked": (10, 10, {
            0: False,
            1: True
        }),
        "slash_reverse": (11, 11, {
            0: False,
            1: True
        }),
        "backslash_reverse": (12, 12, {
            0: False,
            1: True
        }),
        "has_center_line": (13, 13, {
            0: False,
            1: True
        }),
    }


# Table 25
class BorderType(IntEnum):
    SOLID = 0  # 실선
    LONG_DOT = 1  # 긴 점선
    DOT = 2  # 점선
    DASH_DOT = 3  # -.-.-.-.
    DASH_DOT_DOT = 4  # -..-..-..
    LONG_DASH = 5  # Dash보다 긴 선분의 반복
    BIG_DOT = 6  # Dot 보다 큰 동그라미의 반복
    DOUBLE = 7  # 2중선
    THIN_THICK = 8  # 가는선 + 굵은선 2중선
    THICK_THIN = 9  # 긁은선 + 가는선 2중선
    THIN_THICK_THIN = 10  # 가는선+ 굵은선 + 가는선 3중선
    WAVE = 11  # 물결
    DOUBLE_WAVE = 12  # 물결 2중선
    THICK_3D = 13  # 두꺼운 3D
    THICK_3D_REVERSE = 14  # 두꺼운 3D (광원반대)
    SINGLE_3D = 15  # 3D 단선
    SINGLE_3D_REVERSE = 16  # 3D 단선 (광원반대)


# Table 26
class BorderThickness(IntEnum):
    MM_0_1 = 0  # 0.1mm
    MM_0_12 = 1  # 0.12mm
    MM_0_15 = 2  # 0.15mm
    MM_0_2 = 3  # 0.2mm
    MM_0_25 = 4  # 0.25mm
    MM_0_3 = 5  # 0.3mm
    MM_0_4 = 6  # 0.4mm
    MM_0_5 = 7  # 0.5mm
    MM_0_6 = 8  # 0.6mm
    MM_0_7 = 9  # 0.7mm
    MM_1_0 = 10  # 1.0mm
    MM_1_5 = 11  # 1.5mm
    MM_2_0 = 12  # 2.0mm
    MM_3_0 = 13  # 3.0mm
    MM_4_0 = 14  # 4.0mm
    MM_5_0 = 15  # 5.0mm


# Table 27
class DiagonalLineType(IntEnum):
    SLASH = 0  # Slash
    BACKSLASH = 1  # Backslash
    CROOKED_SLASH = 2  # Crooked Slash


# Table 29
class FillPatternType(IntEnum):
    SOLID = -1  # 단색 (명세에는 없음)
    HORIZONTAL_LINE = 1  # - - - -
    VERTICAL_LINE = 2  # |||||
    BACKSLASH = 3  # \\\\\
    SLASH = 4  # /////
    CROSS = 5  # +++++
    DIAGONAL_CROSS = 6  # xxxxx


# Table 30
class GradationType(IntEnum):
    STRIPE = 1  # 줄무늬형
    CIRCLE = 2  # 원형
    CONE = 3  # 원뿔형
    RECTANGLE = 4  # 사각형


# Table 31
class ImageFillType(IntEnum):
    TILE_ALL = 0  # 바둑판식-모두
    TILE_TOP = 1  # 바둑판식-가로/위
    TILE_BOTTOM = 2  # 바둑판식-가로/아래
    TILE_LEFT = 3  # 바둑판식-세로/왼쪽
    TILE_RIGHT = 4  # 바둑판식-세로/오른쪽
    FIT = 5  # 크기에 맞추어
    CENTER = 6  # 가운데로
    CENTER_TOP = 7  # 가운데 위로
    CENTER_BOTTOM = 8  # 가운데 아래로
    LEFT_CENTER = 9  # 왼쪽 가운데로
    LEFT_TOP = 10  # 왼쪽 위로
    LEFT_BOTTOM = 11  # 왼쪽 아래로
    RIGHT_CENTER = 12  # 오른쪽 가운데로
    RIGHT_TOP = 13  # 오른쪽 위로
    RIGHT_BOTTOM = 14  # 오른쪽 아래로
    NONE = 15  # 없음


# Table 32
class ImageEffect(IntEnum):
    REAL_PIC = 0
    GRAY_SCALE = 1
    BLACK_WHITE = 2
    PATTERN8x8 = 4


# Table 32
@dataclass
class ImageFillInfo:
    brightness: int  # 밝기
    contrast: int  # 명암
    effect: ImageEffect  # 그림 효과
    bin_data_id: int  # BinItem의 아이디 참조값


# Table 28
@dataclass
class PatternFill:  # 단색 채우기
    background_color: ColorRef  # 배경색
    pattern_color: ColorRef  # 무늬색
    pattern_type: FillPatternType  # 무늬 종류


# Table 28
@dataclass
class GradientFill:  # 그러데이션 채우기
    gradation_type: GradationType  # 그러데이션 유형
    angle: int  # 그러데이션 기울임(시작 각)
    center_x: int  # 그러데이션 가로 중심(중심 X 좌표)
    center_y: int  # 그러데이션 세로 중심(중심 Y 좌표)
    blur: int  # 그러데이션 번짐 정도 (0~100)

    # 아래의 두 List는 같은 길이를 가짐. (워디안/한글2002/SE에서는 항상 2)
    positions: Optional[List[int]] = None  # 색상이 바뀌는곳의 위치. (길이 > 2일 때만)
    colors: Optional[List[ColorRef]] = None  # 그러데이션 색상.

    # 번짐 정도의 중심 (0~100)
    gradation_center: Optional[int] = None
    # FillInfo 뒤의 "추가 채우기 속성" 블록에 포함되어 있으며,
    # type 비트에 GRADATION(0x04)가 설정된 경우에만 존재함.


# Table 28
@dataclass
class ImageFill:  # 이미지 채우기
    fill_type: ImageFillType  # 이미지 채우기 유형
    info: ImageFillInfo  # 그림 정보


# Table 28
class FillTypeFlag(IntFlag):
    NONE = 0x00  # 채우기 없음
    PATTERN = 0x01  # 단색/무늬 채우기
    IMAGE = 0x02  # 이미지 채우기
    GRADATION = 0x04  # 그러데이션 채우기


# Table 28
@dataclass
class FillInfo:
    type: int  # 채우기 종류
    pattern: Optional[PatternFill] = None
    gradient: Optional[GradientFill] = None
    image: Optional[ImageFill] = None


class BorderDirection(IntEnum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3


# Table 23
@dataclass
class BorderFill:
    property: BorderFillProperty

    border_types: Dict[BorderDirection, BorderType]
    border_thicknesses: Dict[BorderDirection, BorderThickness]
    border_colors: Dict[BorderDirection, ColorRef]

    diagonal_type: DiagonalLineType
    diagonal_thickness: BorderThickness
    diagonal_color: ColorRef

    fill_info: FillInfo
