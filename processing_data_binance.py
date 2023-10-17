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
