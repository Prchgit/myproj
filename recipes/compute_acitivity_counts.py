# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from collections import Counter

# Read recipe inputs
activity_data = dataiku.Dataset("activity_data")
activity_data_df = activity_data.get_dataframe()

# new bundle test
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

acitivity_counts_df = activity_data_df # For this sample code, simply copy input to output
print("some changes")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# acitivity_counts_df.keys()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
clients = dict(Counter(acitivity_counts_df['clients'].tolist()))
dfActCount = pd.DataFrame.from_dict([{"client": x, 'count': y} for x, y in clients.items()])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# dfActCount[0:3]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
acitivity_counts = dataiku.Dataset("acitivity_counts")
acitivity_counts.write_with_schema(dfActCount)