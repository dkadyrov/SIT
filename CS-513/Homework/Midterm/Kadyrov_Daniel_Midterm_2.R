
#  First Name      : Daniel
#  Last Name       : Kadyrov
#  Id              : 10455680
#  purpose         : Midterm - Problem 2

# Reset Environment
remove(list=ls())

# Read the Data 
corona <- read.csv("COVID19_v3.csv")

# I. Summarize 
summary(corona) 

# II. Identify Missing Values
is.na(corona)
missing <- corona[is.na(corona),]

# III. Displaying the frequency table of "Infected" vs. "MaritalStatus"
table(Infected=corona$Infected, MaritalStatus=corona$MaritalStatus)

# IV. Displaying the scatter plot of "Age", "MaritalStatus" and "MonthAtHospital", one pair at a time
pairs(~Age + MaritalStatus + MonthAtHospital, data=corona)

# V. Show box plots for columns:  “Age”, “MaritalStatus” and “MonthAtHospital”
boxplot(corona$Age, corona$MaritalStatus, corona$MonthAtHospital)

# VI.	Replacing the missing values of “Cases” with the “mean” of “Cases”.
for (i in 1:ncol(data)) {
  corona[is.na(corona$Cases[,i]), i] <- mean(corona$Cases[,i], na.rm=TRUE)
}

