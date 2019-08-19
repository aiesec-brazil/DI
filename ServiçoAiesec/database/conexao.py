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
 
#Executa uma query
cur.execute("SELECT * FRO  M analytics_today limit 100")
 
#Obtem o resultado de uma consulta no padrao [{"column_name":<value>},{...}]
print(cur.fetchall())
cur.close()
conn.close()
exit()


 
#Efetua a confirmação das operações de INSERT,UPDATE e DELETE efetuadas na transação atual
#conn.commit() 