import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    df = pd.read_csv("data_1.csv")
    print(df["color"])
    plt.hist(df[df["color"] == 1]["mass"], density=True, bins=30)
    plt.ylabel('Probability')
    plt.xlabel('Data')
    plt.show()