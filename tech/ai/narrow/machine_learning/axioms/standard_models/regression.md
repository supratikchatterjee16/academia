# Regression

Regression is the method of finding the 'best fit' line through *regressing to the normal* in a distribution of points.

Regression analysis works by using the hypothesis :

*h(x) = mx + b*

Here *m* is calculated using the function :

*m = r(s<sub>y</sub> / s<sub>x</sub>)*

*R* is the correlation between 'x' and 'y'.  
*S<sub>y</sub>* is the SD between the 'Y' values.  
*S<sub>x</sub>* is the SD between the 'X' values.

Now that we know the 'm' or the slope of the line, we find out the y-intercept or
'b' of the line. This is given by the equation :

*b = mean(y) - m * mean(x)*

*mean* is the mean of the distribution on the respective axis.

The above is exempted from the gradient descent problem.

## Cost function

When we have to adjust based on incoming points, in order to adjust the values of 'm' and 'b',
we make use of the concept of a 'Cost Function'. Simply put this is a cost we calculate in order to maximize the expectation outcome, or in other words to create better, more probable predictions.

The cost function, in regression, simply put, is the difference of expected 'y' to actual 'y'
given 'x'. i.e.

Given, *y = mx + b*, the calculated 'y' is the expected 'y'.

The actual 'y' is the observed 'y'.

We evaluate cost using :

cost  = (1 / 2m) * (y<sub>Actual</sub> - y<sub>Calculated</sub>)<sup>2</sup>

The algorithm is then developed to reduce this 'cost'.

Also, read Loss functions.

## Gradient Descent
