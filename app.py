import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')
df = pd.read_csv('census_cleaned.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title('India MAP')
columns = sorted(df[['LPG PNG Households', 'Housholds with Electricity', 'Households with Internet',
                 'Households with Computer', 'Households with Television', 'Population',
                 'Households with Telephone Mobile Phone', 'Sex Ratio', 'Literacy Rate']].columns)
selected_state = st.sidebar.selectbox('Select a State', list_of_states)

primary = st.sidebar.selectbox('Select primary parameter', columns)
Secondary = st.sidebar.selectbox('Select secondary parameter', columns)
plot = st.sidebar.button('Plot graph')

if plot:
    st.text("size represents primary parameter")
    st.text("color represents secondary parameter")
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', size=primary, color=Secondary, hover_name='District',
                                size_max=25, zoom=3, mapbox_style="carto-positron", height=700, width=1200)
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=Secondary, hover_name='District',
                                size_max=25, zoom=6, mapbox_style="carto-positron", height=700, width=1200)
        st.plotly_chart(fig, use_container_width=True)


if selected_state == 'Overall India':
    if plot:
        st.subheader("Population state and district wise")
        fig1 = px.sunburst(df, path=['State', 'District'], values='Population',
                           color='Male Population', color_continuous_scale=["red", "green"])
        st.plotly_chart(fig1)

if selected_state != 'Overall India':
    if plot:
        st.subheader("Average Population of Workers")
        temp1 = df[df['State'] == selected_state].groupby('State')[['Male Workers', 'Female Workers', 'Non Workers',
                             'Agricultural Workers', 'Other Workers']].mean().stack().reset_index()
        temp1.rename(columns={'level_1': "Workers", 0: 'population'}, inplace=True)
        fig6 = px.pie(temp1, names='Workers', values='population')
        st.plotly_chart(fig6)

if selected_state != 'Overall India':
    if plot:
        st.subheader("Average Religion Population")
        temp1 = df[df['State'] == selected_state].groupby('State')[['Hindus', 'Muslims', 'Christians', 'Sikhs',
                         'Buddhists', 'Jains', 'Others Religions']].mean().stack().sort_values(ascending=False).head(5).reset_index()
        temp1.rename(columns={'level_1': "Religions", 0: 'population'}, inplace=True)
        fig3 = px.bar(temp1, x='Religions', y='population')
        st.plotly_chart(fig3)

if selected_state != 'Overall India':
    if plot:
        st.subheader("Scatterplot of population and literacy rate")
        st.text('size represents male literate')
        temp1 = df[df['State'] == selected_state]
        fig7 = px.scatter(temp1, x='Population', y='Literacy Rate', size='Male Literate', color='District')
        st.plotly_chart(fig7)

if selected_state != 'Overall India':
    if plot:
        st.subheader("Average Population Education Wise")
        temp1 = df[df['State'] == selected_state].groupby('State')[['Below Primary Education', 'Primary Education', 'Secondary Education',
                    'Graduate Education', 'Other Education']].mean().stack().sort_values(ascending=False).reset_index()
        temp1.rename(columns={'level_1': "Education", 0: 'population'}, inplace=True)
        fig4 = px.bar(temp1, x='Education', y='population')
        st.plotly_chart(fig4)



if selected_state != 'Overall India':
    if plot:
        st.subheader("Average Population Age  Wise")
        temp1 = df[df['State'] == selected_state].groupby('State')[['Age 0-29','Age 30-49','Above 50',]].mean().stack().sort_values(ascending=False).reset_index()
        temp1.rename(columns={'level_1': "Age", 0: 'population'}, inplace=True)
        fig5 = px.pie(temp1, names='Age', values='population')
        st.plotly_chart(fig5)


if selected_state != 'Overall India':
    if plot:
        st.subheader("Average Population Gender  Wise")
        temp1 = df[df['State'] == selected_state].groupby('State')[['Male Population', 'Female population']].mean().stack().reset_index()
        temp1.rename(columns={'level_1': "Gender", 0: 'population'}, inplace=True)
        fig6 = px.pie(temp1, names='Gender', values='population')
        st.plotly_chart(fig6)





