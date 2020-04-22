########____USER 01_____############

from firebase import firebase
FBConn = firebase.FirebaseApplication('https://prun-d5ea2.firebaseio.com/', None)
print('start chating with user 2')

receive=FBConn.get('/c7/use1/',None)
try:
   user1_chat_no=len(receive)+1
except:
   user1_chat_no=1
while True:
   send=str(input('you : '))
   use1={
      send:user1_chat_no
      }   
   result = FBConn.post('/c7/use1/',use1)
   noconnect=True
   while noconnect:
      try:
         receive=FBConn.get('/c7/use2/',None)        #receive={M1:{'hi':1},M2:{'hey':2},M3:{'bye':3}}
         for chat in receive: #chat={M1,M2,M3}
            for receive_messg in receive[chat]:#receive[chat]={{'hi':1},{'hey':2},{'bye':3}} , receive_messg ={'hi','hey','bye'}
               if receive[chat][receive_messg]==user1_chat_no:#receive[chat][receive_messg]={1,2,3}
                  print('friend : ',receive_messg)
                  noconnect=False
      except:
         continue
   user1_chat_no=user1_chat_no+1
