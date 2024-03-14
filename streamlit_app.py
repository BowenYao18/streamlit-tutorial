import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# Day 2
st.write("Day1: Hello, World!")

# Day 3
st.header('Day2: st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')


# Day 5

st.header('Day3: st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['x', 'y', 'z'])
st.write('This is the dataframe for graph', df2)
c = alt.Chart(df2).mark_circle().encode(
     x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.write(c)


# Day 6