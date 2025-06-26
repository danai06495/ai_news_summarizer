from summarizer import summarize_text

def test_summarize_thai():
    input_text = "ประเทศไทยเป็นประเทศในเอเชียตะวันออกเฉียงใต้ มีวัฒนธรรมที่หลากหลายและประวัติศาสตร์ยาวนาน"
    result = summarize_text(input_text, target_lang="th")
    assert isinstance(result, str)
    assert len(result) > 10

def test_summarize_english():
    input_text = "Thailand is a country in Southeast Asia known for its tropical beaches and ancient ruins."
    result = summarize_text(input_text, target_lang="en")
    assert isinstance(result, str)
    assert "Thailand" in result or len(result) > 10
