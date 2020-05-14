# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Final Exam Problem 3

rm(list=ls())
file<-file.choose()
bc <- read.csv(file,
                na.strings = "?",
                colClasses=c("Applicant"="character",
                             "ADMIT"="factor","RANK"="factor","GPA"="factor",
                             "GRE"="factor"))
#install.packages("C50")
library('C50')

#dsn2<-data.frame(lapply(dsn[,-1],as.factor))
index<-sort(sample(nrow( bc),round(.30*nrow(bc ))))
training<-bc[-index,]
test<-bc[index,]

C50_class <- C5.0( ADMIT~.,data=training[,-1] )

summary(C50_class )
plot(C50_class)
C50_predict<-predict( C50_class, test, type="class" )
table(actual=test[,"ADMIT"], C50=C50_predict)
wrong<- (test[,"ADMIT"]!= C50_predict)
c50_rate<-sum(wrong)/length(test[,"ADMIT"])
c50_rate
