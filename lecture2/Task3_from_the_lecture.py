import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_sales_data.csv')
products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
for product in products:
    plt.plot(df['month_number'], df[product], label=product)
plt.title('Product Sales per Month')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.legend()
plt.show()
