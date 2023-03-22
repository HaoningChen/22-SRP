import pandas as pd

df = pd.read_csv("merge.csv", encoding="gbk")
good_words = ["稳健", "亮点", "优", "亮眼", "买入评级", "稳定增长", "推荐评级", "增持评级", "涨", "靓丽", "改善", "均衡发展", "喜讯",
              "报喜", "同比增长", "大增", "成功", "双降", "推荐", "突破", "走强", "显成效", "崛起", "拉升", "不属实", "IPO", "笑", "发行",
              "落地", "量产"]
bad_words = ["投诉", "跌", "不良率", "风险", "下滑", "压降", "低迷", "市场疑问", "失败", "不尽职", "罚", "增速缓慢", "负增长", "违反",
             "走弱", "下挫", "承压", "衰", "乌龙", "停产", "紧张", "降四成", "质疑", "诉讼", "纠纷", "故障"]
pred = []
for i in range(len(df)):
    val = 1
    for gw in good_words:
        if (gw in df["文章标题"][i]) or (gw in df["文章详情"][i]):
            val = 2
            break
    if val == 1:
        for bw in bad_words:
            if (bw in df["文章标题"][i]) or (bw in df["文章详情"][i]):
                val = 0
                break
    pred.append(val)
df["pred"] = pred
print(df["pred"])
df.to_csv("df.csv", encoding="gbk")
