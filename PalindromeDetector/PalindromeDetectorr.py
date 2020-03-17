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
    print(df['ConcatenatedField'][i:i+1])
    string = df['ConcatenatedField'][i:i+1].to_string()
    print("******************************** THE STRAIGHT STRING IS *****************************")
    print(string,'\n')
    print("******************************** THE REVERSE STRING IS *****************************")
    print(string[::-1])
    print("******************************** STARTING THE IF CONDITION *****************************")
    if string == str(string[::-1]):
        print('yes')
    else:
        print('no')
