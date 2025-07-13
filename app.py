
import streamlit as st

st.set_page_config(page_title="Open 에이아밈", page_icon="🧠", layout="centered")

st.title("🧠 Open 에이아밈")
st.write("AI가 밈을 번역해드립니다! 당신이 알고있는 밈을 입력해주세요.")

# 밈 사전
dictionary = {
    "킹받네": "매우 화가 난다는 뜻입니다.",
    "손절각": "관계를 끊어야 할 시기라는 뜻입니다.",
    "빠끄": "빠르게 끝내자는 의미로 쓰입니다.",
    "실화냐": "정말 사실이냐는 뜻입니다.",
    "갓생": "부지런하고 바람직한 생활을 한다는 뜻입니다.",
    "쿠크다스 멘탈": "멘탈이 약하다는 의미입니다.",
    "꽁꽁 얼어붙은 한강 위로 고양이가 걸어 다닙니다":"한국의 한 뉴스에서 나온 기자의 말로, 리듬감과 귀여운 고양이의 모습이 화제가 되어 밈이 되었습니다.",
    "퉁퉁퉁퉁퉁퉁퉁퉁퉁 사후르":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다."
}

sentence = st.text_input("밈 문장을 입력하세요:")

if st.button("번역하기") or sentence:
    result = []
    for word, meaning in dictionary.items():
        if word in sentence:
            result.append(f"👉 **{word}**: {meaning}")
    
    if result:
        for r in result:
            st.success(r)
    elif sentence:
        st.warning("밈을 찾지 못했습니다. 다시 시도해보세요.")

st.markdown("---")
st.caption("제작: Open 에이아밈 탐구팀 | Streamlit 기반 밈 번역기")
