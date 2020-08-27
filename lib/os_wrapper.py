import os
import shutil


class OSWrapper:
    ACCESS_RIGHTS = 0o755

    def __init__(self, directory: str):
        self.directory = directory

    def try_create_directory(self):
        full_dir = os.path.expanduser(os.path.join(self.directory))

        if not os.path.exists(full_dir):
            try:
                os.mkdir(full_dir, self.ACCESS_RIGHTS)
            except OSError:
                print("Creation of the directory %s failed" % full_dir)
                return False

        return True

    def file_exist(self, file_name):
        full_dir = os.path.expanduser(os.path.join(self.directory))
        path = os.path.join(full_dir, file_name)
        
        return os.path.exists(path)

    def save(self, file_name, stream):
        full_dir = os.path.expanduser(os.path.join(self.directory))

        path = os.path.join(full_dir, file_name)

        with open(path, 'wb') as f:
            shutil.copyfileobj(stream, f)
