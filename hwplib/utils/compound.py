import olefile

class HWPCompoundFile:
    def __init__(self, path_or_bytes):
        self.ole = olefile.OleFileIO(path_or_bytes)

    def has_stream(self, path: str) -> bool:
        return self.ole.exists(path)

    def read_stream(self, path: str) -> bytes:
        with self.ole.openstream(path) as f:
            return f.read()

    def list_streams(self):
        return self.ole.listdir()
