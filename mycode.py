import os
data = {'name' : ['alice','rob', 'charlie'], 'age': [32,33,45]}
import pandas as pd
df = pd.DataFrame(data)
print(df.iloc[0:1,:])
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
df.to_csv(os.path.join(data_dir, 'people.csv'), index=False)