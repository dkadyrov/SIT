# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Final Exam Problem 3

rm(list=ls())
file<-file.choose()

admission_raw <- read.csv(file)
summary(admission_raw) 
summary(admission_raw$ADMIT)
table(admission_raw$ADMIT)
