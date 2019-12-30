import pandas
from pyecharts import options as opts
import os
from pyecharts.charts import Pie 
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot

path=os.getcwd()+'/dataset.xlsx'
source=pandas.read_excel(path)

columns=source['地区'].tolist()
data1=source['2018年第一季度']+source['2018年第二季度']+source['2018年第三季度']+source['2018年第四季度']

data2=data1.tolist()
data3=data2[0:8]
temp=list(zip(columns,data3))

def pie_base() -> Pie:
    c = (
        Pie()
        .add("", temp)
        .set_global_opts(title_opts=opts.TitleOpts(title="2018年北方\n大省GDP组成"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c

c=pie_base()

make_snapshot(snapshot,c.render(),"pic2.png")
