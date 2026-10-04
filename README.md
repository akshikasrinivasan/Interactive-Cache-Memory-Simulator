# Interactive Cache Memory Simulator

## 1. Project Overview

The Interactive Cache Memory Simulator is a software-based educational application developed to demonstrate the working of cache memory and different cache mapping techniques.

The simulator allows users to provide memory addresses, select a cache mapping technique, and observe cache hits, cache misses, hit ratio, miss ratio, and the final cache contents.

## 2. Objectives

- Understand the basic working of cache memory.
- Demonstrate different cache mapping techniques.
- Simulate memory access sequences.
- Calculate cache hits and cache misses.
- Calculate hit ratio and miss ratio.
- Provide an interactive and easy-to-use interface.

## 3. Cache Mapping Techniques

### Direct Mapping

In direct mapping, each memory block is mapped to exactly one specific cache line.

### Set Associative Mapping

In set associative mapping, the cache is divided into sets. A memory block is mapped to a particular set and can occupy any available line within that set.

### Fully Associative Mapping

In fully associative mapping, a memory block can be placed in any available cache line.

## 4. Features

- Interactive user interface
- Adjustable cache size
- User-defined memory address sequence
- Direct Mapping
- Set Associative Mapping
- Fully Associative Mapping
- Cache hit and miss calculation
- Hit ratio calculation
- Miss ratio calculation
- Display of final cache contents
- Web-based interface using Streamlit

## 5. Technologies Used

- Python
- Streamlit

## 6. How to Run the Project

### Install dependencies

```bash
python -m p## Live Application

[Open the Interactive Cache Memory Simulator](https://interactive-cache-memory-simulator-9aa9rvrnzgtac4vx6ikmxs.streamlit.app/)ip install -r requirements.txt
