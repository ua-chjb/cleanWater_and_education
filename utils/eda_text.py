eda_text_dct = {
    0: "Explore the data visually in one, two, or three dimensions.",
    1: "In two and three dimensions, the model fit is a natural cubic spline with the natural spline constraint included (linear at the boundaries). Due to the small sample size, the spline model is at risk of overfitting the data; however, higher order polynomial functions generally did not perform well in EDA (degrees1-5 were iterated over, inclusive), and a smoothing spline captures the uptick in the floor effect quite well. While multi linear regression was used as the final model for generalizability, splines provide a nice peek into the nuance of the relationship of this specific sample. Lambda and K knots were set automatically through cross validation with pyGAM.",
}
