# Group Structure
Memo of Group.<br><br>

## Base(getGroup)
|Key|Value|Note|
|:---:|:---:|:---:|
|name|'Bot実験室'|GroupName|
|id|'c1a2ac5e38fb50f9ad82dc2XXXXXXXXXX'|str GroupID|
|createdTime|1498487244747|int Unix Group CreatedTime|
|pictureStatus|'PicturePath'|str GroupPicturePath|
|preventedJoinByTicket|False|True/False|
|groupPreference|groupPreference()||
|creator|Contact()|GroupCreatedUser|
|members|List[Contact()]|GroupMembers|
|invitee|List[Contact()]|InvitingUsers|
|notificationDisabled|False|True/False|

## groupPreference
|Key|Value|Note|
|:---:|:---:|:---:|
|invitationTicket|None|(str maybe Ticket when you made GroupURL)|
|favoriteTimestamp|None|(int maybe TimeStamp that you favorited group)|

## Note
### How to convert createdTime to datetime<br>
from datetime import datetime<br>
gr = cl.getGroup(gid)<br>
dt = datetime.fromtimestamp(int(gr.createdTime[:-3])))<br>
print("GroupCreatedTime : %s"%(dt))
