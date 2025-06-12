from dataclasses import dataclass
from typing import Optional

from hwplib.models.common.bitfield import BitFieldObject
from hwplib.models.docinfo.enum import (BinDataAccessState, BinDataCompress,
                                        BinDataType)


@dataclass
class BinDataProperty(BitFieldObject):
    type: BinDataType
    compress: BinDataCompress
    state: BinDataAccessState

    _spec = {
        "type": (0, 3, BinDataType),
        "compress": (4, 5, BinDataCompress),
        "state": (8, 9, BinDataAccessState),
    }


@dataclass
class BinData:
    property: BinDataProperty
    absolute_path: Optional[str] = None
    relative_path: Optional[str] = None
    storage_id: Optional[int] = None
    extension: Optional[str] = None
