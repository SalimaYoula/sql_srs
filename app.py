import ast
import io
import os
from unittest import result

import streamlit as st
import pandas as pd
import duckdb
from pandas import DataFrame

from init_db import beverages

st.title("Mon Dashboard de Données")
st.write("Bienvenue sur mon premier dashboard avec Streamlit + DuckDB")

path = os.path.abspath("data/sql_exercice.duckdb")
con = duckdb.connect(database=path, read_only=False)

with st.sidebar:
    option = st.selectbox(
        "what would you like to do?",
        ("Cross_Joins", "GroupBy", "Windows Funtions"),
        index=None,
        placeholder="Choose your option",
    )
    st.write("You selected:", option)

    exercice = con.execute(f"select * from memory_state where theme = '{option}'").df()
    st.write(exercice)
st.header("enter your code here: ")
query = st.text_area(label="entrez votre code", key="user input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)
    st.write("result:", result)
tab2, tab3 = st.tabs(["Tables", "Solution"])
with tab2:
    st.write(exercice.loc[0, 'tables'])
    excercice_tables = ast.literal_eval(exercice.loc[0, "tables"])
    for table in excercice_tables:
        st.write(f"table : {table}")
        df_table = con.execute(f"select * from {table}").df()
        st.dataframe(df_table)
with tab3:
    ANSWER_D =exercice.loc[0, 'exercices_name']
    with open(f'answers/{ANSWER_D}') as f:
        answer = f.read()
    st.write(answer)


