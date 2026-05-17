import streamlit as st

# =========================================================================
# 1. 페이지 레이아웃 및 기본 설정
# =========================================================================
st.set_page_config(layout="wide", page_title="공통수학1 - 행렬의 곱셈 원리")

# =========================================================================
# 2. 메인 타이틀 및 상황 설명
# =========================================================================
st.title("🛍️ 1. 행렬의 곱셈은 왜 필요할까?")
st.write("---")

st.subheader("💡 상황: 민수와 영희의 간식 주문")
st.caption("※ 수량과 메뉴 가격을 자유롭게 변경하여 행렬의 실시간 변화를 관찰해 보세요.")

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
    
    # 수량 행렬 A 시각화
    st.write(f"$$ A = \\begin{{pmatrix}} {minsu_tteok} & {minsu_fry} \\\\ {younghee_tteok} & {younghee_fry} \\end{{pmatrix}} $$")
    
with col2:
    st.markdown("### 💰 가격 행렬 $B$ (메뉴 $\\times$ 가격)")
    price_tteok = st.number_input("떡볶이 1인분 가격 (원)", min_value=0, max_value=10000, value=3000, step=500)
    price_fry = st.number_input("튀김 1개 가격 (원)", min_value=0, max_value=10000, value=500, step=100)
    
    # 가격 행렬 B 시각화
    st.write(f"$$ B = \\begin{{pmatrix}} {price_tteok} \\\\ {price_fry} \\end{{pmatrix}} $$")

# =========================================================================
# 4. 연산 및 결과 출력
# =========================================================================
st.write("---")
st.subheader("🧮 총 금액 계산하기")

if st.button("💰 민수와 영희의 총 금액 계산하기", type="primary"):
    col3, col4 = st.columns(2)
    
    # 입력받은 수량과 가격 변수를 실시간 연산에 반영
    ans_minsu = (minsu_tteok * price_tteok) + (minsu_fry * price_fry)
    ans_younghee = (younghee_tteok * price_tteok) + (younghee_fry * price_fry)
    
    with col3:
        st.info("### 🙋‍♂️ 민수의 총액 (1행 $\\times$ 1열)")
        st.write(f"$$ ({minsu_tteok} \\times {price_tteok}) + ({minsu_fry} \\times {price_fry}) = {ans_minsu:,}\\text{{원}} $$")
        
    with col4:
        st.success("### 🙋‍♀️ 영희의 총액 (2행 $\\times$ 1열)")
        st.write(f"$$ ({younghee_tteok} \\times {price_tteok}) + ({younghee_fry} \\times {price_fry}) = {ans_younghee:,}\\text{{원}} $$")
        
    st.write("### 🎯 계산 결과 행렬 $AB$")
    st.write(f"$$ AB = \\begin{{pmatrix}} {ans_minsu:,} \\\\ {ans_younghee:,} \\end{{pmatrix}} $$")
    st.markdown("👉 **규칙 발견:** 앞 행렬의 **가로(행)**와 뒤 행렬의 **세로(열)**를 순서대로 곱해서 더한다!")