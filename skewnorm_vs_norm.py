import scipy.stats as ss
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Comparing skew normal and normal probability density functions")
# Two columns layout
col1, col2 = st.columns(2)

with col1:
    # Input area
    st.header("Select parameters for the distribution")
    alpha = st.number_input('alpha', value=1)
    mu = st.number_input('mu')
    sigma = st.number_input('sigma', value=1)

with col2:
    # plot area
    st.header("PDF of skew-normal vs normal")
    fig, ax = plt.subplots(1, 1)
    x= np.linspace(ss.skewnorm.ppf(0.01, alpha, mu, sigma),ss.skewnorm.ppf(0.99, alpha, mu, sigma), 100)
    ax.plot(x, ss.skewnorm.pdf(x, alpha, loc=mu, scale=sigma),'r-', lw=5, alpha=0.6, label='skewnorm')
    ax.plot(x, ss.norm.pdf(x, loc=mu, scale=sigma),'k-', lw=5, alpha=0.6, label='norm')
    plt.legend()
    st.pyplot(fig)
    
