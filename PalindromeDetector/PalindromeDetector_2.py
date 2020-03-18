#importing the package
import pandas as pd

if __name__ == "__main__":

    #reading the csv file
    df = pd.read_csv("/Users/aakarsh.rajagopalan/Personal documents/Python projects/PalindromeDetector/PalindromeFile.csv")

    #creating a new column that contains the Concatenated filed
    df["concatenatedField"] = df["A"].map(str)+df["B"].map(str)
    is_palindrome = []

    #creating a loop to iterate through each element in the list
    for i in range(len(df)):
        #extracting the value stored in the thrid - newly created field and storing it in a variable called string.
        string = df["concatenatedField"][i:i+1].values

        #converting this ndarray to a list so that it is easier to work with.
        string = list(string)

        #extracting the first value of the list and storing it in a place holder variable. this variable will then be used to perform the
        #reversal to identify if it is a palindrome or not
        x = string[0]

        #note that when a string is sliced as x[a:b:c], a is the starting position / b is the ending position / c is the amount of increment
        rev = x[::-1]

        #using the conditional statement
        if string[0] == rev:
            print("yes")
            is_palindrome.append('yes')
        else:
            print("no")
            is_palindrome.append('no')

        #adding the new column called is_palindrome
        if len(is_palindrome) == len(df):
            print(is_palindrome)
            print(is_palindrome[i:i+1])
            df["is_palidrome"] = is_palindrome
        print(df)

