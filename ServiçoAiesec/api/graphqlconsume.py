import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
import pandas.io.json as pd_json
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import querygraphql

token_get_url = "http://token.aiesec.org.br/get_token.php?token=c0aa46e01d77fb212fe0195636fb515f8e43b530087399ec49f"
access_token_raw = requests.get(token_get_url)
access_token = access_token_raw.text.strip()
#print('Setup complete! \nYour access token is ' + '"'+ access_token +'"')

opp = querygraphql._ICX_

input_query_icx_re = opp

_transport = RequestsHTTPTransport(
    url='https://gis-api.aiesec.org/graphql?access_token='+str(access_token),
    use_json=True,
)
client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)

#Here you insert the query
query_icx_re = gql(input_query_icx_re)
query_icx_re_json = client.execute(query_icx_re)

dados = json.dumps(query_icx_re_json, indent =4)
retorno = json.loads(dados)

retorno = json_normalize(
    retorno['allOpportunityApplication']['data']
    #record_path=['standards'],
    )
for row in retorno:
   campo1 =  retorno['id']
print(campo1)
    
