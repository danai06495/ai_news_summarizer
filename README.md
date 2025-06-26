# AI News Summarizer (ภาษาไทย / English)

โปรเจกต์นี้เป็น AI News Summarizer ที่ดึงข่าวจากเว็บ และสรุปเนื้อหาด้วยโมเดล AI

## ฟีเจอร์
- รองรับข่าวภาษาไทยและอังกฤษ
- เลือกสรุปข่าวเป็นภาษาไทยหรืออังกฤษได้
- ใช้ Hugging Face Transformers สรุปข่าวด้วยโมเดล BART
- แปลภาษาโดยใช้ Google Translate (ผ่าน `googletrans`)

## การติดตั้ง

```bash
pip install -r requirements.txt
