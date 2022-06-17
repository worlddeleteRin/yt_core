import time
from selenium.webdriver.firefox.webdriver import WebDriver
from yt_core.selenium.main import ScreenDimensionEnum, launch_default_selenium_driver
from yt_core.logging import lgd,lgw,lge
import pytest
# import psutil
import threading


test_instances_to_spawn = 10
instances_to_spawn = 1
headless = True 
# link="https://www.youtube.com/watch?v=5qap5aO4i9A"
link="https://www.youtube.com/watch?v=4RLY1Jq7K9c"
play_btn_class="ytp-play-button"

# not threaded
@pytest.mark.skip
def test_webdriver_mem_usage():
    """
    p = psutil.Process()
    lgd(p.memory_info())
    """
    drivers: list[WebDriver] = []
    def add_driver() -> WebDriver:
        wd: WebDriver = launch_default_selenium_driver(headless=True)
        return wd
    drivers = [add_driver() for i in range(0, test_instances_to_spawn)]
    lgd('Ended initialization...')
    for d in drivers:
        d.get("https://google.com")
    lgd('Begin to sleep...')
    time.sleep(10)
    for d in drivers:
        d.close()

@pytest.mark.skip
def test_multiple_instances():
    drivers: list[WebDriver] = []

    def add_driver() -> WebDriver:
        wd: WebDriver = launch_default_selenium_driver(headless=headless)
        return wd
    def play_video(wd: WebDriver):
        play_btn = wd.find_element_by_class_name(play_btn_class)
        if play_btn:
            play_btn.click()

    for i in range(0,4):
        drivers = [add_driver() for d in range(0, instances_to_spawn)]
        for wd in drivers:
            wd.get(link)
            play_video(wd)
        time.sleep(200)
        for wd in drivers:
            wd.quit()
        time.sleep(5)

# threaded in one thread?
# @pytest.mark.skip
def test_multiple_instances_threaded():
    workers = 1
    def play_video():
        wd: WebDriver = launch_default_selenium_driver(
            headless=headless,
            screen_dimension=ScreenDimensionEnum.svga
        )
        wd.get(link)
        time.sleep(1)
        play_btn = wd.find_element_by_class_name(play_btn_class)
        if play_btn:
            play_btn.click()
        time.sleep(5)
        wd.close()

    def thread_play_video():
        for i in range(0, instances_to_spawn):
            th = threading.Thread(target=play_video)
            th.start()

    lgd('Spawning workers...')
    for i in range(0, workers):
        th = threading.Thread(target=thread_play_video)
        th.start()

    lgd('Run before exit...')

