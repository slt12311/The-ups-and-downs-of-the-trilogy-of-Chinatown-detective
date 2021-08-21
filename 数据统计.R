dd1 <- read.csv("D:/py/Spider/Çé¸Ğ·ÖÎö±í.csv", header = T)
dd2 <- read.csv("D:/py/Spider/tt2.csv", header = T)
dd3 <- read.csv("D:/py/Spider/tt3.csv", header = T)

wilcox.test(dd1$ÆÀ·Ö,dd2$ÆÀ·Ö,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd2$ÆÀ·Ö,dd3$ÆÀ·Ö,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd1$ÆÀ·Ö,dd3$ÆÀ·Ö,alternative='greater',var.equal=FALSE, conf.level=0.90)

#½ö¶¹°ê
dd1 <- read.csv("D:/py/Spider/t1.csv", header = T)
dd2 <- read.csv("D:/py/Spider/t2.csv", header = T)
dd3 <- read.csv("D:/py/Spider/t3.csv", header = T)

wilcox.test(dd1$ÆÀ·Ö,dd2$ÆÀ·Ö,alternative='greater',var.equal=FALSE, conf.level=0.90)


#·Ö¾äÇé¸Ğ·ÖÊı
dd1 <- read.csv("D:/py/Spider/qt1.csv", header = T)
dd2 <- read.csv("D:/py/Spider/qt2.csv", header = T)
dd3 <- read.csv("D:/py/Spider/qt3.csv", header = T)
wilcox.test(dd1$¾çÇé,dd2$¾çÇé,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd1$¾çÇé,dd3$¾çÇé,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd2$¾çÇé,dd3$¾çÇé,alternative='greater',var.equal=FALSE, conf.level=0.90)

wilcox.test(dd1$ÑİÔ±,dd2$ÑİÔ±,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd1$ÑİÔ±,dd3$ÑİÔ±,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd2$ÑİÔ±,dd3$ÑİÔ±,alternative='greater',var.equal=FALSE, conf.level=0.90)

wilcox.test(dd1$¸ãĞ¦,dd2$¸ãĞ¦,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd1$¸ãĞ¦,dd3$¸ãĞ¦,alternative='greater',var.equal=FALSE, conf.level=0.90)
wilcox.test(dd2$¸ãĞ¦,dd3$¸ãĞ¦,alternative='greater',var.equal=FALSE, conf.level=0.90)

