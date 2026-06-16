import streamlit as st
import pandas as pd
import duckdb

st.title("Mon Dashboard de Données")
st.write("Bienvenue sur mon premier dashboard avec Streamlit + DuckDB")
option = st.selectbox(
    'what would you like to do?',
    ('Joins','GroupBy','Windows Funtions'),
    index=None,
    placeholder='Choose your option',
)
st.write('You selected:', option)




data ={"a":[1,2,3], "b":[4,5,6]}
df = pd.DataFrame(data)
tab1, tab2, tab3 =st.tabs(['cat','Dog','Owl'])

with tab1:
    sql_query: str | None = st.text_area(label='entrez votre input')
    result = duckdb.query(sql_query)
    st.write(f'vous avez entre la query suivante: {sql_query}')
    st.dataframe(result)
with tab2:
    st.header('A dog')
with tab3:
    st.header('An Owl')
