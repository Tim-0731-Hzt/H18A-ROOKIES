Seprinciples
===========
**From: auth_pickle.py**
**Type: Top-down thinking**
    There are sereval improvements from top down thinking, handle_check was using a for loop to determin
    whether it is a valid handle or not, now it was replaced by a function called "handle_check", which takes in 
    a handle as its parameter, return a boolean value indicating the validation of that particular handle.
    These changes are from the concept of top down thinking, which starts from high levels of abstraction down to lower
    levels of abstraction.

**From: auth_pickle.py**
**Type: Top-down thinking and KISS**
    As for the design to handle when the repeated handle happened, we try to add an increasing num at the end of the handle, and use two for loops to find the repeadted handle. In this case, our code looks a mess and it will generate different length handle which is not a good result. After using the top-town thinking and KISS we improveed our part by adding a num which lengeht is 3 before a repeated handle, eg. "001,010,100,234". And we used a function named digit_check to check the length of added string, so that we added the '0' in the left to keep the length the same. 

    