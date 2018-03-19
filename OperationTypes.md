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
