def lab2_q4():
    word = input("Enter a word: ")
    palindrome = word[::-1]   # reverse the word

    if word.lower() == palindrome.lower():
        print("The word", word, "is a palindrome")
    else:
        print("The word", word, "is not a palindrome")

lab2_q4()