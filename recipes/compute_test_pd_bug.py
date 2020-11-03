# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
raw_data_part1 = dataiku.Dataset("raw_data_part1")
raw_data_part1_df = raw_data_part1.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_pd_bug_df = raw_data_part1_df # For this sample code, simply copy input to output


# Write recipe outputs
test_pd_bug = dataiku.Dataset("test_pd_bug")
test_pd_bug.write_with_schema(test_pd_bug_df)
