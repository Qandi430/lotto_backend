import requests
import json
from .models import DrawHistory

def getLottoByApi():
    last_history = getLastHistory()         #마지막 추첨 기록
    last_draw_no = 0                        #추첨번호
    print(last_history)

    if(last_history != None):                   #마지막 추첨 기록이 있을 경우(데이터 존재)
        last_draw_no = last_history.draw_no     #추첨번호 = 마지막 추첨기록의 추첨번호
    
    print(last_history)
    while True:                                 #반복
        last_draw_no += 1                       #추첨번호 하나씩 증가
        service_address = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="+ str(last_draw_no)       #추첨 기록 API 주소
        print(service_address)
        response = requests.get(service_address)  #api request
        response.raise_for_status()               #error
        results = response.json()                 #response json변환
        print(json.dumps(results))
        if(results["returnValue"] == "fail"):     #기록없을 경우(미추첨 회차)
            break
        else:                                     #추첨 기록 있을경우 database save
            data = DrawHistory(
                draw_no=results["drwNo"],
                draw_no_1=results["drwtNo1"],
                draw_no_2=results["drwtNo2"],
                draw_no_3=results["drwtNo3"],
                draw_no_4=results["drwtNo4"],
                draw_no_5=results["drwtNo5"],
                draw_no_6=results["drwtNo6"],
                draw_date=results["drwNoDate"]
            )
            data.save()

def getLastHistory():
    print("getLastHistory")
    queryset = DrawHistory.objects.last()
    print(queryset)
    return queryset