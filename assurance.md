Assurance
======

## Auth:
**auth_login:**
* Used 6 test cases. Covered
* ValueError when email in not a valid email, email entered is not belong to a user, and password is not correct
* 
**auth_logout:**
* Used 2 test cases. Covered
* User's online status will be false after logout.

**auth_register:**
* Used 13 test cases. Covered
* ValueError when email is not a valid email,  email address is already used by other users, password is less than 6 characters and firstname, lastname are more than 50 characters
* When the same handle occur, function will change the first 3 chararters into numbers, add one more when the second same handle occur.

**auth_passwordreset_request:**
* Used 1 test cases. Covered
* Provide test to test a reset_code will be sent successfully to the user email
* make sure every reset_code is made up by random number to ensure the security

**auth_passwordreset_reset:**
* Used 4 test cases. Covered
* ValueError when invalid reset_code and new_password
* After using the reset_code, reset_code will be null

## Channel:

**channel_invite:** 
* provided five tests to test the the invite to channel owner, and channel member, and ValueError and AccessError

**channel_details:**

## Message:

## User:

**User profile:**
* provided 3 normal tests to test the performance of the function and raise 2 
* exception  tests when having invalid user id and invalid token to  reach the 100% code coverage.

**User_profile_setemail :**  
* provided 3 normal tests to test the performance of the function and raise 3 exception tests when having bad emails("shas@ashd) or used email or bad token to reach 100% code coverage.

**user_profile_setname :** 
* provided 3 normal tests to test the performance of the function and raise 3 exception test when having first or last name too long or having a bad token.

**user_profilr_sethandle :** 
* provided 3 normal tests to test the performance of the function and raise 2 exception tests for handle is too short or bad token.

**user_upload photo :** 
* not yet finished.

**standup_start // standup_send:**  
* provided 3 normal test alone with 9 exception including invalid token , incalid user id(user not in channel), already in standup, message too long and ...etc
* so far , there is one question not solved , noly one cahnnel can start a standup at a time due to the storage of message data.

**search :**
* waiting for more message to be tested , have already 3 test  to be done

**change admin :** 
* having 3 normal test and 7 exception like : giving others owners premission as an admin, member can not access owner can not demote other owners and admins can not demote other admins.


