# Lists

**In this chapter, I learned about what is meant by Lists, Tuples and strings in python.**
    
    1. a list begins with an opening square bracket and ends with a closing square bracket, []. 
    
    2. spam[2]='hello'(we need third value. so in the given list spam= [2,4,6,10] third value index is 2).
    
    3. spam[int(int('3' * 2) // 11)] evaluate to "d". 
       ('3'*2='33' ==> int('33')=33 ==> 33//11=3 ==> int(3)=3 ==> spam[3]='d').
       
    4. It evaluates to 'd'.
    
    5. spam[:2] evaluate to (it gives elements in the index 0,1) ['a', 'b'].
    
    6. bacon.index('cat') evaluate to 1, which is the index position of the element cat in bacon.
    
    7. Appends 99 at the end of the list. The new list will be [3.14, 'cat', 11, 'cat', True, 99].
   
    8. bacon.remove('cat') removes the cat from the list. The new list will be [3.14, 11, 'cat', True, 99].
    
    9. "+" operator for list concatenation and "*" operator for list replication.
    
    10. The previous append() method call adds the argument to the end of the list.
        The insert() method can insert a value at any index in the list.
    
    11. The del statement is good to use when you know the index of the value you want to remove from the list. The remove() method is useful when you
        know the value you want to remove from the list.
    
    12. Both lists and strings are sequential collections of items, can be accessed by index, can be sliced, can be iterated over, can be 
        concatenated, can be multiplied.
    
    13. A list value is a mutable data type: it can have values added, removed, or changed. However, tuples is immutable: it cannot be changed. 
        
    14. eggs= (42,).
    
    15. To get the tuple form of a list value ==> tuple(list).
        To get the list form of a tuple value ==> list(tuple).
        
    16. References to list objects.
    
    17. copy.copy(), can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.
        The deepcopy() function will copy these inner lists as well.
        

