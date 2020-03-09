# Course: CS 513B 
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #2

# Clear 
rm(list=ls())

# Load the “breast-cancer-wisconsin.data.csv” from canvas into R
data <- read.csv("breast-cancer-wisconsin.data.csv", header=TRUE, na.strings="?")

# I. Summarizing each column (e.g. min, max, mean )
summarization <- summary(data)
print(summarization)

# II.	Identifying missing values
which(is.na(data))
sum(is.na(data))

# III. Replacing the missing values with the “mean” of the column.
for (i in 1:ncol(data)) {
  data[is.na(data[,i]), i] <- mean(data[,i], na.rm=TRUE)
}

# Checking that the missing values were replaced
sum(is.na(data))

# IV.	Displaying the frequency table of “Class” vs. F6
class_f6 <- table(data$Class, data$F6)
print(class_f6)

# V.	Displaying the scatter plot of F1 to F6, one pair at a time
pairs(data[2:7])

# VI.	Show histogram box plot for columns F7 to F9
boxplot(data[8:10])

# Delete all the objects from your R- environment 
rm(list=ls())

# Reload the “breast-cancer-wisconsin.data.csv” from canvas into R
data <- read.csv("breast-cancer-wisconsin.data.csv", header=TRUE, na.strings="?")

# Remove any row with a missing value in any of the columns.
nrow(data)
data <- na.omit(data)

#Checking that the rows were removed
nrow(data)
