#importing the package
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("/Users/aakarsh.rajagopalan/Personal documents/Python projects/PalindromeDetector/PalindromeFile.csv")

    #creating a new column that contains the Concatenated filed
    df["concatenatedField"] = df["A"].map(str)+df["B"].map(str)

for i in range(len(df)):
    #extracting the value stored in the thrid , newly created field.
    string = df["concatenatedField"][i:i+1].values
    rev = list(reversed(string))

    #using the conditional statement
    if string == rev:
        print("yes")
    else:
        print("no")