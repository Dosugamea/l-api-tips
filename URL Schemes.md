## List
|Detail(EN)|Detail(JP)| URL Scheme |
|:-----------:|:------------:|:------------:|
|Open TimelinePost|タイムライン投稿を開く|line://home/post?userMid=[userMID]&postId=[postID]|
|Open GroupPost|グループ投稿を開く|line://group/home/posts/post?homeId=[groupID]&postId=[postID]|
|Open GroupAlbum|グループアルバムを開く|line://group/home/albums/album?albumId=[albumID]&homeId=[groupID]|
|Join Group<br/>Open Group|グループに参加する<br/>グループを開く|line://ti/g/[GroupTicket]|
|Add User<br/>Open TalkRoom|友達登録する<br/>トークルームを開く|line://ti/p/[UserTicket]|
|Jump to Message|メッセージに飛ぶ|line://nv/chatMsg?chatId=[groupID]&messageId=[MessageID]|
|Share message|メッセージを共有する|line://msg/text/[URL_Encoded_Message]|
|Open the open user's Timeline|開いたユーザーの<br/>タイムラインを開く|line://ch/1341209850|

## Note
  * Post ID
    * It can get from copy link (WebTimeline Link)<br/>
      [Example]<br/>
      https://timeline.line.me/post/_dXjcwMbh_r0mL7Pwn9ptxi0nzizxTJi2H9TRL-c/1137352897406010950<br/>
      PostID is 1137352897406010950
  * Jump to Message
    * It can be used only in same group.<br/>
      Can't use from outside.
    * It can use all message type.<br/>
      Not only text.
  * Share Message
    * How to add new line is [here](https://rdlabo.jp/web_app-214.php) 
  * Scheme List
    * For official bots are in [here](https://developers.line.me/en/docs/messaging-api/using-line-url-scheme/)
      * Sadly line://oaMessage/{LINE_id}/?{text_message} can't use to normal user.
    * Some other schemes are in [here](https://uragadget.net/line/url_scheme_list)
