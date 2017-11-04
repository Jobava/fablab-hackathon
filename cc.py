import os
import subprocess


def write_caption_file(video_id, file_pattern):
    url = 'https://www.youtube.com/watch?v={}'.format(video_id)
    subprocess.call(["youtube-dl", "--all-subs", "--skip-download", url, "-o{}.vtt".format(file_pattern)])
