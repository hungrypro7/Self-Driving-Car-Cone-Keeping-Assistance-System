from pyproj import Proj
import matplotlib.pyplot as plt

# UTM 좌표계 정의 (Zone 52, WGS84)
utm_proj = Proj(proj='utm', zone=52, ellps='WGS84')

path_lat = [ 37.3014406, 37.301440299999996, 37.301438, 37.3014327, 37.3014248, 37.3014149, 37.3014033, 37.3013897, 37.3013747, 37.3013596, 37.3013443, 37.3013323, 37.3013203, 37.3013068, 37.3012922, 37.3012763, 37.3012619, 37.301246899999995, 37.301229899999996, 37.3012114, 37.3011921, 37.3011732, 37.3011541, 37.3011377, 37.301128999999996, 37.3011228, 37.3011149, 37.301104599999995, 37.3010884, 37.3010704, 37.3010532, 37.3010351, 37.3010174, 37.3009993, 37.300982, 37.300971499999996, 37.3009699]
path_lon = [ 126.8347268, 126.8347266, 126.8347251, 126.83472069999999, 126.8347129, 126.83470279999999, 126.83469149999999, 126.8346796, 126.8346684, 126.8346605, 126.83466, 126.83466659999999, 126.8346744, 126.8346838, 126.83469269999999, 126.83469299999999, 126.8346859, 126.834678, 126.8346711, 126.83466259999999, 126.8346531, 126.8346421, 126.83463139999999, 126.834616, 126.8345935, 126.83456969999999, 126.8345459, 126.8345236, 126.83450939999999, 126.83450389999999, 126.83449429999999, 126.8344826, 126.8344707, 126.83445979999999, 126.83444879999999, 126.8344422, 126.8344412]
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