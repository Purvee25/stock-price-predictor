from predictor import StockPredictor

def test_moving_average():
    sp = StockPredictor()
    prices = [10, 20, 30, 40, 50]
    ma = sp.moving_average(prices, 3)
    assert len(ma) == 3
    assert ma[0] == 20.0

def test_predict():
    sp = StockPredictor()
    prices = [100, 110, 120, 130, 140]
    preds = sp.predict(prices, 3)
    assert len(preds) == 3
    assert all(p > 140 for p in preds)

def test_rsi():
    sp = StockPredictor()
    prices = list(range(100, 130))
    rsi = sp.rsi(prices)
    assert all(0 <= r <= 100 for r in rsi)

if __name__ == "__main__":
    test_moving_average()
    test_predict()
    test_rsi()
    print("All tests passed!")
