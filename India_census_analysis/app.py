import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
df = pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Map Analysis')

selected_state = st.sidebar.selectbox('Select a state',list_of_states)
numerical_columns = ([col for col in df.columns if col != 'District'])
primary = st.sidebar.selectbox("Select Primary Parameter", numerical_columns)
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(numerical_columns))


plot = st.sidebar.button('Plot Graph')
if plot:

    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')

    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
                                zoom=3.5,height=700,width=1100,size_max=35,
                                size=primary,color=secondary,
                                mapbox_style="carto-positron",hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude',
                                zoom=3.5, height=700, width=1100, size_max=35,
                                size=primary, color=secondary,
                                mapbox_style="carto-positron")
        st.plotly_chart(fig, use_container_width=True)
