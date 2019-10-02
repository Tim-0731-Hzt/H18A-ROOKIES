In message_send:
We assumed that this function will return a message dictionary what will contain message_id, u_id, message, time_created, is_unread.
We assumed that message longer than 1000 will cause a ValueError.
In message_remove:
We assumed that message_id nolonger exists means this message has been removed already such that a ValueError will occur.
We assumed that the first two user joined the channel and the poster are authorised to remove this message.