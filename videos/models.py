from pydantic.main import BaseModel

from yt_core.selenium.main import ScreenDimensionEnum


class SeleniumWatchVideoParams(BaseModel):
    instances_count: int=4
    screen_dimenstion: ScreenDimensionEnum = ScreenDimensionEnum.svga
    headless: bool=True
    video_link: str
    play_btn_class: str="ytp-play-button"
    # watch number in seconds
    watch_time: int = 20
