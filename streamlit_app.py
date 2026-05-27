import streamlit as st

# Page config
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🤖",
    layout="wide"
)

# ===== HEADER =====
st.markdown("""
<h1 style='text-align: center;'>🤖 Multi-Agent Research System</h1>
<p style='text-align: center; color: gray;'>
AI agents that research, analyze, and generate structured reports
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ===== SIDEBAR =====
with st.sidebar:
    st.title("⚙️ Settings")
    st.info("AI Research System\n\nBuilt using LangChain + OpenAI + Tavily")

# ===== INPUT SECTION =====
st.markdown("### 🔍 Enter Research Topic")

topic = st.text_input(
    "",
    placeholder="e.g. Artificial Intelligence, Blockchain, Neural Networks"
)

# ===== METRICS =====
col1, col2, col3 = st.columns(3)
col1.metric("Agents", "4")
col2.metric("Mode", "Research")
col3.metric("Status", "Active")

# ===== BUTTON (FIXED) =====
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run_btn = st.button("🚀 Run Research", use_container_width=True)

st.markdown("---")

# ===== RESULT SECTION =====
if run_btn:
    if not topic.strip():
        st.warning("⚠️ Please enter a topic.")
    else:
        with st.spinner("🤖 AI agents are working..."):
            try:
                from pipeline import run_research_pipeline

                result = run_research_pipeline(topic)

                if not result:
                    st.error("❌ No result returned from pipeline.")
                else:
                    st.success("✅ Research Completed!")

                    # ===== TABS =====
                    tab1, tab2, tab3, tab4 = st.tabs([
                        "🔎 Search Results",
                        "📄 Research Analysis",
                        "📝 Draft Report",
                        "✅ Final Report"
                    ])

                    with tab1:
                        st.write(result.get("search_results", "No data available"))

                    with tab2:
                        st.write(result.get("research", "No data available"))

                    with tab3:
                        st.write(result.get("report", "No data available"))

                    with tab4:
                        st.write(result.get("final_report", "No data available"))

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# ===== FOOTER =====
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>🚀 Built by Dnyaneshwar Rathod</p>",
    unsafe_allow_html=True
)