import time
from common import reOpenApp,swipe,clickByPosition
def swipeAndClickFastMenu():
    reOpenApp()
    swipe(x=737, y=736, duration=1000, direction='left', repetitions=3, sleep_time=1)
    swipe(x=737, y=736, duration=1000, direction='right', repetitions=3, sleep_time=1)
    time.sleep(1)
    print('Click vào menu nhanh 1')
    clickByPosition(127, 780)