# FinalExam Sel-organise: Sandpile model
2013301020084 许晗

## 说明
主程序:sandpile.py;

任意曲线方程拟合数据:data_analyse.py;

有一次N=10000的计算结果存入了:data.txt中;

sandavalanch01.png: collapes caused by one drop

![oneshot!](https://raw.githubusercontent.com/MilCOS/computationalphysics_N2013301020084/master/final/sandavalanch01.png)

100_avalanch_10000.png: the amount of collapes happend in 10,000 times randomadd and evolve distributed in the lattice
![10000](https://raw.githubusercontent.com/MilCOS/computationalphysics_N2013301020084/master/final/100_avalanch_10000.png)

1ei_iej_distribution.png: the fitcurve of the data from a N=10,000 calculation, selecting the $N \in [10^i,10^j)$ to fit.
![0,2](https://raw.githubusercontent.com/MilCOS/computationalphysics_N2013301020084/master/final/1e0_1e2_distribution.png)
##全文链接
[To the Moon!](https://www.zybuluo.com/MilCOS/note/412485)

## 不好储存的数据

N:总坍塌次数, D:每次投点所引起的平均坍塌次数的倒数, iN:在$100\times 100$的点阵里有$i$个$10\times 10$的方形边界, L:总点阵大小, l:内部方形边界大小$l\times l$
### 总点阵大小

|L |    10|    20|    30|    40|   50|    60|    80|   100|   200|
|--|-- :  |--   :|--   :|   --:|  --:|   --:|--   :|--:   |--:   |
|N | 398  | 2280 |  4764| 11790|18085|32184 |39863 |75164 |176191|
|D | 0.502| 0.088| 0.042| 0.017|0.011|0.0062|0.0050|0.0027|0.0011|

correspond to "size_distribution"

![](https://raw.githubusercontent.com/MilCOS/computationalphysics_N2013301020084/master/final/size_distribution.png)

### 特殊边界条件
|l*l |    10|    20|    30|    40|    50|    60|    70|    80|
|--  |-- :  |--   :|--   :|   --:|   --:|   --:|--   :|--:   |
|1N  |72660 |50320 |39389 | 29988| 26139|25151 |30753 |50231 |
|1D  |0.0055|0.0080|0.0102|0.0133|0.0153|0.0159|0.0130|0.0080|
|--  |--    |--    |--    |   -- |   -- |   -- |--    |--    |
|2N  |53259 |43972 |22992 |
|2D  |0.0075|0.0091|0.0117|
|3N  |47730 |
|3D  |0.0084|
|4N  |30354 |
|4D  |0.0105|
|5N  |32518 |
|5D  |0.0123|
|6N  |31286 |
|6D  |0.0128|
|7N  |31231 |
|7D  |0.0128|
|8N  |27310 |
|7D  |0.0146|

correspond to "avaboundary_10_400_i", which represent boundary-iN said as above and are averaged for 400 times random add and evolve
![i=4](https://raw.githubusercontent.com/MilCOS/computationalphysics_N2013301020084/master/final/avaboundary_10_400_3.png)
![i=8](https://raw.githubusercontent.com/MilCOS/computationalphysics_N2013301020084/master/final/avaboundary_10_400_8.png)
**and**

correspond to "avaboundary_i_400", which represent boundary-il*il said as above and are averaged for 400 times random add and evolve
![l=70](https://raw.githubusercontent.com/MilCOS/computationalphysics_N2013301020084/master/final/avaboundary_70_400.png)
