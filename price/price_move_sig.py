from config import NEG_PERCENT_THRESHOLD, POS_PERCENT_THRESHOLD
def price_move(symbol_pc, spy_pc):

    if spy_pc < 0 and symbol_pc > POS_PERCENT_THRESHOLD:
        return "outperform_wild"
    elif POS_PERCENT_THRESHOLD > spy_pc >= 0 and symbol_pc > POS_PERCENT_THRESHOLD:
        return "outperform"
    elif spy_pc < NEG_PERCENT_THRESHOLD:
        return "market_wild_drop"
    elif spy_pc > POS_PERCENT_THRESHOLD and symbol_pc > POS_PERCENT_THRESHOLD:
        return "market_surge"
    elif spy_pc > POS_PERCENT_THRESHOLD and symbol_pc < NEG_PERCENT_THRESHOLD:
        return "underperform_wild"
    elif (symbol_pc < spy_pc and spy_pc >= 0):
        return "underperform"
    elif symbol_pc < 0 and spy_pc < 0 and spy_pc > symbol_pc:
        return "underperform_mild"
    elif 0 < spy_pc < POS_PERCENT_THRESHOLD and  0 < symbol_pc < POS_PERCENT_THRESHOLD and symbol_pc > spy_pc:
        return "outperform_mild"
    else:
        return "neutral"


### MEMO FOR PROMPT GENERATING FUNCTION
    # if spy_pc < NEG_PERCENT_THRESHOLD and symbol_pc > POS_PERCENT_THRESHOLD:
    #     return f"{symbol} performs well today. Find the news and causes that lead to this."
    # elif spy_pc < NEG_PERCENT_THRESHOLD and symbol_pc > 0:
    #     return f"{symbol} doesn't seem to be affected like SPY is. Find the news and causes that lead to this."
    # elif spy_pc > 0 and symbol_pc < NEG_PERCENT_THRESHOLD:
    #     return f"{symbol} performs worse than SPY. Search the news or causes for {symbol}."
    # elif spy_pc < NEG_PERCENT_THRESHOLD and symbol_pc < NEG_PERCENT_THRESHOLD:
    #     return f"The market is bad today. Search the news that causes the significant move in stock price"
    # elif abs(spy_pc) > POS_PERCENT_THRESHOLD and abs(symbol_pc) > POS_PERCENT_THRESHOLD:
    #         return "The market is very promising today. Find out the reason."
    
