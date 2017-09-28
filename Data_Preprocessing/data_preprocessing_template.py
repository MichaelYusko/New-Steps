# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as plt
import pandas as pd
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# strategy/axis parameters by default are 'mean' and 0
# But for example, I added both.
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:, 1:3])

# Transform missing data
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding categorical data
label_encoder = LabelEncoder()
X[:, 0] = label_encoder.fit_transform(X[:, 0])

one_hot_encoder = OneHotEncoder(categorical_features= [0] )
X = one_hot_encoder.fit_transform(X).toarray()

label_encoder_Y = LabelEncoder()
Y = label_encoder_Y.fit_transform(Y)
