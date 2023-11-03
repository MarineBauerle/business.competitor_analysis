#### Binance Competitive Analysis Project

This repository contains the dataset, scripts, and visualizations associated with the Binance Competitive Analysis project. The goal of this project is to gain insights into Binance's position within the competitive landscape, focusing on organic traffic, common keywords, AdWords usage, and the overall relevance of competitors.

##### Table of Contents:

1. [Data](#data)
2. [Script](#script)
3. [Documents](#visualizations)
4. [ReadMe](#methodology)

##### Data

The `data` folder is divided into `raw` and `processed` sub-folders:
- `raw`: Contains the initial dataset on Binance and its competitors.
- `processed`: Contains the cleaned and processed data used for the visualizations.

##### Script

- `binance.py`: This script contains the Python code used for data processing and cleaning.

##### Documents

Refer to the [dashboard_info.md](./documents/dashboard_info.md) for insights into the Tableau dashboard visualizations and the [Binance Competitor Analysis Dashboard](https://public.tableau.com/views/BinanceCompetitorAnalysis/Dashboard1?:language=fr-FR&:display_count=n&:origin=viz_share_link).



### Methodology (For `dashboard_info.md`)


For this analysis, the methodology is outlined as follows:

1. **Data Collection**: Data was sourced from SEMRUSH analytics tool that provides insights into website performance and competitive metrics.

2. **Data Cleaning**: Using the `binance.py` script, the raw data was cleaned by removing any missing values, normalizing inconsistent data points, and aggregating metrics as needed.

3. **Data Analysis**: 
    - **Organic Traffic Analysis**: Assessed the volume of organic traffic competitors receive, giving insights into their search engine performance.
    - **Keyword Analysis**: Evaluated the common keywords that Binance and its competitors rank for, providing a perspective on the content strategy.
    - **AdWords Usage**: Analyzed the extent to which competitors use paid advertising to drive traffic to their sites.
    - **Relevance Analysis**: Mapped organic traffic against different metrics (like common keywords and AdWords) to gauge the relevance and performance of competitors in the market.

4. **Visualization**: Created interactive visualizations using Tableau, enabling stakeholders to dynamically explore the competitive landscape and make informed decisions.

The combination of data analysis and visualization allows for a holistic understanding of Binance's positioning among its competitors and highlights areas of opportunity or concern.
