from transformers import pipeline
from langdetect import detect
from googletrans import Translator

summarize = pipeline("summarization", model="facebook/bart-large-cnn")
translator = Translator()

def summarize_text(text, target_lang="th"):
    lang = detect(text)

    if lang == "th":
        # แปลไทย → อังกฤษ
        translated = translator.translate(text, src='th', dest='en').text
        summary_en = summarize(translated, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        
        # แปลกลับอังกฤษ → ไทย (ถ้าเลือกให้สรุปภาษาไทย)
        if target_lang == "th":
            summary = translator.translate(summary_en, src='en', dest='th').text
        else:
            summary = summary_en

    else:
        summary = summarize(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        
        if target_lang == "th":
            summary = translator.translate(summary, src='en', dest='th').text

    return summary
