from sklearn.datasets import fetch_20newsgroups
import numpy as np
groups= fetch_20newsgroups()
print(len(groups.data[0]))
print(len(groups.data[1]))
