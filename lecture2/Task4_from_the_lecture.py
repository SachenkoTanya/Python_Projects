import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Tanya\Documents\GitHub\Python_Projects\lecture2\company_sales_data.csv')
toothpaste_sales = df['toothpaste']
plt.scatter(df['month_number'], toothpaste_sales, marker='.', label='Tooth paste sales data')
plt.grid(True, linestyle='--')
plt.title('Tooth paste sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of Units Sold')
plt.legend()
plt.show()
