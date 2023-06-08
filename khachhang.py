# Module khachhang

# Dữ liệu khách hàng lưu trong một danh sách
khach_hang_list = []

# Hàm thêm khách hàng
def them_khach_hang():
    # Nhập thông tin khách hàng
    ma_khach_hang = input("Nhập mã khách hàng: ")
    ten_khach_hang = input("Nhập tên khách hàng: ")
    sdt_khach_hang = input("Nhập số điện thoại khách hàng: ")
    
    # Tạo đối tượng khách hàng mới
    khach_hang = {
        "ma_khach_hang": ma_khach_hang,
        "ten_khach_hang": ten_khach_hang,
        "sdt_khach_hang": sdt_khach_hang
    }
    
    # Thêm khách hàng vào danh sách
    khach_hang_list.append(khach_hang)
    print("Thêm khách hàng thành công.")

# Hàm xóa khách hàng
def xoa_khach_hang():
    ma_khach_hang = input("Nhập mã khách hàng cần xóa: ")
    for khach_hang in khach_hang_list:
        if khach_hang["ma_khach_hang"] == ma_khach_hang:
            khach_hang_list.remove(khach_hang)
            print("Xóa khách hàng thành công.")
            return
    
    print("Không tìm thấy khách hàng có mã", ma_khach_hang)

# Hàm cập nhật thông tin khách hàng
def cap_nhat_thong_tin_khach_hang():
    ma_khach_hang = input("Nhập mã khách hàng cần cập nhật: ")
    for khach_hang in khach_hang_list:
        if khach_hang["ma_khach_hang"] == ma_khach_hang:
            ten_khach_hang = input("Nhập tên khách hàng mới: ")
            sdt_khach_hang = input("Nhập số điện thoại khách hàng mới: ")
            
            khach_hang["ten_khach_hang"] = ten_khach_hang
            khach_hang["sdt_khach_hang"] = sdt_khach_hang
            
            print("Cập nhật thông tin khách hàng thành công.")
            return
    
    print("Không tìm thấy khách hàng có mã", ma_khach_hang)

# Hàm tìm kiếm thông tin khách hàng
def tim_kiem_thong_tin_khach_hang():
    ma_khach_hang = input("Nhập mã khách hàng cần tìm kiếm: ")
    for khach_hang in khach_hang_list:
        if khach_hang["ma_khach_hang"] == ma_khach_hang:
            print("Thông tin khách hàng:")
            print("Mã khách hàng:", khach_hang["ma_khach_hang"])
            print("Tên khách hàng:", khach_hang["ten_khach_hang"])
            print("Số điện thoại khách hàng:", khach_hang["sdt_khach_hang"])
            return
    
    print("Không tìm thấy khách hàng có mã", ma_khach_hang)
