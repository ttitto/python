import json
import yaml

class Loader:
    def __init__(self, file_path, **kwargs):
        self.file_path = file_path
        self._file = None
        
        if(any(a is None for a in [self.file_path])):
            raise ValueError('Arguments for Loader class missing: file_path')

    def load(self):
        self._file = open(self.file_path)
        return self._file

    def _dispose(self):
        if not self._file.closed:
            self._file.close()

class JsonLoader(Loader):
    def __init__(self, file_path, **kwargs):
        super().__init__(file_path, **kwargs)

    def load(self):
            f = super().load()
            data = json.load(f)
            super()._dispose()
            return data
            

class YamlLoader(Loader):
    def __init__(self, file_path, **kwargs):
        super().__init__(file_path, **kwargs)

    def load(self):
        with open(self.file_path) as f:
            return yaml.load(f)