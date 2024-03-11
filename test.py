# import matplotlib.pyplot as plt

# # Algorithm names
# algorithms = ['CNN', 'VGG', 'MobileNet']

# # Accuracies, Precisions, and Recalls
# accuracies = [76, 50, 94]
# precisions = [76, 20, 48]
# recalls = [76, 98, 98]

# # Create a pie chart for accuracies
# plt.figure(figsize=(12, 6))

# # Accuracy pie chart
# plt.subplot(1, 3, 1)
# plt.pie(accuracies, labels=algorithms, autopct='%1.1f%%', startangle=140)
# plt.title('Accuracies')

# # Precision pie chart
# plt.subplot(1, 3, 2)
# plt.pie(precisions, labels=algorithms, autopct='%1.1f%%', startangle=140)
# plt.title('Precisions')

# # Recall pie chart
# plt.subplot(1, 3, 3)
# plt.pie(recalls, labels=algorithms, autopct='%1.1f%%', startangle=140)
# plt.title('Recalls')

# # Display the chart
# plt.tight_layout()
# plt.show()



import matplotlib.pyplot as plt

# Algorithm names and their metrics
algorithms = ['CNN', 'Hybrid', 'MobileNet']
accuracies = [92, 52, 92]
precisions = [90, 69, 99]
recalls = [40, 36, 31]

import matplotlib.pyplot as plt

# Algorithm names and accuracies
algorithms = ['CNN', 'Hybrid', 'MobileNet']
accuracies = [92, 52, 92]

# Define colors for each segment
colors = ['lightblue', 'lightgreen', 'orange']

# Create a pie chart for accuracies, with the values displayed inside the chart and different colors for each segment
plt.figure(figsize=(6, 6))
plt.pie(accuracies, labels=algorithms, colors=colors, autopct=lambda p: f'{int(p/100.*sum(accuracies))}', startangle=140)
plt.title('Accuracies of Algorithms')
plt.show()
plt.savefig('plot.png')


#Algorithm names and Precision 
algorithms = ['CNN', 'Hybrid', 'MobileNet']
precision = [90, 69, 91]

# Define colors for each segment
colors = ['lightblue', 'lightgreen', 'orange']

# Create a pie chart for accuracies, with the values displayed inside the chart and different colors for each segment
plt.figure(figsize=(6, 6))
plt.pie(precision, labels=algorithms, colors=colors, autopct=lambda p: f'{int(p/100.*sum(accuracies))}', startangle=140)
plt.title('Precision of Algorithms')
plt.show()



# # Algorithm names and recalls 
algorithms = ['CNN', 'Hybrid', 'MobileNet']
recalls = [40, 36, 31]

# Define colors for each segment
colors = ['lightblue', 'lightgreen', 'orange']

# Create a pie chart for accuracies, with the values displayed inside the chart and different colors for each segment
plt.figure(figsize=(6, 6))
plt.pie(recalls, labels=algorithms, colors=colors, autopct=lambda p: f'{int(p/100.*sum(accuracies))}', startangle=140)
plt.title('Recalls of Algorithms')
plt.show()

