import streamlit as st

st.title("Interactive Cache Memory Simulator")

st.subheader("Cache Performance Analyzer")

cache_size = st.number_input("Enter Cache Size", min_value=1, value=4)

addresses = st.text_input(
    "Enter Memory Addresses (comma separated)",
    "1,2,3,4,1,2,5,1"
)

mapping = st.selectbox(
    "Select Mapping Technique",
    ["Direct Mapping", "Fully Associative Mapping", "Set Associative Mapping"]
)

if st.button("Run Simulation"):

    memory = [int(x.strip()) for x in addresses.split(",")]

    cache = []
    hits = 0
    misses = 0

    for address in memory:
        if address in cache:
            hits += 1
        else:
            misses += 1
            if len(cache) < cache_size:
                cache.append(address)
            else:
                cache.pop(0)
                cache.append(address)

    total = hits + misses
    hit_ratio = (hits / total) * 100
    miss_ratio = (misses / total) * 100

    st.success("Simulation Completed")

    st.write("Cache Contents:", cache)
    st.write("Cache Hits:", hits)
    st.write("Cache Misses:", misses)
    st.write(f"Hit Ratio: {hit_ratio:.2f}%")
    st.write(f"Miss Ratio: {miss_ratio:.2f}%")
