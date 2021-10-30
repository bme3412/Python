# fill-database.py
import sys
import psycopg2
import mysql.connector
from sec_api import QueryApi

queryApi = QueryApi(api_key="f9ecedc27fe61f3446e4fbed18506805f8c78aebc5b9b679e5be375cbfb206ec")



# establishing the connection
conn = mysql.connector.connect(user='root', password='Boston1429$$',
                              host='127.0.0.1', database = '13F')

def get_13f_filings(start=0, period="2021-06-30"):
    print(f"Getting next 13F batch starting at {start}, {period}")

    query = {
        "query": {
            "query_string": {
                "query": f'formType:"13F-HR" AND NOT formType:"13F-HR/A" AND periodOfReport:"{period}"'
            }
        },
        "from": start,
        "size": "10",
        "sort": [{"filedAt": {"order": "desc"}}],
    }

    response = queryApi.get_filings(query)

    return response["filings"]
    
    
def save_to_db(filings):
    cur = conn.cursor()

    for filing in filings:
        if len(filing["holdings"]) == 0:
            continue

        insert_commands = (
            """
                INSERT INTO filings (
                    filing_id, 
                    cik,
                    filer_name,
                    period_or_report
                ) 
                VALUES (%s, %s, %s, %s)
            """,
            """
                INSERT INTO holdings (
                    filing_id, 
                    name_of_issuer,
                    cusip,
                    title_of_class,
                    value,
                    shares,
                    put_call
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
        )

        filing_values = (
            filing["id"],
            filing["cik"],
            filing["companyName"].upper(), 
            filing["periodOfReport"],
        )

        cur.execute(insert_commands[0], filing_values)

        for holding in filing["holdings"]:
            holding_values = (
                filing["id"],
                holding["nameOfIssuer"].upper(), 
                holding["cusip"],
                holding["titleOfClass"] if "titleOfClass" in holding else "",
                holding["value"],
                holding["shrsOrPrnAmt"]["sshPrnamt"],
                holding["putCall"] if "putCall" in holding else ""
            )

            cur.execute(insert_commands[1], holding_values)

    cur.close()
    conn.commit()
    
    
def fill_database():
    start = 0
    period = '2021-06-30'

    while start < 10000:
        filings = get_13f_filings(start, period)
        
        if len(filings) == 0:
            break
            
        save_to_db(filings)
        start = start + 10

    print("Done")
       

fill_database()