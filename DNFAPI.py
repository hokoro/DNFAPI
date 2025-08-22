from http.client import responses

import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get('API_KEY')

class APIClient:
    def __init__(self):
        self.base_url="https://api.neople.co.kr/df"
        self.api_key = os.environ.get('API_KEY')

    ## 전체 서버 정보 조회
    def get_servers(self):
        url = f"{self.base_url}/servers"
        params = {"apikey": self.api_key}
        response = requests.get(url,params=params)
        return response.json()

    ## 직업 정보 조회
    def get_jobs(self):
        url = f"{self.base_url}/jobs"
        params = {"apikey": self.api_key}
        response = requests.get(url , params=params)
        return response.json()   # 직업별 1차 2차 3차 고유 아이디가 존재함

    ## 캐릭터 조회
    def get_character(self , server, nickname):
        url= f"{self.base_url}/servers/{server}/characters?characterName={nickname}"    # 서버는 무조건 영어 1.all(전 서버) 2.서버 이름
        params = {"apikey": self.api_key}
        response = requests.get(url , params=params)
        return response.json()

    ## 캐릭터 기본 정보 조회
    def get_character_basic_information(self , server , nickname):
        url=f"{self.base_url}/servers/{server}/characters?characterName={nickname}"      # 해당 함수는 all 조건이 없음
        params = {"apikey":self.api_key}
        response = requests.get(url , params=params)
        return response.json()

    ## 캐릭터 타임라인 정보 조회
    def get_character_timeline_information(self,server,characterId,startdate , enddate,limit):
        url = f"{self.base_url}/servers/{server}/characters/{characterId}/timeline"
        params = {
            "startDate": startdate,
            "endDate": enddate,
            "limit": limit,
            "apikey": self.api_key
        }
        response = requests.get(url , params=params)
        return response.json()

    ## 캐릭터 스탯 조회
    def get_character_status_information(self , server , characterId):
        url= f"{self.base_url}/servers/{server}/characters/{characterId}/status"
        params = {"apikey":self.api_key}
        response = requests.get(url , params=params)
        return response.json()

    ## 캐릭터 장착 장비 조회
    def get_character_equipment_information(self,server,characterId):
        url= f"{self.base_url}/servers/{server}/characters/{characterId}/equip/equipment"
        params = {"apikey":self.api_key}
        response = requests.get(url , params=params)
        return response.json()

    ## 캐릭터 장착 아바타
    def get_character_avartar_information(self,server,characterId):
        url = f"{self.base_url}/servers/{server}/characters/{characterId}/equip/avatar"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    ## 캐릭터 장착 크리처
    def get_character_creature_information(self , server,characterId):
        url = f"{self.base_url}/servers/{server}/characters/{characterId}/equip/creature"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    ## 캐릭터 장착 휘장
    def get_character_flag_information(self,server,characterId):
        url = f"{self.base_url}/servers/{server}/characters/{characterId}/equip/flag"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    ## 캐릭터 스킬트리
    def get_character_skills_information(self,server,characterId):
        url = f"{self.base_url}/servers/{server}/characters/{characterId}/skill/style"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    ### 버프강화 장비
    def get_character_buff_skills_equip_information(self,server,characterId):
        url = f"{self.base_url}/servers/{server}/characters/{characterId}/skill/buff/equip/equipment"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    ### 버프강화 아바타
    def get_character_buff_skills_equip_avartar_information(self,server,characterId):
        url = f"{self.base_url}/servers/{server}/characters/{characterId}/skill/buff/equip/avatar"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()

    ### 버프강화 크리처
    def get_character_buff_skills_equip_creature_information(self,server,characterId):
        url = f"{self.base_url}/servers/{server}/characters/{characterId}/skill/buff/equip/creature"
        params = {"apikey": self.api_key}
        response = requests.get(url, params=params)
        return response.json()


api_1 = APIClient()

# servers = api_1.get_servers()['rows']
#
# for info in servers:
#     print(f'serverId:{info['serverId']} , serverName: {info['serverName']}')




# jobs = api_1.get_jobs()['rows']
#
# for info in jobs:
#     print(f'직업 고유 아이디: {info['jobId']} , 직업 이름: {info['jobName']}')
#
#     for firstChangeJob in info['rows']:
#         print(firstChangeJob)
#         print(f'1차 고유 id: {firstChangeJob['jobGrowId']} , jobGrowName: {firstChangeJob['jobGrowName']}')
#         secondChangeJob = firstChangeJob['next']
#         print(f'2차 고유 id: {secondChangeJob['jobGrowId']} , jobGrowName: {secondChangeJob['jobGrowName']}')
#         thirdChangeJob = secondChangeJob['next']
#         print(f'3차 고유 id: {thirdChangeJob['jobGrowId']} , jobGrowName: {thirdChangeJob['jobGrowName']}')
#         if info['jobName'] != '다크나이트' and info['jobName'] != '크리에이터':
#             lastChangeJob = thirdChangeJob['next']
#             print(f'4차 고유 id: {lastChangeJob['jobGrowId']} , jobGrowName: {lastChangeJob['jobGrowName']}')
#         print('-' * 30)
#     print('-' * 30)

characterid='fccf5f0b7533219313aed50bbb6f403d'
# print(api_1.get_character('all','반요반인'))
#
#
#
#
# print(api_1.get_character_basic_information('cain' , '반요반인'))
#
# #timeline?startDate=2018-09-01 00:00&endDate=2018-09-30 23:59
# startdate_str = "2025-08-22 07:23"
# enddate_str = "2025-08-22 07:24"
#
# import datetime
#
# startdate = datetime.datetime.strptime(startdate_str , "%Y-%m-%d %H:%M")
# enddate = datetime.datetime.strptime(enddate_str , "%Y-%m-%d %H:%M")
#
# limit = 20
# #https://api.neople.co.kr/df/servers/cain/characters/fccf5f0b7533219313aed50bbb6f403d/timeline?startDate=2025-07-01 00:00&endDate=2025-08-01 00:00&limit=10&apikey=XeHPXQEJzwWd7RN9aTTAq1o8YroOdrFi
# print(api_1.get_character_timeline_information('cain' , characterid , startdate , enddate,limit))
#
#
#
# print(api_1.get_character_status_information('cain',characterid))


#print(api_1.get_character_equipment_information('cain',characterid))

#print(api_1.get_character_avartar_information('cain',characterid))
#print(api_1.get_character_creature_information('cain',characterid))

# print(api_1.get_character_flag_information('cain',characterid))
# print(api_1.get_character_skills_information('cain',characterid))
#print(api_1.get_character_buff_skills_equip_information('cain',characterid))

#print(api_1.get_character_buff_skills_equip_avartar_information('cain',characterid))
print(api_1.get_character_buff_skills_equip_creature_information('cain',characterid))
