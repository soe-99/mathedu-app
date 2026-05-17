import streamlit as st

# =========================================================================
# 1. 페이지 레이아웃 및 기본 설정
# =========================================================================
st.set_page_config(layout="wide", page_title="공통수학1 - 행렬의 곱셈 원리")

# =========================================================================
# 2. 메인 타이틀 및 상황 설명
# =========================================================================
st.title("🛍️ 1. 행렬의 곱셈 원리와 실생활 적용")
st.write("---")

st.subheader("💡 실생활 상황: 실시간 수량 및 가격 연산 예시")
st.caption("※ 수량과 메뉴 가격을 변경하며 대수적 구조의 변화를 관찰해 보세요.")

# =========================================================================
# 3. 입력 데이터 구성 (수량 행렬 A & 가격 행렬 B)
# =========================================================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛒 수량 행렬 $A$ (사람 $\\times$ 메뉴)")
    minsu_tteok = st.number_input("민수 떡볶이 (인분)", min_value=0, max_value=10, value=2)
    minsu_fry = st.number_input("민수 튀김 (개)", min_value=0, max_value=10, value=3)
    younghee_tteok = st.number_input("영희 떡볶이 (인분)", min_value=0, max_value=10, value=1)
    younghee_fry = st.number_input("영희 튀김 (개)", min_value=0, max_value=10, value=5)
    
    st.write(f"$$ A = \\begin{{pmatrix}} {minsu_tteok} & {minsu_fry} \\\\ {younghee_tteok} & {younghee_fry} \\end{{pmatrix}}_{{2 \\times \\mathbf{{2}}}} $$")
    
with col2:
    st.markdown("### 💰 가격 행렬 $B$ (메뉴 $\\times$ 가격)")
    price_tteok = st.number_input("떡볶이 1인분 가격 (원)", min_value=0, max_value=10000, value=3000, step=500)
    price_fry = st.number_input("튀김 1개 가격 (원)", min_value=0, max_value=10000, value=500, step=100)
    
    st.write(f"$$ B = \\begin{{pmatrix}} {price_tteok} \\\\ {price_fry} \\end{{pmatrix}}_{{\\mathbf{{2}} \\times 1}} $$")

# =========================================================================
# 4. 연산 및 결과 출력
# =========================================================================
st.write("---")
st.subheader("🧮 총 금액 계산하기")

calc_triggered = st.button("💰 민수와 영희의 총 금액 계산하기", type="primary")

if calc_triggered:
    col3, col4 = st.columns(2)
    
    ans_minsu = (minsu_tteok * price_tteok) + (minsu_fry * price_fry)
    ans_younghee = (younghee_tteok * price_tteok) + (younghee_fry * price_fry)
    
    with col3:
        st.info("### 🙋‍♂️ 민수의 총액 (1행 $\\times$ 1열)")
        st.write(f"$$ ({minsu_tteok} \\times {price_tteok}) + ({minsu_fry} \\times {price_fry}) = {ans_minsu:,}\\text{{원}} $$")
        
    with col4:
        st.success("### 🙋‍♀️ 영희의 총액 (2행 $\\times$ 1열)")
        st.write(f"$$ ({younghee_tteok} \\times {price_tteok}) + ({younghee_fry} \\times {price_fry}) = {ans_younghee:,}\\text{{원}} $$")
        
    st.write("### 🎯 계산 결과 행렬 $AB$")
    st.write(f"$$ AB = \\begin{{pmatrix}} {ans_minsu:,} \\\\ {ans_younghee:,} \\end{{pmatrix}}_{{2 \\times 1}} $$")
    st.markdown("👉 **연산 규칙:** 앞 행렬의 **행(가로줄)** 성분과 뒤 행렬의 **열(세로줄)** 성분을 순서대로 곱한 후 그 합을 구합니다.")

# =========================================================================
# 5. [교육과정 준수] 행렬의 곱셈 성립 조건 및 불가능 케이스
# =========================================================================
st.write("---")
st.markdown("### 🔍 2. 행렬의 곱셈이 정의되기 위한 조건")
st.write("모든 행렬이 서로 곱해질 수 있는 것은 아닙니다. 교과서 범위($2 \times 2$ 이하) 내에서 성립 조건을 알아봅시다.")

st.info(r"""
$$
A_{m \times \mathbf{n}} \times B_{\mathbf{n} \times p} = C_{m \times p}
$$
* **핵심 조건:** 앞 행렬의 **열(가로 칸수)**과 뒤 행렬의 **행(세로 칸수)**이 반드시 같아야 연산이 정의됩니다.
""")

# 불가능 케이스를 어렵지 않게, 딱 교과서 크기로 보여주기
st.markdown("#### ❌ [불가능 케이스] 데이터의 짝이 맞지 않는 경우")
col_err1, col_err2 = st.columns(2)

with col_err1:
    st.error(r"""
    **🧩 구조적 예시 ($1 \times 2$ vs $1 \times 2$)**
    * $A = \begin{pmatrix} 1 & 2 \end{pmatrix}_{1 \times \mathbf{2}}$, $B = \begin{pmatrix} 3 & 4 \end{pmatrix}_{1 \times 2}$
    * 두 행렬의 곱 $A \times B$를 시도하면?
    * 안쪽 숫자가 다릅니다: $\mathbf{2} \neq \mathbf{1}$
    * ➔ 가로 $[1, 2]$를 세로로 돌려서 곱하려는데, 뒤 행렬에는 세로줄이 없고 가로만 있습니다. 짝이 안 맞아서 **곱셈 불가능!**
    """)

with col_err2:
    st.success(r"""
    **💡 실생활로 이해하기**
    * **앞 행렬 (주문):** 철수가 [떡볶이 1인분, 튀김 2개]를 주문함. (데이터 2개)
    * **뒤 행렬 (가격):** 분식집에 [떡볶이 가격] 1개 정보만 적혀 있음. (데이터 1개)
    * ➔ **결과:** 튀김 가격을 알 수 없어서 포스기 계산이 안 됩니다. 즉, 앞의 열과 뒤의 행이 다르면 수학적으로 아예 에러가 납니다.
    """)


# =========================================================================
# 6. [교육과정 완벽 준수] 실생활 2x2 행렬 간의 곱셈 실제 적용 문제
# =========================================================================
st.write("---")
st.markdown("### 📝 [원리 적용] 도전! 실생활 2×2 행렬 곱셈 계산하기")
st.write("""
이제 조건에 맞는 정상적인 **$2 \times 2$ 행렬과 $2 \times 2$ 행렬의 곱셈**을 실생활에 적용해 봅시다. 
철수와 지수가 간식을 주문하려고 하는데, 집 앞 **[A분식]과 [B분식]의 가격을 비교**하여 총 금액 행렬을 구해봅시다.
""")

# 상황 조건 제시
st.info("""
**📌 주문 및 가격 상황 (2×2 행렬 구조)**
* **수량 행렬 $X$ :** 철수와 지수(2명)가 각각 [떡볶이, 튀김]을 주문한 수량
* **가격 행렬 $Y$ :** [A분식, B분식] 두 가게의 [떡볶이, 튀김] 메뉴별 단가표
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
<div style='background-color: #f0f2f6; padding: 12px; border-radius: 5px;'>
💡 <b>생각해보기 (교과서 핵심):</b><br>
앞 행렬 $X$의 가로줄(철수의 주문)과 뒤 행렬 $Y$의 세로줄(A분식의 가격)을 매칭하면 <b>철수가 A분식에서 주문했을 때의 총액</b>이 나옵니다.<br>
그렇다면 <b>철수가 B분식에서 주문했을 때의 총액</b>은 몇 행 몇 열의 자리에 들어가게 될까요?
</div>
""", unsafe_allow_html=True)

st.write("")
user_ans = st.number_input("🧩 행렬 곱셈 규칙을 적용했을 때, '철수의 A분식 총 금액(1행 1열 성분)'은 얼마일까요? (원)", min_value=0, value=0, step=500)

if st.button("🎯 정답 및 행렬 연산 풀이 보기", type="primary"):
    # 실제 정답 연산 (2x2 결과)
    ans_chul_A = (1 * 3000) + (2 * 500)     # 4000
    ans_chul_B = (1 * 2500) + (2 * 700)     # 3900
    ans_ji_A = (3 * 3000) + (1 * 500)       # 9500
    ans_ji_B = (3 * 2500) + (1 * 700)       # 8200
    
    if user_ans == ans_chul_A:
        st.balloons()
        st.success(f"🎉 정답입니다! 철수의 A분식 주문 금액 {ans_chul_A:,}원을 정확하게 계산하셨습니다.")
    
    st.markdown("#### 🧮 전체 결과 행렬 $XY$ 도출 과정 ($2 \times 2$)")
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
    * **1행 (철수의 영수증):** A분식에서 먹으면 **{ans_chul_A:,}원**, B분식에서 먹으면 **{ans_chul_B:,}원**
    * **2행 (지수의 영수증):** A분식에서 먹으면 **{ans_ji_A:,}원**, B분식에서 먹으면 **{ans_ji_B:,}원**
    
    👉 **결론:** $2 \times 2$ 행렬끼리 곱했더니 최종 결과도 **$2 \times 2$ 행렬**이 되었습니다. 
    행렬 곱셈 단 한 번으로 **두 사람의 주문량에 따른 두 가게의 가격 비교 데이터**를 한눈에 정리할 수 있게 되었습니다!
    """)