# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
test1 = dataiku.Dataset("test1")
test1_df = test1.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

tees2_df = test1_df # For this sample code, simply copy input to output


# Write recipe outputs
tees2 = dataiku.Dataset("tees2")
tees2.write_with_schema(tees2_df)
