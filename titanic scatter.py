import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")  

df_scatter = df[['Age', 'Fare']]
print(df_scatter)
plt.scatter(df_scatter['Age'], df_scatter['Fare'], color='r', label='Age vs Fare')
plt.title('Titanic Passenger Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()
