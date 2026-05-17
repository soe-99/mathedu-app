import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# =========================================================================
# 1. 페이지 레이아웃 및 Matplotlib 나눔고딕 폰트 강제 설정
# =========================================================================
st.set_page_config(layout="wide", page_title="공통수학1 - 행렬의 곱셈과 교환법칙")

# --- 다운로드받은 나눔고딕 폰트 파일 적용 로직 ---
font_path = "NanumGothic.ttf"  # 코드와 같은 폴더에 폰트 파일이 있어야 합니다.

if os.path.exists(font_path):
    # 폰트 속성 정의 및 추가
    font_prop = fm.FontProperties(fname=font_path)
    plt.rc('font', family=font_prop.get_name())
else:
    # 폰트 파일이 없을 때를 대비한 시스템 폰트 백업
    plt.rc('font', family='Malgun Gothic')

# 마이너스 기호 깨짐 방지
plt.rc('axes', unicode_minus=False)

# =========================================================================
# 2. 메인 타이틀 및 설명
# =========================================================================
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

# =========================================================================
# 3. 두 가지 순서 비교 (시각화 및 연산)
# =========================================================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🟦 순서 1: $AB$")
    st.caption("💡 [회전 마법 $B$]로 먼저 회전한 후, 그 결과를 [확대 마법 $A$]로 늘리기")
    
    run_ab = st.button("🔮 AB 계산하기", type="primary")
    
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
    
    run_ba = st.button("🔮 BA 계산하기")
    
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

# =========================================================================
# 4. 결론 출력
# =========================================================================
st.write("---")
st.error("### 📢 최종 결론: 두 도형의 최종 위치와 모양이 다릅니다! 즉, $AB \\neq BA$ (교환법칙 불성립)")