import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Simulation[tm]")
st.write("Here is our simulation")

# add side-bar
st.sidebar.markdown("## Controls")
st.sidebar.markdown("You can **change** the values to change the *chart*")

x = st.sidebar.slider('Slope', min_value=0.01, max_value=0.10, step=0.01)
y = st.sidebar.slider('Noise', min_value=0.01, max_value=0.10, step=0.01)

st.write(f"x={x} y={y}")
values = np.cumprod(1 + np.random.normal(x, y, (100, 10)), axis=0)

for i in range(values.shape[1]):
    plt.plot(values[:, i])

st.pyplot()