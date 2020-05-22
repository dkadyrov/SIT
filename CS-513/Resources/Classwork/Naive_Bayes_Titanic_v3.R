#  First Name       : Khasha
#  Last Name        : Dehnad   
#  Purpose          : Apply naive bayes to Titanic_row dataset 
#                   : see cr8_multi_rows_dsn program.
#  Creation date    : 

rm(list=ls())

#install.packages('e1071', dependencies = TRUE)
 

library(e1071)
#library(class) 
## main functions used in this program
?read.csv()
?naiveBayes()
?tabulate();  tabulate(c(2,3,3,5), nbins = 10);
?table()
?ftable()
?as.character()

# read in the Titanic dataset 

csvfile<-file.choose()
Titanic_rows<-  read.csv(csvfile)

View(Titanic_rows)
class(Titanic_rows)
?prop.table
prop.table



table(class=Titanic_rows$Class,Survival=Titanic_rows$Survived)
prop.table(table(Class=Titanic_rows$Class,Survived=Titanic_rows$Survived)) 


## Naive Bayes classification using only one variable 
nBayes_class <- naiveBayes(Survived ~Class, data =Titanic_rows)
category_class<-predict(nBayes_class,Titanic_rows  )


ftable(class=Titanic_rows$Class,Age=Titanic_rows$Age,Sex=Titanic_rows$Sex,
       Survival=Titanic_rows$Survived,row.vars = 1:3)
prop.table(
  ftable(class=Titanic_rows$Class,Age=Titanic_rows$Age,Sex=Titanic_rows$Sex,
         Survival=Titanic_rows$Survived,row.vars = 1:3)
      )



 

## Compare the prediction to actual
data_class<-cbind(Titanic_rows,category_class)
table(Class=Titanic_rows$Class,Survived=Titanic_rows$Survived)
table(Class=Titanic_rows$Class,NBayes=category_class)
table(NBayes=category_class,Survived=Titanic_rows$Survived)
?prop.table
prop.table(table(Class=Titanic_rows$Class,Survived=Titanic_rows$Survived))
## Naive Bayes classification using two variables 
nBayes_class_age <- naiveBayes(Survived ~Class+Age, data =Titanic_rows)
category_class_age<-predict(nBayes_class_age,Titanic_rows  )


## Compare the prediction to actual for two variables
table(Class=Titanic_rows$Class,Survived=Titanic_rows$Survived)
ftable(Class=Titanic_rows$Class,Titanic_rows$Age,Survived=Titanic_rows$Survived,NBayes=category_class_age,row.vars = 1:3)
ftable(Class=Titanic_rows$Class,Titanic_rows$Age,Survived=Titanic_rows$Survived,NBayes=category_class_age)
ftable(Class=Titanic_rows$Class,Age=Titanic_rows$Age,Survived=Titanic_rows$Survived)



nBayes_all <- naiveBayes(Survived ~., data =Titanic_rows)

## Naive Bayes classification using all variables 

category_all<-predict(nBayes_all,Titanic_rows  )
 

table(NBayes_all=category_all,Survived=Titanic_rows$Survived)

NB_wrong<-sum(category_all!=Titanic_rows$Survived)

NB_error_rate<-NB_wrong/length(category_all)










