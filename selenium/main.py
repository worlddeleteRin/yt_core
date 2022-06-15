from enum import Enum
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
import time

import logging

logger = logging.getLogger(__name__)

class ScreenDimensionEnum(tuple, Enum):
    fullhd = (1920,1080)
    hd = (1600,900)
    lowhd = (1366,768)
    sxga = (1280,1024)
    svga = (800,600)

def launch_default_selenium_driver(
    headless: bool = True,
    screen_dimenstion: ScreenDimensionEnum = ScreenDimensionEnum.fullhd
) -> WebDriver:
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

    chrome_options = Options()

    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument(f"--window-size={screen_dimenstion[0]},{screen_dimenstion[1]}")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--mute-audio")

    driver = webdriver.Chrome(
        options=chrome_options
    )
    return driver

