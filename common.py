import subprocess
import time
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