# Course: CS 513B 
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #3 KNN

rm(list=ls())

library(e1071)

# Import Data
data <- read.csv("breast-cancer-wisconsin.data.csv", header=TRUE, na.strings="?")

# Remove Missing Rows
data <- na.omit(data)

# Seperate Data into Training / Test
index <- sort(sample(nrow(data), as.integer(0.70*nrow(data))))
training <- data[index,]
test <- data[-index,]

# Naive Bayes
table(F6=data$F6, Class=data$Class)

nBayes_class = naiveBayes(Class ~Class, data=data)

#nBayes_all <- naiveBayes(Class ~., data=index)
