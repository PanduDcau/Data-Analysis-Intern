# Gold ETFs Price Forecast, Trends, & 2 Year Predictions
The scope of this project is focused on GOLD ETF price forecasting, trends and 2 year predictions. The goal of this project is to understand and apply time-series models like ARIMA, SARIMA and Facebook Prophet in forecasting the price of gold ETF

# What Is The Problem?
Many investors buy gold  as a safe haven to protect themselves against a possible catastrophe, profit from these tremendous increases in the price of gold, diversify their portfolio and protect themselves against inflation. 

With recent fears of an economic recession looming in the distance, investors are looking to recession-proof their portfolios. Gold has historically been touted as an asset that booms in a recession because unlike fiat currencies such as the Dollar, Yen and the Pound, it has inherent value as a commodity currency.

However, with the rapidly changing economic landscape, does this still hold true? Is gold a good commodity to buy now for later profits?

# Where Is The Data From?
SPDR® Gold Shares (NYSE Arca : GLD) is a cost-effective and convenient way to invest in gold without buying the real gold.

The historical prices of SPDR® Gold Shares (NYSE Arca : GLD) was downloaded from [Yahoo](https://finance.yahoo.com/quote/GLD/history?p=GLD). Data spans from the inception of this share from 11/18/2004 to the date of download, 11/22/2019.

# What Is Time Series
A time series is a series of data points indexed (or listed or graphed) in time order. Most commonly, a time series is a sequence taken at successive equally spaced points in time. Thus it is a sequence of discrete-time data. Examples include daily closing price of S&P Index, daily average temperate etc. Time Series are analyzed to determine the long term trend so as to forecast the future or perform some other form of analysis.

# Important Data Files
The Data folder contains these important files:
  * GLD.csv - the original data downloaded from [Yahoo](https://finance.yahoo.com/quote/GLD/history?p=GLD)
  * gld-nomissing.csv - the original data file with missing data filled in. For example, data for weekends and holidays are missing because the stock market was closed.
  * sarimax_manualgridsearch_results.csv - this file contains the different parameters and tha associated AIC results produced by a manual grid search

# Machine Learning Models Used
There are machine learning algorithms that are better suited for time series. For this project, we are going to use:
  * ARIMA
  * Facebook Prophet

### ARIMA Model
An [ARIMA model](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average) (AutoRegressive Integrated Moving Average) is a class of statistical models for analyzing and forecasting time series data. ARIMA models take into account the past values to predict the future values

### Facebook Prophet
[Prophet](https://facebook.github.io/prophet/), developed by Facebook, is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data.

### Goal
We are going to apply these different models to find which one will produce the best predictions. Then we use the best fitted model to forecast the price of GOLD ETF for the next 2 years.

# Conclusion
  * Between ARIMA and Facebook Prophet, ARIMA shows a better fit between actual data and predicted data.
  * In the out-of-sample forecast, the ARIMA model shows an upward trend in gold prices for the next 2 years, forecasting the price of gold to be at $150.80 by 11/21/2021. That's 9.28% increase from today's price of $138.
