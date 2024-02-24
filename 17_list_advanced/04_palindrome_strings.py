def palindrome_func(list_to_check, word_to_count):
    """"This function gets a list of all palindromes from list_to_check
    and count how many times we find the word_to_count in that list"""
    palindromes_list = [
        palindrome for palindrome in list_to_check
        if palindrome == palindrome[::-1]
    ]
    palindrome_count = palindromes_list.count(word_to_count)
    return print(palindromes_list,
                 f"\nFound palindrome {palindrome_count} times"
                 )


string_to_check = input().split()
palindrome_to_find = input()
palindrome_func(string_to_check, palindrome_to_find)
