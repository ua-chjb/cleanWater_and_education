assumptions_summ_text = """
While OLS is robust to deviations from its assumptions, it is still important to note whether these assumptions were met, so we know how much we can rely on our model’s output. The five generally tested assumptions of OLS are linearity, independence of observations, homoscedasticity, normality of residuals, and no perfect multicollinearity.
"""

assumptions_text_dct = {
    "Linearity": "To test linearity, the linear rainbow test was used. The statistic for the test was 1.0432, and the p-value was 0.4503; this is much larger than the alpha of 0.05, and so we fail to reject the null and linearity holds.",
    "Independence of observations": "The data from each country are considered to be independent of each other.",
    "Homoskedasticity": "The Het Breusch-Pagan test checks whether the variance of residuals in the model is constant, or if it changes with different X variables. Here we use the fstat due to small sample size. The test statistic is 3.3520, and the p-value is 0.0137; this is below the alpha of 0.05, and therefore tells as that heteroskedasticity is present.",
    "Normality of residuals": "To test for normality of residuals, the Shapiro-Wilk Test was used, as the sample size is quite small. The test statistic is 0.9701, and the p-value is 0.0473: very close to the alpha of 0.05, but unfortunately below it. We reject the null that the residuals are normally distributed.",
    "No perfect multicollinearity": "To test for multicollinearity the Variance Inflation Factor method was used. In the original, uncleaned dataset with 11 predictors, some VIFs were extremely large (hundreds of thousands). In the final dataset, all VIF values were under 3.5.",
}

assumptions_pf_dct = {
    "Linearity": "Passed",
    "Independence of observations": "Passed",
    "Homoskedasticity": "Failed",
    "Normality of residuals": "Failed",
    "No perfect multicollinearity": "Passed",
}
