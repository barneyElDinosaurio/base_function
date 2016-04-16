import numpy as np
import pandas as pd
dates=pd.date_range('20150102',periods=10)
print dates
df = pd.DataFrame(np.random.randn(4,4))
print df
print df.describe()