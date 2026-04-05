import pandas as pd
from io import StringIO

raw_data = """name,age,department,score
Henry,20,IT,85
John,22,HR,90
Mary,,IT,70
Paul,21,HR,55
Anna,19,IT,88
James,23,Finance,60"""
df = pd.read_csv(StringIO(raw_data))
print(df)
