import threading
import time

from selenium.webdriver.firefox.webdriver import WebDriver

from yt_core.selenium.main import launch_default_selenium_driver
from yt_core.selenium.main import ScreenDimensionEnum
from yt_core.logging import lgd,lgw,lge
from yt_core.videos.models import SeleniumWatchVideoParams

class YtVideo:

    def __init__(self):
        pass

    @staticmethod
    def selenium_watch_video(q: SeleniumWatchVideoParams):
        lgd(f'** Run selenium watch video with, params: {q.dict()} **')
        def play_video():
            wd: WebDriver = launch_default_selenium_driver(
                headless=q.headless,
                screen_dimension=ScreenDimensionEnum.svga
            )
            wd.get(q.video_link)
            time.sleep(1)
            play_btn = wd.find_element_by_class_name(q.play_btn_class)
            if play_btn:
                play_btn.click()
            time.sleep(q.watch_time)
            wd.close()

        for i in range(0, q.instances_count):
            th = threading.Thread(target=play_video)
            th.start()
