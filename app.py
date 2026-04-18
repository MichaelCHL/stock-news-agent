import streamlit as st
from orchestrator import orchestrator

def main():
    st.title("Stock News Agent 🤖📈")

    with st.form("ticker_accpeter"):
        st.write("Please enter a ticker symbol.")
        ticker_symbol = st.text_input("Ticker Symbol", "NVDA")
        st.write(f"The entered ticker is **{ticker_symbol}**")

        submitted = st.form_submit_button("Send!")
    
    if submitted:
        if ticker_symbol:
            text = orchestrator(ticker_symbol)
            st.write(f"Here the news summary related to {ticker_symbol}")
            st.write(text)
        else: 
            st.warning("Please enter a valid ticker!")
    
if __name__ == "__main__":
    main()
    