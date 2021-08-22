
## Moment

Quantitative measure related to the shape of the graph of a distribution(or a function).
If the function represents mass then the first moment is the center of the mass, the second moment is the rotational inertia.
If it is probability distribution, then the first moment is the expected value, the second central moment is variance, the third standardized moment is the skewness, the fourth standardized moment is the kurtosis.

## Expected value

It is the generalization of the weighted average, and is intuitively the arithmetic mean for a large number of independent realizations of X. This is termed as the expectation, mean, average or first statistical moment.

## Variance

It is the expected value of the squared deviation from the mean of X.
i.e. Var(x) = E[(x - mean(x))^2] = sum((x - mean(x))^2) / n
This can also be written as :
Var(x) = sum(sum((xi - xj)^2) / n^2
Which means that is the squared deviations of all points from each other.

This is different for every kind of distribution. The following link gives a degree of verbosity to it.

[Variance](https://en.wikipedia.org/wiki/Variance)

The usual one we study are the formulae for normal distributions

## Skewness

It is the measure of asymmetry of the probability distribution. It can be positive, negative, zero or undefined.
A negative skew means the tail is more towards the left of the distribution, or the peak is shifted towards the positive x axis.
A positive skew is vice versa.

Make use of Pearson's Moment Coefficient of Skewness.

## Kurtosis

It is a measure of the shape of the tailedness,

## Mean

The average over a set of values over a random variable x.

## Median

The value occurring at the center of a sorted set of data describing the random variable x.

## Mode

The value that appears the most in the set of data describing the random variable x.


## Standard deviation

A measure of the degree of spread around the mean of a dataset. This is useful for explaining the quality of the spread of a dataset.

sigma(x) = sqrt( (sum(xi - mean(x))^2 ) / N )

This like covariance is dependent on an 'expectation', for which we most often make use of mean to make it reasonably easy to explain, but it just as easily could be anything else.

## Co-Variance

Square of the deviation.
