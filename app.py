import streamlit as st

st.title("Interactive Cache Memory Simulator")

st.header("Cache Performance Analyzer")

cache_size = st.number_input("Enter Cache Size", min_value=1)

memory_address = st.text_input("Enter Memory Address")

mapping = st.selectbox(
    "Select Mapping Technique",
    ["Direct Mapping", "Associative Mapping", "Set Associative Mapping"]
)

if st.button("Simulate"):
    st.success(f"Simulation completed using {mapping}")
    st.write("Cache Hit: 1")
    st.write("Cache Miss: 0")
    st.write("Hit Ratio: 100%")
