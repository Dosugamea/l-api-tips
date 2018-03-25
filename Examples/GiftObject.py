'''
<Send Gift Object>
  This can send Gift to specify place.
  productId can be got from LINE GIFT(actually have to pay)
  Used productId can be sent, but can't get actually.
'''

cl = LINE(authtoken)
to = "SEND_TO(gid/mid)"

# This productId is Koala’s March(コアラのマーチ)(Japanese snack)
productId = '1131ccc5-2a34-4c5a-9536-73041f72767f'
cl.sendGift(to,productId)
