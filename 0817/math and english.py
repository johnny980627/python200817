mathscore = int(input("請輸入數學成績:"))
engscore = int(input("請輸入英文成績:"))
if mathscore >= 0 and mathscore <=100 and engscore >= 0 and engscore <=100:
    if mathscore >=90 and engscore >=90:
        print("有獎品!")
    elif mathscore <60 and engscore <60:
        print("有處罰!")
    elif  mathscore <60 or engscore <60:
        print("再加油!")
else:
    print("請輸入正確成績")