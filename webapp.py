import os
import streamlit as st

#EDA Pkgs
import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)

#Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns


root = "/home/kaalachasma/Yaswanth/Projects/electricity/data/"
location = root+'Actual_generation_202006010000_202007312345_1.csv'

act_gen = pd.read_csv(location, sep=';', error_bad_lines=False, parse_dates=[['Date', 'Time of day']])
act_gen.index = pd.to_datetime(act_gen['Date_Time of day'])
act_gen.drop(labels = ['Date_Time of day'], axis=1, inplace=True)

st.write("""
# simple line chart  
# Let's fucking nail it!!!""")

st.dataframe(act_gen)

# st.pyplot()
# st.table(act_gen)

# print(act_gen.index[3].second)


# st.line_chart(act_gen['Biomass[MWh]'])
# st.line_chart(act_gen['Fossil gas[MWh]'])
# st.line_chart(act_gen)
# print(act_gen.head(5))
# print(act_gen.info())
# print(act_gen['Biomass[MWh]'])

# print(int(act_gen.index[1]))