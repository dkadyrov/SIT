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
##  Step 0:  Load the data
##           
##
#########################################################
rm(list=ls())
file<-file.choose()
bc <-  read.csv(file,
                na.strings = "?",
                colClasses=c("Sample"="character",
                             "F1"="factor","F2"="factor","F3"="factor",
                             "F4"="factor","F5"="factor","F6"="factor",
                             "F7"="factor","F8"="factor","F9"="factor",
                             "Class"="factor"))

#########################################################
##  Step 1: Load the relavent packages
##           
##
#########################################################


#install.packages("C50")
library('C50')

#dsn2<-data.frame(lapply(dsn[,-1],as.factor))
index<-sort(sample(nrow( bc),round(.30*nrow(bc ))))
training<-bc[-index,]
test<-bc[index,]

 
C50_class <- C5.0( Class~.,data=training[,-1] )

summary(C50_class )
dev.off()
plot(C50_class)
C50_predict<-predict( C50_class ,test , type="class" )
table(actual=test[,"Class"],C50=C50_predict)
wrong<- (test[,"Class"]!=C50_predict)
c50_rate<-sum(wrong)/length(test[,"Class"])
c50_rate



