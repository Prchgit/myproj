# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
records_data = dataiku.Dataset("records_data")
records_data_df = records_data.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

id_centric_agg_py_df = records_data_df # For this sample code, simply copy input to output


# Write recipe outputs
id_centric_agg_py = dataiku.Dataset("id_centric_agg_py")
id_centric_agg_py.write_with_schema(id_centric_agg_py_df)
