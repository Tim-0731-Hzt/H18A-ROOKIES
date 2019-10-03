Assumptions:

**In test_auth_login:**
    * I could assume that the first user who login will have "u_id: 00001" and "token: 1", the second user will have "u_id: 00002" and "token: 2" and so on. 

**In auth_login:**
* We could help user save email and password on local, so that they don't need to type in email and password agian and   again.

**In test_auth_register:**
* I could assume that the first user who register will have "u_id: 00001" and "token: 1". 
* the second user will have "u_id: 00002" and "token: 2" and so on.

**In auth_password_request:**
* We should still have a function that generate a serious of random security code, and set it's valid period to 1 min.
    
**In channel_details:**
* We need to set a function for set up the name of channel, or we couldn't get a return "name" from the function channel_details

**In channel_messages:**
* we need a function that could count the total number of messages. Now, I assume that the total number of messages are 150

**In channel_invite:**
* u_id is the id who is invited