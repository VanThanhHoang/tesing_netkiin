import subprocess
import time
from uiautomator import Device
from common import clickByPosition,fillText,reOpenApp,clickByTextView

def searchTesting():
    try:
        reOpenApp()
        print("Mở màn hình tìm kiếm...")
        # Bấm vào nút tìm kiếm
        clickByPosition(720, 156)
        time.sleep(1)
        print("Điền text...")
        fillText('ao')
        #Xoá text
        print("Xoá text...")
        clickByPosition(777, 209)
        time.sleep(1)
        print("Điền text lần 2...")
        #Điền text
        fillText('ao')
        time.sleep(1)
        print("Tìm kiếm...")
        #Tìm kiếm
        clickByPosition(995,209)
        time.sleep(4)
        print("Trở lại màn chính")
        #Back màn chính
        clickByPosition(81, 208)    
    except subprocess.CalledProcessError as e:
        # In lỗi nếu có
        print("Error:", e.stderr)
def searchByHistory():
    reOpenApp()
    print("Mở màn hình tìm kiếm...")
    # Bấm vào nút tìm kiếm
    clickByPosition(720, 156)
    time.sleep(2)
    print("Đang tìm kiếm theo lịch sử...")
    clickByPosition(103, 470)
    time.sleep(3)
    print("Trở lại màn chính")
    #Back màn chính
    clickByPosition(81, 208)  
def deleteSearchHistory():
    reOpenApp()
    print("Mở màn hình tìm kiếm...")
    # Bấm vào nút tìm kiếm
    clickByPosition(720, 156)
    time.sleep(2)
    print("Xoá 1 lịch sử tìm kiếm đầu tiên...")
    clickByPosition(990, 470)
    time.sleep(1)
    clickByTextView('Xoá tất cả')
    print("Xoá tất cả lịch sử tìm kiếm.")
    time.sleep(2)   
    clickByTextView('XÓA')
    clickByPosition(81, 208) 
