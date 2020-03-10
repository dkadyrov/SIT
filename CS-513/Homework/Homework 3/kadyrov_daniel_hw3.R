# Course: CS 513B 
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #3 KNN

rm(list=ls())

# Import KKNN
library(kknn)

# Import Data
data <- read.csv("breast-cancer-wisconsin.data.csv", header=TRUE, na.strings="?")

# Remove Missing Rows
data <- na.omit(data)

# Seperate Data into Training / Test
index <- sort(sample(nrow(data), as.integer(0.70*nrow(data))))
training <- data[index,]
test <- data[-index,]

# Perform KNN k=3
predict_k3 <- kknn(formula=Class~., training[2:11], test[2:10], k=3, kernel ="rectangular")
fit_k3 <- fitted(predict_k3)
table(Actual=test$Class, Fitted=fit_k3)

# Perform KNN k=5
predict_k5 <- kknn(formula=Class~., training[2:11], test[2:10], k=5, kernel ="rectangular")
fit_k5 <- fitted(predict_k5)
table(Actual=test$Class, Fitted=fit_k5)

# Perform KNN k=10
predict_k10 <- kknn(formula=Class~., training[2:11], test[2:10], k=10, kernel ="rectangular")
fit_k10 <- fitted(predict_k10)
table(Actual=test$Class, Fitted=fit_k10)
