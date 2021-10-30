import mysql.connector

# establishing the connection
conn = mysql.connector.connect(user='root', password='Boston1429$$',
                              host='127.0.0.1', database='13F')



def create_tables():
    cur = conn.cursor()

    # create tab;es
    create_table_commands = (
        """
            CREATE TABLE filings (
                filing_id varchar(255) PRIMARY KEY,
                cik int,
                filer_name varchar(255),
                period_or_report date
            )
        """,
        """
            CREATE TABLE holdings (
                filing_id varchar(255),
                name_of_issuer varchar(255),
                cusip varchar(255),
                title_of_class varchar(255),
                value bigint,
                shares int,
                put_call varchar(255)
            )

        """,
        """
            CREATE TABLE holdings_infos (
                cusip varchar(255),
                security_name varchar(255),
                ticker varchar(50),
                exchange_code varchar(10),
                security_type varchar(50)
            )
        """)
    
    # creeat table one by one
    for command in create_table_commands:
        cur.execute(command)
    
    # close cursor
    cur.close()

    # make the changes to the database persistent
    conn.commit()

create_tables()