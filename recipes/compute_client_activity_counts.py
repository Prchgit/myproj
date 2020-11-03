# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
activity_records = dataiku.Dataset("activity_records")
activity_records_df = activity_records.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

client_activity_counts_df = activity_records_df # For this sample code, simply copy input to output


# Write recipe outputs
client_activity_counts = dataiku.Dataset("client_activity_counts")
client_activity_counts.write_with_schema(client_activity_counts_df)