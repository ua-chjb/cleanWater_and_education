methodology_text_dct = {
    "Informal hypothesis": {
        0: "Informally, this analysis investigated the relationship between clean water levels and education rates, by country.",
        1: "Specifically, water availability in lower schools was determined to be the best predictor, in terms of both absence of null values and in variance explained. The outcome variable landed on was college enrollment. So, the final informal hypothesis question was: does the prevalence of clean water in lower schools impact the percentage of people who end up attending college?",
    },
    "Data identification": {
        0: "The data was gathered from two sources: clean water data was extracted through the WHO/UNICEF Joint Monitoring Programme for Water Supply, Sanitation, and Hygiene (JMP); and education data was found on a Kaggle repository. This data was grouped at the country level."
    },
    "Data extraction": {
        0: "While the education data was stored in a simple CSV, the water data was stored in a series of complex excel documents. Claude was used to create ETL functions that read from the spreadsheets and extracted the information identified in prompting. 11 predictor features were finally extracted from the JMP source, including water availability in education systems and in the household."
    },
    "Data cleaning": {
        0: "Several challenges existed from a data cleaning perspective. ",
        1: "Firstly, the JMP data contained a large proportion of null values, and as there could be high variance between different countries, imputation did not seem appropriate, as it could potentially skew the model. ",
        2: "Secondly, JMP data was listed for years 2000-2024, with various countries having various dates filled in. A filtering function was used to take the latest data, if such data existed, from 2020-2024; the number of final countries was reduced from 191 to 84.",
    },
    "Final dataset": {
        0: "Based on this outcome feature of “college enrollment”, several combinations of the 11 predictors were attempted; due to the existence of multicollinearity, nine features were dropped, and “percentage no water supply in school” and “percentage limited water supply in school” were kept – one feature that captured variance around poor water supply, and one feature that captured variance around better water supply. ",
        1: "Additionally, a ceiling effect existed around countries that had “0%” for either feature, or for both features. Two binary variables were created to help the model identify this information. Finally, four predictors existed, encompassing “no” and “limited” water supply for both continuous and floor effect patterns. The Variance Inflation Factor for all four features was under 3.5.",
    },
    "Inference": {
        0: "While both sklearn and statsmodels were used in Exploratory Data Analysis, the main goal of this analysis was inference, so statsmodels OLS was selected as the final model. Due to the limited number of entries and the presence of heteroskedasticity, the standard error function was updated to the “HC3” type. ",
        1: "The final model clocked an r2 value of 0.231, meaning the model does not explain very much variance, and has little predictive power. However, two of the predictors were statistically significant: “no water, continuous” and “limited water, boolean”. Because “none” and “limited” each have two features, it is expected that only one from each pair would have statistical significance. ",
        2: "Interestingly, though, it was the continuous “none” feature that proved useful to the model, and the binary “limited” feature. This implies that it is not limited access to water that affects education rates, but rather the complete absence of it. ",
        3: "Final model coefficients and details can be found in the “model” section from the dropdown menu.",
    },
}
