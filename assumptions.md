<<<<<<< HEAD
# Assumptions:

## Auth Part 

**In test_auth_login:**
* We  assume that the first user who login will have "u_id: 00001" and "token: 1". 
* The second user will have "u_id: 00002" and "token: 2" and so on. 

**In auth_login:**
* We assume we could help user save email and password on local, so that they don't need to type in email and password agian and again.

**In test_auth_logout:**
* We assume every time a "token" try to logout, it will be examined whether it is valid.

**In test_auth_register:**
* We assume that the first user who register will have "u_id: 00001" and "token: 1". 
* The second user will have "u_id: 00002" and "token: 2" and so on.
* We assume that there is a connection between "token" and "email", so that we could know whether an email is already exist.

**In auth_password_request:**
* We assume that the password_request funciton still need a function that generate a serious of random security code, and set it's valid period to 1 min.

## Channel Part 

**In channel_invite:**
* We assume that u_id is the id who is invited  

**In channel_details:**
* We assume that we need to set a function for set up the name of channel, or we couldn't get a return "name" from the function channel_details

**In channel_messages:**
* We assume that we need a function that could count the total number of messages. Now, I assume that the total number of messages are 150

=======
Assumptions
======

**Overall**
* We assumed that assume everytime a "def test_*()" function is run that the "state" of the program is reset (e.g. all users are wiped).
* We assumed that all functions excepted for the function we are testing should be working as we expected.

**In channel_assumption**
* we assume owner_members and all_members are dictionary in the return dictionary in channel_details 
* we assume the keys in owner_member and all_member is user_id
* we assume the channel we create to test channel_removeowner does not exist
* we assume the user_id we create to test channel_removeowner is not exist

**In message_assumption**
* we assume the channel we create to test message_sendlater does not exist

**In message_send:**
* We assumed that this function will return a message dictionary what will contain message_id, u_id, message, time_created, is_unread.
* We assumed that message longer than 1000 will cause a ValueError.
* We assumed that after someone has created a channel, that user is already a member and owner of that channel.

**In message_remove:**
* We assumed that message_id nolonger exists means this message has been removed already such that a ValueError will occur.
* We assumed that the first two user joined the channel and the poster are authorised to remove this message.
* We assumed that a normal user cannot remove a message with message_id was sent by another member in channel.
* We assumed that a normal user cannot remove a message which was posted by the owner of the channel or an admin or owner of slackr.
* We assumed that a normal user can only remove the message sent by himself.
* We assumed that the owner of the channel or an admin or owner of slackr can remove any messages.

**In message_edit:**
* same as message_remove

**In message_react:**
* We assumed that a message_id is not valid is because this message hase been deleted or does not exist.
* We assumed that a valid react_id should be in range 0-10. Any other react_id will be considered invalid.

**In message_unreact:**
* same as message_react

**In user_profile:**
* We assumed that any negative number is a invalid u_id

**In standup_send:**
* We assumed the time is unchanged so the user willnot be expired from the current session. The same thing happened in **all "stand"** function.

**In upload photo:**
* We assumed that the input value for the image was directly a number -- so if it is not "200 Ok", it won't pass the test.

**In admin_userpermission_change:**
* I assumed the person already is the admin or the owner.
>>>>>>> fa793bd05612ec37f9bec154b723781a84d61b41
