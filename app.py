import streamlit as st
from news_scraper import fetch_news
from summarizer import summarize_text


def main():
    st.set_page_config(page_title="AI News Summarizer", layout="centered")

    st.title("🧠 AI News Summarizer (TH/EN)")

    url = st.text_input("🔗 ใส่ URL ข่าว:")
    lang = st.radio("🗣 ต้องการสรุปเป็นภาษาใด?", options=["ไทย", "English"])

    if url:
        with st.spinner("📄 กำลังดึงข่าว..."):
            article = fetch_news(url)
            st.subheader("เนื้อข่าวบางส่วน:")
            st.write(article[:500] + "...")

        if st.button("✨ สรุปข่าว"):
            with st.spinner("🤖 กำลังสรุปข่าวด้วย AI..."):
                target = "th" if lang == "ไทย" else "en"
                summary = summarize_text(article, target_lang=target)
                st.success("✅ สรุปข่าว:")
                st.write(summary)

if __name__ == "__main__":
    main()
