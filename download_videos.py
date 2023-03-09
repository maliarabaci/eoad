
import os
import argparse
import csv
import urllib.request
from pytube import YouTube
from enum import Enum


class source_type(Enum):
    youtube = 1,
    url = 2

class dataset_name(Enum):
    eoad = 1,
    huji = 2,
    fpvsum = 3

parser = argparse.ArgumentParser()
parser.add_argument('--metadata-file', type=str, help="video metadata file holding URLs of the raw videos")
parser.add_argument('--download-folder', type=str, help="download folder for raw videos")


def parse_metadata(metadata_filepath):
    """
    Parse metadata file to get download URLs and labels
    """
    video_url_list = []
    video_name_list = []
    dataset_name_list = []
    source_type_list = []
    # To open CSV file
    with open(metadata_filepath, 'r', encoding='ISO8859') as metadata_file:
        metadata_reader = csv.reader(metadata_file, delimiter=";")

        for idx, row in enumerate(metadata_reader):
            # yield [unicode(cell, 'utf-8') for cell in row]
            print("row = ", row)
            vid_name = row[1]
            str_dataset_name = row[2]
            str_source_type = row[3]
            vid_url = row[4]

            # Skip header and previously downloaded videos
            if idx == 0 or (vid_url in video_url_list):
                continue

            # Parse video title and link
            video_name_list.append(vid_name)
            video_url_list.append(vid_url)
            # Parse dataset name
            if str_dataset_name == 'EOAD':
                dataset_name_list.append(dataset_name.eoad)
            elif str_dataset_name == 'HUJI':
                dataset_name_list.append(dataset_name.huji)
            elif str_dataset_name == 'FPVSum':
                dataset_name_list.append(dataset_name.fpvsum)
            else:
                raise Exception("Undefined dataset name = {}".format(str_dataset_name))    
            # Parse source type
            if str_source_type == 'YouTube':
                source_type_list.append(source_type.youtube)
            elif str_source_type == 'URL':
                source_type_list.append(source_type.url)
            else:
                raise Exception("Undefined source type = {}".format(str_source_type))    
            
    return video_url_list, video_name_list, dataset_name_list, source_type_list


def download_youtube_video(url_link, download_folder, filename):

    youtubeObject = YouTube(url_link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=download_folder, filename=filename)
        print("Download has been completed successfully")
        return True
    except:
        print("An error has occurred")
        return False


if __name__ == '__main__':

    args = parser.parse_args()

    metadata_filepath = args.metadata_file
    download_folder_path = args.download_folder

    # operation
    print('parsing dataset information from metadata file..')
    video_url_list, video_name_list, dataset_name_list, source_type_list = parse_metadata(metadata_filepath)

    # check whether the output folder exists or not 
    if not os.path.isdir(download_folder_path):
        print("creating folder: " + download_folder_path)
        os.makedirs(download_folder_path)

    # Save raw videos to the output directory
    print('downloading videos from URLs')
    download_error_filepath = os.path.join(download_folder_path, "download_error.txt")
    error_count = 0
    
    with open(download_error_filepath, 'w') as error_file:

        for idx, video_url in enumerate(video_url_list):
            print("dowloading {}...".format(video_url))
            try:
                if source_type_list[idx] == source_type.url:
                    # save video file with its original file name
                    urllib.request.urlretrieve(video_url, os.path.join(download_folder_path, video_name_list[idx] + ".mp4")) 
                elif source_type_list[idx] == source_type.youtube:
                    # save video file with YouTube file ID
                    youtube_file_id = video_url.split("=")[1]
                    bres = download_youtube_video(video_url, download_folder_path, youtube_file_id + ".mp4")
                    if bres == False:
                        error_count += 1
                        print("Could not download the video {}".format(video_name_list[idx])) 
                        error_file.write(video_name_list[idx])
                else: 
                    raise Exception("Undefined source type!")
            except:
                error_count += 1
                print("Could not download the video {}".format(video_name_list[idx]))
                error_file.write(video_name_list[idx])

    if error_count > 0:
        print("Some files could not be downloaded. Check output error file!")
    else:
        print("All files have been downloaded succesfully")