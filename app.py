import streamlit as st
import re  # 문장 정제에 필요한 모듈

st.set_page_config(page_title="AI 밈 번역기", page_icon="🧠", layout="centered")

st.title("🧠 AI 기반 X 밈 번역기")
st.write("인간이 직접 밈을 번역해드립니다! 당신이 알고있는 밈을 입력해주세요.(정확하게 입력해 주셔야 알아볼 수 있습니다.)")
# 밈 사전
dictionary = {
    "킹받네": "열받는다에서 조금 더 짜증날 때 쓰는 말입니다.",
    "손절각": "관계를 끊어야 할 시기라는 뜻입니다.",
    "손절":"원래 주식커뮤니티에서 손해 보기 전에 주식 빼라라는 뜻으로 쓰였으나 현재는 인간관계에서 별로 좋지 못한 사람과 절교하는 의미로 널리 쓰입니다.",
    "빠끄": "빠르게 끝내자는 의미로 쓰입니다.",
    "실화냐": "정말 사실이냐는 뜻입니다.",
    "갓생": "부지런하고 바람직한 생활을 한다는 뜻입니다.",
    "쿠크다스 멘탈": "멘탈이 약하다는 의미입니다.",
    "꽁꽁 얼어붙은 한강 위로 고양이가 걸어 다닙니다":"한국의 한 뉴스에서 나온 기자의 말로, 리듬감과 귀여운 고양이의 모습이 화제가 되어 밈이 되었습니다.",
    "퉁퉁퉁퉁퉁퉁퉁퉁퉁 사후르":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다. 큰눈과 항상 들고 있는 야구 방망이가 인상적이며 캐릭터 중 가장 셉니다.",
    "봄바르디로 크로코딜로":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다.폭격기 머리 부분에 악어머리가 달려 있습니다.",
    "트랄랄레로 트랄랄라":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다.나이키 운동화 신은 상어의 모습을 하고 있습니다.",
    "리릴리 라릴라":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다. 샌들 신은 선인장 코끼리 입니다.",
    "침판지니 바나니니":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다. 바나나 안에 침팬지가 들어 있습니다.",
    "카푸치노 아싸시노":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다. 카푸치노인데 닌자 입니다.",
    "브르르 브르르 파타핌":"이탈리안 브레인 러트의 캐릭터 중 하나 입니다. 다리에 풀이 자라는 코주부 원숭이의 모습을 하고 있습니다.",
    "얼죽아":"얼어죽어도 아이스 아메리카노의 줄임말 입니다.",
    "갓생":"정말 개쩌는 인생을 일컫는 말입니다.",
    "중꺾마":"중요한 것은 꺾이지 않는 마음의 줄임말 입니다.",
    "스불재":"스스로 불러온 재앙의 줄임말 입니다.",
    "chil guy":"2024년 후반부터 필립 뱅크스가 창작한 캐릭터를 중심으로 낙관주의를 표방하여 퍼지고 있는 인터넷 밈입니다.",
    "오운완":"오늘 운동 완료의 줄임말 입니다. 멸치나 헬창들이 주로 쓰는 말입니다",
    "헬창":"헬스에 몸바친 사람들을 뜻하며 원래 비속어이지만 요즘에는 그 본래 뜻이 많이 연해졌습니다.",
    "알잘딱깔센":"알아서 잘 딱 깔끔하고 센스있게 좀 해라.",
    "할많하않":"할 말은 많지만 하지 않겠다.의 줄임말 입니다. 요즘엔 발음하기 어려워서 잘 안쓰는 듯.",
    "낄끼빠빠":"낄 때 끼고 빠질 때 빠져의 줄임말입니다.",
    "에겐남":"에스트로겐 많이 나오는 남자의 줄임말으로 여리여리한 남자들을 일컫습니다.",
    "테토남":"테스토스테론 많이 나오는 남자의 줄임말으로 근육이 많고 활동적인 남자들을 일컫습니다.",
    "에겐녀":"에스트로겐 많이 나오는 여자의 줄임말로 여리여리한 여자들을 일컫습니다.",
    "테토녀":"테스토스테론 많이 나오는 여자의 줄임말로 근육이 있고 활동적인 여자들을 일컫습니다.",
    "tmi":"to much information의 줄임말입니다.",
    "자낳괴":"자본주의가 낳은 괴물이라는 뜻입니다.",
    "느좋":"느낌 좋은 의 줄임말 입니다. \'느좋녀\'와 \'느좋남\'은..뭔 뜻인지 알겠죠?",
    "무야호":"???:그만큼 신나신다는 거지.",
    "빵빵아":"옥지얌!",
    "어쩔티비":"어쩌라고 가서 티비나 봐 의 줄임말 입니다.",
    "쿠쿠루삥뽕":"주로 인터넷 방송 플랫폼에서 웃음 소리나 도네이션을 할 때 사용되는 말입니다.",
    "듣보잡":"듣도보도 못한 잡것 이란 뜻입니다.",
    "현타":"현실 자각 타임 이란 뜻입니다.",
    "한잔해":"시험 이 사이트 개발자보다 잘봤잖아 한잔해.",
    "잼민이":"초등학생을 악간 비하하는 표현입니다.",
    "급식충":"학생을 급식이나 먹는 벌레라고 보는 학생 비하 표현입니다.",
    "멈춰":"학교폭력 멈춰!",
    "이제 이 차는 제겁니다.":"제 마음대로 팔 수 있는 겁니다.",
    "나유":"사랑해",
    "ㄹㅇㅋㅋ":"아 잘 모르겠음 ㄹㅇㅋㅋ만 치라고 ㅋㅋ",
    "님아":"님아..그건 좀...",
    "야 개 짖는 소리 좀 안 나게 하라":"컬투쇼에서 소개되었던 사연으로 개 짖는 소리에 빡친 아저씨의 음성이 밈이 되었습니다.",
    "국뽕":"자국에 대한 환상에 도취되어 자국을 찬양하는 행태를 뜻하는 인터넷 신조어로, 국가와 헤로인의 합성어 입니다.",
    "너 때문에 흥이 다 깨져버렸으니까 책임져":"예 알겠습니다. 디오니소스 님",
    "더 이상의 자세한 설명은 생략한다.":"김성모의 만화에서 나오는 대사로, 모방범죄의 위험을 막기 위해 사용한 컷이 밈이 되었습니다.",
    "안녕하세요 스위트":"걸이에요",
    "군침이 싹도노":"루피의 사진을 사악하게 비웃는 표정으로 합성한 밈에서 파생된 밈입니다.",
    "오타쿠":"일본 애니메이션풍 컨텐츠 서브컬처 문화를 취미로 하는 사람을 일컫습니다.", 
    "씹덕":"오타쿠의 멸칭입니다.",
    "그뭔씹":"그게 뭔데 씹덕아의 줄임말로 주로 쓸데없는 정보가 올라올 때 이를 풍자하기 위해 쓰입니다.",
    "너 t야?":"mbti가 유행하고 나서 나온 밈으로 차가운 사람에게 너 mbti에서 t(이성적)니?라고 물으며 까는 것입니다.",
    "뇌절":"1절만 하자라는 말에서 나온 밈으로 과장되거나 불필요한 행동을 가리키는 말입니다.",
    "뉴진스의 하입보이요":"커즈아아 아 아이 노 왓츄 라이크 보이~",
    "당근을 흔들어 주세요":"납치되었다고 의심되는 만화가나 일러스트레이터에게 당근을 그려주세요 라고 말하는 드립의 일종입니다.",
    "마라탕후루":"그럼 제가 선배 맘에 탕탕 후루 후루 탕탕 탕 후루루루~",
    "bts,봉준호,손흥민":"Jay Park, let's go!",
    "상상도 못한 정체":"복면가왕에서 복면 가수가 자신의 정체를 공개 했을 때 신봉선이 보였던 리액션으로, 이후 유명해지며 밈이 되었습니다.",
    "알파메일":"주로 무리에서 리더를 맡고 인싸 재질을 가진 남성을 말합니다.",
    "알파피메일":"주로 무리에서 리더를 맡고 인싸 재질을 가진 여성을 말합니다.",
    "알빠노":"내 알 바 아니다 라는 뜻이며 롤 인터넷 방송에서 처음 등장했습니다.",
    "와 샌즈":"언더테일 아시는구나! 혹시 모르시는분들에 대해 설명해드립니다 샌즈랑 언더테일의 세 가지 엔딩루트중 몰살엔딩의 최종보스로 진.짜.겁.나.어.렵.습.니.다", 
    "이왜진":"이게 왜 진짜임의 뜻으로 쓰입니다.",
    "자강두천":"자존심 강한 두 천재의 대결의 줄임말입니다.",
    "장충동왕족발보쌈":"말왕이 부른 장충동왕족발보쌈 cm송에 오케스트라를 입힌 영상이 알고리즘을 타면서 밈이 되었습니다.",
    "창렬":"가굑에 비해 양이나 품질이 터무니없이 떨어져 제 값을 못하는 상품 혹은 그러한 상태를 뜻합니다.가수 김창열이 광고 모텡이 된 편의점 음식으로 인해 유래한 신조어입니다.",
    "탈룰라":"영화 쿨 러닝에서 나온 장면에서 파생된 인터넷 밈입니다. 의도치않게 상대의 부모욕을 한 사람이 빠르게 태세 전환하여 상황을 수습하는 모습을 표현할 때 쓰입니다.",
    "트롤":"관심 끌기, 관심 유발, 남을 화나게 하기 등을 일부러 하며 이런 행위를 오히려 즐기는 것을 뜻하는 인터넷 밈입니다.",
    "햄부기햄북 햄북어 햄북스딱스 함부르크햄부가우가 햄비기햄부거 햄부가티햄부기온앤 온":"햄부기햄북 햄북어 햄북수딱수 함부르크햄부가우가 햄비기햄부거 함부가티햄부기온앤 온을 차려오라고 하지 않앗으냐.",
    "호박고구마":"드라마 거침없이 하이킥에서 나오는 나문희의 대사가 밈이 된 것입니다."
}
sentence = st.text_input("밈 문장을 입력하세요:")

if st.button("번역하기") or sentence:
    # ✅ 문장 전처리: 소문자화 + 특수문자 제거
    cleaned_sentence = re.sub(r"[^\w\s]", "", sentence.lower())

    result = []
    for word, meaning in dictionary.items():
        # 검색할 단어도 소문자화해서 비교 (대소문자 무시)
        if word.lower() in cleaned_sentence:
            result.append(f"👉 **{word}**: {meaning}")
    
    if result:
        for r in result:
            st.success(r)
    elif sentence:
        st.warning("밈을 찾지 못했습니다. 다시 시도해보세요.")

st.markdown("---")
st.caption("AI수준의 밈 해석은 준비 중입니다!")
st.caption("제작: Open 에이아밈 탐구팀 | Streamlit 기반 밈 번역기")
