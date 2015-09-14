# coding: utf-8
import socket
import urllib2
import json
from termcolor import colored


prefix = "HeWeather data service 3.0"


def get_response(city):
    url = 'http://apis.baidu.com/heweather/weather/free?'
    if '.' not in city:
        url = url + 'city='+ city
    else:
        url = url + 'cityip='+city
    try:
        req = urllib2.Request(url)
        req.add_header("apikey", "cae6f7080f56f747e0ad1c87100018e4")
        resp = urllib2.urlopen(req)
        content = resp.read()
        content = json.loads(content)
        return content
    except urllib2.URLError:
        print u"网络好像有些故障"
        return
# print get_response('北京')

def get_local_weather():
    localIP = socket.gethostbyname(socket.gethostname())#得到本地ip
    content = get_response(localIP)
    return  content


def get_weather(content):
    basic = content[prefix][0]
    if content.get("errNum", False):
        print content["errMsg"]
    elif basic["status"] != "ok":
        print basic[0]["status"]
    else:
        city = basic["basic"]["city"]
        pm25 = basic["aqi"]["city"]["pm25"]
        weather = basic["now"]["cond"]["txt"]
        temp = basic["now"]["tmp"]

        print u"城 市:".ljust(5," ") + city
        print colored(u"PM2.5:".ljust(5," ") + pm25, "blue")
        print colored(u"天 气:".ljust(5," ")+ weather, "green")
        print colored(u"气 温:".ljust(5," ") + temp, "red")

def main():
    city = raw_input("city input: ")
    con = get_response(city)
    get_weather(con)

if __name__ == '__main__':
    main()
