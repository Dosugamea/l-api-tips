# OperationTypes
Memo of LINE operations.

## 0:END_OF_OPERATION
 Operation End
 
## 2:NOTIFIED_UPDATE_PROFILE
When Friend Profile Updated.

| Type | Value | Note |
|:---:|:-----:|:-----:|
|param1|'u2268852ba9a80e13dXXXXXXXXXXXXXXX'|mid|
|param2|'16'|?|
|param3|'{}' |?|
|message|None||

## 5:NOTIFIED_ADD_CONTACT
Happen when Add as Contact.
 
| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|'u2268852ba9a80e13dXXXXXXXXXXXXXXX'|mid(Added User)|
|param2|None||
|param3|None||
|message|None||

## 8:NOTIFIED_RECOMMEND_CONTACT
Happen when Add as Contact.
 
| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|'u2268852ba9a80e13dXXXXXXXXXXXXXXX'|mid(Added User)|
|param2|'0'|?|
|param3|None||
|message|None||

## 9:CREATE_GROUP
Happen when Create Group(by self)
 
| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 10:UPDATE_GROUP
Happen when Group Update(by self)
 
| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 11:NOTIFIED_UPDATE_GROUP
Happen when Group Updated
 
| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 12:INVITE_INTO_GROUP
Happen when Invite anyone to group.(by self)

| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 13:NOTIFIED_INVITE_INTO_GROUP
Happen when someone invited you to group.<br>
Or when someone invited other in Group that you joined.<br>
(自分が招待されたとき<br>
および 自分の参加しているグループの誰かが誰かをグループに招待したとき)
 
| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 14:LEAVE_GROUP
Happen when you leave.

| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 15:NOTIFIED_LEAVE_GROUP
Happen when anyone leave from group that you joined.

| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 16:ACCEPT_GROUP_INVITATION
Happen when you join to group.

| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 17:NOTIFIED_ACCEPT_GROUP_INVITATION
Happen when someone join to group that you joined.

| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 18:KICKOUT_FROM_GROUP
Happen when you kickout someone.

| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

## 19:NOTIFIED_KICKOUT_FROM_GROUP
Happen when someone kickouted in group that you joined.

| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|||
|param2|||
|param3|||
|message|||

20:CREATE_ROOM<br>
21:INVITE_INTO_ROOM<br>
22:NOTIFIED_INVITE_INTO_ROOM<br>
23:LEAVE_ROOM<br>
24:NOTIFIED_LEAVE_ROOM

## 26:RECEIVE_MESSAGE
Happen when Recieve Message.
 
| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|'0'|gid/mid|
|param2|None|AnnounceID|
|param3|None||
|message|Message()||

## 30:RECEIVE_ANNOUNCEMENT
Happen when Announce Changed.
 
| Type | Value | Note |
|:---:|:-------:|:------:|
|param1|'u406682701b0d659deXXXXXXXXXXXXXXX'|gid/mid|
|param2|'219'|AnnounceID|
|param3|'c' |c="Created", d="Deleted"|
|message|None||

31:CANCEL_INVITATION_GROUP<br>
32:NOTIFIED_CANCEL_INVITATION_GROUP<br>
34:REJECT_GROUP_INVITATION<br>
35:NOTIFIED_REJECT_GROUP_INVITATION<br>
40:SEND_CHAT_CHECKED<br>
41:SEND_CHAT_REMOVED<br>
50:NOTIFIED_RECEIVED_CALL<br>
51:CANCEL_CALL<br>
55:NOTIFIED_READ_MESSAGE<br>
62:FRIEND_REQUEST_ACCEPTED<br>
69:UPDATE_GROUPPREFERENCE<br>
88:NOTIFIED_FRIEND_REQUEST
