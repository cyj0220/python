import pygame as p

p.init() #파이게임 초기화

screen = p.display.set_mode([800,800]) # 해상도설정 -  [가로 , 세로 ]

p.display.set_caption("이런 XXXXXX") #게임창 제목


playing = True

while playing:
    for event in p.event.get(): #사용자가 뭘 눌렀는지 감지
        if event.type == p.QUIT: #파이게임 x 버튼을 누르면
            p.quit() #파이게임 창을 끄는 명령어
            quit()
            playing = False
    screen.fill([255,255,255])
    #선 만들기
    p.draw.line(screen,[0,255,0],[100,100],[200,200],10)
    #               ([스크린],[선색깔],[시작좌표],끝좌표   ,선두깨)
    #다각형 그리기 
    p.draw.polygon(screen,[0,0,0],[[350,100],[350,200],[450,150],[450,50]],5)
    p.display.flip() #화면 업데이트 
    


    

