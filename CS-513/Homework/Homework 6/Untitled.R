#  First Name      : Daniel
#  Last Name       : Kadyrov
#  Id              : 10455680
#  purpose         : Homwork 6

# Reset Environment
remove(list=ls())
rm(list=ls())

filename<-file.choose()
dsn<-  read.csv(filename ) 
dev.off

### remove all the records with missing value

#?na.omit()
#dsn2<-na.omit(dsn)
set.seed(123)
#?ifelse


index<-sort(sample(nrow(dsn),round(.25*nrow(dsn))))
training<-dsn[-index,]
test<-dsn[index,]


#install.packages("C50", repos="http://R-Forge.R-project.org")
#install.packages("C50")
library('C50')
View(dsn)
?C5.0
# C50  classification 
library('C50')
C50_class <- C5.0( Class~.,data=as.factor(training) )

summary(C50_class )
dev.off()
plot(C50_class)
C50_predict<-predict( C50_class ,test , type="class" )
table(actual=test[,4],C50=C50_predict)
wrong<- (test[,4]!=C50_predict)
c50_rate<-sum(wrong)/length(test[,4])
c50_rate



