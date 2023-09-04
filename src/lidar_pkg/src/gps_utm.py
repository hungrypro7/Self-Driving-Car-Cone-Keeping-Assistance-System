from pyproj import Proj
import matplotlib.pyplot as plt

# UTM 좌표계 정의 (Zone 52, WGS84)
utm_proj = Proj(proj='utm', zone=52, ellps='WGS84')

path_lat = [
    37.2988071, 37.298808199999996, 37.2988103, 37.298814199999995,
    37.2988213, 37.2988289, 37.2988357, 37.2988424, 37.2988494,
    37.2988572, 37.2988648, 37.2988721, 37.2988777, 37.2988852,
    37.298893199999995, 37.298901199999996, 37.298908999999995, 37.2989171,
    37.2989254, 37.2989332, 37.2989405, 37.2989471, 37.2989525,
    37.2989564, 37.2989572
]

path_lon = [
    126.83789519999999, 126.8378936, 126.8378918, 126.83788999999999,
    126.8378857, 126.8378814, 126.83787699999999, 126.8378723, 126.83786819999999,
    126.83786339999999, 126.8378585, 126.8378534, 126.8378482, 126.83784379999999,
    126.83783989999999, 126.8378352, 126.83783039999999, 126.8378243, 126.8378185,
    126.8378132, 126.8378084, 126.83780469999999, 126.837801, 126.8377982,
    126.83779779999999
]
path_x = []
path_y = []

# 위경도를 UTM (x, y) 좌표로 변환
for longitude, latitude in zip(path_lon, path_lat):
    x, y = utm_proj(float(longitude), float(latitude))
    path_x.append(x)
    path_y.append(y)

print(path_x)

print(path_y)
plt.scatter(path_x, path_y)
plt.show()