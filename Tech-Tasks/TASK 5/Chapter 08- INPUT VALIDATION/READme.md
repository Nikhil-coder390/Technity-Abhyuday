# INPUT VALIDATION


**In this chapter, I learned about what is meant by INPUT VALIDATION in python.**
    
    1. PyInputPlus is not a part of the Python Standard Library.
    
    2. The as pyip code in the import statement saves us from typing pyinputplus each time we want to call a PyInputPlus function.
    
    3. inputInt()   ==> Takes input in integer.
       inputFloat() ==> Takes input in integer float.
       
    4. response = pyip.inputNum(min=0, lessThan=99).
    
    5. The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will
       accept or reject as valid input.
    
    6. It will throw RetryLimitException exception.
    
    7. When you use limit keyword arguments and also pass a default keyword argument, the function returns the default value instead of raising an
       exception.
