import subprocess
import time
from common import clickByPosition,fillText,closeApp,openApp
def searchTesting():
    try:
        # Đóng ứng dụng trước
        print("Đóng ứng dụng...")
        closeApp()
        time.sleep(2)
        print("Mở ứng dụng...")
        # Mở ứng dụng
        openApp()
        time.sleep(6)
        print("Mở màn hình tìm kiếm...")
        # Bấm vào nút tìm kiếm
        clickByPosition(720, 156)
        time.sleep(1)
        fillText('ao')
        #Xoá text
        clickByPosition(777, 209)
        time.sleep(1)
        fillText('ao')
        time.sleep(1)
        clickByPosition(995,209)
    except subprocess.CalledProcessError as e:
        # In lỗi nếu có
        print("Error:", e.stderr)
# Gọi hàm searchTesting
searchTesting()
