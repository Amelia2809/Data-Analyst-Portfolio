import pandas as pd

csv_path = 'indian_food.csv'
df = pd.read_csv(csv_path)
head = df.head()
print (head)
print ("========================================================================")
print ()
z = df[['name','region']]
print (z)
print ("========================================================================")
print ()
y = df.loc[0:9,'name':'ingredients']
print (y)

