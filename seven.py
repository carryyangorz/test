from pyecharts import options as opts
import re
import pandas
import os
import random
from pyecharts.charts import Line
import math
from pyecharts.globals import ChartType, SymbolType
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot

path=os.getcwd()+'/dataset.xlsx'
source=pandas.read_excel(path)
mine=source.loc[:,['地区','2018年第一季度','2018年第二季度','2018年第三季度','2018年第四季度','2019年第一季度','2019年第二季度','2019年第三季度']]
temp=mine.groupby('地区')
beijing=temp.get_group('北京市')
del beijing['地区']
#x=beijing.columns.tolist()
x=['2018/1','2018/2','2018/3','2018/4','2019/1','2019/2','2019/3']
print(x)
data1=beijing.loc[0]
shanghai=temp.get_group('上海市')
del shanghai['地区']
data2=shanghai.loc[8]

guang=temp.get_group('广东省')
del guang['地区']
data3=guang.loc[18]

def line_base() -> Line:
    c = (
        Line()
        .add_xaxis(x)
        .add_yaxis("北京", data1)
        .add_yaxis("上海", data2)
		.add_yaxis("广东",data3)
        .set_global_opts(title_opts=opts.TitleOpts(title="北上广GDP走势"))
    )
    return c

c=line_base()

make_snapshot(snapshot,c.render(),"pic7.png")

