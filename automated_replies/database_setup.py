import duckdb

conn = duckdb.connect('Tweets.duckdb')
conn.execute("CREATE SEQUENCE seq START 1;")
conn.execute('''Create Table If Not Exists Tweet_Replies (
    id INTEGER DEFAULT nextval('seq'),
    datetime  DATETIME,
    tweet_id BIGINT,
    tweet TEXT Primary Key,
    reply TEXT)''')
