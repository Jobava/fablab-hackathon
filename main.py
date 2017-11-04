import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://localhost:8080/index.html")

CONFIGS = {
    'bad_words': ['trump', 'iphone'],
    'warn_time': 10,  # warn time in seconds
}


def launch_browser():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/index.html")
    return driver


def is_bad_time():
    pass


def ask_user(skip=False, blur=False, play=True):
    pass


def skip():
    pass


def blur():
    pass


def play_video(driver):
    driver.execute_script("player.playVideo()")


def pause_video(driver):
    driver.execute_script("player.pauseVideo()")


def seek_to(driver, target_time):
    driver.execute_script("player.seekTo({})".format(target_time))


def get_answer_text(driver):
    return driver.execute_script("return get_answer_text()")


def is_overlay_on(driver):
    driver.execute_script("return is_overlay_on()")


def get_current_time(driver):
    return driver.execute_script("return player.getCurrentTime()")


def ask_question(driver):
    driver.execute_script("hide_video()")


def execute_ticks(captions):
    driver = launch_browser()
    while True:
        time.sleep(0.5)
        if is_overlay_on(driver):
            continue
        current_time = get_current_time(driver)
        if is_bad_time(current_time, captions):
            ask_question(driver)
