import pandas as pd
import yfinance as yf
import numpy as np

# Tickers on the NYSE traded assets, 7 stocks and 3 ETFS
tickers = ['NVDA', 'TSLA', 'GME','AMD','MSFT','META','WMT']
etfs = ['SPY', 'IWM', 'DIA']

# Downloading the historical data, 10 years is a safe number
start_date = '2012-11-23'
end_date = '2022-11-23'
data = yf.download(tickers + etfs, start = start_date, end = end_date)['Adj Close']

# Portfolio Weight: A percentage of an investment portfolio that a specific asset or holding represents
# Formula = [(Stock's Value) / (Total Portfolio Value)]. In this case they all weigh the same amount.
portfolio = pd.DataFrame(index=tickers)
n = len(tickers)
portfolioWeight = (n/100) 
portfolio['Portfolio Weight (%)'] = portfolioWeight

# Calculate Annualized Volatility
portfolio['Annualized Volatility'] = data.pct_change()[-63:].std() * np.sqrt(252)

# Beta = Covariance (Stock Returns, Market Returns) / Variance (Market Returns)
# Credit: https://github.com/CCNY-Analytics-and-Quant/PortfolioAnalysis-Rifat_Kaljang/blob/main/PortfolioAnalysis.ipynb
# This extracts the covariance between the asset and the specified ETF from the covariance matrix.
returns = data.pct_change() 

for etf in etfs:
    portfolio['Beta Against ' + etf] = returns[-252:].cov()[etf] / returns[-252:][etf].var()

# Calculate Average Weekly Drawdowns
# Window = 5 for weekly, .mean to calculate weekly drawdown average, .iloc[-1] to pull most recent
average_weekly_drawdowns = drawdowns.rolling(window=5).mean().iloc[-1]
portfolio['Average Weekly Drawdown'] = average_weekly_drawdowns

# Calculate Maximum Weekly Drawdowns
maximum_weekly_drawdown = drawdowns.rolling(window=5).max().iloc[-1]
portfolio['Maximum Weekly Drawdown'] = maximum_weekly_drawdown

# Calculate Total Return = (final - initial) / (initial)
total_return = (data.iloc[-1] - data.iloc[252])/data.iloc[252]
portfolio['Total Return'] = total_return

# 1 + R_n is a series until there are no more values hence why we use data.iloc functionality instead of 1 + R_1... There are many values
# Annualized Total Return: [(1 + R_n)^(1/n) - 1]
# Credit for Formula: https://corporatefinanceinstitute.com/resources/wealth-management/annualized-total-return/
annualized_total_return = ((data.iloc[-1] / data.iloc[252])**(1/10) - 1) * 100
portfolio['Annualized Total Return (%)'] = annualized_total_return

# Creating a table showing Portfolio Risk against the three ETFS
etf_portfolio = pd.DataFrame(index=etfs)
etf_portfolio

# Credit: https://github.com/CCNY-Analytics-and-Quant/PortfolioAnalysis-Rifat_Kaljang/blob/main/PortfolioAnalysis.ipynb
portfolioCorr = (data[tickers].pct_change() * portfolioWeight).sum(axis=1)
portfolioCorr = portfolioCorr.rename("Portfolio")
returns = pd.concat([data.pct_change(), portfolioCorr], axis = 1)

corr_matrix = returns[252:].corr(method="pearson")

etf_portfolio['Correlation against ETF'] = [corr_matrix['Portfolio'][etf] for etf in etfs]

etf_cov = returns[252:].cov()
etf_portfolio['Covariance against ETF'] = [etf_cov['Portfolio'][etf] for etf in etfs]

# Calculate Tracking Errors for the etf in etfs
# Tracking Error: Standard Deviation of (P - B) where P = Portfolio Returns and B = Benchmark Returns
# Formula: Standard Deviation of (Stock Return - ETF return)
# Measures how consistently close or wide an index ETF's performance is relative to its benchmark
# Source: https://corporate.vanguard.com/content/corporatesite/us/en/corp/articles/tracking-error-often-overlooked-cost.html#:~:text=Tracking%20error%20is%20measured%20as,around%20performance%20adds%20uncertainty%20costs.
etf_portfolio['Tracking Errors'] = [(returns['Portfolio'] - returns[etf]).std() for etf in etfs]

# Sharpe Ratio:  (Expected Asset Return - Risk Free Rate) / Standard Deviation
# Formula: Sharpe Ratio = (Rx - Rf) / StdDev(Rx)
# Expected Asset Return = Portfolio Stock, Risk Free Rate = ETFs (benchmarks)
# Caclulate Sharpe Ratio
etf_portfolio['Sharpe Ratio'] = [(returns['Portfolio'].mean() - returns[etf].mean())/(returns['Portfolio'].std()) for etf in etfs]

# Calculate Annualized Volatility for ETF
etf_portfolio['Annualized Volatility'] = [(returns['Portfolio'][252:].std())*(np.sqrt(252)) - (returns[etf][252:].std())*(np.sqrt(252)) for etf in etfs]

# Thanks ChatGPT for making it easy to input the values
# I could have used Matplotlib/Seaborn to make it easier to create a correlation matrix but I wanted to strictly use 3 libraries only for this project
asset_portfolio = {
    'NVDA': [0.07, 0.634418, 2.214848, 1.839605, 2.376997, 42.095012, 43.106507, 43.763331, 46.248776],
    'TSLA': [0.07, 0.557269, 1.780724, 1.539481, 1.788735, 313.493467, 329.974925, 19.997282, 35.586455],
    'GME': [0.07, 0.746471, 1.957305, 1.972465, 2.045533, 2.398628, 2.521421, 1.945622, 11.408341],
    'AMD': [0.07, 0.642289, 2.067816, 1.721387, 2.218046, 152.996285, 156.500007, 21.529941, 36.545064],
    'MSFT': [0.07, 0.400705, 1.259122, 0.916869, 1.393819, 1338.645560, 1353.504558, 6.677201, 22.608419],
    'META': [0.07, 0.716671, 1.702263, 1.337453, 1.773996, 251.827006, 255.505948, 1.410556, 9.197255],
    'WMT': [0.07, 0.246433, 0.428176, 0.265739, 0.570775, 316.223712, 319.981791, 1.320966, 8.784466]
}

benchmark_portfolio = {
    'SPY': [0.706765, 0.000077, 0.007969, 0.027550, -0.024024],
    'IWM': [0.668021, 0.000091, 0.010187, 0.034955, -0.068011],
    'DIA': [0.625429, 0.000069, 0.008936, 0.029568, -0.024560]
}

df_asset = pd.DataFrame(asset_portfolio)
df_benchmark = pd.DataFrame(benchmark_portfolio)

combined_portfolios = pd.concat([df_asset, df_benchmark],axis=1)
coMatrix = combined_portfolios.corr()

portfolio

coMatrix







