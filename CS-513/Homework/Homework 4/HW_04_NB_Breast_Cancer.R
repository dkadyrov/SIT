#  First Name       : Khasha
#  Last Name        : Dehnad   
#  Purpose          : Apply naive bayes to the breast cancer data 
#                   :  
#  Creation date    : 

rm(list=ls())
file<-file.choose()
bc_raw<-  read.csv(file,
           na.strings = "?",
           colClasses=c("Sample"="character",
                        "F1"="factor","F2"="factor","F3"="factor",
                        "F4"="factor","F5"="factor","F6"="factor",
                        "F7"="factor","F8"="factor","F9"="factor",
                        "Class"="factor"))


#bc_raw<-
#  read.csv("C://AIMS/Stevens_/2019_S_CS513/Raw_data/breast-cancer-wisconsin.data.csv",
#           na.strings = "?",
#           colClasses=c("Sample"="character",
#                        "F1"="factor","F2"="factor","F3"="factor",
#                        "F4"="factor","F5"="factor","F6"="factor",
#                        "F7"="factor","F8"="factor","F9"="factor",
#                        "Class"="factor"))



is.factor(bc_raw$F1)
bc<-na.omit(bc_raw)

idx<-sort(sample(nrow(bc),as.integer(.70*nrow(bc))))

training<-bc[idx,]

test<-bc[-idx,]

#install.packages('e1071', dependencies = TRUE)

library(e1071)


nBayes <- naiveBayes(factor(Class)~., data =training[,-1])

## Naive Bayes classification using all variables 

category_all<-predict(nBayes,test[,-1]  )


table(NBayes=category_all,Survived=test$Class)
NB_wrong<-sum(category_all!=test$Class )
NB_error_rate<-NB_wrong/length(category_all)
NB_error_rate
