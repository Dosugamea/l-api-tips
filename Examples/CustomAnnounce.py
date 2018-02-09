from akad.ttypes import ChatRoomAnnouncementContents

'''
<Set Custom Announce>
  It can set text,link,icon,and lock.
  (displayFields is unknown. what can do by it?)

  For Type
    0 -> Normal  1 -> Lock
    At Lock,
    It can't delete from user
    And Icon changes to Note.
  For text
    Normally Message to jump is set.
    It is displayed Text
    Can't make new line, it doesn't show.
  For link
    Normally "Jump to message" is set.
    It is opened link when tap.
    URL and Scheme can be used.
  For thumbnail
    Normally None is set.
    It is direct link to image.
    May be 128x128 or 256x256 is best? (Need more infos!)
  For displayFields
    Normally 5 is set.
    It set text height but I don't think it's useful when change.
'''

gid = "GroupID or UserID"
type = 0
customText = "Hello World"
customLink = "https://google.com"
customThumbnail = "http://dp.lnwfile.com/_/dp/_raw/i4/40/np.png"

an = ChatRoomAnnouncementContents(displayFields=5,text=customText,link=customLink,thumbnail=customThumbnail)
cl.createChatRoomAnnouncement(gid,type,an)
