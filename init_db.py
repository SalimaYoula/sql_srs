import duckdb
import pandas as pd
import io

con = duckdb.connect(database="data/sql_exercice.duckdb", read_only=False)

data = {
    "theme": ['Cross_Joins','test_ictif'],
    'exercices_name': ['beverage_and_food','test_ictif'],
    'tables': [['beverages','food_items'],'test_ictif'],
    'last_review' : ['1970-01-01',
                     '1970-01-01']
}
memory_state_df = pd.DataFrame(data)
con.execute("create table if not exists memory_state as select * from memory_state_df")
csv = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages = pd.read_csv(io.StringIO(csv))
con.execute("create table if not exists Beverages as select * from beverages ")
csv2 = """
food_item,food_price
cookie juice,2.5
chocolatine,2
muffin,3"""
food_items = pd.read_csv(io.StringIO(csv))
con.execute("create table if not exists food_items as select * from food_items ")