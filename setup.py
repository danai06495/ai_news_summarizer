from setuptools import setup, find_packages

setup(
    name="ai-news-summarizer",
    version="0.1.0",
    description="AI News Summarizer รองรับภาษาไทยและอังกฤษ พร้อมแปลภาษา",
    author="Danai",
    author_email="fxdanai@gmail.com",
    url="https://github.com/danai06495/ai_news_summarizer",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "streamlit",
        "beautifulsoup4",
        "requests",
        "langdetect",
        "googletrans==4.0.0-rc1",
    ],
    entry_points={
        "console_scripts": [
            "news-summarizer=app:main",  # ถ้าใน app.py มีฟังก์ชัน main() ที่เป็น entry point
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
