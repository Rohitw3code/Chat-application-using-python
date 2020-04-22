#########_____USER 02_____##########
#connection will be started by the user 1

from firebase import firebase
FBConn = firebase.FirebaseApplication('https://prun-d5ea2.firebaseio.com/', None)
print('start chating with user 1')
receive=FBConn.get('/c7/use2/',None)
try:
   user2_chat_no=len(receive)+1
except:
   user2_chat_no=1
while True:
   noconnect=True
   while noconnect:
      try:
         receive=FBConn.get('/c7/use1/',None)
         for chat in receive:
            for receive_messg in receive[chat]:
               if receive[chat][receive_messg]==user2_chat_no:
                  print('friend : ',receive_messg)
                  noconnect=False
      except:
         continue
   send=str(input('you : '))
   use2={
      send:user2_chat_no
      }
   
   result = FBConn.post('/c7/use2/',use2)      
   user2_chat_no=user2_chat_no+1
   
               




   
