
#  First Name      : Khasha
#  Last Name       : Dehnad
#  Id              : 12345
#  purpose         : Accessing extrenal data and replacing missing value  
#                  : accessing data and perofrming EDA

remove(list=ls())
dev.off()
## Step 1 load the data
## changing ? to NA
#3.2 Load the "breast-cancer-wisconsin.data.csv"
# from CANVAS

# bc<- read.csv("C://AIMS/Stevens_/2018_DataMining/Raw_Data/breast-cancer-wisconsin.data.csv",
 #          na.strings = "?")
 file<-file.choose()
 bc<- read.csv(file, na.strings = "?", colClasses=c("Class"="factor" ))
 is.factor(bc$Class)
#a.	Remove the rows with missing values
 bc_clean<-na.omit(bc)

#b. and c.	create training and test data sets 
 index<-sort(sample(nrow( bc_clean),round(.30*nrow(bc_clean ))))
 training<- bc_clean[-index,]
 test<- bc_clean[index,]

#d.	Use knn with k=1 and classify the test dataset
 #install.packages("kknn")
 #Use the R library("kknn") 
 
 library(kknn) 
 predict_k1 <- kknn(formula= Class~., training[,c(-1)] , test[,c(-1)], k=1,kernel ="rectangular"  )
 
 fit <- fitted(predict_k1)
 table(test$Class,fit)
 
  
  
#e.	Measure the performance of knn
  
  wrong<- ( test$Class!=fit)
  rate<-sum(wrong)/length(wrong)
  rate
  
#f.	Repeat the above steps with k=2, k=5, k=10.
for(i in c(1,2,5,10,15,20)){
  predict <- kknn(formula= Class~., training[,c(-1)] , test[,c(-1)], k=i,kernel ="rectangular"  )
  
  fit <- fitted(predict)

  #e.	Measure the performance of knn
  
  wrong<- ( test$Class!=fit)
  rate<-sum(wrong)/length(wrong)
  rate
  print('***************')
  print(i)
  print( table(test$Class,fit))
  print( rate)
  print('***************') 
}
   
   
 
