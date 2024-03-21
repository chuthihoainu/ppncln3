import streamlit as st
pip install nbformat
st.image("download.jpg")
st.write("VPANDAS xin chào ạ")
import requests
import nbformat
from nbformat import read
# Lấy URL của file Jupyter Notebook
url = "https://github.com/chuthihoainu/ppncln2/blob/master/Main_RFM_3.ipynb"

# Gửi yêu cầu GET đến URL để lấy nội dung file Jupyter Notebook
response = requests.get(url)

# Kiểm tra mã trạng thái
if response.status_code == 200:

    # Đọc nội dung file Jupyter Notebook
    notebook = read(response.content)

    # Hiển thị tiêu đề của file Jupyter Notebook
    st.title(notebook["metadata"]["title"])

    # Duyệt qua các cell trong file Jupyter Notebook
    for cell in notebook["cells"]:

        # Kiểm tra loại cell
        if cell["cell_type"] == "markdown":

            # Hiển thị nội dung markdown
            st.markdown(cell["source"])

        elif cell["cell_type"] == "code":

            # Chạy mã code
            exec(cell["source"])

else:

    # Hiển thị thông báo lỗi
    st.error("Lỗi khi lấy file Jupyter Notebook")
