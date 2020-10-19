text = "X-DSPAM-Confidence:    0.8475"
a =text.find(':')
p=text[a+2:]
v=float(p)
print(v)
value: 'Chat',
                      child: Container(
                        child: Row(
                          children: <Widget>[Text('Chat')],
                        ),
                      )),
                ],
                onChanged: (value) async {
                  if (value == "Chat") {
                    final userData = await FirebaseAuth.instance.currentUser();

                    await Firestore.instance
                        .collection("InfluencerChats")
                        .document(
                            userData.uid + "-" + widget.influencer.userName)
                        .get()
                        .then((value)async {
                              if (value.data.containsKey('AdvertiserBlocked'))
                                {
                                  Navigator.of(context).push(MaterialPageRoute(
                                      builder: (ctx) => ChatPage(
                                            chatId: userData.uid +
                                                "-" +
                                                widget.influencer.userName,
                                            influencerId:
                                                widget.influencer.userName,
                                            advertiserId: userData.uid,
                                          )));
                                }
                              else if (value.data['InfluencerBlocked']==true)
                                {
simplestDialogBox(context, 'This InfluencerBlocked You');
                                }
