from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.models.common.enum import RecordTag
from hwplib.utils.binary import BinaryReader
from hwplib.models.docinfo.document_properties import (DocumentProperties,
                                                       StartNumber,
                                                       CaretPosition)


@RecordParserRegistry.register(RecordTag.DOCUMENT_PROPERTIES)
def parse_document_properties(reader: BinaryReader) -> DocumentProperties:
    section_count = reader.read_uint16()

    start_number = StartNumber(
        page=reader.read_uint16(),
        footnote=reader.read_uint16(),
        endnote=reader.read_uint16(),
        picture=reader.read_uint16(),
        table=reader.read_uint16(),
        equation=reader.read_uint16(),
    )

    caret_position = CaretPosition(
        list_id=reader.read_uint32(),
        para_index=reader.read_uint32(),
        char_index=reader.read_uint32(),
    )

    return DocumentProperties(
        section_count=section_count,
        start_number=start_number,
        caret_position=caret_position,
    )
