#Assumptions:

##Auth Part 
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

 ##Channel Part 
**In channel_invite:**
* We assume that u_id is the id who is invited  

s**In channel_details:**
* We assume that we need to set a function for set up the name of channel, or we couldn't get a return "name" from the function channel_details

**In channel_messages:**
* We assume that we need a function that could count the total number of messages. Now, I assume that the total number of messages are 150

