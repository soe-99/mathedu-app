import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# [기본 설정] 1. 페이지 레이아웃 및 Matplotlib 마이너스 기호 설정
# =========================================================================
st.set_page_config(layout="wide", page_title="공통수학1 - 행렬의 곱셈")

# 시스템 폰트를 사용하므로 폰트 설정 제외, 마이너스 깨짐만 방지
plt.rc('axes', unicode_minus=False)

# =========================================================================
# [사이드바] 2. 수업 목차 구성
# =========================================================================
st.sidebar.title("🎓 수업 목차")
page = st.sidebar.radio("이동할 페이지", [
    "📝 0. 지난 시간 복습",
    "📊 1. 행렬의 곱셈 원리 (간식 계산)",
    "🔄 2. 교환법칙 성립 여부 (회전변환)",
    "🎯 3. 오늘의 형성 평가"
])

# =========================================================================
# PAGE 0: 지난 시간 복습
# =========================================================================
if page == "📝 0. 지난 시간 복습":
    st.title("📝 지난 시간에 무엇을 배웠나요?")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. 행렬(Matrix)의 뜻과 성분")
        st.write("숫자나 문자를 직사각형 모양으로 배열하여 괄호로 묶은 것")
        st.markdown("- **행(Row):** 행렬의 가로줄")
        st.markdown("- **열(Column):** 행렬의 세로줄")
        st.write(r"$$ A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} $$")
        
    with col2:
        st.subheader("2. 행렬의 덧셈, 뺄셈, 실수배")
        st.markdown("- **덧셈/뺄셈:** 크기가 같은 두 행렬에서 **대응하는 성분끼리** 계산")
        st.markdown("- **실수배 ($kA$):** 행렬의 **모든 성분에 공평하게 $k$배**를 수행")
        st.write(r"$$ 2 \cdot \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix} $$")

# =========================================================================
# PAGE 1: 행렬의 곱셈 원리 (간식 계산 - 수량 & 가격 커스텀 버전)
# =========================================================================
elif page == "📊 1. 행렬의 곱셈 원리 (간식 계산)":
    st.title("🛍️ 1. 행렬의 곱셈은 왜 필요할까?")
    st.write("---")
    
    st.subheader("💡 상황: 민수와 영희의 간식 주문")
    st.caption("※ 수량과 메뉴 가격을 자유롭게 변경하여 행렬의 실시간 변화를 관찰해 보세요.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🛒 수량 행렬 $A$ (사람 $\\times$ 메뉴)")
        minsu_tteok = st.number_input("민수 떡볶이 (인분)", min_value=0, max_value=10, value=2)
        minsu_fry = st.number_input("민수 튀김 (개)", min_value=0, max_value=10, value=3)
        younghee_tteok = st.number_input("영희 떡볶이 (인분)", min_value=0, max_value=10, value=1)
        younghee_fry = st.number_input("영희 튀김 (개)", min_value=0, max_value=10, value=5)
        
        st.write(f"$$ A = \\begin{{pmatrix}} {minsu_tteok} & {minsu_fry} \\\\ {younghee_tteok} & {younghee_fry} \\end{{pmatrix}} $$")
        
    with col2:
        st.markdown("### 💰 가격 행렬 $B$ (메뉴 $\\times$ 가격)")
        # 선생님의 요청대로 가격도 직접 입력 및 수정 가능하도록 변경 (기본값 제공)
        price_tteok = st.number_input("떡볶이 1인분 가격 (원)", min_value=0, max_value=10000, value=3000, step=500)
        price_fry = st.number_input("튀김 1개 가격 (원)", min_value=0, max_value=10000, value=500, step=100)
        
        st.write(f"$$ B = \\begin{{pmatrix}} {price_tteok} \\\\ {price_fry} \\end{{pmatrix}} $$")
  
    st.write("---")
    st.subheader("🧮 총 금액 계산하기")
    
    if st.button("💰 민수와 영희의 총 금액 계산하기", type="primary"):
        col3, col4 = st.columns(2)
        
        # 입력받은 가격 변수를 실시간 연산에 반영
        ans_minsu = (minsu_tteok * price_tteok) + (minsu_fry * price_fry)
        ans_younghee = (younghee_tteok * price_tteok) + (younghee_fry * price_fry)
        
        with col3:
            st.info("### 🙋‍♂️ 민수의 총액 (1행 $\\times$ 1열)")
            st.write(f"$$ ({minsu_tteok} \\times {price_tteok}) + ({minsu_fry} \\times {price_fry}) = {ans_minsu}\\text{{원}} $$")
        with col4:
            st.success("### 🙋‍♀️ 영희의 총액 (2행 $\\times$ 1열)")
            st.write(f"$$ ({younghee_tteok} \\times {price_tteok}) + ({younghee_fry} \\times {price_fry}) = {ans_younghee}\\text{{원}} $$")
            
        st.write("### 🎯 계산 결과 행렬 $AB$")
        st.write(f"$$ AB = \\begin{{pmatrix}} {ans_minsu} \\\\ {ans_younghee} \\end{{pmatrix}} $$")
        st.markdown("👉 **규칙 발견:** 앞 행렬의 **가로(행)**와 뒤 행렬의 **세로(열)**를 순서대로 곱해서 더한다!")

# =========================================================================
# PAGE 2: 교환법칙 성립 여부 (회전변환 - 중간 과정 및 영역 시각화 버전)
# =========================================================================
elif page == "🔄 2. 교환법칙 성립 여부 (회전변환)":
    st.title("⚔️ 2. 행렬의 곱셈과 교환법칙 ($AB$ vs $BA$)")
    st.write("---")
    st.write("행렬의 곱셈은 도형을 움직이는 **'연속 마법'**입니다. 순서를 바꾸면 결과가 어떻게 달라지는지 눈으로 확인해 보세요!")
    
    # 가로 1, 세로 2 크기의 직사각형 정의 (꼭짓점 5개로 닫힌 경로)
    rect_points = np.array([
        [0, 0], [1, 0], [1, 2], [0, 2], [0, 0]
    ]).T  # Shape: (2, 5)

    # 변환 행렬 정의
    B = np.array([[0, -1], [1, 0]])  # 90도 회전변환 행렬
    A = np.array([[2, 0], [0, 1]])   # X축 2배 확대변환 행렬
    
    # 마법 정보 안내 상자
    st.info("""
    ### 🔮 이번 실험에 사용할 두 가지 행렬 마법
    * **확대 마법 $A$** : $\\begin{pmatrix} 2 & 0 \\\\ 0 & 1 \\end{pmatrix}$ ➔ **X축 방향(가로)으로 도형을 2배 늘리는 마법**
    * **회전 마법 $B$** : $\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}$ ➔ **도형을 원점 기준으로 반시계 방향 90도 회전시키는 마법**
    """)
    st.write("")

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🟦 순서 1: $AB$")
        st.caption("💡 [회전 마법 $B$]로 먼저 회전한 후, 그 결과를 [확대 마법 $A$]로 늘리기")
        
        run_ab = st.button("🔮 AB 마법 부리기", type="primary")
        
        fig, ax = plt.subplots(figsize=(5, 5))
        
        # 1. 원래 직사각형 형태를 명확하게 시각화 (회색 채우기 + 실선)
        ax.fill(rect_points[0], rect_points[1], color='#E0E0E0', alpha=0.5)
        ax.plot(rect_points[0], rect_points[1], '#555555', linewidth=2, linestyle='-', label='Original (가로1, 세로2)')
        
        if run_ab:
            # 1단계: 회전 마법(B)만 먼저 적용한 중간 형태
            pts_step1 = B @ rect_points
            ax.plot(pts_step1[0], pts_step1[1], color='#FFA500', linewidth=2, linestyle='--', label='1단계: 회전(B) 완료')
            
            # 2단계: 그 결과에 확대 마법(A)까지 최종 적용
            pts_final = A @ pts_step1
            ax.plot(pts_final[0], pts_final[1], 'blue', linewidth=3, marker='o', label='2단계: 최종 확대(AB)')
            
        # 그래프 격자 및 축 설정
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.set_xlim(-4, 4)
        ax.set_ylim(-4, 4)
        ax.set_aspect('equal')
        ax.legend(loc='upper right', fontsize='small')
        st.pyplot(fig)
        
        if run_ab:
            st.success("**[대수적 계산 결과]**")
            st.write(r"$$ AB = A \times B = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix} $$")
            
    with col2:
        st.markdown("### 🟩 순서 2: $BA$")
        st.caption("💡 [확대 마법 $A$]로 먼저 늘린 후, 그 결과를 [회전 마법 $B$]로 회전하기")
        
        run_ba = st.button("🔮 BA 마법 부리기")
        
        fig, ax = plt.subplots(figsize=(5, 5))
        
        # 1. 원래 직사각형 형태를 명확하게 시각화 (회색 채우기 + 실선)
        ax.fill(rect_points[0], rect_points[1], color='#E0E0E0', alpha=0.5)
        ax.plot(rect_points[0], rect_points[1], '#555555', linewidth=2, linestyle='-', label='Original (가로1, 세로2)')
        
        if run_ba:
            # 1단계: 확대 마법(A)만 먼저 적용한 중간 형태
            pts_step1 = A @ rect_points
            ax.plot(pts_step1[0], pts_step1[1], color='#17A2B8', linewidth=2, linestyle='--', label='1단계: 확대(A) 완료')
            
            # 2단계: 그 결과에 회전 마법(B)까지 최종 적용
            pts_final = B @ pts_step1
            ax.plot(pts_final[0], pts_final[1], 'green', linewidth=3, marker='o', label='2단계: 최종 회전(BA)')
            
        # 그래프 격자 및 축 설정
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.set_xlim(-4, 4)
        ax.set_ylim(-4, 4)
        ax.set_aspect('equal')
        ax.legend(loc='upper right', fontsize='small')
        st.pyplot(fig)
        
        if run_ba:
            st.success("**[대수적 계산 결과]**")
            st.write(r"$$ BA = B \times A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 2 & 0 \end{pmatrix} $$")
            
    st.write("---")
    st.error("### 📢 최종 결론: 두 도형의 최종 위치와 모양이 다릅니다! 즉, $AB \\neq BA$ (교환법칙 불성립)")
# =========================================================================
# PAGE 3: 오늘의 형성 평가
# =========================================================================
elif page == "🎯 3. 오늘의 형성 평가":
    st.title("🎯 오늘의 형성 평가 퀴즈")
    st.write("---")
    st.markdown("#### [문제] 두 행렬 $A$와 $B$의 크기가 다음과 같을 때, 옳은 설명을 고르세요.")
    st.markdown("- 행렬 $A$의 크기: $3 \\times \\mathbf{2}$")
    st.markdown("- 행렬 $B$의 크기: $\\mathbf{2} \\times 4$")
    
    quiz_ans = st.radio("선택지:", [
        "1. A × B는 앞의 열(2)과 뒤의 행(2)의 개수가 달라서 계산할 수 없다.",
        "2. A × B는 계산이 가능하며, 순서를 바꾼 B × A도 항상 같은 결과가 나온다.",
        "3. A × B는 계산이 가능하지만, 순서를 바꾼 B × A는 크기 조건이 맞지 않아 정의되지 않는다. 즉, 교환법칙이 성립하지 않는다."
    ])
    
    if st.button("정답 확인하기", type="primary"):
        if "3." in quiz_ans:
            st.balloons()  # 축하 폭죽 효과
            st.success("🎉 정답입니다! 행렬의 연산 조건과 교환법칙의 성질을 완벽하게 이해하셨네요!")
        else:
            st.error("❌ 다시 한번 안쪽 크기 숫자를 차분하게 비교해 보세요!")