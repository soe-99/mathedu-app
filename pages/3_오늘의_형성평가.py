import streamlit as st

# =========================================================================
# 1. 페이지 레이아웃 및 기본 설정
# =========================================================================
st.set_page_config(layout="wide", page_title="공통수학1 - 오늘의 형성 평가")

# =========================================================================
# 2. 메인 타이틀 및 문제 출제
# =========================================================================
st.title("🎯 오늘의 형성 평가 퀴즈")
st.write("---")

st.markdown("### 📝 [원리 적용] 도전! 실생활 2×2 행렬 곱셈 계산하기")
st.write("이제 조건에 맞는 정상적인 **2×2 행렬과 2×2 행렬의 곱셈**을 실생활에 적용해 봅시다. 철수와 지수가 간식을 주문하려고 하는데, 집 앞 **[A분식]과 [B분식]의 가격을 비교**하여 총 금액 행렬을 구해봅시다.")

# 상황 조건 제시
st.info("""
**📌 주문 및 가격 상황 (2×2 행렬 구조)**
* **수량 행렬 $X$** : 철수와 지수(2명)가 각각 [떡볶이, 튀김]을 주문한 수량
* **가격 행렬 $Y$** : [A분식, B분식] 두 가게의 [떡볶이, 튀김] 메뉴별 단가표
""")

# 문제 행렬의 시각화 (2x2 × 2x2 구조 강조)
col_q1, col_q2 = st.columns(2)

with col_q1:
    st.markdown("<center><b>🛍️ 앞 행렬: 수량 행렬 $X$ (사람 × 메뉴)</b></center>", unsafe_allow_html=True)
    st.write(r"""
    $$
    X = \begin{pmatrix} 
    1 & 2 \\ 
    3 & 1 
    \end{pmatrix}_{2 \times \mathbf{2}}
    \begin{matrix}
    \leftarrow \text{철수 주문 (떡볶이 1, 튀김 2)} \\
    \leftarrow \text{지수 주문 (떡볶이 3, 튀김 1)}
    \end{matrix}
    $$
    """)

with col_q2:
    st.markdown("<center><b>💰 뒤 행렬: 가격 행렬 $Y$ (메뉴 × 가게)</b></center>", unsafe_allow_html=True)
    st.write(r"""
    $$
    Y = \begin{pmatrix} 
    3000 & 2500 \\ 
    500 & 700 
    \end{pmatrix}_{\mathbf{2} \times 2}
    \begin{matrix}
    \leftarrow \text{떡볶이 가격 (A점: 3000원 / B점: 2500원)} \\
    \leftarrow \text{튀김 가격 (A점: 500원 / B점: 700원)}
    \end{matrix}
    $$
    """)

st.write("")
st.markdown("""
<div style='background-color: #f0f2f6; padding: 15px; border-radius: 5px;'>
💡 <b>생각해보기 (교과서 핵심):</b><br>
앞 행렬 X의 가로줄(철수의 주문)과 뒤 행렬 Y의 세로줄(A분식의 가격)을 매칭하면 <b>철수가 A분식에서 주문했을 때의 총액</b>이 나옵니다.<br>
그렇다면 <b>철수가 B분식에서 주문했을 때의 총액</b>은 결과 행렬에서 몇 행 몇 열의 자리에 들어가게 될까요?
</div>
""", unsafe_allow_html=True)

st.write("")
user_ans = st.number_input("🧩 행렬 곱셈 규칙을 적용했을 때, '철수의 A분식 총 금액(1행 1열 성분)'은 얼마일까요? (원)", min_value=0, value=0, step=500)

if st.button("🔮 정답 및 행렬 연산 풀이 보기", type="primary"):
    # 실제 정답 연산 (2x2 결과)
    ans_chul_A = (1 * 3000) + (2 * 500)     # 4000
    ans_chul_B = (1 * 2500) + (2 * 700)     # 3900
    ans_ji_A = (3 * 3000) + (1 * 500)       # 9500
    ans_ji_B = (3 * 2500) + (1 * 700)       # 8200
    
    if user_ans == ans_chul_A:
        st.balloons()
        st.success(f"🎉 정답입니다! 철수의 A분식 주문 금액 {ans_chul_A:,}원을 정확하게 계산하셨습니다.")
    else:
        st.error(f"❌ 값이 조금 다르네요! 철수의 주문(1행)과 A분식의 가격(1열)을 다시 차근차근 매칭해 볼까요?")
    
    st.markdown("#### 🧮 전체 결과 행렬 $XY$ 도출 과정 (2×2)")
    st.write(r"""
    $$
    XY = \begin{pmatrix} 
    1 & 2 \\ 
    3 & 1 
    \end{pmatrix} 
    \begin{pmatrix} 
    3000 & 2500 \\ 
    500 & 700 
    \end{pmatrix}
    $$
    """)
    st.write(r"""
    $$
    = \begin{pmatrix}
    (1 \times 3000 + 2 \times 500) & (1 \times 2500 + 2 \times 700) \\
    (3 \times 3000 + 1 \times 500) & (3 \times 2500 + 1 \times 700)
    \end{pmatrix}
    = \begin{pmatrix}
    4000 & 3900 \\
    9500 & 8200
    \end{pmatrix}_{2 \times 2}
    $$
    """)
    
    # 결과 해석으로 원리 마무리
    st.markdown(f"""
    * **1행 (철수의 영수증)** : A분식에서 먹으면 **{ans_chul_A:,}원**, B분식에서 먹으면 **{ans_chul_B:,}원**
    * **2행 (지수의 영수증)** : A분식에서 먹으면 **{ans_ji_A:,}원**, B분식에서 먹으면 **{ans_ji_B:,}원**
    
    👉 **최종 정리** : 2×2 행렬끼리 곱했더니 최종 결과도 **2×2 행렬**이 되었습니다. 
    행렬 곱셈 단 한 번으로 **두 사람의 주문량에 따른 두 가게의 가격 비교 데이터**를 한눈에 표로 정리할 수 있게 되었습니다!
    """)