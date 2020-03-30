#########################################################
##  Purpose: Create CART classification tree
##  Developer: KD         
##
#########################################################

#########################################################
##  Step 0: Clear the environment
##           
##
#########################################################
rm(list=ls())


#########################################################
##  Step 1: Load the relavent packages
##           
##
#########################################################

 
file<-file.choose()
bc <-  read.csv(file,
                   na.strings = "?",
                   colClasses=c("Sample"="character",
                                "F1"="factor","F2"="factor","F3"="factor",
                                "F4"="factor","F5"="factor","F6"="factor",
                                "F7"="factor","F8"="factor","F9"="factor",
                                "Class"="factor"))







#install.packages("rpart")
#install.packages("rpart.plot")     # Enhanced tree plots
#install.packages("rattle")         # Fancy tree plot
#install.packages("RColorBrewer")   # colors needed for rattle
library(rpart)
library(rpart.plot)  			# Enhanced tree plots
library(rattle)           # Fancy tree plot
library(RColorBrewer)     # colors needed for rattle

#dsn2<-data.frame(lapply(dsn[,-1],as.factor))
index<-sort(sample(nrow(bc),round(.30*nrow(bc ))))
training<-bc[-index,]
test<-bc[index,]

?rpart()
#Grow the tree 


CART_class<-rpart( Class~.,data=training[,-1])
rpart.plot(CART_class)
CART_predict2<-predict(CART_class,test, type="class")
df<-as.data.frame(cbind(test,CART_predict2))
table(Actual=test[,"Class"],CART=CART_predict2)

CART_wrong<-sum(test[,"Class"]!=CART_predict2)

error_rate=CART_wrong/length(test$Class)

dev.off()






