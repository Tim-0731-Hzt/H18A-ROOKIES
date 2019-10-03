Daniel:
Most of the test I wrote assumed the function to directly pass.
So only the case of correctness of input values would be considered.
In function standup_send, I assumed the time is unchanged so the user will
not be expired from the current session. The same thing happened in all 
"stand" function.
In the function "upload photo" I assumed that the input value for the image
was directly a number -- so if it is not "200 Ok", it won't pass the test.