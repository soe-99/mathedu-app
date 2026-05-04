import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="데이터 시각화", layout="wide")

# 메인 페이지
st.title("👋 데이터 시각화 페이지")

st.subheader("📊 역량 시각화")

tab1, tab2, tab3 = st.tabs(["스킬 수준", "관심 분야", "학습 진행도"])

# Tab 1: 스킬 수준 (Seaborn)
with tab1:
    skills = {
        "Python": 85,
        "데이터 분석": 75,
        "교육 콘텐츠": 80,
        "문제 해결": 88,
        "커뮤니케이션": 82
    }
    
    df_skills = pd.DataFrame(list(skills.items()), columns=["스킬", "숙련도"])
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=df_skills, x="숙련도", y="스킬", palette="viridis", ax=ax)
    ax.set_xlim(0, 100)
    plt.title("기술 숙련도", fontsize=14, fontweight="bold")
    plt.xlabel("숙련도 (%)")
    for i, v in enumerate(df_skills["숙련도"]):
        ax.text(v + 1, i, str(v), va="center")
    
    st.pyplot(fig)
    plt.close()

# Tab 2: 관심 분야 (Plotly)
with tab2:
    interests = {
        "교육 콘텐츠": 40,
        "데이터 분석": 35,
        "기술 학습": 25
    }
    
    fig = px.pie(
        values=list(interests.values()),
        names=list(interests.keys()),
        title="관심 분야 분포",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig, use_container_width=True)

# Tab 3: 학습 진행도 (Plotly)
with tab3:
    months = ["1월", "2월", "3월", "4월", "5월", "6월"]
    learning_progress = [60, 65, 70, 75, 82, 88]
    project_count = [2, 3, 3, 4, 5, 6]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=months, y=learning_progress,
        mode="lines+markers",
        name="학습 진행도 (%)",
        line=dict(color="rgb(0, 100, 200)", width=3),
        marker=dict(size=8)
    ))
    
    fig.add_trace(go.Scatter(
        x=months, y=project_count,
        mode="lines+markers",
        name="프로젝트 수",
        line=dict(color="rgb(255, 100, 0)", width=3),
        marker=dict(size=8),
        yaxis="y2"
    ))
    
    fig.update_layout(
        title="최근 6개월 성장 추세",
        xaxis_title="월",
        yaxis_title="학습 진행도 (%)",
        yaxis2=dict(title="프로젝트 수", overlaying="y", side="right"),
        hovermode="x unified",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

