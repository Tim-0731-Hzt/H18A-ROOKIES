'''For a given channel, start the standup period whereby for the next 15 minutes if someone calls "standup_send" with a message, it is 
buffered during the 15 minute window then at the end of the 15 minute window a message will be added to the message queue in the channel
 from the user who started the standup.''' ''' availble channel 1,2,3'''
import pytest
from standup_start import standup_start
def test1_standup_start():
    standup_start(123,1)
def test2_standup_start():
    standup_start(123,5)