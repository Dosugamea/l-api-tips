from linepy import *
from datetime import datetime

cl = LINE("Input your token")
tracer = OEPoll(cl)
log = {}

# msg.createdTime -> 00:00:00
def cTime_to_Text(unixtime):
    dt = datetime.fromtimestamp(int(unixtime[:-3]))
    return dt.strftime('%H:%M:%S')
# make response text
def mk_resp(msg_id):
    return '\n'.join([
    'SentMessage cancelled.',
    '[Sender]',
    cl.getContact(log[msg_id]["from"]).displayName,
    '[Time]',
    cTime_to_Text(str(log[msg_id]["createdTime"])),
    '[Message]',
    log[msg_id]["text"]
    ])

# Save to Log when get TextMessage
def RECEIVE_MESSAGE(op):
    try:
        msg = op.message
        if msg.contentType == 0:
            log[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
    except Exception as e:
        print(e)
tracer.addOpInterrupt(26, RECEIVE_MESSAGE)

# Load from Log when message cancelled
def NOTIFIED_DESTROY_MESSAGE(op):
    try:
        at = op.param1
        msg_id = op.param2
        if msg_id in log:
            cl.sendMessage(at,mk_resp(msg_id))
    except Exception as e:
        print(e)
tracer.addOpInterrupt(65, NOTIFIED_DESTROY_MESSAGE)

while True:
    tracer.trace()
