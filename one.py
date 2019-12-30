import pandas
from pyecharts import options as opts
import os
from pyecharts.charts import Bar
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot

path=os.getcwd()+'/dataset.xlsx'
source=pandas.read_excel(path)

columns=source['地区'].tolist()
data1=source['2019年第一季度'].tolist()
data2=source['2018年第一季度'].tolist()

bar=Bar()
bar.add_xaxis(columns[0:6])
bar.add_yaxis('2018',data2[0:6])
bar.add_yaxis('2019',data1[0:6])
bar.set_global_opts(title_opts=opts.TitleOpts(title='部分省市2018/2019年第一季度GDP对比'))
def main():
	make_snapshot(snapshot,bar.render(),"pic1.png")

if __name__ == "__main__":
	main()
