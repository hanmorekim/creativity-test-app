import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="창의성 셀프 조사", layout="wide")
st.title("🎨 창의성 셀프 조사 테스트")

# 30문항 리스트
questions = [
    "주위의 미묘한 변화를 잘 알아차린다.",
    "어떤 물건을 보고 다른 용도로 쓸 수 없을까 생각한다.",
    "남이 하지 않는 생각을 해내려고 노력한다.",
    "한 가지 정답보다는 여러 가지 가능성을 생각한다.",
    "아이디어가 막힘없이 술술 나오는 편이다.",
    "일을 시작하면 끝까지 철저하게 해낸다.",
    "호기심이 많아서 이것저것 잘 물어본다.",
    "고정관념을 깨는 것을 좋아한다.",
    "나만의 독특한 해결 방법을 찾는다.",
    "고집을 부리기보다 상황에 따라 생각을 바꾼다.",
    "연상되는 단어나 이미지가 풍부하다.",
    "엉성한 계획보다 치밀한 계획을 선호한다.",
    "분위기나 흐름을 민감하게 파악한다.",
    "쓸모없어 보이는 물건도 쓸모 있게 바꾼다.",
    "평범한 것보다 파격적인 것을 좋아한다.",
    "여러 분야의 지식을 연결해서 생각한다.",
    "대화할 때 다양한 화제를 끌어낼 수 있다.",
    "하나를 알아도 깊이 있게 파고든다.",
    "자연의 변화나 예술 작품에 감동을 잘 받는다.",
    "익숙한 것을 낯설게 보려고 시도한다.",
    "관습이나 전통에 얽매이지 않는다.",
    "이 생각 저 생각으로 옮겨가는 것이 빠르다.",
    "문장이나 그림을 풍부하게 표현한다.",
    "작은 부분도 소홀히 하지 않고 정성껏 다룬다.",
    "언제나 새로운 것을 추구하고 있다.",
    "사람들이 못보고 넘어간 곳을 읽어낸다.",
    "남과 다른 복장에 신경 안 쓴다.",
    "그럴 수도 있다고 늘 생각하는 편이다.",
    "상상이든 기존의 지식이든 쉽게 발상을 짐작 전개해 간다.",
    "도중에서 타협하지 않는다."
]

# 요소별 문항 매핑
categories = {
    "감수성 Sensitivity": [0, 6, 12, 18, 24],
    "재정의 Reidentification": [1, 7, 13, 19, 25],
    "독창성 Originality": [2, 8, 14, 20, 26],
    "유연성 Flexibility": [3, 9, 15, 21, 27],
    "유창성 Fluency": [4, 10, 16, 22, 28],
    "정교성/집중 Elaboration": [5, 11, 17, 23, 29]
}

# 설문 입력
scores = []
with st.form("survey"):
    st.write("각 문항을 읽고 1점(전혀 아니다) ~ 5점(매우 그렇다) 중 선택하세요.")
    for i, q in enumerate(questions):
        score = st.slider(f"{i+1}. {q}", 1, 5, 3)
        scores.append(score)
    submitted = st.form_submit_button("결과 보기")

if submitted:
    # 요소별 점수 합산
    results = {cat: sum(scores[i] for i in idxs) for cat, idxs in categories.items()}
    st.subheader("📊 결과 점수")
    st.write(results)

    # Radar Chart
    labels = list(results.keys())
    values = list(results.values())
    values += values[:1]  # 닫힌 도형을 위해 첫 값 반복

    angles = [n / float(len(labels)) * 2 * 3.14159 for n in range(len(labels))]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, 'skyblue', alpha=0.4)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticks([5,10,15,20,25])
    st.pyplot(fig)

    # 개선 가이드
    st.subheader("💡 개선을 위한 가이드")
    st.markdown("""
    - **감수성**: '왜?' 질문 5번 던지기. 귀차니즘을 벗어나기. 문제의식 호기심 갖기  
    - **재정의**: 여러가지 관점으로 보려고 노력하기  
    - **독창성**: 남과 다르려고 노력하기  
    - **유연성**: 고집을 내려놓기.엉뚱한 것도 받아드리기. 듣기연습  
    - **유창성**: 쉬지않고 생각하기. 5분 동안 아이디어 30개 적기 등,  
    - **정교성/집중**: 끈기를 갖고 노력하고 집중하기.  
    """)
