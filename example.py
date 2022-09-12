import requests
import json

# Author : MicosLiang
# email : liangjh21@lzu.edu.cn
# online tool : http://power.micosliang.space:9100/gis/factorfinder

def getfactors(lat, lon):
    url = 'http://power.micosliang.space:9100/gis/getfactors'
    param = {
        'lat' : lat,
        'lon' : lon
    }
    respone = json.loads(requests.get(url, params=param).text)
    return respone

if __name__ == '__main__':
    # 可以接受度分秒格式的输入
    ans = getfactors('35;56;34;N', '104;9;2;E')
    print(ans)
    # 可以接受度
    ans = getfactors(16.02, -10.12)
    print(ans)
    if ans['status_code'] == -1:
        print('输入格式错误或空值/超出范围')
    elif ans['status_code'] == 300:
        print('每日使用次数达到上限')
    elif ans['status_code'] == 200:
        data = ans['data']
        lat = data['lat'] # 纬度
        lon = data['lon'] # 经度
        elev = data['elev'] # 高程
        prec = data['prec'] # 年总降水(mm)
        prec_monthly = data['prec_monthly'] # 月降水(mm)
        tavg = data['tavg_monthly'] # 年均温(摄氏度)
        tavg_monthly = data['tavg_monthly'] # 月均温(摄氏度)
