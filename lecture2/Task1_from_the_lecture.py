import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Tanya\Documents\GitHub\Python_Projects\lecture2\company_sales_data.csv')
profit_list = df['total_profit'].tolist()
month_list = df['month_number'].tolist()
plt.plot(month_list, profit_list)
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Total profit of all months')
plt.show()
