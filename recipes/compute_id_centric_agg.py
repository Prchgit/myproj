# -*- coding: utf-8 -*-
import dataiku
from dataiku import spark as dkuspark
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

# Read recipe inputs
records_data = dataiku.Dataset("records_data")
records_data_df = dkuspark.get_dataframe(sqlContext, records_data)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a SparkSQL dataframe
id_centric_agg_df = records_data_df # For this sample code, simply copy input to output

# Write recipe outputs
id_centric_agg = dataiku.Dataset("id_centric_agg")
dkuspark.write_with_schema(id_centric_agg, id_centric_agg_df)
