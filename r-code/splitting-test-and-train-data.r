library(readr,png)

y.images <- readr::read_csv(file='~/Desktop/data/y.csv')
y.images$X1 <- NULL
# head(y.images) # glimpse at the data

x.images <- list() # nrow(y.images)
for(i in 1:(nrow(y.images)-1)) {
  x.filename <- paste0('~/Desktop/breast-cancer-img/', i, '.png')
  x.images[[i]] <- png::readPNG(x.filename)
}
# dim(x.images[[1]]) # checking the dimension, should be 50x50x3 (50x50 = pixel; 3 = RGB)
# head(x.images) # glimpse at the data

# setting seed
set.seed(123)

# splitting into train and test for machine learning
index.train <- sample(1:length(x.images), round(length(x.images) * 0.8))
x.train <- x.images[index.train]
x.test <- x.images[-index.train]
y.train <- y.images[index.train,]
y.test <- y.images[-index.train,]

saveRDS(x.train, "~/Desktop/data/x_train.rds")
saveRDS(x.test, "~/Desktop/data/x_test.rds")
saveRDS(y.train, "~/Desktop/data/y_train.rds")
saveRDS(y.test, "~/Desktop/data/y_test.rds")
