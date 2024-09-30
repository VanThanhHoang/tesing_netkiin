import time
from common import reOpenApp,swipe,clickByPosition
def swipeBanner():
    reOpenApp()
    swipe(x=535, y=414, duration=1000, direction='left', repetitions=3, sleep_time=1)
    time.sleep(4)
    swipe(x=535, y=414, duration=1000, direction='right', repetitions=3, sleep_time=1)
def clickBanner():
    reOpenApp()
    for i in range(3):
        clickByPosition(535, 414)
        time.sleep(2)
        clickByPosition(84, 100)
        clickByPosition(540, 364)
        time.sleep(2)