import json

'''
<Set custom music to musicProfile>

　MusicID can get from LINE music share link.
　For example,
　https://music.line.me/launch?target=track&item=mb00000000011e07d4&subitem=mt000000000a609032&cc=JP&from=tw
　This link's subitem, mt000000000a609032 is the MusicID.

　Original Image Size is 256x256,
　But it auto scale it, so we don't have to mind it.

　Sure, URL scheme can be used for url.
'''

music = {
	"id": "MusicID",
	"name": "Music Title",
	"artistName": "Music SubTitle",
	"imageUrl": "Icon Image URL",
	"url": "URL to be opened when touching music",
	"type": "mt",
	"country": "JP"
}

profile = client.getProfile()
profile.musicProfile = json.dumps(music)
client.updateProfile(profile)
