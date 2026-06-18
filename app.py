import io
from unittest import result

import streamlit as st
import pandas as pd
import duckdb
from pandas import DataFrame

st.title("Mon Dashboard de Données")
st.write("Bienvenue sur mon premier dashboard avec Streamlit + DuckDB")
csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""
beverage = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3"""
food_items = pd.read_csv(io.StringIO(csv))

answer_str = """
select * from beverage
cross join food_items"""

solution_df: DataFrame = duckdb.sql(answer_str).df()
st.header("enter your code: ")
query = st.text_area(label="entrez votre code", key="user input")
if query:
    result = duckdb.query(query).df()
    st.dataframe(result)
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

st.write(beverage)
with st.sidebar:
    option = st.selectbox(
        "what would you like to do?",
        ("Joins", "GroupBy", "Windows Funtions"),
        index=None,
        placeholder="Choose your option",
    )
    st.write("You selected:", option)


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    st.write("table : beverages")
    st.dataframe(beverage)
    st.write("table : food_items")
    st.dataframe(food_items)
    st.write("expected:", solution_df)
with tab3:
    st.write(solution_df)
