import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import scikit-learn as

# set matplotlib style sheet

plt.style.use('ggplot')

# read data from kaggle website

path = '/home/taylor/dev/projects/kaggle/hr_turnover_analysis/HR_comma_sep.csv'

df = pd.read_csv(path, header=0)

# convert categorical variables to integers

pd.options.mode.chained_assignment = None

sales_set = []

for i in range(0, len(df)):
    if df['sales'][i] in sales_set:
        continue
    else:
        sales_set.append(df['sales'][i])

print(sales_set)

sales_dict = {}
k = 1
for i in sales_set:
    sales_dict[i] = k
    k += 1

print(sales_dict)

df['salary_grade'] = 0

for i in range(0, len(df)):
    if df['salary'][i] == 'low':
        df['salary_grade'][i] = 1
    elif df['salary'][i] == 'medium':
        df['salary_grade'][i] = 2
    else:
        df['salary_grade'][i] = 3

# set random seed

np.random.seed(76)

# seperate data into train and test data sets

df['random'] = np.random.uniform(0, 1, df.shape[0])

train = df[df['random'] < 0.67]
test = df[df['random'] >= 0.67]

# visual data exploration

# side-by-side histograms

fig, axes = plt.subplots(nrows=3, ncols=3)
ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8 = axes.flat

ax0.hist(train['satisfaction_level'][train['left'] == 1], range=[0, 1], bins=20, color=['m'], alpha=1)
ax0.hist(train['satisfaction_level'][train['left'] == 0], range=[0, 1], bins=20, color=['c'], alpha=0.5)
ax0.set_title('Employee Satisfaction')
ax0.set_xlabel('Employee Satisfaction')
ax0.set_ylabel('Employee Count')

ax1.hist(train['average_montly_hours'][train['left'] == 1], range=[50, 350], bins=15, color='m', alpha=1)
ax1.hist(train['average_montly_hours'][train['left'] == 0], range=[50, 350], bins=15, color='c', alpha=0.5)
ax1.set_title('Monthly Hours')
ax1.set_xlabel('Average Monthly Hours')
ax1.set_ylabel('Employee Count')

ax2.hist(train['last_evaluation'][train['left'] == 1], range=[0, 1], bins=20, color='m', alpha=1)
ax2.hist(train['last_evaluation'][train['left'] == 0], range=[0, 1], bins=20, color='c', alpha=0.5)
ax2.set_title('Last Evaluation')
ax2.set_xlabel('Years Since Last Evaluation')
ax2.set_ylabel('Employee Count')

ax3.hist(train['number_project'][train['left'] == 1], range=[1, 9], bins=8, color='m', alpha=1, align='left')
ax3.hist(train['number_project'][train['left'] == 0], range=[1, 9], bins=8, color='c', alpha=0.5, align='left')
ax3.set_title('Number of Projects')
ax3.set_xlabel('Number of Projects')
ax3.set_ylabel('Employee Count')

ax4.hist(train['time_spend_company'][train['left'] == 1], range=[1, 9], bins=8, color='m', alpha=1, align='left')
ax4.hist(train['time_spend_company'][train['left'] == 0], range=[1, 9], bins=8, color='c', alpha=0.5, align='left')
ax4.set_title('Employee Tenure')
ax4.set_xlabel('Years Spent at Company')
ax4.set_ylabel('Employee Count')

ax5.hist(train['salary_grade'][train['left'] == 1], range=[1, 3], bins=3, color='m', alpha=1, align='left')
ax5.hist(train['salary_grade'][train['left'] == 0], range=[1, 3], bins=3, color='c', alpha=0.5, align='left')
ax5.set_title('Employee Salary')
ax5.set_xlabel('Salary Category')
ax5.set_ylabel('Employee Count')

ax6.hist(train['promotion_last_5years'][train['left'] == 1], range=[0, 1], bins=2, color='m', alpha=1)
ax6.hist(train['promotion_last_5years'][train['left'] == 0], range=[0, 1], bins=2, color='c', alpha=0.5)
ax6.set_title('Promotion in Last 5 Years')
ax6.set_xlabel('Promotion in Last 5 Years')
ax6.set_ylabel('Employee Count')

ax7.hist(train['Work_accident'][train['left'] == 1], range=[0, 1], bins=2, color='m', alpha=1)
ax7.hist(train['Work_accident'][train['left'] == 0], range=[0, 1], bins=2, color='c', alpha=0.5)
ax7.set_title('Work Accident in Last 2 Years')
ax7.set_xlabel('Work Accident in Last 2 Years')
ax7.set_ylabel('Employee Count')

ax8.hist(train['left'][train['left'] == 1], range=[0, 1], bins=2, color='m', alpha=1)
ax8.hist(train['left'][train['left'] == 0], range=[0, 1], bins=2, color='c', alpha=0.5)
ax8.set_title('Employees')
ax8.set_xlabel('Employees')
ax8.set_ylabel('Employee Count')

plt.tight_layout()
plt.show()
