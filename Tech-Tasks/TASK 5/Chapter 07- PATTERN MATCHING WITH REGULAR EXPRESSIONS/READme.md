# PATTERN MATCHING WITH REGULAR EXPRESSIONS



**In this chapter, I learned about what is meant by PATTERN MATCHING WITH REGULAR EXPRESSIONS in python.**
    
    1. re.compile() is the function that creates Regex objects.
    
    2.  Raw strings are particularly useful when working with regular expressions, as they allow us to specify patterns that may contain backslashes
        without having to escape them.
    
    3. The search() method will return None if the regex pattern is not found in the string. If the pattern is found, the search() method returns a
       Match object, which have a group() method that will return the actual matched text from the searched string.
       
    4. If the pattern is found, the search() method returns a Match object, which have a group() method that will return the actual matched text from
       the searched string.
    
    5. The first set of parentheses in a regex string will be group 1.
       The second set will be group 2.
       By passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text. Passing 0 or nothing to the
       group() method will return the entire matched text.
    
    6. Need to escape the ( and ) characters with a backslash.
    
    7. If the pattern includes 2 or more parentheses groups.
    
    8. The | character in regular expressions is used to indicate a logical OR operation. It means that the pattern on either side of the | character
       can be matched. 
       
    9. The ? character flags the group that precedes it as an optional part of the pattern.
       
    10. The * (called the star or asterisk) means “match zero or more”—the group that precedes the star can occur any number of times in the text. It
       can be completely absent or repeated over and over again.
       While * means “match zero or more,” the + (or plus) means “match one or more.” Unlike the star, which does not require its group to appear in
       the matched string, the group preceding a plus must appear at least once. It is not optional.
    
    11. The {3} and {3,5} characters in regular expressions are also quantifiers, meaning they specify the exact or minimum and maximum number of
       times the preceding element can be repeated. 
       The difference between them is that {3} requires exactly n occurrences, while {3,5} allows any number of occurrences between 3 and 5,
       inclusive.
       (Ha){3}   ==> (Ha)(Ha)(Ha)
       (Ha){3,5} ==> ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha)).
       
    12. \d ==> Any numeric digit from 0 to 9.
       \w  ==> Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
       \s  ==> Any space, tab, or newline character. (Think of this as matching “space” characters.)
       
    13. \D ==> Any character that is not a numeric digit from 0 to 9.
       \W  ==> Any character that is not a letter, numeric digit, or the underscore character.
       \S  ==> Any character that is not a space, tab, or newline.
       
    14. The dot-star (.*) to stand in for that “anything.” Remember that the dot character means “any single character except the newline,” and the
        star character means “zero or more of the preceding character.”
        The dot-star uses greedy mode: It will always try to match as much text as possible. To match any and all text in a non-greedy fashion, use
        the dot, star, and question mark (.*?). Like with braces, the question mark tells Python to match in a non-greedy way.
        
    15. The character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers. 
    
    16. To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
    
    17. The . character normally matches any character except the newline character. If re.DOTALL is passed as the second argument to re.compile(),
        then the dot will also match newline characters.
        
    18. 'X drummers, X pipers, five rings, X hens'.
    
    19. The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile().
    
    20. re.compile(r'^\d{1,3}(,\d{3})*$') will create this regex, but other regex strings can produce a similar regular expression.
    
    21. re.compile(r'[A-Z][a-z]*\sNakamoto').
    
    22. re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE).
