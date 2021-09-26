import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from PIL import Image
import web3 as w3
from web3 import Web3, HTTPProvider, eth
from web3.middleware import geth_poa_middleware
from solc import compile_source
from web3.contract import ConciseContract
import streamlit.components.v1 as components
import os
from eth_account import Account
from dotenv import load_dotenv
#from etherscan import Etherscan
import json
from pathlib import Path
from getpass import getpass
import dotenv


with open("contract_abi.txt") as f:
    MuseumContract_json = json.load(f)


load_dotenv('museum.env')

https_str = f'https://kovan.infura.io/v3/{WEB3_INFURA_PROJECT_ID}'
w1 = Web3(Web3.HTTPProvider(https_str))
w1.middleware_onion.inject(geth_poa_middleware, layer=0)
museum_contract_instance = w1.eth.contract(address=nft_museum_address, abi=MuseumContract_json)

def create_raw_tx(account, recipient, amount):
    gasEstimate = w1.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w1.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w1.eth.getTransactionCount(account.address),
    }


def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w1.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()

def buyTicket(private_key):
    
    #define how much 1 ticket cost
    tickets_remaining=0
    ticket_price = 1
    # check if seller has tikcets left
    #tickets_remaining = museum_contract_instance.functions.balanceOf('0xe72b2c4391a8d1bd1e6a98d96978bfaa20d02b62').call()
    #st.write('test',tickets_remaining)
    if tickets_remaining >=0:
        # transfer ETHER from buyers private key to sellers private key
        buyer_account = Account.from_key(private_key)
        owner_account = Account.from_key(PRIV_KEY)
        # the transaction might not go through if it doesnt dont send ticket
        tx_send = send_tx(buyer_account, owner_account.address, ticket_price)
        nonce = w1.eth.getTransactionCount(account_one_address)+1
        st.write(nonce)
        chain_id = w1.eth.chain_id
        # For Gas get latest block for better estimation
        w1.eth.getBlock("latest")
        dict1 = w1.eth.getBlock("latest")
        gasEstimate = dict1['gasUsed']
        # we sometimes see that the Latest block could return 0 too
        if gasEstimate < 600000:
            gasEstimate = 600000
        gas_price = w1.eth.gasPrice
        print('nonce=', nonce )
        print('gasEstimate=', gasEstimate)
        print('gas_price=', gas_price)
        # transfer 1 MTKN to buyer
        
        tx_hash = museum_contract_instance.functions.transfer(buyer_account.address, 1).buildTransaction({'chainId':chain_id, 'gas': gasEstimate, 'gasPrice': gas_price, 'nonce': nonce})
        st.write('tx_hash',tx_hash)
        register_signed_txn = w1.eth.account.sign_transaction(tx_hash, private_key=PRIV_KEY)
        register_sent_txn = w1.eth.send_raw_transaction(register_signed_txn.rawTransaction)
        return tx_send, register_sent_txn
        # museum_contract_instance.functions.balanceOf(buyer_account).call()
        # museum_contract_instance.functions.balanceOf(account_one).call()

st.markdown("<h1 style='text-align: center; color: LightSeaGreen;'>NFT MUSEUM</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: LightSeaGreen;'>Welcome to the first NFT Museum powered on Web3</h1>", unsafe_allow_html=True)

col7,col8,col9 = st.columns([1.5,1,1])



image=Image.open('mama-san-copy.jpg')
image2=Image.open('beeple.jpg')

col4,col5,col6 = st.columns([1,2,1])
with col4:
    st.markdown("""
    ### -  This is a testcase for a way to explore,share, and sell NFTs on web3. For our final porject we explored web3 aplications for building and running a museum with solidity as the backbone.
    ### -  Everything you see here is a test and is run on the Kovan Testnet. Please do not use real Ethereum on this site or it will be lost.
    
    """)
st.markdown("""
 ### This project explores:
    > ### solidity contract creation for purchasing of NFTs
    - ### erc 721 tokens for access to the NFT museum
    - ### Profit sharing between the owners and the artists
    - ### NFT's shown in the museum are created through Python Generative art transfer and design
    - ### it :fire:
     """)

with col5:
    st.image('ethgif.gif')

with col6:
    st.markdown("""
    | Creators | tasks |
| ----------- | ----------- |
| David | Streamlit,Spatial.io Enviroment, NFT design |
| Chuck | Solidity Contract Creation, NFT design |
| Jerry | Solidity contract creation, NFT design |
| Flor | NFT design |
    """)



with st.form('Payment'):
    st.write('Membership Information')
    name=st.text_input('Name')
    st.date_input('What is your bithday?')
    account_one_address=st.text_input('Kovan wallet ID')
    private_key=st.text_input('Kovan private key(never do this IRL)')
    payment=st.checkbox('This is a one time payment of .0001 ETH for unlimited access to the NFT museum on the Kovan Testnet, the profits are split even with the artists')
    submit=st.form_submit_button('Pay')
    if submit:
        buyTicket(private_key)
        st.write('Welcome to the MEME Museum us this link to navigate')
        st.sidebar.image(image)
        st.write('https://app.spatial.io/rooms/614e160a5008940001b595a2?share=4139357422959649709')


col0,col1, col3 = st.columns([1,1,1])
col0.image(image2,width=1500)
