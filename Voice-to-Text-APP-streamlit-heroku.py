# 在terminal里输入： 
# streamlit run "/Users/qinxu/GitHub_files/20241216_制作语音转文字桌面app/20250109_把语音转文字的APP放到网页上供用户下载/Voice-to-Text-APP-streamlit-heroku.py"
#   Local URL: http://localhost:8501
#   Network URL: http://192.168.1.5:8501

import streamlit as st
import os

# 设置页面标题
st.title('Voice-to-Text APP')

# 页面简介
st.markdown("""
    Voice-to-Text APP 是基于 [OpenAI Whisper](https://github.com/openai/whisper) 的 “turbo”、“large-v2”、“large-v3”模型而开发的一款语音转文字的APP。<br>
    您可以点击下面的 “Download” 按钮下载 Voice-to-Text APP。
""", unsafe_allow_html=True)


# 选择文件并提供下载链接
base_url = "/Users/qinxu/GitHub_files/20241216_制作语音转文字桌面app/20250109_把语音转文字的APP放到网页上供用户下载/"
app_file_path = base_url+ "APP/Voice-to-Text.app.zip"  # 替换为实际文件路径

# 检查文件是否存在
if os.path.exists(app_file_path):
    # 提供文件下载链接
    with open(app_file_path, "rb") as file:
        st.download_button(
            label="⬇️ Download　Voice-to-Text APP",
            data=file,
            file_name=os.path.basename(app_file_path),
            mime="application/octet-stream"
        )
else:
    st.error("文件未找到，请确保文件路径正确。")


st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("------------")

# 在网页中插入本地图片
# 使用 st.columns() 来创建并排布局
col1, col2 = st.columns(2)
# 第一列：插入第一张图片
image_path_001 = base_url + "Picture/001.jpg"  # 替换为图片的实际路径
if os.path.exists(image_path_001):
    with col1:
        st.image(image_path_001, caption="Voice-to-Text APP 界面", use_container_width=True)
else:
    with col1:
        st.error("图片未找到，请确保文件路径正确。")

# 第二列：插入第二张图片
image_path_002 = base_url + "Picture/002.jpg"  # 替换为图片的实际路径
if os.path.exists(image_path_002):
    with col2:
        st.image(image_path_002, caption="Voice-to-Text APP 语音转文字示例", use_container_width=True)
else:
    with col2:
        st.error("图片未找到，请确保文件路径正确。")



# 自定义CSS样式，修改按钮颜色为蓝色
st.markdown("""
<style>
/* 确保自定义的按钮样式优先 */
div.stDownloadButton > button {
    background-color: #007bff !important;  /* 蓝色 */
    color: #ffffff !important;  /* 字体颜色为白色 */
    font-size: 22px !important;  /* 字体大小 */
    height: 2em !important;  /* 按钮高度 */
    width: 12em !important;  /* 按钮宽度 */
    border-radius: 10px !important;  /* 圆角 */
    border: none !important;  /* 去除边框 */
}

/* 悬停时的按钮样式 */
div.stDownloadButton > button:hover {
    background-color: #0056b3 !important;  /* 悬停时深蓝色 */
    color: #ffffff !important;
    font-size: 22px !important;
    font-weight: bold !important;
    height: 2em !important;
    width: 12em !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)




st.write("------------")

st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


st.markdown("""
######
- **本项目受 JSPS科研费 23K18866、24K16129（代表者：京都大学 徐勤），以及 JSPS科研费21K00773、JP24K04091（代表者： 早稻田大学 砂岡和子）的资助。**
- **网页搭建者：徐　勤 （京都大学文学研究科）**
- **网页搭建日：2025.01.09**

""")
