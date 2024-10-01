import subprocess
import time
from uiautomator import Device
device = Device('BDB00044546')  
def reOpenApp():
         # Đóng ứng dụng trước
        print("Đóng ứng dụng...")
        closeApp()
        time.sleep(2)
        print("Mở ứng dụng...")
        # Mở ứng dụng
        openApp()
        time.sleep(6)
def clickByPosition( x, y):
    clickCommand = f"adb shell input tap {x} {y}"
    subprocess.run(clickCommand, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
def fillText(text):
        print("Điền text...")
        # Bấm vào EditText
        commandClickEditText = "adb shell input tap 538 208"
        subprocess.run(commandClickEditText, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
        # Nhập văn bản vào EditText
        commandInputText = f"adb shell input text '{text}'"
        subprocess.run(commandInputText, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(1)
        print("Đã nhập văn bản thành công.")  
def openApp():
    try:
        # Lệnh ADB để chạy ứng dụng với package name
        command = f"adb shell monkey -p com.netkiin -c android.intent.category.LAUNCHER 1"
        # Chạy lệnh ADB
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # In kết quả ra màn hình
        print("Ứng dụng đã được mở...")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        # In lỗi nếu có
        print("Error:", e.stderr)
def closeApp():
    try:
        # Lệnh ADB để chạy ứng dụng với package name
        command = f"adb shell am force-stop com.netkiin"
        # Chạy lệnh ADB
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        time.sleep(1)   
        # In k
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        # In lỗi nếu có
        print("Error:", e.stderr)
def swipe(x, y, duration, direction, repetitions, sleep_time):
    # Xác định tọa độ x kết thúc dựa trên hướng
    if direction.lower() == 'left':
        x_end = 0  # Tọa độ x kết thúc cho thao tác vuốt trái
        print_direction = "trái"
    elif direction.lower() == 'right':
        x_end = 1000  # Tọa độ x kết thúc cho thao tác vuốt phải (giả sử màn hình có chiều rộng 1000)
        print_direction = "phải"
    else:
        print("Hướng không hợp lệ. Vui lòng sử dụng 'left' hoặc 'right'.")
        return

    # Thực hiện thao tác vuốt
    for i in range(repetitions):
        if direction.lower() == 'left':
            print(f"Thao tác vuốt trái lần {i + 1}: từ ({x}, {y}) đến ({x_end}, {y})")
            subprocess.run(["adb", "shell", "input", "swipe", str(x), str(y), str(x_end), str(y), str(duration)])
        else:
            print(f"Thao tác vuốt phải lần {i + 1}: từ ({x_end}, {y}) đến ({x}, {y})")
            subprocess.run(["adb", "shell", "input", "swipe", str(x), str(y), str(x_end), str(y), str(duration)])
        time.sleep(sleep_time)   
        
def clickByTextView(text):
    element = device(text=text)
    if element.exists:
        element.click()  # Bấm vào phần tử nếu tìm thấy
        time.sleep(1)   
        print("Clicked on ${text} button.")
    else:
        print("Element ${text} b not found.")