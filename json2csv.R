library("RJSONIO")
library(data.table)
library(Amelia)
setwd("~/Documents/dev/coursolve")
cd <- fromJSON("collaboration_data.improved.txt")

to_csv <- function(data) {
    data <- lapply(data, function(x) {
        x[sapply(x, is.null)] <- NA
        unlist(x)
    })
    csv_data <- do.call("rbind", data)
    data <- data.frame(csv_data)
    data
}

convert.magic <- function(obj, types){
    out <- lapply(1:length(obj),
                  FUN = function(i) {
                      as.numeric.factor <- function(x) {as.numeric(levels(x))[x]}
                      FUN1 <- switch(types[i], character = as.character, numeric = as.numeric.factor, factor = as.factor)
                      FUN1(obj[, i])
                  })
    names(out) <- colnames(obj)
    as.data.table(out)
}

data_raw <- to_csv(cd)
types = c('factor', 'numeric', 'factor', 'numeric', 'numeric', 'factor', 'numeric', 'numeric', 'numeric', 'numeric', 'numeric', 'numeric', 'numeric', 'numeric', 'factor', 'numeric', 'numeric', 'numeric', 'numeric', 'numeric', 'factor', 'character')
data <- convert.magic(data_raw, types)
data[1:3,]
summary(data)

qplot(data$Highest.Education) + theme(axis.text.x = element_text(angle = 45, hjust = 1)) + ylab("Cumulative count") + xlab("Highest Education")
qplot(data$Year.of.Birth, data$Highest.Education)
qplot(data$Location) + theme(axis.text.x = element_text(angle = 90, hjust = 1)) + ylab("Cumulative count") + xlab("Location")
