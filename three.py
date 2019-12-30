from pyecharts import options as opts
import os
from pyecharts.charts import Geo 
from pyecharts.globals import ChartType, SymbolType
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot
import pandas
path=os.getcwd()+'/dataset.xlsx'
source=pandas.read_excel(path)
value=source['2018年第一季度'].tolist()
value = [15.4,21.6,32,16,53.3,30.4,98.4,16.8,34.3,
         3.2,91.8,86.8,63.4,113,11.3,8.7,119,117.6,3.8,
         15.1,14.1,85.2,92.6,14.8,12.2,38.2,69.8,74.7,15.4,
         74.6,18.7]
attr = ['甘肃','广东', '广西','贵州','海南',
        '河南','湖北', '湖南','宁夏','青海',
        '陕西','四川', '西藏','新疆','云南',
        '重庆','北京', '天津','河北','山西','内蒙古',
        '辽宁','吉林', '黑龙江','上海','江苏','浙江','安徽','福建'
        ,'江西','山东']
temp= list(zip(attr,value))
def geo_base() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china")
        .add("各省GDP比较", temp)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="各省GDP比较"),
        )
    )
    return c

c=geo_base()

make_snapshot(snapshot,c.render(),"pic3.png")
