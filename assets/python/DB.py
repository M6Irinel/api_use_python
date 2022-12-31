import mysql.connector

from env import ENV

env = ENV()

db = mysql.connector.connect(
    host=env['host'],
    user=env['user'],
    password=env['password'],
    database=env['database']
)

cursor = db.cursor()

def select(table):
    try:
        columns = selectColumns(table)
        sql = "SELECT * FROM {};".format(table)
        cursor.execute(sql)
        res = []
        for i in cursor.fetchall():
            di = {}
            for e in range(len(columns)):
                di.update({columns[e][0] : i[e]})
            res.append(di)
        return res
    except:
        return 'ERROR: NELLA SELEZIONE DELLA TABELLA'


def selectColumns(table: str):
    sql = "SHOW COLUMNS FROM {}".format(table)
    cursor.execute(sql)
    return cursor.fetchall()
    

def insert(table: str, columns: str, values: str):
    try:
        tc = columns.split(',')
        tv = values.split(',')
        if len(tc) == len(tv):
            v = ''
            for i in range(len(tc)): v += "'{}',".format(tv[i])
            sql = "INSERT INTO {} {} VALUES ({});".format(table, "({})".format(columns), v[:-1])
            cursor.execute(sql)
            db.commit()
            return 'SUCCESS QUERY'
        else:
            return 'ERROR: LA LUNGHEZZA DEI CAMPI DELLA COLONNA E VALORI NON SONO UGUALI'
    except:
        return 'ERROR: NELLA COMPILAZIONE DELLA QUERY'