import json
from akad.ttypes import Message

'''
<Send Custom Music>
  Really Similar to Profile Music
　I didn't check a-* because I don't have iPhone.
'''
cl = LINE(authtoken)
my_music = Message()
my_music.to = "SEND_TO(gid/mid)"
my_music.contentType = 19
sl.contentMetadata={
  'text': 'songTitle',
  'subText': 'artistName',
  'id': 'mt000000000a7546d5',
  'previewUrl': 'Thumbnail to be displayed',
  'linkUri': 'Other Link to be opened',
  'i-linkUri': 'iPhone Link to be opened(?)',
  'a-linkUri': 'Android Link to be opened(?)',
  'i-installUrl': 'iPhone LINE_Music AppInstall_Link(?)',
  'a-installUrl': 'Android LINE_Music AppInstall_Link(?)',
  'a-packageName': 'jp.linecorp.linemusic.android',
  'type': 'mt',
  'countryCode': 'JP',
  'ORGCONTP': 'MUSIC'
  }
#LINE-PY's sendMessage is optimized for text, so have to send by Client".talk."
cl.talk.sendMessage(0,msg)
