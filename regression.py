import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('charlottedata.csv')
print(dataset.shape)
#dataset.plot(x='Hours Worked', y='Tax Rate', style='o')
#plt.title('Tax Rate Effects Hours Worked')
#plt.xlabel('Hours Worked')
#plt.ylabel('Tax Rate')
#plt.show()

print(dataset.Hours)
y = dataset.Hours
x = dataset.Tax
x = sm.add_constant(x)
x.head()

est=sm.OLS(y, x)
est = est.fit()
print(est.summary())
#print(est.params)
X_prime = np.linspace(x.Tax.min(), x.Tax.max(), 10)[:, np.newaxis]
X_prime = sm.add_constant(X_prime)
y_hat = est.predict(X_prime)
plt.scatter(x.Tax, y, alpha=0.3)
plt.xlabel("Hours Worked")
plt.ylabel("Tax Rate")
plt.plot(X_prime[:, 1], y_hat, 'r', alpha=0.9)

est = smf.ols(formula='Hours ~ Tax', data=dataset).fit()
print(est.summary())
