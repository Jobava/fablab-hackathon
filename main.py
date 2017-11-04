import time

from cc import write_caption_file
from ccparser import get_captions
from selenium import webdriver


CONFIGS = {
    'bad_words': ['trump', 'iphone'],
    'warn_time': 10,  # warn time in seconds
}


def launch_browser():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/index.html")
    return driver


def play_video(driver):
    driver.execute_script("player.playVideo()")


def pause_video(driver):
    driver.execute_script("player.pauseVideo()")


def seek_to(driver, target_time):
    driver.execute_script("player.seekTo({})".format(target_time))


def get_answer_text(driver):
    return driver.execute_script("return get_answer_text()")


def is_overlay_on(driver):
    return driver.execute_script("return is_overlay_on()")


def get_current_time(driver):
    return driver.execute_script("return player.getCurrentTime()")


def ask_question(driver):
    driver.execute_script("hide_video()")


def get_captions_for_video(video_id):
    write_caption_file(video_id, 'out')
    pass


def get_current_video(driver):
    p = driver.execute_script("return player.getPlaylistIndex()")
    return driver.execute_script("return player.getCurrentTime()")

def execute_ticks(driver, playlist):
    # playlist is a dict from video IDs to caption lists
    bad_time = False
    while True:
        time.sleep(0.5)
        if is_overlay_on(driver):
            continue
        current_video =
        current_time = get_current_time(driver)
        next_good_captions = get_next_good_captions(current_time=current_time,captions=playlist['B9EV_h7LIuQ'], warn_time=CONFIGS['warn_time'])
        if is_bad_time(current_time, captions):
            bad_time = True
            ask_question(driver)


if __name__ == '__main__':
    driver = launch_browser()
    playlist = driver.execute_script("return playlist")
    # convert the playlist list into a dict
    playlist = {p: get_captions_for_video(p) for p in playlist}
    execute_ticks(driver, playlist)
