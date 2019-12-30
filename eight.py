from pyecharts.faker import Faker
import random
from pyecharts import options as opts
from pyecharts.charts import Bar3D
import pandas
import os
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot
path=os.getcwd()+'/dataset.xlsx'
source=pandas.read_excel(path)

data1=source['2018年第一季度'].tolist()[0:6]
data2=source['2018年第二季度'].tolist()[0:6]
data3=source['2018年第三季度'].tolist()[0:6]
data4=source['2018年第四季度'].tolist()[0:6]
data=data1+data2+data3+data4
x=['北京','天津','河北','山西','内蒙古','辽宁']
y=['2018年第一季度','2018年第二季度','2018年第三季度','2018年第四季度']
aa=[]
for i in range(len(x)):
    for j in range(len(y)):
        aa.append([x[i],y[j]])
for l in range(len(aa)):
    aa[l].append(data[l])
def bar3d_base() -> Bar3D:
    c = (
        Bar3D()
        .add(
            "",
			aa,
            xaxis3d_opts=opts.Axis3DOpts(x, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(y, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=27000),
            title_opts=opts.TitleOpts(title="北方五省2018年四季度GDP分布"),
        )
    )
    return c


c=bar3d_base()
c.render()
