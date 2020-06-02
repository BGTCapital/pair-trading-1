# The source of this file: https://medium.com/auquan/pairs-trading-data-science-7dbedafcfe5a
# To run the venv in the Windows, use this command > Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

def find_cointegrated_pairs(data):
    n = data.shape[1]
    score_matrix = np.zeros((n, n))
    pvalue_matrix = np.ones((n, n))
    keys = data.keys()
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            S1 = data[keys[i]]
            S2 = data[keys[j]]
            result = coint(S1, S2)
            score = result[0]
            pvalue = result[1]
            score_matrix[i, j] = score
            pvalue_matrix[i, j] = pvalue
            if pvalue < 0.02:
                pairs.append((keys[i], keys[j]))
    return score_matrix, pvalue_matrix, pairs

from backtester.dataSource.yahoo_data_source import YahooStockDataSource
from datetime import datetime