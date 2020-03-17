import pandas as pd

df = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Python projects/PalindromeDetector/PalindromeFile.csv')
print("******************************** THE DATA FRAME IS *****************************")
print(df)
print("******************************** \n  ")

#Practicing retrieving rows
print("******************************** RETRIEVING THE RECORDS *****************************")
print("using the .loc to retrieve the records --> \n", df.loc[df['A']==123])
print("the columns are --> \n", df[:0])
#creating a concatenated field
df['ConcatenatedField'] = df['A'].map(str) + df['B'].map(str)

for i in range(len(df)):
    print(df['ConcatenatedField'])