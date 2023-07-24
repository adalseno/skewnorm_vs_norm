import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Comparing skew normal and normal probability density functions")
# Two columns layout
col1, col2 = st.columns(2)

with col1:
    # Input area
    st.header("Select parameters for the distribution")
    alpha = st.number_input('alpha')
    mu = st.number_input('mu')
    sigma = st.number_input('sigma')

with col2:
    # plot area
    st.header("PDF of skew-normal vs normal")
    fig, ax = plt.subplots(1, 1)
    x= np.linspace(st.skewnorm.ppf(0.01, alpha),
                    st.skewnorm.ppf(0.99, a), 100)
    ax.plot(x, st.skewnorm.pdf(x, alpha, mu, sigma),
           'r-', lw=5, alpha=0.6, label='skewnorm pdf')
    ax.plot(x, st.norm.pdf(x, mu, sigma),
           'k-', lw=5, alpha=0.6, label='norm pdf')
    st.pyplot(fig)
    