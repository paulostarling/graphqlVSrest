import pandas as pd

df = pd.read_csv("graphql_query_1.csv")
query1_graphql_time =  df['miliseconds'].median()
query1_graphql_size =  df['size'].median()

df = pd.read_csv("graphql_query_2.csv")
query2_graphql_time =  df['miliseconds'].median()
query2_graphql_size =  df['size'].median()

df = pd.read_csv("rest_query_1.csv")
query1_rest_time =  df['miliseconds'].median()
query1_rest_size =  df['size'].median()

df = pd.read_csv("rest_query_2.csv")
query2_rest_time =  df['miliseconds'].median()
query2_rest_size =  df['size'].median()

print(query1_graphql_time) 