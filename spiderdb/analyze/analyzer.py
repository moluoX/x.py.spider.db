from spiderdb.dataaccess import get_lagou
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False

db = get_lagou()
datas = pd.DataFrame(list(db.position.find({'city': {'$in': ['北京', '上海', '深圳', '广州']}},
                                           projection={'xkeyword': True, 'salary': True, 'city': True})))
datas['xkeyword'][datas['xkeyword'] == 'C#'] = '.net'
datas['xlow'] = datas['salary'].str.extract(r'(\d+k-|\d+k以上)').replace(regex=r'k|-|以上', value='').astype(float)
datas['xhigh'] = datas['salary'].str.extract(r'(-\d+k|\d+k以上)').replace(regex=r'k|-|以上', value='').astype(float)
datas['xmid'] = (datas['xlow'] + datas['xhigh']) / 2
group = datas.groupby(['xkeyword', 'city'])

mean = group.mean()[['xlow', 'xmid', 'xhigh']].sort_values(by=['xkeyword'], ascending=[True])
mean.plot(kind='bar', stacked=False)
plt.show()

max = group.max()[['xlow', 'xmid', 'xhigh']].sort_values(by=['xkeyword'], ascending=[True])
max.plot(kind='bar', stacked=False)
plt.show()
