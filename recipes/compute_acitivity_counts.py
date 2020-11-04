# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
activity_data = dataiku.Dataset("activity_data")
activity_data_df = activity_data.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

acitivity_counts_df = activity_data_df # For this sample code, simply copy input to output


# Write recipe outputs
acitivity_counts = dataiku.Dataset("acitivity_counts")
acitivity_counts.write_with_schema(acitivity_counts_df)
