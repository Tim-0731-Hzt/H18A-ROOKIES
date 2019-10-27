Assurance
======

## Auth:
**auth_login:**
* Used 6 test cases. Covered
* ValueError when email in not a valid email, email entered is not belong to a user, and password is not correct

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

Reached 98% coverage for all message functions.

**channel_invite:** 
* five test cases 
* ValueError when:
* channel_id does not refer to a valid channel that the authorised user is part of.
* u_id does not refer to a valid user
* AccessError when the authorised user is not already a member of the channel

**channel_details:**
* Used 3 test cases. Covered 
* ValueError when:
* Channel ID is not a valid channel
* AccessError when Authorised user is not a member of channel with channel_id

**channel_messages:**
* five test cases
* ValueError when:
* Channel ID is not a valid channel
* start is greater than the total number of messages in the channel
* AccessError when Authorised user is not a member of channel with channel_id

**channel_leave:**
* five test cases
* ValueError when:Channel ID is not a valid channel

**channel_join:**
* five test cases
* ValueError when:Channel ID is not a valid channel
* AccessError whenchannel_id refers to a channel that is private (when the authorised user is not an admin)

**channel_addowner:**
* five test cases
* ValueError when:
* Channel ID is not a valid channel
* When user with user id u_id is already an owner of the channel
* AccessError when the authorised user is not an owner of the slackr, or an owner of this channel

**channel_removeowner:**
* five test cases
* ValueError when:
* Channel ID is not a valid channel
* When user with user id u_id is not an owner of the channel
* AccessError when the authorised user is not an owner of the slackr, or an owner of this channel

**channels_list:**
* five test cases

**channels_listall:**
* five test cases

**channels_create:**
* five test cases
* ValueError when:Name is more than 20 characters long
## Message:
Reached 100% coverage for all message functions.

**message_sendlater:**
* Used 3 test cases. Covered 
* ValueError when:
* Channel ID is not a valid channel
* Message is more than 1000 characters
* Time sent is a time in the past
* AccessError when the authorised user has not joined the channel they are trying to post to

**message_send:**
* Used 3 test cases. Covered 
* ValueError when message is more than 1000 characters
* AccessError when the authorised user has not joined the channel they are trying to post to

**message_remove:**
* Used 5 test cases. Covered
* ValueError when message (based on ID) no longer exists
* AccessError when none of the following are true:
* Message with message_id was sent by the authorised user making this request
* The authorised user is an admin or owner of this channel or the slackr

**message_edit:**
* Used 4 test cases. Covered
* AccessError when none of the following are true:
* Message with message_id was sent by the authorised user making this request
* The authorised user is an admin or owner of this channel or the slackr

**message_react:**
* Used 7 test cases. Covered
* ValueError when:
* message_id is not a valid message within a channel that the authorised user has joined
* react_id is not a valid React ID. For iteration 2, the only valid react ID is 1
* Message with ID message_id already contains an active React with ID react_id

**message_unreact:**
* Used 6 test cases. Covered
* ValueError when:
* message_id is not a valid message within a channel that the authorised user has joined
* react_id is not a valid React ID
* Message with ID message_id does not contain an active React with ID react_id

**message_pin:**
* Used 5 test cases. Covered
* ValueError when:
* message_id is not a valid message
* The authorised user is not an admin
* Message with ID message_id is already pinned
* AccessError when the authorised user is not a member of the channel that the message is within

**message_unpin:**
* Used 5 test cases. Covered
* ValueError when:
* message_id is not a valid message
* The authorised user is not an admin
* Message with ID message_id is already unpinned
* AccessError when the authorised user is not a member of the channel that the message is within


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


