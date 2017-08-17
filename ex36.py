# coding=utf-8

hp = 100


def start():
    print
    print
    print "公主被怪兽抓走啦！！！你快去救她！\n"
    print "选个方法去找怪兽吧\n"
    print "A.一路小跑"
    print "B.骑大飞龙过去"
    way = raw_input(">")
    if way == "A":
        print "你在路上被兽人抓起来吃掉了"
    elif way == "B":
        print "你到了城堡啦！！恭喜发财！\n"
        open_door()
    else:
        print("连选择题都不会还想救公主？")



def open_door():
    print "你要怎么打开城堡的大门啊？\n"
    print "A.地上有钥匙，捡起来开门\n"
    print "B.用脚踹开\n"
    print "C.爬窗进去\n"
    way = raw_input(">")
    if (way == "A"):

        print "哇，门打开了，一个怪兽正在睡觉\n"
        monster()
    elif way == "B":
        print "惊动了守卫！\n"
        fight()
        print "哇，门打开了，一个怪兽正在睡觉\n"
        monster()
    elif way == "C":
        print "你摔死了"
        exit(0)
    else:
        print "傻了啊？"
        exit(0)


def monster():
    print "地上有好多武器，还有很多食物。"
    print "你打算干啥？\n"
    print "A.拿起大砍刀就去看怪兽\n"
    print "B.好饿，我先吃饱再说\n"
    monster_wakeup = False
    while True:
        way = raw_input(">")
        if way == "A":
            fight()
        elif way == "B" and not monster_wakeup:
            print "你吃的真大声，怪兽被你吵醒了，朝你望过来\n"
            monster_wakeup = True
            print "你该怎么办？\n"
            print "A.好慌！跑啊！\n"
            print "B.把看起来最好吃的肉丢到角落去勾引怪兽\n"
        elif way == "A" and monster_wakeup:
            print "你滑到摔死了"
        elif way == "B" and monster_wakeup:
            print "很机智哦！上楼吧！\n"
            find_princess()
        else:
            print "快选啊，不然公主死了"
          


def fight():
    global hp
    hp = hp - 50
    print "当前生命值为：",hp
    if hp > 0:
        print "生命减少50"
    else:
        print "生命为0.你被杀了"
        exit(0)


def find_princess():
    print "往左还是往右,输入L或者R\n"
    how=raw_input(">")
    if how=='L':
        print "遇到陷阱！\n"
        fight()
    elif how == 'R' :
        print "找到公主了！\n"
        back()
    else:
        print "玩到这里还乱选？？？"
        print "PH=0 GG"
        exit(0) 
def back():
    print "你怎么回去好？"
    print "A.骑马 B.骑龙\n"
    go=raw_input(">")
    if go=="A":
        print "和公主过上了幸福的生活"
    elif go == "B":
        print "公主太漂亮，龙造反了，你跟他打了起来\n"
        fight()
    else:
        print "你牛逼！你赢了！"

start()
