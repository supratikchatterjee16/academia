# Modern Portfolio Theory

Modern portfolio theory (MPT), or **mean-variance analysis**, is a mathematical framework for assembling a portfolio of assets such that the expected return is maximized for a given level of risk. It is a formalization and extension of diversification in investing, the idea that owning different kinds of financial assets is less risky than owning only one type. Its key insight is that an asset's risk and return should not be assessed by itself, but by how it contributes to a portfolio's overall risk and return. It uses the variance of asset prices as a proxy for risk.

MPT assumes that investors are risk averse, meaning that given two portfolios that offer the same expected return, investors will prefer the less risky one. Thus, an investor will take on increased risk only if compensated by higher expected returns. Conversely, an investor who wants higher expected returns must accept more risk. The exact trade-off will not be the same for all investors. Different investors will evaluate the trade-off differently based on individual risk aversion characteristics. The implication is that a rational investor will not invest in a portfolio if a second portfolio exists with a more favorable risk-expected return profile—i.e., if for that level of risk an alternative portfolio exists that has better expected returns.

Under the model:

1. Portfolio return is the proportion-weighted combination of the constituent assets' returns.
2. Portfolio return volatility ${\displaystyle \sigma _{p}}\sigma _{p}$ is a function of the correlations ρij of the component assets, for all asset pairs $(i, j)$. The volatility gives insight into the risk which is associated with the investment. The higher the volatility, the higher the risk.

General theory : 

1. Expeced Return
    $$E(R_p) = \sum_{i}w_iE(R_i)$$
    where, $R_p$ is return of the portfolio  
    $R_i$ is the reurn on asset $i$  
    $w_i$ is the weighting component of asset $i$
2. Portfolio Return Variance
    $$ \sigma_p^2 = \sum_{i}w_i^2\sigma_i^2 +  \sum_{i}\sum_{j \neq i}  w_iw_j\sigma_i\sigma_j\rho_{ij} $$
3. Portflio return volatality :
    $$ \sigma_p = \sqrt{\sigma_p^2} $$
