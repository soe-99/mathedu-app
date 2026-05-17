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
st.write("모든 행렬이 서로 곱해질 수 있는 것은 아닙니다. 아주 간단한 규칙 하나만 기억해 봅시다.")

# 핵심 조건을 수식 박스로 깔끔하게 분리
st.info(r"""
$$
A_{m \times \mathbf{n}} \times B_{\mathbf{n} \times p} = C_{m \times p}
$$
👉 **핵심 규칙** : 앞 행렬의 열(가로 칸수)과 뒤 행렬의 행(세로 칸수)인 안쪽 숫자(n)가 반드시 일치해야 합니다!
""")

st.markdown("#### ❌ [불가능 케이스] 데이터의 짝이 맞지 않는 경우")
col_err1, col_err2 = st.columns(2)

with col_err1:
    st.error("🧩 **구조적 예시** (1×2 행렬 × 1×2 행렬)")
    st.write(r"""
    $$
    A = \begin{pmatrix} 1 & 2 \end{pmatrix}_{1 \times \mathbf{2}} ,\quad B = \begin{pmatrix} 3 & 4 \end{pmatrix}_{1 \times \mathbf{2}}
    $$
    """)
    st.markdown("안쪽 숫자가 서로 다릅니다! (앞의 열은 **2**, 뒤의 행은 **1**). 가로줄을 세로로 돌려서 곱하려는데, 뒤 행렬에 세로줄이 없어서 짝이 맞지 않습니다.")

with col_err2:
    st.success("💡 **실생활로 이해하기**")
    st.markdown("""
    * **앞 행렬 (주문)** : 철수가 [떡볶이 1인분, 튀김 2개]를 주문함 (데이터 2개)
    * **뒤 행렬 (가격)** : 메뉴판에 [떡볶이 가격] 정보만 적혀 있음 (데이터 1개)
    
    👉 **결과** : 튀김 가격을 알 수 없어서 포스기 계산이 안 됩니다. 즉, 데이터의 짝이 맞지 않으면 수학적으로 **곱셈 불가능!**
    """)