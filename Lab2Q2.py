#(String) Write a program that reads in a string input consisting of 2 words with 
#a  blank  in  between.  The  program  displays  each  of  the  word  in  reverse. 
#Example: 
#       Enter string: java python 
#       Output: avaj nohtyp 
#       Assume input is valid. 


def lab2q2():
    string = (input("Enter string"))
    print("Output:", string[::-1])


def lab2_q2():
    word1, word2 = input("Enter string: ").split()
    print("Output: {} {}".format(word1[::-1], word2[::-1]))