questions = ["1. Former Australian captain Mark Taylor has had several nicknames over his playing career. Which of the following was NOT one of them", 
"2 . Which was the 1st non Test playing country to beat India in an international match" , 
"3 . Track and field star Carl Lewis won how many gold medals at the 1984 Olympic games" ,
 "4 . Which county did Ravi Shastri play for",
 "5 . Who was the first Indian to win the World Amateur Billiards title",
 "6 . Who is the first Indian woman to win an Asian Games gold in 400m run",
 "7. Which two counties did Kapil Dev play",
 "8. When was Amateur Athletics Federation of India established" , 
 "9. Who did Stone Cold Steve Austin wrestle at the 1998 edition of Over the Edge",
 "10. Ricky Ponting is also known as what",
 "11. How long are professional Golf Tour players allotted per shot",
 "12. Which NBA player scored 8 points in the final 7 seconds of a game to lead his team to victory",
 "13. The ratio of width of our National flag to its length is",
 "14. Rabindranath Tagore's 'Jana Gana Mana' has been adopted as India's National Anthem. How many stanzas of the said song were adopted",
 "15. Natya - Shastra the main source of India's classical dances was written by"]
first_options = ["0. Tubby" , "0. Canada" , "0. Two" , "0. Leicestershire" , "0. Geet Sethi" , "0. M.L.Valsamma" , "0. Northamptonshire & Worcestershire" , "0. 1936" , "0. Cactus Jack" , "0. The Rickster" , "0. 45 seconds" ,"0. Baron Davis" , "0. 3:5" , "0. Only the first stanza" , "0. Nara Muni"]
second_options = ["1. Stodge" , "1. Sri Lanka" , "1. Three" , "1. Glamorgan" , "1. Wilson Jones" , "1. P.T.Usha" , "1. Northamptonshire & Warwickshire" , "1. 1946" , "1. Mankind" , "1. Ponts" , "1. 25 seconds" , "1. Kevin Garnett" , "1. 2:3" , "1. The whole song" , "1. Bharat Muni"]
third_options = ["2. Helium Bat" , "2. Zimbabwe" , "2. Four" , "2. Gloucestershire" , "2. Michael Ferreira" , "2. Kamaljit Sandhu" , "2. Nottinghamshire & Worcestershire" , "2. 1956" , "2. Dude Love" , "2. Ponter" , "2. 1 minute" , "2. Stephon Maurbury" , "2. 2:4" , "2. Third and Fourth stanza" , "2. Abhinav Gupt"]
fourth_options = ["3. Stumpy" , "3. East Africa" , "3. Eight" , "3. Lancashire" , "3. Manoj Kothari" ,"3. K.Malleshwari" , "3. Nottinghamshire & Warwickshire" , "3. 1966" , "3. Mick Foley" , "3. Punter" , "3. 2 minutes" , "3. Reggie Miller" , "3. 3:4" , "3. First and Second stanza", "3. Tandu Muni"]
all_options = [first_options , second_options , third_options , fourth_options]
correct_answers = 0
ans_key = [3 , 1 , 2 , 1 , 1 , 3 , 0 , 1 , 2 , 3 , 0 , 3 , 1 , 0, 1]
winer_price = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,250000,5000000,10000000]
print ans_key
answers_list = []
listlen = len(questions)
i = 0
sum = 0
while i < listlen:
      print questions[i] ,"-", len(questions[i])
      print first_options[i]
      print second_options[i]
      print third_options[i]
      print fourth_options[i]
      ans = (raw_input(" enter correct answers "))
      ans = int(ans)
      answers_list.append(ans)
      if ans_key[i] == ans:
      	 correct_answers = correct_answers + 1
         print "Congrats! Aapka answer sahi " , winer_price[i] , "winer price aapko mila hai" , correct_answers , "answer sahi hey aapka"
         sum = winer_price[i] 
         
         if i == 4:
          	 print "Congrats! Aapka padaav pura ho gaya hai."
         elif i == 9:
          		print "Congrats! Aapka doosra padaav pura ho gaya hai."
         elif i == 14:
          		print "Congrats! Aap ek crore rupye jeet gaye hai." 
      else:
	      print "Aap KBC haar chuke hai" , sum , "winer price aapko mila hai"
	      break   
      i = i + 1
