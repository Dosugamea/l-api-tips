# Message Structure
Memo of Message.<br><br>

## Base(Text Type)
|Key|Value|Note|
|:---:|:---:|:---:|
|_from|'Sent_User|Certainly User|
|to|Sent_To|Group/Room/User|
|toType|2|2=Group, 1=Room, 0=User|
|id|'7651875313444'|str MessageID|
|createdTime|1521471809391|int UnixTime|
|deliveredTime|0|maybe doesn't work|
|text|'Text_Message'|str|
|location|None||
|hasContent|False||
|contentType|0||
|contentPreview|None||
|contentMetadata|{'EMTVER': '4'}|dict|
|sessionId|0||
|chunks|None||
|relatedMessageId|None||
|messageRelationType|0||
|readCount|None||
|relatedMessageServiceCode|None||
