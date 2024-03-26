import streamlit as st

# Tạo biến để lưu trữ trạng thái đăng nhập
logged_in = False

# Hiển thị màn hình đăng nhập
while not logged_in:
    # Thêm tiêu đề
    st.text("Đăng nhập")

    # Thêm ô nhập tên người dùng
    username = st.text_input("Tên người dùng:")

    # Thêm ô nhập mật khẩu
    password = st.text_input("Mật khẩu:", type="password")

    # Thêm nút bấm đăng nhập
    if st.button("Đăng nhập"):
        # Kiểm tra tên người dùng và mật khẩu
        if username == "admin" and password == "password":
            # Đặt trạng thái đăng nhập thành True
            logged_in = True
        else:
            # Hiển thị thông báo lỗi
            st.error("Tên người dùng hoặc mật khẩu không chính xác.")

# Hiển thị trang chủ sau khi đăng nhập thành công
if logged_in:
    st.text("Đăng nhập thành công!")
    # Thêm nội dung trang chủ ở đây
