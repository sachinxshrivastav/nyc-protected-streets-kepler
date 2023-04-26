import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
from streamlit_keplergl import keplergl_static


st.set_page_config(layout="wide")
st.title('NYC Protected Streets')
st.text('Application displays New York City street segments that are blocked for performing any kind of digging and repair work as a layer on 3D Maps.')

# Reading the Data from NYC Open Data
soql_url = ('https://data.cityofnewyork.us/resource/wyih-3nzf.json?' + '$select=the_geom,fromstreet,tostreetna,dateprotec,dateprot_1').replace(' ', '%20')

# read into pandas as dataframe
df = pd.read_json(soql_url)

# Converting DataTime data into proper Format
df['dateprotec'] =  pd.to_datetime(df['dateprotec'])
df['dateprotec'] = df['dateprotec'].dt.strftime('%Y%m%d')

df['dateprot_1'] =  pd.to_datetime(df['dateprot_1'])
df['dateprot_1'] = df['dateprot_1'].dt.strftime('%Y%m%d')

from keplergl import KeplerGl
map = KeplerGl(height=800, data={"data_1": df})
keplergl_static(map)

#map.save_to_html(file_name='data/protected_streets.html',read_only=True)

#p = open("data/protected_streets.html")
#components.html(p.read(),height=600)