import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Tanya\Documents\GitHub\Python_Projects\lecture2\company_sales_data.csv')

plt.plot(df['month_number'], df['total_profit'], '--ro', linewidth=3)
plt.title('Total Profit of All Months', fontsize=14)
plt.xlabel('Month Number', fontsize=12)
plt.ylabel('Total Profit', fontsize=12)
plt.legend(['Profit'], loc='lower right')
plt.show()
