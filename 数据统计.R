dd1 <- read.csv("D:/py/Spider/情感分析表.csv", header = T)
dd2 <- read.csv("D:/py/Spider/tt2.csv", header = T)
dd3 <- read.csv("D:/py/Spider/tt3.csv", header = T)

wilcox.test(dd1$评分,dd2$评分,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd2$评分,dd3$评分,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd1$评分,dd3$评分,alternative='greater',var.equal=FALSE, conf.level=0.90)

#仅豆瓣
dd1 <- read.csv("D:/py/Spider/t1.csv", header = T)
dd2 <- read.csv("D:/py/Spider/t2.csv", header = T)
dd3 <- read.csv("D:/py/Spider/t3.csv", header = T)

wilcox.test(dd1$评分,dd2$评分,alternative='greater',var.equal=FALSE, conf.level=0.90)


#分句情感分数
dd1 <- read.csv("D:/py/Spider/qt1.csv", header = T)
dd2 <- read.csv("D:/py/Spider/qt2.csv", header = T)
dd3 <- read.csv("D:/py/Spider/qt3.csv", header = T)
wilcox.test(dd1$剧情,dd2$剧情,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd1$剧情,dd3$剧情,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd2$剧情,dd3$剧情,alternative='greater',var.equal=FALSE, conf.level=0.90)

wilcox.test(dd1$演员,dd2$演员,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd1$演员,dd3$演员,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd2$演员,dd3$演员,alternative='greater',var.equal=FALSE, conf.level=0.90)

wilcox.test(dd1$搞笑,dd2$搞笑,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd1$搞笑,dd3$搞笑,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd2$搞笑,dd3$搞笑,alternative='greater',var.equal=FALSE, conf.level=0.90)

