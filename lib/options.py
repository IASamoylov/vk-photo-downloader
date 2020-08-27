from argparse import ArgumentParser


class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        """
        Init argparse lib
        """
        self.parser = ArgumentParser(description='VK photos downloader')
        self.parser.add_argument('-u', '--user', action="store", dest="user", type=str, required=True, help="Numeric VK profile ID")
        self.parser.add_argument('-t', '--token', action="store", dest="token", type=str, required=True, help="User access_token with photos scope")
        self.parser.add_argument('-d', '--dir', action="store", dest="directory", type=str, required=True, help="Directory where photos will be saved")
        self.parser.add_argument('-a', '--album', action="store", dest="album_id", type=str, help="Album id or one of values [profile, wall, saved], default value 'saved'", default='saved')

    def parse(self, args):
        """
        Parse command-line arguments
        :param args: Command-line arguments
        """
        parse_result = self.parser.parse_args(args)

        self.user: str = parse_result.user
        self.token: str = parse_result.token
        self.album_id: str = parse_result.album_id
        self.directory: str = parse_result.directory
