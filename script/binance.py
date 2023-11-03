import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('binance.com-organic.Competitors-uk-20231016-2023-10-17T11_10_16Z.csv')

print(data.head())
print(data.describe())

sns.scatterplot(data=data, x='Competitor Relevance', y='Organic Traffic')
plt.title('Scatter Plot of Competitor Relevance vs. Organic Traffic')
plt.show()

from scipy import stats

z_scores = stats.zscore(data['Organic Traffic'])
data['Z-Score'] = z_scores
outliers = data[abs(data['Z-Score']) > 3]
print("Potential Outliers:")
print(outliers)

data.to_csv('cleaned_data.csv', index=False)


### Binance Competitor Analysis Script

#### Description:
This Python script provides a comprehensive analysis of the competitors' relevance against organic traffic. The script primarily focuses on visualizing the data and identifying potential outliers.

#### Key Features:
1. **Data Loading and Overview**: Loads a dataset that contains information about competitors' relevance and organic traffic and provides a quick overview of the data.
2. **Data Visualization**: Creates a scatter plot to showcase the relationship between competitor relevance and organic traffic.
3. **Outlier Detection**: Uses Z-score calculations to detect potential outliers in the organic traffic data.
4. **Data Export**: Saves the processed dataset, including calculated z-scores, into a new CSV file for further analysis.


#### Potential Enhancements:
- Incorporation of additional outlier detection methods.
- Enhanced visualizations, such as histograms or box plots.
- Advanced statistical analysis to derive more insights from the data.
