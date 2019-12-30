import pandas
from pyecharts import options as opts
import os
from pyecharts.charts import Funnel
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot

path=os.getcwd()+'/dataset.xlsx'
source=pandas.read_excel(path)
data1=source['2018年第一季度']+source['2018年第四季度']+source['2018年第三季度']+source['2018年第二季度']
data2=data1.tolist()
columns=source['地区'].tolist()
temp=list(zip(columns[0:8],data2[0:8]))
def funnel() -> Funnel:
    c = (
        Funnel()
        .add(
            "GDP",
			temp,
            label_opts=opts.LabelOpts(position="inside"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="2018年部分省\n市GDP漏斗图"))
    )
    return c

c=funnel()
make_snapshot(snapshot,c.render(),"pic9.png")

