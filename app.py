import streamlit as st
import pandas as pd
import duckdb

st.title("Mon Dashboard de Données")
st.write("Bienvenue sur mon premier dashboard avec Streamlit + DuckDB")
data ={'a':[1,2,3], 'b':[4,5,6]}
df = pd.DataFrame(data)
tab1, tab2, tab3 =st.tabs('cat')

with tab1:
    sql_query = st.text_area(label='entrez votre text')
    result = duckdb.query(sql_query)
    st.write(f'vous avez {sql_query}')
    st.dataframe(result)
    st.write(df)
