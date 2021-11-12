import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


if __name__ == '__main__':
    df = pd.read_csv("data_1.csv")
    fig = plt.figure(figsize=(8, 8))
    ax = fig.gca()
    df[df["color"] == 4].hist(ax=ax)
    plt.show()
