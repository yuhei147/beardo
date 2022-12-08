import streamlit as st
from PIL import Image

st.title('ベアドゥアプリ')
st.caption('ベアドゥかわいい')
st.subheader('自己紹介')
st.text('ほたてスープが大好きなクマ。\n'
        'チャンネル登録よろしくクマ')
code = '''
import streamlit as st
st.title('ベアドゥチャンネル')
'''
st.code(code, language='python')

image = Image.open('bear-do_11.jpg')
st.image(image, width=200)
