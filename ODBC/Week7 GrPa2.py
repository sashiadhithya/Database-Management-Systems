import psycopg2
import sys
import os
from math import pi, cos

database = sys.argv[1]
user = os.environ.get('PGUSER')
password = os.environ.get('PGPASSWORD')
host = os.environ.get('PGHOST')
port = os.environ.get('PGPORT')

def char():
    with open('parameter.txt') as f:
        first_line = f.readline()
    return first_line[0]+'%'

def calc(ans):
    return round(cos((ans)*10*(pi/180)),2)

def get_ans(database, user, password, host, port):
    conn = None
    para = char()
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database = database, user = user,
                password = password, host = host, port = port)
        cur = conn.cursor() # create a new cursor
        # execute the SELECT statement
        cur.execute('select SUM(m.host_team_score) as ans from matches as m, teams as t where t.name like %s and t.team_id = m.host_team_id and m.host_team_score > m.guest_team_score', (para,))
        ans = cur.fetchall() # fetches all rows of the query result set
        return(calc(int(ans[0][0])))
        cur.close() # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection

print(get_ans(database, user, password, host, port))

'''
import psycopg2
import sys
import os
from math import pi, cos

def char():
    with open('parameter.txt') as f:
        first_line = f.readline()
    return first_line[0]+'%'

def calc(ans):
    return round(cos((ans)*10*(pi/180)),2)

def get_ans(database, user, password, host, port):
    conn = None
    para = char()
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database = database, user = user,
                password = password, host = host, port = port)
        cur = conn.cursor() # create a new cursor
        # execute the SELECT statement
        cur.execute('select SUM(m.host_team_score) as ans from matches as m, teams as t where t.name like %s and t.team_id = m.host_team_id and m.host_team_score > m.guest_team_score', (para,))
        ans = cur.fetchall() # fetches all rows of the query result set
        return(calc(int(ans[0][0])))
        cur.close() # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection

print(get_ans('flisdb', 'postgres', 'Gfivez17!', 'localhost', '5432'))
'''