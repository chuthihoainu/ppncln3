import streamlit as st
st.image("download.jpg")
st.write("VPANDAS xin chào ạ")

import requests
from nbformat import read

# Đọc file Jupyter Notebook
url = "url_to_your_notebook.ipynb"
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


