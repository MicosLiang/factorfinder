# 经纬度查询环境条件工具

## API

#### 请求
- url : http://power.micosliang.space:9100/gis/getfactors
- method : get

- parmas:

| 参数 | 说明 |
|----- | -----|
| lat  | string, 可以为';'分隔的度分秒形式，如南纬36度03分0秒写作36;3;0;S。也可为度，如-36.05。南纬为负，北纬为正|
| lon  | string, 同上。东经为正，西经为负|

- return:

|返回值|说明|
|----- | -----|
|lat|纬度|
|lon|经度|
|elev|高程（m）|
|prec|年降水（mm）|
|prec_monthly|月降水（mm）|
|tavg|年均温（摄氏度）|
|tavg_monthly|月均温（摄氏度）|


#### 其他
- 数据引用：Fick, S.E. and R.J. Hijmans, 2017. WorldClim 2: new 1km spatial resolution climate surfaces for global land areas. International Journal of Climatology 37 (12): 4302-4315.
- 每IP每日访问量1000次，如有大量使用需要或指导意见请联系
- 邮箱：liangjh21@lzu.edu.cn
