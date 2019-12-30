from pyecharts import options as opts
import os
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot

value = [15.4,21.6,32,16,53.3,30.4,98.4,22,42,16,9]
attr = ['惠州','东莞','广州','深圳','佛山','中山','肇庆','汕尾','云浮','江门','珠海']
temp= list(zip(attr,value))

def geo_guangdong() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="广东")
        .add(
            "GDP",
			temp,
            type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="广东GDP热力图模拟"),
        )
    )
    return c




c=geo_guangdong()

make_snapshot(snapshot,c.render(),"pic5.png")


