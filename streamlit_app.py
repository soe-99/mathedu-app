import streamlit as st

# 페이지 설정
st.set_page_config(page_title="자기소개", layout="wide")

# 사이드바 네비게이션
st.sidebar.title("📑 메뉴")
page = st.sidebar.radio("선택하세요:", ["소개", "학력", "연락처"])

# 메인 페이지
st.title("👋 자기소개 페이지")

if page == "소개":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/250", use_column_width=True)
    with col2:
        st.subheader("안녕하세요! 저는 김서연입니다.")
        st.write("""
        - 나이: 23
        - 전공: 수학과
        - 관심 분야: 교육, 콘텐츠 제작
        """)

    st.markdown("---")
    st.subheader("✨ 한 줄 소개")
    st.write("창의적인 문제 해결과 사람을 돕는 교육 콘텐츠 제작에 열정을 가진 학생입니다.")

    st.subheader("🎯 주요 강점")
    st.write("- 논리적인 사고와 문제 분석 능력")
    st.write("- 협업과 커뮤니케이션 능력")
    st.write("- 새로운 기술과 도구를 빠르게 배우는 적응력")

    st.subheader("📌 소개 글")
    st.write("""
    저는 수학과 전공으로 논리적 사고를 쌓았고, 교육과 콘텐츠 제작에 관심을 두고 있습니다.
    학생들의 학습 경험을 더 즐겁게 만들기 위해 다양한 방법을 고민하며 새로운 도전을 즐깁니다.
    """)

    st.subheader("🚀 현재 목표")
    st.write("- 데이터 기반 교육 콘텐츠 기획 및 제작 경험 쌓기")

elif page == "학력":
    st.subheader("📚 학력")
    st.write("**학력**")
    st.write("- 대학: 숙명여자대학교 ")
    st.write("- 전공: 수학과")

elif page == "연락처":
    st.subheader("📧 연락처")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**이메일:**xxxxx@sookmyung.ac.kr")
        st.write("**전화:** 010-xxxx-xxxx")

