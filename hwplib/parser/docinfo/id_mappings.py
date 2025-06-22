from hwplib.models.common.enum import RecordTag
from hwplib.models.docinfo.id_mappings import (ID_MAPPING_INDEX_TO_TAG,
                                               FaceNameType, IDMappings)
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.binary import BinaryReader


@RecordParserRegistry.register(RecordTag.ID_MAPPINGS)
def parse_id_mappings(reader: BinaryReader) -> IDMappings:
    counts = {}

    ID_MAPPING_FACE_NAME_START = ID_MAPPING_INDEX_TO_TAG.index(
        RecordTag.FACE_NAME)

    for index, tag in enumerate(ID_MAPPING_INDEX_TO_TAG):
        count = reader.read_int32()

        if tag == RecordTag.FACE_NAME:
            subtype = list(FaceNameType)[index - ID_MAPPING_FACE_NAME_START]
            counts[(tag, subtype)] = count
        else:
            counts[tag] = count

    return IDMappings(counts=counts)
