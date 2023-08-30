# MANIPULATING STRINGS


**In this chapter, I learned about what is meant by MANIPULATING STRINGS in python.**
    
    1. An escape character lets you use characters that are otherwise impossible to put into a string. An escape character consists of a backslash
       (\) followed by the character you want to add to the string.
    
    2.  \t ==> Tab
        \n ==> Newline (line break).
    
    3. If we need to use the \ character, we'll have to escape it: \\ .
       
    4. The single quote in Howl's is fine because, we have used double quotes to mark the beginning and end of the string.
    
    5. Using Multiline Strings with Triple Quotes we can write a string with newlines in it.
       A multiline string in Python begins and ends with either three single quotes or three double quotes. Any quotes, tabs, or newlines in between
       the “triple quotes” are considered part of the string.
    
    6. i)   'Hello, world!'[1]   ==> 'e'.
       ii)  'Hello, world!'[0:5] ==> 'Hello'.
       iii) 'Hello, world!'[:5]  ==> 'Hello'.
       iv)  'Hello, world!'[3:]  ==> 'lo, world!'.
    
    7.  i)  'Hello'.upper()           ==> 'HELLO'.
       ii)  'Hello'.upper().isupper() ==>  True.
       iii) 'Hello'.upper().lower()   ==> 'hello'.
    
    8.  i)  'Remember, remember, the fifth of November.'.split()  ==> ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.'].
       ii)  '-'.join('There can be only one.'.split())            ==>  'There-can-be-only-one.'.
       
    9. rjust()  ==> right-justify.
       ljust()  ==> left-justify.
       center() ==> center.
       
    10. The strip() string method will return a new string without any whitespace characters at the beginning or end. The lstrip() and rstrip()
        methods will remove whitespace characters from the left and right ends, respectively. 
