# Stock Price Predictor

Machine learning model for stock price prediction using historical data and technical indicators.

## Features
- Moving average crossover strategy
- RSI and MACD indicators
- Linear regression and LSTM models
- Backtesting framework

## Usage
```python
from predictor import StockPredictor
sp = StockPredictor()
prediction = sp.predict("AAPL", days=30)
```
