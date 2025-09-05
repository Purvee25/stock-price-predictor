import csv
import math
from collections import deque

class StockPredictor:
    def __init__(self, window=20):
        self.window = window

    def moving_average(self, prices, period):
        if len(prices) < period:
            return []
        result = []
        window = deque(prices[:period], maxlen=period)
        result.append(sum(window) / period)
        for price in prices[period:]:
            window.append(price)
            result.append(sum(window) / period)
        return result

    def rsi(self, prices, period=14):
        if len(prices) < period + 1:
            return []
        deltas = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
        gains, losses = [], []
        for d in deltas:
            gains.append(d if d > 0 else 0)
            losses.append(-d if d < 0 else 0)
        avg_gain = sum(gains[:period]) / period
        avg_loss = sum(losses[:period]) / period
        rsi_values = []
        for i in range(period, len(deltas)):
            avg_gain = (avg_gain * (period - 1) + gains[i]) / period
            avg_loss = (avg_loss * (period - 1) + losses[i]) / period
            rs = avg_gain / avg_loss if avg_loss != 0 else float('inf')
            rsi_values.append(100 - (100 / (1 + rs)))
        return rsi_values

    def linear_regression(self, prices):
        n = len(prices)
        x_mean = (n - 1) / 2
        y_mean = sum(prices) / n
        numerator = sum((i - x_mean) * (p - y_mean) for i, p in enumerate(prices))
        denominator = sum((i - x_mean) ** 2 for i in range(n))
        slope = numerator / denominator if denominator != 0 else 0
        intercept = y_mean - slope * x_mean
        return slope, intercept

    def predict(self, prices, days=5):
        slope, intercept = self.linear_regression(prices)
        n = len(prices)
        return [slope * (n + i) + intercept for i in range(days)]

    def backtest(self, prices, strategy="ma_crossover", short=5, long=20):
        if strategy == "ma_crossover":
            short_ma = self.moving_average(prices, short)
            long_ma = self.moving_average(prices, long)
            offset = long - short
            signals = []
            for i in range(len(long_ma)):
                if i > 0:
                    if short_ma[i + offset] > long_ma[i] and short_ma[i + offset - 1] <= long_ma[i - 1]:
                        signals.append(("BUY", i + long, prices[i + long]))
                    elif short_ma[i + offset] < long_ma[i] and short_ma[i + offset - 1] >= long_ma[i - 1]:
                        signals.append(("SELL", i + long, prices[i + long]))
            return signals
        return []

if __name__ == "__main__":
    sample_prices = [100, 102, 101, 103, 105, 104, 106, 108, 107, 109, 111, 110, 112, 114, 113, 115, 117, 116, 118, 120, 119, 121, 123, 122, 124]
    sp = StockPredictor()
    print("MA:", sp.moving_average(sample_prices, 5)[:5])
    print("RSI:", sp.rsi(sample_prices)[:5])
    print("Prediction:", sp.predict(sample_prices, 3))
