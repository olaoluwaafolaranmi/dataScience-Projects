import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#load image
image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA 

""")

#sequence input
st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

#shows input sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count

st.header('OUTPUT (DNA Nucleotide Count)')

# display of output as dictionary
st.subheader('1. print dictionary')

def nucleotideCount(seq):
    seq_dict = {
        'A': seq.count('A'),
        'T': seq.count('T'),
        'G': seq.count('G'),
        'C': seq.count('C')
    }

    return seq_dict


query_nucleotide_count = nucleotideCount(sequence)
#query_nucleotide_count_label = list(query_nucleotide_count)
#query_nucleotide_count_value = list(query_nucleotide_count.values())
st.write(query_nucleotide_count)

#display of output as texts

nucleotide_dict = {'A': 'Adenine', 'T': 'Thymine', 'C': 'Cytosine', 'G': 'Guanine'}

st.subheader('2. Print text')
for nucleotide in query_nucleotide_count:
    st.write('There are ' + str(query_nucleotide_count[nucleotide]) + " " + nucleotide_dict[nucleotide])



# display as dataframe

st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(query_nucleotide_count, orient='index')
df = df.rename({0: 'count'}, axis = 'columns')
df.reset_index(inplace = True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# display as bar chart

st.subheader('4. Display as bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80)
)
st.write(p)