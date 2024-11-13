#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('timewave_data.csv')

plt.figure(figsize=(12, 8))

for column in df.columns[1:]:
    plt.plot(df["Days to Zero (DTZ)"], df[column], label=column)

# Adding titles and labels
plt.title("Timewave Zero Approximation with Various Models")
plt.xlabel("Days to Zero (DTZ)")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.show()
