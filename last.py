
import csv
import math as m
f = open('a.csv', encoding = 'cp949')
c = csv.reader(f)

city = input("도시를 입력하세요(~도 ~시): ")
alldata = []
g = 978032.677

        
def standardG(o):  #표준 중력값 구하기
    sin2 = (m.sin(m.radians(o)))**2
    return g*(1+0.005278895*sin2+0.000023462*sin2**2)

def freeAirCorrection(h): #프리에어 보정
    return 0.308*h

def freeAirAnomaly(g, h, o): #프리에어 이상
    return (g - standardG(o)+freeAirCorrection(h))

def bouguerCorrection(p, h): #부게보정
    return 0.0419 * p * h

def bouguerAnomaly(g, h, o, p): #부게이상
    return freeAirAnomaly(g, h, o) - bouguerCorrection(p, h)

def terrainCorrection(g, h, o, p, gBC): #완전 부게이상
    return gBC - bouguerAnomaly(g,h,o,p)


for row in c:
    if city in row[0]:
        alldata = row
        wido = float(row[1])
        kyongdo = float(row[2])
        godo = float(row[3])
        g_obs = float(row[4])
        gb = float(row[5])
        den = float(row[7])
        print(alldata)
        tc = terrainCorrection(g,godo, wido, den, gb)
        print(tc/1000)
    else:
        print("데이터가 없쪄용ㅠㅠ")
        
for i in c:
    l = i
    location = str(l[0])
    latitude = float(l[1])
    longitude = float(l[2])
    h = float(l[3])
    g = float(l[4])
    gBC = float(l[5])
    stone = str(l[6])
    p = float(l[7])
    dgt = terrainCorrection(g, h, latitude, p, gBC)
