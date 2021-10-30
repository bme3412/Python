from sec_api import QueryApi
import pandas as pd

# initialize the query API
queryApi = QueryApi(api_key="f9ecedc27fe61f3446e4fbed18506805f8c78aebc5b9b679e5be375cbfb206ec")

def get_13f_filings(start=0):
    print(f"Getting next 13F batch starting at {start}")
    
    query = {
      "query": { "query_string": { 
          "query": "formType:\"13F-HR\" AND NOT formType:\"13F-HR/A\" AND periodOfReport:\"2021-06-30\"" 
        } },
      "from": start,
      "size": "10",
      "sort": [{ "filedAt": { "order": "desc" } }]
    }

    response = queryApi.get_filings(query)

    return response['filings']

# fetch the 10 most recent 13F filings
filings_batch = get_13f_filings(10)

# load all holdings of the first 13F filing into a pandas dataframe 
holdings_example = pd.json_normalize(filings_batch[0]['holdings'])
holdings_example.head()