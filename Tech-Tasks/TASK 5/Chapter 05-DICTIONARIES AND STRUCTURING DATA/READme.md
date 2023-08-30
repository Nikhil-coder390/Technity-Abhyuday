# DICTIONARIES AND STRUCTURING DATA


**In this chapter, I learned about what is meant by DICTIONARIES AND STRUCTURING DATA in python.**
    
    1.  empdict={}.
    
    2.  myDict={'foo':42}.
    
    3. Unlike lists, items in dictionaries are unordered. The first item in a list named spam would be spam[0]. But there is no “first” item in a
       dictionary. While the order of items matters for determining whether two lists are the same, it does not matter in what order the key-value
       pairs are typed in a dictionary.
       
    4. As the key 'foo' doesn't exist, a KeyError: 'foo' is displayed.
    
    5. Both check for 'cat' in dictionary's keys.
    
    6. 'cat' in spam will check if 'cat' is a key in spam. 'cat' in spam.values() checks if there's a value 'cat' corresponding to any key in the
       dictionary.
    
    7.  spam.setdefault('color', 'black').
    
    8. We use pprint module to pretty print a dictionary's values. The function used is pprint.pprint(dcitionary_name).
