import streamlit as st
from utils import generate_word_context

st.title("📒 单词记忆小助手")

with st.sidebar:
    api_key = st.text_input("请输入DeepSeek API Key：", type="password")
    st.markdown("[申请DeepSeek API Key](https://api-docs.deepseek.com)")

word = st.text_input("请输入单词：")

if word:
    if not api_key:
        st.info("请先在侧边栏输入DeepSeek API Key")
        st.stop()
    else:
        with st.spinner("AI正在思考中，请稍等..."):
            result = generate_word_context(word, api_key)
        st.success(f"与单词【{word}】相关的有趣小故事及造句生成完毕！")
        st.write(result)