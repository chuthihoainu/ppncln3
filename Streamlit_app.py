import streamlit as st
st.image("download.jpg")
st.write("VPANDAS xin chào ạ")

import requests
from nbformat import read

# Đọc file Jupyter Notebook
url = "https://github.com/chuthihoainu/ppncln3/blob/master/Main_RFM_3.ipynb"
notebook = read(url)

# Hiển thị tiêu đề của file Jupyter Notebook
st.title(notebook['metadata']['title'])

# Duyệt qua các cell trong file Jupyter Notebook
for cell in notebook['cells']:
    # Kiểm tra loại cell
    if cell['cell_type'] == 'markdown':
        # Hiển thị nội dung markdown
        st.markdown(cell['source'])
    elif cell['cell_type'] == 'code':
        # Chạy mã code
        exec(cell['source'])


