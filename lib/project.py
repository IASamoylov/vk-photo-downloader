from .options import Options
from .os_wrapper import OSWrapper
from .photo_parser import PhotoParser
from .vk_api import Api as VK_api


class Project:

    def __init__(self, options: Options):
        """
        :param options: Parsed command-line arguments
        """
        self.options = options
        self.vk_api = VK_api(options.user, options.token)
        self.osWrapper = OSWrapper(options.directory)
        self.photoParser = PhotoParser()

    def run(self):
        print(f'- Tries to create the directory {self.options.directory}')
        if not self.osWrapper.try_create_directory():
            return

        print(f'- Downloads photos info from album {self.options.album_id}')
        photos_response = self.vk_api.photos.get_all(self.options.album_id)

        min_width = 390
        index = 0
        print(f'- Extracts URLs of photos with min-width {min_width}')
        for url in self.photoParser.extract_urls(photos_response, min_width=min_width):
            filename = url.split("/")[-1]

            print(f'\t - processing of file {filename}')

            print(f'\t\t - Checks that file is exist')
            if self.osWrapper.file_exist(filename):
                print('\t\t - Image already downloaded: ', filename)
                continue

            print(f'\t\t - Downloads photo by url {url}')
            stream = self.vk_api.photos.download_photo(url)

            if stream is None:
                print(f'\t\t - Image couldn\'t be retreived')
                continue

            print(f'\t\t - Saves photo')
            self.osWrapper.save(filename, stream)
            index += 1

        print(f'- Was downloaded {index} photos')
