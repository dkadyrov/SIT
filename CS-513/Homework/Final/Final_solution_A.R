#  Course          :  
#  First Name      : Khasha
#  Last Name       : Dehnad
#  Id              : 12345
#  purpose         : HW 7 Random Forest 

## Step 0 clean up!!!

#	Use the kmeans clustering method to create two clusters
#for the Admission dataset using gre and gpa as clustering variables. 
#Tabulate the clustered rows against the "ADMIT" column.
#	Use the hierarchical clustering method to create two clusters
#for the Admission dataset using gre and gpa as clustering variables.
#Tabulate the clustered rows against the "ADMIT" column.


rm(list=ls())
file<-file.choose()

admission<-  read.csv(file)
summary(admission) 




mmnorm2 <-function(x)
{z<-((x-min(x))/(max(x)-min(x)))
return(z)                              
}

myvector<-1:20
mmnorm2(myvector)



admission_norm<- data.frame(Applicant=as.character(admission$Applicant )
                ,    ADMIT= admission$ADMIT    
                ,    GRE=mmnorm2(admission$GRE)
                ,    GPA=mmnorm2(admission$GPA)
                ,    RANK=admission$RANK  
                      ) 


admission_dist <-dist( admission_norm[,c(-1,-2,-5)])
hclust_resutls<-hclust(admission_dist )
plot(hclust_resutls)
hclust_2<-cutree(hclust_resutls,2)
table(Cluster=hclust_2,Actual= admission_norm[,2])

dev.off()

kmeans_2<- kmeans(admission_norm[,c(-1,-2,-5)],2,nstart = 10)
kmeans_2$cluster
table(kmeans_2$cluster,Actual= admission_norm[,2] )

#Problem 2 - (20 points)
#Use the Random Forest methodology to develop a classification model
#for the Admission_cat dataset using gre, gpa and the rank variables as predictors.
#Use 30% of the records to create the test dataset and score the test dataset. 
#What is the accuracy of your model?







rm(list=ls())
file<-file.choose()





Admission<-  read.csv(file,
                   na.strings = "?",
                   colClasses=c("Applicant"="character",
                    "ADMIT"="factor","RANK"="factor","GRE"="factor"))

summary(Admission)





index<-sort(sample(nrow(Admission),round(.30*nrow(Admission))))
training<- Admission[-index,]
test<-Admission[index,]


#install.packages('randomForest')

library(randomForest)

fit <- randomForest( ADMIT~., data=training[,-1], importance=TRUE, ntree=500)
importance(fit)
varImpPlot(fit)
dev.off()
Prediction <- predict(fit, test[,-1])
table(actual=test$ADMIT ,Prediction)

wrong<- (test$ADMIT !=Prediction )
error_rate<-sum(wrong)/length(wrong)
error_rate
#Problem 3 - (20 points)
#Use the c5.0 methodology to develop a classification model
#for the Admission_cat dataset using the gre,
#the gpa and the rank variables as predictors. 
#Use 30% of the records to create the test dataset and score
#the test dataset. What is the accuracy of your model?



library('C50')
C50_class <- C5.0( ADMIT~.,data=training[,-1] )

summary(C50_class )
dev.off()
plot(C50_class)
C50_predict<-predict( C50_class ,test , type="class" )
table(actual=test[,"ADMIT"],C50=C50_predict)
wrong<- (test[,"ADMIT"]!=C50_predict)
c50_rate<-sum(wrong)/length(test[,"ADMIT"])
c50_rate

C50_predict_prob<-predict( C50_class ,test , type="prob" )



