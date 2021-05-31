#required library
import streamlit as st
import altair as alt
import pandas as pd


#import dataset

filename = 'teens_club.txt'
# read txt as csv
df = pd.read_csv(filename, header = None, error_bad_lines = False)
#name column
df.columns =['Date', 'Chat']
message = df['Chat'].str.split('-', n=1, expand = True)
df['Time'] = message[0]
df['Text'] = message[1]

name_text = df['Text'].str.split(':', n = 1, expand = True)
df['Name'] = name_text[0]
df['Text'] = name_text[1]
df = df.drop(columns= ['Chat'])


count = df.groupby('Name').size()
count.name = 'number_of_text'


st.write(df)
st.write(count)
