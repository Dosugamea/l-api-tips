from linepy import *
from datetime import datetime

cl = LINE("Input your token")
tracer = OEPoll(cl)
log = {}

# msg.createdTime -> 00:00:00
def cTimeToText(unixtime):
    dt = datetime.fromtimestamp(int(str(unixtime)[:-3]))
    return dt.strftime('%H:%M:%S')
# make response text
def mk_resp(gid):
    users = ["%s\n[%s]"%(cl.getContact(u[0]).name,u[0].strftime('%H:%M:%S')) for u in log[msg.to]]
    return '\n'.join(['%s users are reading.'%(len(log[msg.to])),'']+users)

# Start Logging / Check Log by command
def RECEIVE_MESSAGE(op):
    try:
        msg = op.message
        if msg.contentType == 0 and msg.toType == 2:
            if msg.text == "start":
                cl.sendMessage(msg.to,"Start read check.")
                log[msg.to] = []
            elif msg.text == "check":
                if msg.to in log:
                    cl.sendMessage(msg.to,mk_resp(msg.to))
                else:
                    cl.sendMessage(msg.to,"ReadData not exists")
    except Exception as e:
        print(e)
tracer.addOpInterrupt(26, RECEIVE_MESSAGE)

# Load from Log when message cancelled
def NOTIFIED_READ_MESSAGE(op):
    try:
        at = op.param1
        mid = op.param2
        if at in log:
            log[msg.to].append([mid,datetime.now()])
    except Exception as e:
        print(e)
tracer.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)

while True:
    tracer.trace()
