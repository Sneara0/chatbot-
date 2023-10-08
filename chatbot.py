qna={
    'helloo':'hi',
    'What is your name':'my name is sneara',
    'How old are you':'iam 23 years old'


}
while True:
   try:
       ques = input()
       if   ques == 'quit':

         break
       else:
       print(qna[ques])
       except:
       print("i don't know")