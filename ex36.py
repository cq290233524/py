# coding=utf-8

hp = 100


def start():
    print
    print
    print "����������ץ�������������ȥ������\n"
    print "ѡ������ȥ�ҹ��ް�\n"
    print "A.һ·С��"
    print "B.��������ȥ"
    way = raw_input(">")
    if way == "A":
        print "����·�ϱ�����ץ�����Ե���"
    elif way == "B":
        print "�㵽�˳Ǳ���������ϲ���ƣ�\n"
        open_door()
    else:
        print("��ѡ���ⶼ���ỹ��ȹ�����")



def open_door():
    print "��Ҫ��ô�򿪳Ǳ��Ĵ��Ű���\n"
    print "A.������Կ�ף�����������\n"
    print "B.�ý��߿�\n"
    print "C.������ȥ\n"
    way = raw_input(">")
    if (way == "A"):

        print "�ۣ��Ŵ��ˣ�һ����������˯��\n"
        monster()
    elif way == "B":
        print "������������\n"
        fight()
        print "�ۣ��Ŵ��ˣ�һ����������˯��\n"
        monster()
    elif way == "C":
        print "��ˤ����"
        exit(0)
    else:
        print "ɵ�˰���"
        exit(0)


def monster():
    print "�����кö����������кܶ�ʳ�"
    print "������ɶ��\n"
    print "A.����󿳵���ȥ������\n"
    print "B.�ö������ȳԱ���˵\n"
    monster_wakeup = False
    while True:
        way = raw_input(">")
        if way == "A":
            fight()
        elif way == "B" and not monster_wakeup:
            print "��Ե�����������ޱ��㳳���ˣ�����������\n"
            monster_wakeup = True
            print "�����ô�죿\n"
            print "A.�ûţ��ܰ���\n"
            print "B.�ѿ�������óԵ��ⶪ������ȥ��������\n"
        elif way == "A" and monster_wakeup:
            print "�㻬��ˤ����"
        elif way == "B" and monster_wakeup:
            print "�ܻ���Ŷ����¥�ɣ�\n"
            find_princess()
        else:
            print "��ѡ������Ȼ��������"
          


def fight():
    global hp
    hp = hp - 50
    print "��ǰ����ֵΪ��",hp
    if hp > 0:
        print "��������50"
    else:
        print "����Ϊ0.�㱻ɱ��"
        exit(0)


def find_princess():
    print "����������,����L����R\n"
    how=raw_input(">")
    if how=='L':
        print "�������壡\n"
        fight()
    elif how == 'R' :
        print "�ҵ������ˣ�\n"
        back()
    else:
        print "�浽���ﻹ��ѡ������"
        print "PH=0 GG"
        exit(0) 
def back():
    print "����ô��ȥ�ã�"
    print "A.���� B.����\n"
    go=raw_input(">")
    if go=="A":
        print "�͹����������Ҹ�������"
    elif go == "B":
        print "����̫Ư�������췴�ˣ��������������\n"
        fight()
    else:
        print "��ţ�ƣ���Ӯ�ˣ�"

start()
