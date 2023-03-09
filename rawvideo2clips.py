
import os
import argparse
import csv
import urllib.request
from pytube import YouTube
from enum import Enum
import ffmpeg


class download_source_type(Enum):
    youtube = 1,
    huji = 2,
    fpvsum = 3

parser = argparse.ArgumentParser()
parser.add_argument('--metadata-file', type=str, help="video metadata file holding URLs of the raw videos")
parser.add_argument('--video-folder', type=str, help="input folder containing the raw videos")
parser.add_argument('--output-folder', type=str, help="output folder for the trimmed video clips")


def parse_metadata(metadata_filepath):
    """
    Parse metadata file to get download URLs and labels
    """
    clip_name_list = []
    raw_video_list = []
    time_list = []
    frames_idx_list = []
    # To open CSV file
    with open(metadata_filepath, 'r', encoding='ISO8859') as metadata_file:
        metadata_reader = csv.reader(metadata_file, delimiter=";")

        for idx, row in enumerate(metadata_reader):
            # Skip header row
            if idx == 0:
                continue

            vid_clip_name = row[0]
            print("Video clip name = {}".format(vid_clip_name))

            source_type = row[3]
            if source_type != "YouTube":
                # get raw file name
                vid_name = row[1]
            else:
                # Get file name from YouTube ID
                vid_name = row[4].split("=")[1]

            # Convert millisecond to second
            start_frame_time = int(row[8])/1000
            end_frame_time = int(row[9])/1000
            # get frame indexes
            start_frame_idx = row[11]
            end_frame_idx = row[9]

            clip_name_list.append(vid_clip_name)
            raw_video_list.append(vid_name)
            time_list.append((start_frame_time, end_frame_time))
            frames_idx_list.append((start_frame_idx, end_frame_idx))

    return raw_video_list, clip_name_list, time_list, frames_idx_list


if __name__ == '__main__':

    args = parser.parse_args()

    metadata_filepath = args.metadata_file
    video_folder = args.video_folder
    output_folder = args.output_folder

    # operation
    print('parsing dataset information from metadata file ...')
    raw_video_list, clip_name_list, time_list, frames_idx_list = parse_metadata(metadata_filepath)

    # check whether the output folder exists or not and create if not exist
    if not os.path.isdir(output_folder):
        print("creating folder: " + output_folder)
        os.makedirs(output_folder)

    # Save trimmed videos to the output directory
    print('trimming videos...')
    download_error_filepath = os.path.join(output_folder, "download_error.txt")
    error_count = 0
    with open(download_error_filepath, 'w') as error_file:

        for idx, clip_name in enumerate(clip_name_list):
            # if idx == 0:
            print("trimming {} ...".format(raw_video_list[idx]))
            print("frame ranges = ", frames_idx_list[idx])
            try:
                vid_path = os.path.join(video_folder, raw_video_list[idx] + ".mp4")
                if os.path.isfile(vid_path) is False:
                    print("Input video file ({}) does not exist ".format(raw_video_list[idx]))
                    error_count += 1
                    error_file.write(raw_video_list[idx])
                    continue

                output_filepath = os.path.join(output_folder, clip_name + ".mp4")
                # If the output video clip file was previously extracted, then skip it
                if os.path.isfile(output_filepath):
                    continue

                input_vid = ffmpeg.input(vid_path)
                vid = (
                    input_vid
                    .trim(start = time_list[idx][0], end = time_list[idx][1])
                    .setpts('PTS-STARTPTS')
                )
                aud = (
                    input_vid
                    .filter_('atrim', start = time_list[idx][0], end = time_list[idx][1])
                    .filter_('asetpts', 'PTS-STARTPTS')
                )

                ffmpeg.concat(vid, aud, v=1, a=1).output(output_filepath).run(overwrite_output=True)
            except:
                print("Cannot trim {}".format(raw_video_list[idx]))
                error_count += 1
                error_file.write(raw_video_list[idx])
    
    if error_count > 0:
        print("Some files could not be trimmed. Check output error file!")
    else:
        print("All video clip files have been trimmed succesfully")