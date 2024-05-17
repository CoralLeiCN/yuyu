import numpy as np

df = np.random.normal(0, 1, size=(500, 30000))
result = np.corrcoef(df)
