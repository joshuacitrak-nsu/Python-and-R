# To run test individually the following commands in the console:
# library(testthat)
# test_file("test_mt_cars.R")

library(testthat)
testthat::local_edition(3)
library(data.table)


# Load the mtcars data set
data("mtcars")
dt_mt_cars <- as.data.table(mtcars)[am == 1 & cyl == 6]

# Write a test to ensure that the data table has the correct number of rows
test_that("mt_cars data table has correct number of rows", {
    expect_equal(nrow(dt_mt_cars), 3)
})

# Write a test to ensure that the data table has the correct columns
test_that("mt_cars data table has correct columns", {
    expected_cols <- c("mpg", "cyl", "disp", "hp", "drat", "wt", 
                       "qsec", "vs", "am", "gear", "carb")
    expect_equal(colnames(dt_mt_cars), expected_cols)
})

# Write a test to ensure that the data table is filtered correctly
test_that("mt_cars data table is filtered correctly", {
    expected_mpg <- c(21.0, 21.0, 19.7)
    expected_cyl <- c(6, 6, 6)
    expected_hp <- c(110, 110, 175)
    expected_wt <- c(2.620, 2.875, 2.770)
    
    expect_equal(dt_mt_cars[, .(mpg, cyl, hp, wt)], 
                 data.table(mpg = expected_mpg, 
                            cyl = expected_cyl, 
                            hp = expected_hp, 
                            wt = expected_wt))
})

