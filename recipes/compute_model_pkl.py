# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import xgboost as XGB
import pickle
# Read recipe inputs
inner_cv = dataiku.Dataset("inner_cv")
df = inner_cv.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
model = XGB.XGBClassifier(learning_rate = 0.2)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
leaveOut = ['client', 'ID', 'label', 'Date', 'Rank', 'category1']
ftsRaw = [x for x in df.keys() if x not in leaveOut]
lbCol = 'label'

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dfdummy = pd.get_dummies(df['category1'])
dftrain = pd.concat([df[ftsRaw + [lbCol]], dfdummy], axis = 1)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
dftrain = dftrain.loc[dftrain[lbCol].notnull()]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
fts = ftsRaw + list(dfdummy.keys())

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
X = dftrain[fts].values
y = dftrain[lbCol].tolist()
model.fit(X, y)
folder = dataiku.Folder("qmPE2pZN")
with folder.get_writer("xgbMd.pkl") as file_obj:
    pickle.dump(model, file_obj)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# any(dftrain[lbCol].isnull())

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# model_pkl_df = inner_cv_df # For this sample code, simply copy input to output
# # Write recipe outputs
# model_pkl = dataiku.Dataset("model_pkl")
# model_pkl.write_with_schema(model_pkl_df)