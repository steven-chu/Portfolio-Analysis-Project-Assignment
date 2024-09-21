# Portfolio-Analysis-Project-Assignment

**Primary Objective**: Create a portfolio of seven (7) NYSE traded assets. Complete all the steps below and return the risk analysis of your seven (7) stock portfolio against the S&P500 (SPY), Russell 2000 (IWM), and the Dow Jones Industrial Average (DIA).

**Requirements:**
1. Create a table showing constituent (stocks) risk analysis in the equal-weight portfolio analysis as of the
current date.
  
    a. Column 1 – Ticker
  
    b. Column 2 – Portfolio Weight (equally weighted)
  
    c. Column 3 – Annualized Volatility (using trailing 3-months)
  
    d. Column 4 – Beta against SPY (using trailing 12-months)
  
    e. Column 5 – Beta against IWM (using trailing 12-months)
  
    f. Column 6 – Beta against DIA (using trailing 12-months
  
    g. Column 7 – Average Weekly Drawdown (52-week Low minus 52-week High) / 52-week High
    
    h. Column 8 – Maximum Weekly Drawdown (52-week Low minus 52-week High) / 52-week High
  
    i. Column 9 – Total Return (using trailing 10-years)
  
    j. Column 10 – Annualized Total Return (using trailing 10-years)

2. Create a table showing Portfolio Risk against the three ETFs:
  
    a. Column 1 – ETF Ticker
  
    b. Column 2 – Correlation against ETF
  
    c. Column 3 – Covariance of Portfolio against ETF
  
    d. Column 4 – Tracking Errors (using trailing 10-years)
  
    e. Column 5 – Sharpe Ratio (using current risk-free rate)
  
    f. Column 6 – Annualized Volatility (252 days) Spread (Portfolio Volatility – ETF Volatility)

3. Create a correlation matrix showing the correlations between the equal-weighted portfolio created from
your 7 assets, 3 ETFs, and your 7 individual stocks.

**Parting Thoughts:** We will discuss many of the Pandas built-in functions you’ll need to use to complete this
project. However, you are still responsible for finding the formulas and merging those into your code using Python
or Pandas. You are encouraged to use the internet to find code snippets, but make sure to annotate where you found
the code (# comment). I highly recommend diving into how to accomplish these with the Pandas library
