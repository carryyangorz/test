from pyecharts.faker import Faker
import random
from pyecharts import options as opts
from pyecharts.charts import Bar3D,Scatter3D
import pandas
import os
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot
path=os.getcwd()+'/dataset.xlsx'
source=pandas.read_excel(path)

data111=source['2017年第一季度']
data222=source['2017年第二季度']
data333=source['2017年第三季度']
data444=source['2017年第四季度']
data11=source['2018年第一季度']
data22=source['2018年第二季度']
data33=source['2018年第三季度']
data44=source['2018年第四季度']
data1=((data11-data111)/data111).tolist()[0:6]
data2=((data22-data222)/data222).tolist()[0:6]
data3=((data33-data333)/data333).tolist()[0:6]
data4=((data44-data444)/data444).tolist()[0:6]
data=data1+data2+data3+data4
x=['北京','天津','河北','山西','内蒙古','辽宁']
y=['2018年第一季度','2018年第二季度','2018年第三季度','2018年第四季度']
aa=[]
for i in range(len(x)):
    for j in range(len(y)):
        aa.append([x[i],y[j]])
for l in range(len(aa)):
    aa[l].append(data[l])


def scatter3d_base() -> Scatter3D:
    c = (
        Scatter3D()
        .add("", aa)
        .set_global_opts(
            title_opts=opts.TitleOpts("部分省2018/2017年 同季度GDP增量分布"),
            visualmap_opts=opts.VisualMapOpts(max_=1, min_=0,range_color=Faker.visual_color),
        )
    )
    return c
c=scatter3d_base()
c.render()
