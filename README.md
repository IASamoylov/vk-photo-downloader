# vk photo downloader

The script allows you to download photos from the desired VK album.

For using the script you need have access token with next scope:
* photos

## Creating of access token

1. Format URL https://oauth.vk.com/authorize?client_id={{CLIENT_ID}}&display=page&scope=photos&response_type=token&v=5.122, 
instead **{{CLIENT_ID}}**, you must specify your numeric VK profile ID.
2. Open the received URL in the browser.
3. After authorizing need to copy **access token** from the address bar.

## System requirements

* Anaconda 3 ([link](https://www.anaconda.com/products/individual#Downloads))
* Python 3.8 ([link](https://www.python.org/downloads/release/python-380/)) 

## Script options
| key | short key | description | required | default |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| --help  | -h | Show help message | -  | -  |
| --user  | -u | Numeric VK profile ID| True  | -  |
| --token  | -t | User access_token with photos scope| True  | -  |
| --dir  | -d | Directory where photos will be saved| True  | -  |
| --album  | -a | Album id or one of values [profile, wall, saved] | False  | saved  |

## Usage
```shell script
main.py [-h] -u USER -t TOKEN -d DIRECTORY [-a ALBUM_ID]
```