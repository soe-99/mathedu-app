import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# 1. 페이지 레이아웃 및 Matplotlib 설정
# =========================================================================
st.set_page_config(layout="wide", page_title="공통수학1 - 행렬의 곱셈과 교환법칙")

# 마이너스 기호 깨짐 방지 (영문 폰트 기본 매칭으로 한글 폰트 에러 원천 차단)
plt.rc('axes', unicode_minus=False)

# =========================================================================
# 2. 메인 타이틀 및 개요
# =========================================================================
st.title("📐 2. 행렬의 곱셈과 교환법칙 ($AB$ vs $BA$)")
st.write("---")
st.write("행렬의 곱셈은 기하학적으로 도형을 변환시키는 연속적인 사상(Mapping)입니다. 두 선형변환의 합성 순서를 바꿨을 때 결과가 어떻게 달라지는지 확인해 보세요.")

# 가로 1, 세로 2 크기의 직사각형 정의 (꼭짓점 5개로 닫힌 경로)
rect_points = np.array([
    [0, 0], [1, 0], [1, 2], [0, 2], [0, 0]
]).T  # Shape: (2, 5)

# 변환 행렬 정의
B = np.array([[0, -1], [1, 0]])  # 원점 기준 90도 회전변환 행렬
A = np.array([[2, 0], [0, 1]])   # x축 방향 2배 확대변환 행렬

# 변환 행렬 정보 정의
st.info("""
### 📊 실험에 사용될 선형변환 행렬 정의
* **확대변환 행렬 $A$** : $\\begin{pmatrix} 2 & 0 \\\\ 0 & 1 \\end{pmatrix}$ ➔ **$x$축 방향으로 도형을 2배 확대하는 변환**
* **회전변환 행렬 $B$** : $\\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}$ ➔ **원점을 기준으로 반시계 방향으로 90도 회전하는 변환**
""")
st.write("")

# =========================================================================
# 3. 합성 순서에 따른 변환 비교 (시각화 및 연산)
# =========================================================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🟦 순서 1: $AB$")
    st.caption("💡 $B$를 먼저 적용하여 회전변환을 수행한 후, 그 결과에 $A$를 적용하여 확대변환을 수행")
    
    run_ab = st.button("연산 및 시각화 (AB)", type="primary")
    
    fig, ax = plt.subplots(figsize=(5, 5))
    
    # 1. 초기 도형 시각화 (영문 label 사용으로 한글 깨짐 방지)
    ax.fill(rect_points[0], rect_points[1], color='#E0E0E0', alpha=0.5)
    ax.plot(rect_points[0], rect_points[1], '#555555', linewidth=2, linestyle='-', label='Original')
    
    if run_ab:
        # 1단계: 회전변환(B) 적용
        pts_step1 = B @ rect_points
        ax.plot(pts_step1[0], pts_step1[1], color='#FFA500', linewidth=2, linestyle='--', label='Step 1: B (Rotation)')
        
        # 2단계: 확대변환(A) 합성
        pts_final = A @ pts_step1
        ax.plot(pts_final[0], pts_final[1], 'blue', linewidth=3, marker='o', label='Step 2: AB (Composite)')
        
    # 그래프 격자 및 축 설정
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.legend(loc='upper right', fontsize='small')
    st.pyplot(fig)
    
    # 그래프 하단 한글 텍스트 가이드
    st.markdown("📌 도형 변환 단계: 초기 도형(가로1, 세로2) " + ("➔ 주황색 점선(회전변환 완료) ➔ **파란색 실선(최종 합성변환 $AB$)**" if run_ab else ""))
    
    if run_ab:
        st.success("**[대수적 계산 결과]**")
        st.write(r"$$ AB = A \times B = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -2 \\ 1 & 0 \end{pmatrix} $$")
        
with col2:
    st.markdown("### 🟩 순서 2: $BA$")
    st.caption("💡 $A$를 먼저 적용하여 확대변환을 수행한 후, 그 결과에 $B$를 적용하여 회전변환을 수행")
    
    run_ba = st.button("연산 및 시각화 (BA)")
    
    fig, ax = plt.subplots(figsize=(5, 5))
    
    # 1. 초기 도형 시각화
    ax.fill(rect_points[0], rect_points[1], color='#E0E0E0', alpha=0.5)
    ax.plot(rect_points[0], rect_points[1], '#555555', linewidth=2, linestyle='-', label='Original')
    
    if run_ba:
        # 1단계: 확대변환(A) 적용
        pts_step1 = A @ rect_points
        ax.plot(pts_step1[0], pts_step1[1], color='#17A2B8', linewidth=2, linestyle='--', label='Step 1: A (Scaling)')
        
        # 2단계: 회전변환(B) 합성
        pts_final = B @ pts_step1
        ax.plot(pts_final[0], pts_final[1], 'green', linewidth=3, marker='o', label='Step 2: BA (Composite)')
        
    # 그래프 격자 및 축 설정
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.legend(loc='upper right', fontsize='small')
    st.pyplot(fig)
    
    # 그래프 하단 한글 텍스트 가이드
    st.markdown("📌 **도형 변환 단계:** 초기 도형(가로1, 세로2) " + ("➔ 하늘색 점선(확대변환 완료) ➔ **초록색 실선(최종 합성변환 $BA$)**" if run_ba else ""))
    
    if run_ba:
        st.success("**[대수적 계산 결과]**")
        st.write(r"$$ BA = B \times A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 2 & 0 \end{pmatrix} $$")

# =========================================================================
# 4. 결론 출력
# =========================================================================
st.write("---")
st.error("### 📢 최종 결론: 일반적인 행렬의 곱셈에서 교환법칙은 성립하지 않습니다. ($AB \\neq BA$)")