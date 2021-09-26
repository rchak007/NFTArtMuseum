import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from PIL import Image
from web3 import Web3, HTTPProvider, eth
import json
from web3.middleware import geth_poa_middleware
from solc import compile_source
from web3.contract import ConciseContract

st.markdown("<h1 style='text-align: center; color: LightSeaGreen;'>NFT Gallery</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: LightSeaGreen;'>Welcome, everything you see is available for purchase</h1>", unsafe_allow_html=True)

col1,col2,col3 = st.columns([1,1,1])
with col1:
    st.video('random_grid_12.mp4')
    st.markdown("""
    test
    """)


with col2:
    st.image('mama-san-copy.jpg')
    st.markdown("""

     """)
with col3:
    st.image('animeface.png')
    st.markdown("""
 test
    """)

col4,col5,col6 = st.columns([1,1,1])
with col4:
    st.image('animesinglerow.png')
    st.markdown("""
    
    """)

with col5:
    st.image('museumticket.gif')
    st.markdown("""

     """)
with col6:
    st.video('gans_training(2).mp4')
    st.markdown("""
 
    """)

col7,col8,col9 = st.columns([1,1,1])
with col7:
    st.image('')
    st.markdown("""
    
    """)

with col8:
    st.image('')
    st.markdown("""

     """)
with col9:
    st.image('')
    st.markdown("""
 
    """)
