# stacked histograms

'''
fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flat

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['satisfaction_level'])
ax0.hist(tmp, bins=10, stacked=True, color=['m', 'c'])
ax0.set_title('Employee Satisfaction')
ax0.set_xlabel('Employee Satisfaction')
ax0.set_ylabel('Employee Count')

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['last_evaluation'])
ax1.hist(tmp, bins=10, stacked=True, color=['m', 'c'])
ax1.set_title('Last Evaluation')
ax1.set_xlabel('Last Evaluation')
ax1.set_ylabel('Employee Count')

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['number_project'])
ax2.hist(tmp, bins=5, stacked=True, color=['m', 'c'])
ax2.set_title('Number of Projects')
ax2.set_xlabel('Number of Projects')
ax2.set_ylabel('Employee Count')

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['average_montly_hours'])
ax3.hist(tmp, bins=10, stacked=True, color=['m', 'c'])
ax3.set_title('Monthly Hours')
ax3.set_xlabel('Monthly Hours')
ax3.set_ylabel('Employee Count')

ax3.legend(train['left'], labels=('left', 'stayed'))

plt.tight_layout()
plt.show()
'''


'''
tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['last_evaluation'])
ax1.hist(tmp, bins=10, stacked=True, color=['m', 'c'])
ax1.set_title('Last Evaluation')
ax1.set_xlabel('Last Evaluation')
ax1.set_ylabel('Employee Count')

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['number_project'])
ax2.hist(tmp, bins=5, stacked=True, color=['m', 'c'])
ax2.set_title('Number of Projects')
ax2.set_xlabel('Number of Projects')
ax2.set_ylabel('Employee Count')

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['average_montly_hours'])
ax3.hist(tmp, bins=10, stacked=True, color=['m', 'c'])
ax3.set_title('Monthly Hours')
ax3.set_xlabel('Monthly Hours')
ax3.set_ylabel('Employee Count')

ax3.legend(train['left'], labels=('left', 'stayed'))


# box plots

fig, axes = plt.subplots(nrows=1, ncols=1)
ax0 = axes

ax0.boxplot(train['satisfaction_level'])
ax0.set_ylim(0, 1.2)
'''

'''
fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flat

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['satisfaction_level'])
ax0.boxplot(tmp)
ax0.set_title('Employee Satisfaction')
ax0.set_xlabel('Employee Satisfaction')
ax0.set_ylabel('Employee Count')

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['last_evaluation'])
ax1.boxplot(tmp)
ax1.set_title('Last Evaluation')
ax1.set_xlabel('Last Evaluation')
ax1.set_ylabel('Employee Count')

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['number_project'])
ax2.boxplot(tmp)
ax2.set_title('Number of Projects')
ax2.set_xlabel('Number of Projects')
ax2.set_ylabel('Employee Count')

tmp = list()
for i in range(2):
    indices = train[train['left'] == i]
    tmp.append(train['average_montly_hours'])
ax3.boxplot(tmp)
ax3.set_title('Monthly Hours')
ax3.set_xlabel('Monthly Hours')
ax3.set_ylabel('Employee Count')

plt.tight_layout()
plt.show()
'''