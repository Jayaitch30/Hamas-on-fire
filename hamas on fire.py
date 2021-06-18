import turtle
import winsound
import time

gaza = turtle.Screen()
gaza.bgpic("start.gif")
idf = turtle.Turtle()
hamas = turtle.Turtle()
exp = turtle.Turtle()
logo = turtle.Turtle()
attack = turtle.Turtle()
score = turtle.Turtle()
speed = 1

def init():
    winsound.PlaySound('music.wav',winsound.SND_ASYNC)
    gaza.setup(1000, 800)
    gaza.title('Hamas on fire game')
    score.speed(100000)
    score.penup()
    score.goto(-400, 350)
    exp.hideturtle()
    idf.hideturtle()
    hamas.hideturtle()
    logo.hideturtle()
    attack.hideturtle()
    score.hideturtle()
    hamas.penup()
    idf.penup()
    idf.speed(20)
    hamas.speed(20)
    hamas.left(180)
    gaza.addshape("explosion.gif")
    gaza.addshape("rocket.gif")
    gaza.addshape("terrorist.gif")
    gaza.addshape("logo.gif")
    gaza.addshape("terrorist1.gif")
    gaza.addshape("terrorist2.gif")
    gaza.addshape("rocket2.gif")
    gaza.addshape("plane.gif")
    gaza.addshape("tank.gif")
    gaza.addshape("tank_rocket.gif")
    gaza.addshape("plane_bombs.gif")
    gaza.addshape("plane_exp.gif")
    gaza.addshape("tank_exp.gif")
    exp.shape('explosion.gif')
    logo.shape("logo.gif")
    logo.penup()
    logo.goto(-370, -200)
    exp.penup()
    attack.penup()
    idf.goto(0, constant['max_height'])


constant = {
    'max_right' : 450,
    'max_left' : -450,
    'max_height' : 350,
    'min_height' : -350,
    'max_score': 1000,
    'min_score': 900,

}
running = True
def setup():
    idf.speed(20)
    idf.setpos(0,constant['max_height'])
    hamas.speed(20)
    hamas.speed(100000)
    hamas.goto(350, constant['min_height'])
    gaza.bgpic("ilan.gif")
    idf.showturtle()
    hamas.showturtle()
    logo.showturtle()
def enemyshop():
    if gaza.bgpic() == "ilan.gif" and idf.ycor() == constant['max_height'] or gaza.bgpic() == "start.gif" and idf.ycor() == constant['max_height']: #   אם לוחצים enter זה יעביר לenemy shop רק אם זה על המסך הנכון והפצצה לא יורדת
        gaza.bgpic("enemyshop.gif")
        hamas.hideturtle()
        idf.hideturtle()
        def buttonclick(x, y):
            if x > 85 and x < 312 and y > 55 and y < 245 and gaza.bgpic() == "enemyshop.gif":#לחיצה על כפתור
                hamas.shape("terrorist.gif")
                rocketshop()
            elif x > -295 and x < -74 and y > 55 and y < 245 and gaza.bgpic() == "enemyshop.gif":#לחיצה על כפתור
                hamas.shape("terrorist2.gif")
                rocketshop()
        gaza.onscreenclick(buttonclick, 1)
        gaza.listen()
def rocketshop():
    gaza.bgpic("rocketshop.gif")
    def buttonclick2(x, y):
        count = 0
        if idf.shape() == "rocket2.gif" or idf.shape() == "rocket.gif":#לבדוק אם הוא בחר כבר צורה בפעם הקודמת כדי לא לקבל error
            count = 1
        if x > 85 and x < 312 and y > 55 and y < 245 and gaza.bgpic() == "rocketshop.gif":#לחיצה על כפתור
            idf.shape("rocket2.gif")
            if count == 1:
                setup()
            else:
                game_function()
        elif x > -295 and x < -74 and y > 55 and y < 245 and gaza.bgpic() == "rocketshop.gif":#לחיצה על כפתור
            idf.shape("rocket.gif")
            if count == 1:
                setup()
            else:
                game_function()
    gaza.onscreenclick(buttonclick2, 1)
    gaza.listen()

def game_function():
    setup()
    speed = 10
    while running:#כל עוד המשחק רץ הכל פועל ברגע שלוחצים ESC המשחק מפסיק
        def kL():
            if idf.ycor() == constant['max_height']:#שהפצצה לא תזוז באמצע נחיתה ותזוזה שמאלה בליצה על חץ שמאלי
                if idf.xcor() != constant['max_left']:
                    idf.goto(idf.xcor()-10, idf.ycor())

        def kR():
            if idf.ycor() == constant['max_height']:#שהפצצה לא תזוז באמצע נחיתה ותזוזה שמאלה בליצה על חץ ימני
                if idf.xcor() != constant['max_right']:
                    idf.goto(idf.xcor() + 10, idf.ycor())

        def kSpace():
            idf.speed(2)
            while idf.ycor() == constant['max_height']:#הפצצה תיפול רק אם היא בגובה המקסימלי
                bombdrop()
        def kr():
            if idf.ycor() == constant['max_height'] or idf.ycor() <= constant['min_height'] + 1:#ניתן לעשות ריסטרט אם הפצצה למעלה או למטה ולא באמצע נחיתה ולאחר פעולת הטנק עדיין יהיה אפשר לשנות מתקפה ולא לעשות ריסטרט ישר
                if gaza.bgpic() == 'perfect.gif' or gaza.bgpic() == 'tank_mission.gif' or gaza.bgpic() == 'plane_mission.gif':#אם נעשה מקס סקור יש אופציה למתקפות מיוחדות
                    idf.hideturtle()
                    hamas.hideturtle()
                    score.clear()
                    gaza.bgpic("attacks.gif")
                    winsound.PlaySound('music.wav',winsound.SND_ASYNC)
                    def buttonclick3(x, y):
                        if x > 85 and x < 312 and y > 55 and y < 245 and gaza.bgpic() == "attacks.gif":#לחיצת כפתור
                            attack.shape("plane.gif")
                            plane_attack()
                        elif x > -295 and x < -74 and y > 55 and y < 245 and gaza.bgpic() == "attacks.gif":#לחיצת כפתור
                            attack.shape("tank.gif")
                            tank_attack()
                        else:
                            if gaza.bgpic() == "attacks.gif":
                                restart()
                    gaza.onscreenclick(buttonclick3, 1)
                    gaza.listen()
                else:
                    if gaza.bgpic() == 'ilan2.gif' or gaza.bgpic() == 'close.gif' or gaza.bgpic() == 'ilan.gif' and idf.ycor() == constant['max_height']:# שלא יהיה ריסטרט באמצע נחיתה או בדיוק בסוף
                        restart()
        def plane_attack():
            gaza.bgpic("ilan.gif")
            current_shape = idf.shape()
            hamas.goto(0, constant['min_height'])
            hamas.showturtle()
            attack.speed(10000)
            attack.goto(400, constant['max_height'])
            attack.speed(3)
            attack.showturtle()
            while attack.xcor() > idf.xcor():
                attack.goto(attack.xcor()-3, attack.ycor()-1)
            idf.goto(0, attack.ycor()-20)
            idf.shape("plane_bombs.gif")
            idf.showturtle()
            exp.shape("plane_exp.gif")
            bombdrop()
            attack.goto(-600, constant['max_height'])
            attack.hideturtle()
            idf.shape(current_shape)
            exp.shape("explosion.gif")
            hamas.hideturtle()
            gaza.bgpic("plane_mission.gif")
            winsound.PlaySound('plane_music.wav', winsound.SND_ASYNC)
        def bombdrop():
            winsound.PlaySound('bombdrop.wav', winsound.SND_ASYNC)
            if attack.shape() == 'plane.gif':
                idf.goto(idf.xcor(), constant['min_height'] - 1)
            else:
                idf.goto(idf.xcor(), constant['min_height'])
            if exp.shape() == "plane_exp.gif":
                exp.goto(idf.xcor(), -330)
            else:
                exp.goto(idf.xcor(), -300)
            idf.hideturtle()
            exp.showturtle()
            time.sleep(1.5)
            exp.hideturtle()
        def tank_attack():
            gaza.bgpic("ilan.gif")
            hamas.goto(0, constant['min_height'])
            hamas.showturtle()
            current_shape2 = idf.shape()
            idf.shape("tank_rocket.gif")
            exp.shape("tank_exp.gif")
            attack.speed(10000)
            attack.goto(1200, constant['min_height'])
            attack.speed(2)
            attack.showturtle()
            attack.goto(380, constant['min_height'])
            idf.goto(400,constant['min_height'])
            idf.showturtle()
            idf.goto(30, -351)
            exp.speed(10000)
            exp.goto(0, constant['min_height'])
            idf.hideturtle()
            exp.showturtle()
            winsound.PlaySound('tank_bomb.wav', winsound.SND_ASYNC)
            time.sleep(1.5)
            exp.hideturtle()
            exp.shape("explosion.gif")
            idf.shape(current_shape2)
            attack.hideturtle()
            hamas.hideturtle()
            gaza.bgpic("tank_mission.gif")
            winsound.PlaySound('tank_music.wav', winsound.SND_ASYNC)

        def restart():
            idf.hideturtle()
            hamas.hideturtle()
            score.clear()
            exp.hideturtle()
            gaza.bgpic("ilan.gif")
            winsound.PlaySound('music.wav', winsound.SND_ASYNC)
            setup()
            if hamas.shape() == 'terrorist1.gif':
                hamas.shape('terrorist.gif')
            else:
                hamas.speed(100000)
                hamas.goto(350, constant['min_height'])

        gaza.listen()
        def shape_change():
            if hamas.shape() == "terrorist.gif" and hamas.xcor() <= -constant['max_left']:#ישנה את התמונה לתמונת הפוכה כדי להתאים לכיוון התזוזה
                hamas.shape("terrorist1.gif")
            if hamas.shape() == "terrorist1.gif" and hamas.xcor() >= constant['max_right']:
                hamas.shape("terrorist.gif")
        while idf.ycor() != constant['min_height']:
            hamas.goto(hamas.xcor() - speed, hamas.ycor())
            if hamas.xcor() == constant['max_left']:#זז בכיוון ההפוך כאשר מגיע למיקום מקסימלי
                shape_change()
                hamas.left(180)
                speed = -speed
            if hamas.xcor() == constant['max_right']:
                shape_change()
                hamas.left(180)
                speed = -speed
            if running == False:
                return gaza.bye()
            gaza.onkeypress(kL, "Left")
            gaza.onkeypress(kR, "Right")
            gaza.onkey(kSpace, "space")
            gaza.onkeyrelease(kr, "r")
        def score_calc():
            if constant['max_score'] - abs(idf.xcor() - hamas.xcor()) >= constant['min_score'] and constant['max_score'] - abs(idf.xcor() - hamas.xcor()) < constant['max_score']:#מחשב את התוצאה לפי הנתונים ומבצע את הפעולה המתאימה
                idf.hideturtle()
                hamas.hideturtle()
                score.write("points: {}".format(constant['max_score'] - abs(idf.xcor() - hamas.xcor())), align="center",font=("Comic Sans MS", 24, "normal"))
                gaza.bgpic("ilan2.gif")
                winsound.PlaySound('almost.wav', winsound.SND_ASYNC)
            elif constant['max_score'] - abs(idf.xcor() - hamas.xcor()) < constant['min_score']:
                idf.hideturtle()
                hamas.hideturtle()
                score.write("points: {}".format(constant['max_score'] - abs(idf.xcor() - hamas.xcor())), align="center",font=("Comic Sans MS", 24, "normal"))
                gaza.bgpic("close.gif")
                winsound.PlaySound('bambam.wav', winsound.SND_ASYNC)
            else:
                idf.hideturtle()
                hamas.hideturtle()
                score.write("points: {}".format(constant['max_score'] - abs(idf.xcor() - hamas.xcor())), align="center",font=("Comic Sans MS", 24, "normal"))
                exp.hideturtle()
                winsound.PlaySound("hatikva", winsound.SND_ASYNC)
                gaza.bgpic("perfect.gif")

        if idf.ycor() == constant['min_height']:#בשביל שיתבצע החישוב והלולאה לא תמשיך לחשב את התוצאה
            score_calc()
            idf.goto(idf.xcor(), constant['min_height'] + 1)
    return gaza.bye()



def kESC():
    if gaza.bgpic() == 'start.gif' or gaza.bgpic() == 'enemyshop.gif' or gaza.bgpic() == 'attacks.gif' or gaza.bgpic() == 'rocketshop.gif':#במידה והמשחק על אחד המסכים האלה היציאה תהיה רגילה ואם לא צריך לסגור את לולאת המשחק קודם.
        gaza.bye()
    else:
        global running
        running = False


init()
gaza.onkey(kESC, "Escape")
gaza.onkey(enemyshop, "Return")
gaza.listen()
gaza.mainloop()