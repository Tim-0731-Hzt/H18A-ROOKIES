Assumptions
======

Overall:
* We assumed that assume everytime a "def test_*()" function is run that the "state" of the program is reset (e.g. all users are wiped).
* We assumed that all functions excepted for the function we are testing should be working as we expected.

In message_send:
* We assumed that this function will return a message dictionary what will contain message_id, u_id, message, time_created, is_unread.
* We assumed that message longer than 1000 will cause a ValueError.

In message_remove:
* We assumed that message_id nolonger exists means this message has been removed already such that a ValueError will occur.
* We assumed that the first two user joined the channel and the poster are authorised to remove this message.

In message_edit:
* same as message_remove

In message_react:
* We assumed that a message_id is not valid is because this message hase been deleted or does not exist.
* We assumed that a valid react_id should be in range 0-10. Any other react_id will be considered invalid.

In message_unreact:
* same as message_react

In user_profile:
* We assumed that any negative number is a invalid u_id
