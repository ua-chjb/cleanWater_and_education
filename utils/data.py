import pandas as pd
import plotly.express as px
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor


we = pd.read_csv(
    "C:/Users/benno/OneDrive/Data/cleanWater_education/final/water_education_fs_final.csv"
)
we = we.rename(
    columns={
        "Gross_Tertiary_Education_Enrollment": "college_enrollment",
        "sch_water_none_pct": "lower_school_water__none",
        "sch_water_limited_pct": "lower_school_water__limited",
        "sch_water_none_pct_0": "lower_school_water__none_0%",
        "sch_water_limited_pct_0": "lower_school_water__limited_0%",
    }
)

collst_fe = [
    "college_enrollment",
    "lower_school_water__none",
    "lower_school_water__limited",
    "lower_school_water__none_0%",
    "lower_school_water__limited_0%",
]

summ = pd.read_csv(
    "C:/Users/benno/OneDrive/Data/cleanWater_education/final/summ_table.csv"
)

formula = """
    college_enrollment ~ 
        lower_school_water__none + 
        lower_school_water__limited + 
        Q('lower_school_water__none_0%') + 
        Q('lower_school_water__limited_0%')
"""
sm_model = smf.ols(formula, data=we).fit(cov_type="HC3")
summary = sm_model.summary()
sm_Y_preds = sm_model.fittedvalues
sm_resids = sm_model.resid
predictions = sm_model.get_prediction(we)
sm_sf_preds = predictions.summary_frame(alpha=0.05)

x = sm_model.model.exog
x_cols = sm_model.model.exog_names

vif_df = pd.DataFrame(
    {
        "feature": x_cols,
        "VIF": [variance_inflation_factor(x, j) for j in range(x.shape[1])],
    }
).sort_values(by="VIF", ascending=False)
