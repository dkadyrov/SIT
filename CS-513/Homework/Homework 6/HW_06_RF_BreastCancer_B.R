#  Course          :  
#  First Name      : Khasha
#  Last Name       : Dehnad
#  Id              : 12345
#  purpose         : HW 7 Random Forest 

## Step 0 clean up!!!


 

rm(list=ls())
file<-file.choose()


 
#bc_raw<-  read.csv(file,
#                   na.strings = "?",
#                   colClasses=c("Sample"="character",
#                                "F1"="factor","F2"="factor","F3"="factor",
#                                "F4"="factor","F5"="factor","F6"="factor",
#                                "F7"="factor","F8"="factor","F9"="factor",
#                                "Class"="factor"))
bc_raw<-  read.csv(file,
                   na.strings = "?",
                   colClasses=c("Sample"="character",
                                "F1"="factor","F2"="factor","F3"="factor",
                                "F4"="factor","F5"="factor","F6"="character",
                                "F7"="factor","F8"="factor","F9"="factor",
                                "Class"="factor"))
summary(bc_raw$F6)

bc_raw[is.na(bc_raw$F6),"F6"]<- "M" 

bc<-data.frame(bc_raw[,1:6],F6=as.factor(bc_raw$F6),bc_raw[,8:11]) 

 

index<-sort(sample(nrow(bc),round(.30*nrow(bc))))
training<-bc [-index,]
test<-bc[index,]


#install.packages('randomForest')

library(randomForest)

fit <- randomForest( Class~., data=training[,-1], importance=TRUE, ntree=1000)
importance(fit)
varImpPlot(fit)
dev.off()
Prediction <- predict(fit, test[,-1])
table(actual=test$Class,Prediction)

wrong<- (test$Class!=Prediction )
error_rate<-sum(wrong)/length(wrong)
error_rate


