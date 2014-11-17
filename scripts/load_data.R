library(scatterplot3d)

data_2005 = read.csv("data/2005.csv")
data_2006 = read.csv("data/2006.csv")
data_2007 = read.csv("data/2007.csv")
data_2008 = read.csv("data/2008.csv")
data_2009 = read.csv("data/2009.csv")
data_2010 = read.csv("data/2010.csv")
data_2011 = read.csv("data/2011.csv")
data_2012 = read.csv("data/2012.csv")
data_2013 = read.csv("data/2013.csv")
data_2014 = read.csv("data/2014.csv")

sum_2005 <- aggregate(World.Rank ~ Country, data = data_2005, FUN=sum)
sum_2005 <- sum_2005[order(sum_2005$Country),]

sum_2006 <- aggregate(World.Rank ~ Country, data = data_2006, FUN=sum)
sum_2006 <- sum_2006[order(sum_2006$Country),]

sum_2007 <- aggregate(World.Rank ~ Country, data = data_2007, FUN=sum)
sum_2007 <- sum_2007[order(sum_2007$Country),]

sum_2008 <- aggregate(World.Rank ~ Country, data = data_2008, FUN=sum)
sum_2008 <- sum_2008[order(sum_2008$Country),]

sum_2009 <- aggregate(World.Rank ~ Country, data = data_2009, FUN=sum)
sum_2009 <- sum_2009[order(sum_2009$Country),]

sum_2010 <- aggregate(World.Rank ~ Country, data = data_2010, FUN=sum)
sum_2010 <- sum_2010[order(sum_2010$Country),]

sum_2011 <- aggregate(World.Rank ~ Country, data = data_2011, FUN=sum)
sum_2011 <- sum_2011[order(sum_2011$Country),]

sum_2012 <- aggregate(World.Rank ~ Country, data = data_2012, FUN=sum)
sum_2012 <- sum_2012[order(sum_2012$Country),]

sum_2013 <- aggregate(World.Rank ~ Country, data = data_2013, FUN=sum)
sum_2013 <- sum_2013[order(sum_2013$Country),]

sum_2014 <- aggregate(World.Rank ~ Country, data = data_2014, FUN=sum)
sum_2014 <- sum_2014[order(sum_2014$Country),]

allSums <- merge(sum_2005, sum_2006, by="Country")
suppressMessages(allSums <- merge(allSums, sum_2007, by="Country"))
suppressMessages(allSums <- merge(allSums, sum_2008, by="Country"))
suppressMessages(allSums <- merge(allSums, sum_2009, by="Country"))
suppressMessages(allSums <- merge(allSums, sum_2010, by="Country"))
suppressMessages(allSums <- merge(allSums, sum_2011, by="Country"))
suppressMessages(allSums <- merge(allSums, sum_2012, by="Country"))
suppressMessages(allSums <- merge(allSums, sum_2013, by="Country"))
suppressMessages(allSums <- merge(allSums, sum_2014, by="Country"))

col_headings <- c('Country', '2005','2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014')
names(allSums) <- col_headings

write.csv(allSums, file = "data/allSums.csv")

allSumsSorted <- allSums[order(-allSums$'2005'), ]
me <- rowSums( allSums[,2:11] )
small <- data.frame(allSums[1], me)

topFive <- head(small[order(-small$me),], 5)
header <- c('Country', 'Sum')
names(topFive) <- header

#plot(small, las=2, xlab=NA, ylab= NA, sub="First plot!")

usa.sub <- subset(allSums, Country=='USA')
uk.sub <- subset(allSums, Country=='UK')
germany.sub <- subset(allSums, Country=='Germany')
japan.sub <- subset(allSums, Country=='Japan')
canada.sub <- subset(allSums, Country=='Canada')

usa.sub <- usa.sub[,c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014")]
uk.sub <- uk.sub[,c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014")]
germany.sub <- germany.sub[,c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014")]
japan.sub <- japan.sub[,c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014")]
canada.sub <- canada.sub[,c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014")]

usa_bar_plot <- barplot(as.numeric(usa.sub[1,]), horiz=TRUE, names.arg=c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"), col="red")
uk_bar_plot <- barplot(as.numeric(uk.sub[1,]), horiz=TRUE, names.arg=c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"), col="red")
germany_bar_plot <- barplot(as.numeric(germany.sub[1,]), horiz=TRUE, names.arg=c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"), col="red")
japan_bar_plot <- barplot(as.numeric(japan.sub[1,]), horiz=TRUE, names.arg=c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"), col="red")
canada_bar_plot <- barplot(as.numeric(canada.sub[1,]), horiz=TRUE, names.arg=c("2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"), col="red")

scatterplot3d(allSums)