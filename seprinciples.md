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

**From: auth_pickle.py**
**Type: Dry**
   There wew three if statements which contains same content that have three lines. After using Dry, I write them in one line out side the if statement. 

**From: channel.py**
**Type: Top-down thinking**
    We write several helper function in channel which effectively using top-down thinking. For example, we use "get_channels, get_messages, get_members" to get the exact information we need for the function. Besides, we use helper funtion named "channel_id_check, u_id_check, auth_id_check, channel_property_check, channel_admin_check" to follow the principles of Top-down thinking.


**From: channel.py**s
**Type: Top-down thinking and KISS and DRY**
    In the past when we invite a user to join in the channel we would use a for loop to check whether the user is already in the channel. After using Top-down thinking, KISS and DRY, we write a function called "is_in_channel" to check whether the user is in channel, and then it will return a boolean value. 

**From: message_pickle.py**
**Type: Top-down thinking and KISS**
    For the function "message_edit" and "message_remove", we need to check whether user is the owner of the channel, to keep code better, we used a helper function named "is_owner" to check this value and return a boolean. As same as the helper function "is_sender". 

**From: user.py**
**Type: Top-down thinking and KISS**
    There are some parts in functions that we need to user for loop to find the exact user in userDict which is a complicated process. In order to use Top-down thinking and KISS we write a helper function to do that job.