import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import psycopg2
import psycopg2.extras




try:
    #Efetua a conexao com o banco de dados
     conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (
        "dashboardbf",
        "thaleslopes",
       "dashboard-bf.cpcjumtjwpk7.us-west-1.rds.amazonaws.com",
        "4568520rds"
        ))
except:
    print("Erro ao logar no banco de dados.")
    exit()
 
#Efetua a criacao do cursor python com o banco de dados para efetuar a execucao dos sqls
cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
cur.execute("INSERT INTO teste (user_dsc) VALUES ('Jeje')")
conn.commit()
cur.execute("SELECT * FROM teste")
cur.fetchall()
cur.close()
conn.close()

token_get_url = "http://token.aiesec.org.br/get_token.php?token=c0aa46e01d77fb212fe0195636fb515f8e43b530087399ec49f"
access_token_raw = requests.get(token_get_url)
access_token = access_token_raw.text.strip()
#print('Setup complete! \nYour access token is ' + '"'+ access_token +'"')

input_query = querygraphql.query_01 

_transport = RequestsHTTPTransport(
    url='https://gis-api.aiesec.org/graphql?access_token='+str(access_token),
    use_json=True,
)
client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)

#Here you insert the query
def executaGraphQL(grapgQl):
    query = gql(input_query)
    query_json = client.execute(query)

    dados = json.dumps(query_json, indent =4)
    retorno = json.loads(dados)

    retorno = json_normalize(
        retorno['allOpportunityApplication']['data']
    )
    for row in retorno:
        conexao.cur.execute("INSERT INTO TESTE(user_id,user_dsc,grant_date) VALUES (%s, %s, %s )",(retorno['id'],
                                                                                                   retorno['status'],
                                                                                                   retorno['status']))
      
