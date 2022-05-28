import requests
import queries
import json
import sys
import csv
import time


api_token = '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'
token1 = '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'
token2 = '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'
token3 = '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'

headers = {'Authorization': 'token %s' % token1, 'User-Agent': 'request'}

# A simple function to use requests.post to make the API call. Note the json= section.
def run_query(query):
    request = requests.post('https://api.github.com/graphql',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return [request.json(), request.elapsed.microseconds]
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))

# A simple function to use requests.post to make the API call. Note the json= section.
def run_query_rest(query):
    time.sleep(2)
    request = requests.get(query, headers=headers)
    if request.status_code == 200:
        return [request.json(), request.elapsed.microseconds]
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))

def write_in_file(file, header, row):
    with open(file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write multiple rows
        writer.writerows(row)

# for idx, query in enumerate(queries.query_graphql):
#     data = []
#     for x in range(500):
#         row = []
#         query_result = run_query(query)
#         size = sys.getsizeof(json.dumps(query_result[0]))
#         microseconds = query_result[1]
#         row = [size, microseconds]
#         data.append(row)
#     header = ['size', 'miliseconds']
#     if idx == 0:
#         file_name = 'graphql_query_1.csv'
#     else:
#         file_name = 'graphql_query_2.csv'
#     write_in_file(file_name, header, data)

# for idx, query in enumerate(queries.query_rest):
data = []
query = queries.query_rest[1]
for x in range(500):
    row = []
    query_result = run_query_rest(query)
    size = sys.getsizeof(json.dumps(query_result[0]))
    microseconds = query_result[1]
    row = [size, microseconds]
    data.append(row)
header = ['size', 'miliseconds']
idx = 1
if idx == 0:
    file_name = 'rest_query_1.csv'
else:
    file_name = 'rest_query_2.csv'
write_in_file(file_name, header, data)



    

