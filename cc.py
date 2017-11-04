import os
import subprocess

def get_cc(url, write_name):
    subprocess.call(["youtube-dl", "--all-subs", "--skip-download", url, "-o{}.vtt".format(write_name)]) 
