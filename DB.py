import mysql.connector
from dotenv import load_dotenv
import os
from DNFAPI import APIClient

load_dotenv()



conn = mysql.connector.connect(
    host=os.environ.get('HOST'),
    user=os.environ.get('USER'),
    password=os.environ.get('PASSWORD'),
    database= os.environ.get('DATABASE')
)

if conn.is_connected():
    print('연결 성공')
else:
    print('연결 실패')


cursor = conn.cursor()


api_2 = APIClient()


# ## 서버 데이터 테이블에 데이터 삽입
# servers = api_2.get_servers()['rows']
#
#
# for info in servers:
#     insert_query = "INSERT INTO server (serverId , serverName) VALUES (%s, %s)"
#     values = (info['serverId'] , info['serverName'])
#     cursor.execute(insert_query, values)
#
# conn.commit()
# print('서버 데이터 삽입 완료 ')


# ## 데이터 읽어오기
# select_query = "SELECT * FROM server"
# cursor.execute(select_query)
# rows = cursor.fetchall()
#
# for row in rows:
#     print(row)

## 직업 데이터 베이스 데이터 삽입

jobs = api_2.get_jobs()['rows']
## 기본 캐릭 정보
for info in jobs:
    insert_query_base = "INSERT INTO base_job (jobid , jobname) Values(%s, %s)"
    values_base = (info['jobId'] , info['jobName'])
    cursor.execute(insert_query_base , values_base)

conn.commit()
print('기본 직업 데이터 삽입 완료 ')
