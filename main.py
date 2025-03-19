import streamlit as st
from utils import generate_word_context

st.title("📒 单词记忆小助手")
st.markdown("##### 基于DeepSeek的AI小助手：为陌生的英文单词创作一个有趣的小故事并造句，以帮助记忆英文单词。")

with st.sidebar:
    api_key = st.text_input("请输入DeepSeek API Key：", type="password")
    st.markdown("[申请DeepSeek API Key](https://api-docs.deepseek.com)")

word = st.text_input("请输入单词：")

submit = st.button("开始创作")

if submit:
    if not api_key:
        st.info("请先在侧边栏输入DeepSeek API Key")
        st.stop()
    if not word:
        st.info("请先输入单词")
        st.stop()
    else:
        with st.spinner("AI正在思考中，请稍等..."):
            result = generate_word_context(word, api_key)
        st.success(f"与单词【{word}】相关的有趣小故事及造句生成完毕！")
        st.write(result)