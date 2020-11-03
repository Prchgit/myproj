# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
mock_data_3 = dataiku.Dataset("mock_data_3")
mock_data_3_df = dkuspark.get_dataframe(sqlContext, mock_data_3)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
id_centric_aggregation_df = mock_data_3_df # For this sample code, simply copy input to output

# Write recipe outputs
id_centric_aggregation = dataiku.Dataset("id_centric_aggregation")
dkuspark.write_with_schema(id_centric_aggregation, id_centric_aggregation_df)
