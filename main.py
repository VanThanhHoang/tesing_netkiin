from search import searchByHistory, searchTesting, deleteSearchHistory
from banner import swipeBanner, clickBanner
from fast_menu import swipeAndClickFastMenu

def main_menu():
    options = {
        '1': (searchTesting, "Tìm kiếm"),
        '2': (deleteSearchHistory, "Xoá lịch sử tìm kiếm"),
        '3': (searchByHistory, "Tìm kiếm bằng lịch sử"),
        '4': (swipeBanner, "Thao tác vuốt banner"),
        '5': (clickBanner, "Thao tác bấm banner"),
        '6': (swipeAndClickFastMenu, "Thao tác vuốt menu")
    }
    
    while True:
        print("\n--- Menu ---")
        for key, (_, desc) in options.items():
            print(f"{key}. {desc}")
        print("0. Thoát")
        
        choice = input("Vui lòng chọn một tùy chọn: ")
        
        if choice == '0':
            print("Đang thoát chương trình...")
            break
        elif choice in options:
            func, desc = options[choice]
            print(f"Bạn đã chọn {desc}.")
            func()
        else:
            print("Tùy chọn không hợp lệ. Vui lòng thử lại.")
if __name__ == "__main__":
    main_menu()