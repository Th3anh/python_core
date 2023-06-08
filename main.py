# Import module khachhang
import khachhang

# Hàm hiển thị menu
def hien_thi_menu():
    print("+----------------------------------------------------+")
    print("|                Quản lý khách hàng                   |")
    print("+----------------------------------------------------+")
    print("|                       MENU                         |")
    print("+----------------------------------------------------+")
    print("| 1. Thêm khách hàng                                  |")
    print("| 2. Xóa bỏ khách hàng                                |")
    print("| 3. Cập nhật thông tin khách hàng                    |")
    print("| 4. Tìm kiếm thông tin khách hàng                    |")
    print("| 5. Thoát                                            |")
    print("+----------------------------------------------------+")

# Hàm thêm khách hàng
def them_khach_hang():
    # Gọi hàm thêm khách hàng từ module khachhang
    khachhang.them_khach_hang()

# Hàm xóa khách hàng
def xoa_khach_hang():
    # Gọi hàm xóa khách hàng từ module khachhang
    khachhang.xoa_khach_hang()

# Hàm cập nhật thông tin khách hàng
def cap_nhat_thong_tin_khach_hang():
    # Gọi hàm cập nhật thông tin khách hàng từ module khachhang
    khachhang.cap_nhat_thong_tin_khach_hang()

# Hàm tìm kiếm thông tin khách hàng
def tim_kiem_thong_tin_khach_hang():
    # Gọi hàm tìm kiếm thông tin khách hàng từ module khachhang
    khachhang.tim_kiem_thong_tin_khach_hang()

# Chương trình chính
def main():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn (1-5): ")
        
        if lua_chon == '1':
            them_khach_hang()
        elif lua_chon == '2':
            xoa_khach_hang()
        elif lua_chon == '3':
            cap_nhat_thong_tin_khach_hang()
        elif lua_chon == '4':
            tim_kiem_thong_tin_khach_hang()
        elif lua_chon == '5':
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

# Gọi chương trình chính
if __name__ == "__main__":
    main()