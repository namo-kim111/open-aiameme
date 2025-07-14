
import streamlit as st

st.set_page_config(page_title="AI 밈 번역기", page_icon="🧠", layout="centered")

st.title("🧠 AI 밈 번역기")
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
    "퉁퉁퉁퉁퉁퉁퉁퉁퉁 사후르":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다. 큰눈과 항상 들고 있는 야구 방망이가 인상적이며 캐릭터 중 가장 셉니다.",
    "봄바르디로 크로코딜로":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다.폭격기 머리 부분에 악어머리가 달려 있습니다.",
    "트랄랄레로 트랄랄라":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다.",
    "얼죽아":"얼어죽어도 아이스 아메리카노의 줄임말 입니다.",
    "갓생":"정말 개쩌는 인생을 일컫는 말입니다.",
    "중꺾마":"중요한 것은 꺾이지 않는 마음의 줄임말 입니다."
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
