# Central Limit Theorem

In probability theory, the central limit theorem (CLT) states that, under appropriate conditions, the distribution of a normalized version of the sample mean converges to a standard normal distribution. This holds even if the original variables themselves are not normally distributed. There are several versions of the CLT, each applying in the context of different conditions.

Some of the important versions of this are:

| Variant                    | Assumptions                           | Formula Type                                          | Use Case                              |
| -------------------------- | ------------------------------------- | ----------------------------------------------------- | ------------------------------------- |
| Classical / Lindeberg–Lévy | i.i.d., finite variance               | $Z_n \to \mathcal{N}(0,1)$                            | General inference, sample mean        |
| Lyapunov                   | Independent, not identically dist.    | Normalized sum $\to \mathcal{N}(0,1)$                 | Heterogeneous data                    |
| Lindeberg–Feller           | Independent, with Lindeberg condition | General normalized sum                                | Most general CLT                      |
| Multivariate CLT           | i.i.d. vectors                        | $\sqrt{n}(\bar{X} - \mu) \to \mathcal{N}_d(0,\Sigma)$ | Multivariate stats, finance           |
| Functional CLT             | i.i.d., viewed as stochastic process  | $S_n(t) \Rightarrow W(t)$                             | Time series, Brownian motion modeling |
| Dependent Variable CLT     | Weakly dependent vars                 | Sum $\to \mathcal{N}(0,1)$                            | Time series, Markov chains            |

## Classical Central Limit Theorem

If $X_1, X_2, ..., X_n$ are **independent and identically distributed (i.i.d.)** random variables with:

* Mean $\mu$,
* Variance $\sigma^2 < \infty$,

Then the standardized sum:

$$
Z_n = \frac{\sum_{i=1}^n X_i - n\mu}{\sigma \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)
$$

as $n \to \infty$.

## Application 1 - Usage of Standard Deviation(σ)

## CLT says:

> The **sampling distribution of the sample mean** ( $\bar{x}$ ) will be approximately **normal** with:

* Mean: $\mu$ (same as the population mean)
* Standard Deviation (of the sample mean):

  $$
  \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}
  $$

Where:

* $\sigma_{\bar{x}}$ = standard deviation of the sampling distribution (also called **standard error**)
* $\sigma$ = population standard deviation
* $n$ = sample size

## How σ Works with CLT

## 1. **Reduces Variability with Bigger Samples**

As sample size $n$ increases:

$$
\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \quad \text{gets smaller}
$$

This means: **Your sample mean becomes more stable and reliable** as you take larger samples.

## 2. **Allows Confidence Interval Estimation**

In business, we often construct a confidence interval for the mean:

$$
\bar{x} \pm z \cdot \frac{\sigma}{\sqrt{n}}
$$

Where:

* $\bar{x}$ = sample mean
* $z$ = z-score (e.g., 1.96 for 95% confidence)
* $\sigma / \sqrt{n}$ = standard error

You need **σ** to determine how “wide” or “narrow” your estimate is.

## 3. **Enables Hypothesis Testing**

When comparing two groups (A/B testing, quality control, etc.), you calculate:

$$
Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}}
$$

* A smaller σ → more precise Z-scores → clearer decisions.

## Example

Let’s say a factory produces nails with a known population standard deviation $\sigma = 2 \text{ mm}$, and you take a sample of 100 nails.

* Standard error:

  $$
  \sigma_{\bar{x}} = \frac{2}{\sqrt{100}} = 0.2
  $$

So your sampling distribution of the **mean length** will have:

* Mean = population mean (say, 50 mm)
* Std dev = **0.2 mm**, not 2 mm!

Your estimate of the average length from the sample is **much more precise** than any one nail.

## Summary

| Concept                      | Role of σ (sigma)                        |
| ---------------------------- | ---------------------------------------- |
| Sampling distribution        | Determines **spread** of sample means    |
| Standard error               | $\sigma / \sqrt{n}$: lower with bigger n |
| Confidence intervals         | Used to calculate **margin of error**    |
| Hypothesis testing (Z-tests) | Critical in test statistic formula       |

If the **population σ is unknown**, we use the **sample standard deviation $s$** and apply the **t-distribution** — another extension of CLT.
