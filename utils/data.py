import boto3
import io
import pandas as pd
import pickle
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor

from utils.secrets import *

s3 = boto3.client("s3", region_name=REGION)


def read_csv_from_s3(key):
    obj = s3.get_object(Bucket=aws_bucket_name, Key=key)
    return pd.read_csv(io.BytesIO(obj["Body"].read()))


def load_model_from_s3(key):
    model_buffer = io.BytesIO()
    s3.download_fileobj(aws_bucket_name, key, model_buffer)
    model_buffer.seek(0)
    return pickle.load(model_buffer)


we = read_csv_from_s3("water_education_fs_final.csv")
summ = read_csv_from_s3("summ_table.csv")
sm_sf_preds = read_csv_from_s3("sm_sf_preds.csv")
sm_model = load_model_from_s3("sm_model.pkl")

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

tables = summ.tables

sm_Y_preds = sm_model.fittedvalues
sm_resids = sm_model.resid
x = sm_model.model.exog
x_cols = sm_model.model.exog_names

vif_df = pd.DataFrame(
    {
        "feature": x_cols,
        "VIF": [variance_inflation_factor(x, j) for j in range(x.shape[1])],
    }
).sort_values(by="VIF", ascending=False)
