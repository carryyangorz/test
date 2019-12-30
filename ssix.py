import pandas
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot
import os
path=os.getcwd()+'/dataset.xlsx'
source=pandas.read_excel(path)
mine=source.loc[:,['地区','2019年第一季度','2018年第一季度']]
a=mine['2019年第一季度']
b=mine['2018年第一季度']
c=a-b
d=c/b
ls=[]
city=['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆']
temp= list(zip(city,d))
def map_visualmap() -> Map:
    c = (
        Map()
        .add("GDP",temp, "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="各省2018/2019年第一季度GDP增速分布"),
            visualmap_opts=opts.VisualMapOpts(max_=0.2, is_piecewise=True),
        )
    )
    return c

aa=map_visualmap()

make_snapshot(snapshot,aa.render(),"pic6.png")


