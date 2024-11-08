# ML Project: California Housing Prediction

## Getting Started

Setting up the project in a docker container is the easiest way to ensure no package versioning conflicts with your environment. I created an image for this project which can be found [here](https://hub.docker.com/r/zedems/web_pricing_app).   

```
1. docker pull zedems/web_pricing_app   
2. docker run -itd -p *port*:8000 --name *container_name* zedems/web_pricing_app 
3. App available at http://localhost:*port*
```

The California Housing dataset provides data on various housing attributes across different districts in California, aiming to predict median house values. It originates from the 1990 U.S. Census and includes details for each block group, which typically represents populations ranging from 600 to 3,000 individuals.

## Data Characteristics

- **Number of Instances**: 20,640
- **Number of Attributes**: 8 (all numeric, predictive) + 1 target variable

### Attribute Information
1. **MedInc**: Median income in block group
2. **HouseAge**: Median house age in block group
3. **AveRooms**: Average number of rooms per household
4. **AveBedrms**: Average number of bedrooms per household
5. **Population**: Block group population
6. **AveOccup**: Average number of household members
7. **Latitude**: Block group latitude
8. **Longitude**: Block group longitude

- **Target Variable**: Median house value (in hundreds of thousands of dollars)

### Additional Information
- **No Missing Values**
- **Source**: This dataset was obtained from the StatLib repository: [StatLib California Housing](https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html)
- **Usage**: This dataset can be accessed via the `sklearn.datasets.fetch_california_housing` function in Python's Scikit-learn library.

## Background

Each entry in this dataset represents a census block group, which is the smallest geographical unit reported by the U.S. Census Bureau. These entries include aggregated data on housing and demographic information, helping model the median house value for each district.

Since the average number of rooms and bedrooms is provided per household, these figures may appear high for areas with fewer households, such as vacation resort regions.

## References

- Pace, R. Kelley, and Ronald Barry, "Sparse Spatial Autoregressions," *Statistics and Probability Letters*, 33 (1997) 291-297.
