from hwplib.parser.file_header_reader import parse_file_header
from hwplib.parser.record_registry import RecordParserRegistry
from hwplib.utils.record_reader import RecordReader
from hwplib.utils.compression import decompress_stream
from hwplib.utils.compound import HWPCompoundFile


def parse_hwp_file(path: str):
    # 1. Open the HWP file as a compound file.
    streams = HWPCompoundFile(path)

    # 2. FileHeader parsing.
    file_header_data = streams.read_stream("FileHeader")
    if not file_header_data:
        raise ValueError("FileHeader stream not found.")
    file_header = parse_file_header(file_header_data)
    print("✅ FileHeader:", file_header)

    # 3. DocInfo parsing.
    doc_info_data = streams.read_stream("DocInfo")
    if not doc_info_data:
        raise ValueError("DocInfo stream not found.")
    # decompress if necessary
    if file_header.properties.is_compressed:
        doc_info_data = decompress_stream(doc_info_data)

    reader = RecordReader(doc_info_data)

    records_all = reader.read_all()
    print(f"✅ Total Records in DocInfo: {len(records_all)}")
    for record in records_all:
        parsed_data = RecordParserRegistry.parse(record)
        if parsed_data:
            print(f"Parsed Record {record.header.tag_id}: {parsed_data}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python hwp_parse_main.py <path_to_hwp_file>")
        exit(1)

    parse_hwp_file(sys.argv[1])
