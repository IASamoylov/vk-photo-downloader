import sys
from functools import cmp_to_key

sizes = {
    's': 75,
    'm': 130,
    'x': 605,
    'o': 130,
    'p': 200,
    'q': 320,
    'r': 510,
    'y': 807,
    'z': 1080,
    'w': 2560,
}


class PhotoParser:
    def __init__(self):
        pass

    def extract_urls(self, photos, min_width=0, max_width=5120):
        """
        Extract urls of images,

        :param photos: a list of VK photo objects.
        :param min_width: min image width for which the url should be returned
        :param max_width: max image width for which the url should be returned
        :return: a list of urls
        """
        self.__sort_item_sizes(photos)

        for photo in photos:
            size = photo['sizes'][-1]
            if min_width <= size['width'] <= max_width:
                yield size['url']

    def __sort_item_sizes(self, photos):
        """
        Sort by width, because the values in the `items` field are in a different order,

        :param photos: a list of VK photo objects.
        """
        for item in photos:
            item['sizes'] = sorted(item['sizes'], key=cmp_to_key(lambda x, y: x.get('width', sizes[x['type']]) - y.get('width', sizes[x['type']])))
        pass
