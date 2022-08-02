import pandas as pd

csv_path = 'Groceries_dataset.csv'
df = pd.read_csv(csv_path)
head = df.head()
print (head)
print ("========================================================================")
print ()

items = {'itemDescription':['whole milk','tropical fruit'],'Member_number':['2552','1808']}
items_frame = pd.DataFrame(items)
print (items_frame)
