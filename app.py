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

    exercice = con.execute(f"select * from memory_state where theme = '{option}'").df().sort_values('last_review').reset_index()
    st.write(exercice)
    ANSWER_D = exercice.loc[0, 'exercices_name']
    st.write(ANSWER_D)
    with open(f'answers/{ANSWER_D}.sql') as f:
        answer = f.read()
    solution_df: DataFrame = con.execute(answer).df()

st.header("enter your code here: ")
query = st.text_area(label="entrez votre code", key="user input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)
    st.write("result:", result)
    if len(result.columns) != len(solution_df.columns):
        st.write("wrong number of columns")
        st.dataframe(result)
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))

    except KeyError as e:
        st.write("wrong number of columns")

    nb_lignes_difference = len(solution_df.columns) - len(result.columns)
    if nb_lignes_difference != 0:
        f"Result has {nb_lignes_difference} lignes difference with the solution"

tab2, tab3 = st.tabs(["Tables", "Solution"])
with tab2:
    st.write(exercice.loc[0, 'tables'])
    #excercice_tables = exercice.loc[0, "tables"]
    excercice_tables = [t for row in exercice["tables"] for t in row]
    print(excercice_tables)
    for table in excercice_tables:
        st.write(f"table : {table}")
        df_table = con.execute(f"select * from {table}").df()
        st.dataframe(df_table)
with tab3:
    st.write(answer)


