# Course: CS 513B 
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #7 ANN

library(neuralnet)

data <- read.csv("wisc_bc_ContinuousVar.csv", na.strings="?")
data <- data[, -c(1)]

data[, 1] <- as.numeric(data[, 1] == "M")

colnames(data)[2] <- "F2"
colnames(data)[3] <- "F3"
colnames(data)[4] <- "F4"
colnames(data)[5] <- "F5"
colnames(data)[6] <- "F6"
colnames(data)[7] <- "F7"
colnames(data)[8] <- "F8"
colnames(data)[9] <- "F9"
colnames(data)[10] <- "F10"
colnames(data)[11] <- "F11"
colnames(data)[12] <- "F12"
colnames(data)[13] <- "F13"
colnames(data)[14] <- "F14"
colnames(data)[15] <- "F15"
colnames(data)[16] <- "F16"
colnames(data)[17] <- "F17"
colnames(data)[18] <- "F18"
colnames(data)[19] <- "F19"
colnames(data)[20] <- "F20"
colnames(data)[21] <- "F21"
colnames(data)[22] <- "F22"
colnames(data)[23] <- "F23"
colnames(data)[24] <- "F24"
colnames(data)[25] <- "F25"
colnames(data)[26] <- "F26"
colnames(data)[27] <- "F27"
colnames(data)[28] <- "F28"
colnames(data)[29] <- "F29"
colnames(data)[30] <- "F30"
colnames(data)[31] <- "F31"

train.proportion <- 0.7
train.index <- sample(x = 1:nrow(data),
                      size = floor(train.proportion * nrow(data)),
                      replace = F)
train.data <- data[train.index, ]
test.data <- data[-train.index, ]
test.labels <- test.data$diagnosis
test.data <- subset(test.data, select = -c(diagnosis))

formula <- sprintf("%s%s", "diagnosis ~ ", paste("F", 2:31, collapse = " + ", sep = ""))

set.seed(7)

data.net <- neuralnet(formula, data = train.data,
                            hidden = c(5), # 1 hidden layer with 5 nodes
                            linear.output = F, rep = 5,
                            err.fct = "ce", act.fct = "logistic", threshold = 2)

train.score <- sapply(list(data.net),
                      function(x) {min(x$result.matrix[c("error"), ])})
                                    
                                    