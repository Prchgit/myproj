# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


# Read recipe inputs
inner_cv = dataiku.Dataset("inner_cv")
inner_cv_df = inner_cv.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

model_pkl_df = inner_cv_df # For this sample code, simply copy input to output


# Write recipe outputs
model_pkl = dataiku.Dataset("model_pkl")
model_pkl.write_with_schema(model_pkl_df)
