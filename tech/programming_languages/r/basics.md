# Types

1. class(var/val)
2. is.numeric(var/val)

Boolean can be written as True or False, but also as T or F. NA is also logical.

numerics
integer
double
complex
raw
character

## Coercion

as.numeric(TRUE) yields 1
as.numeric("4.5")


## Categorical Variables

'factor' is a datatype for saving categorical data.

blood <- c("B", "AB", "O", "O")
blood_factor <- factor(blood)

It is possible to add custom levels in factor.

Ex : blood_factor2 <- factor(blood , levels = c("A", "B", "AB", "O"))

'labels' can be used for transformation.

Ex : blood_factor3 <- factor(blood , levels = c("A", "B", "AB", "O"), labels=("BT_A", "BT_B", "BT_AB", "BT_O"))

## Nominal and Ordinal

Ordinal are list that can be ordered. Nominal are collections that cannot be ordered.

## Dates and Times

Date class represents date.
Time is represented by POSIXct and POSIXlt

unclass() shows the number of days from 1970-01-01(Y-m-d)
use as.Date() for gettinga date.
You can mention format using the 'format' parameter in as.Date


It is possible to give names to a collection(c) using the 'names()' function with collection.

Everything is a vector in R.

i.e. x <- 'hello'
length(x) gives 1
is.vector(x) gives 'True'.

R auto-coerces to the most frequent used type in the collection/vector.

Vector Calculation extends to every element naturally.

i.e. x <- c(5, 10, 15)
x * 3 yields 15, 30, 45

we have sum() function as well.

This priamrily does matrix calculations. Hence the term vectors.

Python slicing is called subset in R., except it recycles to fit the outputs.

R can make multivariate calculations easier.


## Matrices

matrix(1:6, nrow=2)
matrix(1:6, ncol=3) # fills in a column-by-column fashion
matrix(1:6, nrow=2, byrow=TRUE) # row-by-row fashion

recycling happens here as well.

cbind & rbind

cbind takes 2 vectors and attaches them in a column fashion
rbind does the same in a row fashion.

rownames & colnames, or use dimnames attribute in matrix

coercion is applicable here as well.

colSums and rowSums

## Order of importance of datatypes

Characters > Numeric > Logical
