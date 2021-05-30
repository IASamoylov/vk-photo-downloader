# DOES NOT WORK 

script temporary does not work

# vk photo downloader

The script allows you to download photos from the desired VK album.

For using the script you need have access token with next scope:
* photos


## System requirements

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