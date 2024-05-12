import pyautogui as pg
from PIL import ImageGrab  # 导入ImageGrab模块，用于截取屏幕图像
import numpy as np  # 导入numpy模块，用于处理图像数据   
from skimage.metrics import structural_similarity as ssim #图片相似度比较算法
import time
import pyperclip 
import io
import cv2
import sys
import os

def run():
    global num
    num = int(pg.prompt(text='请输入想要刷的遗器本',title='PyAutoGUI消息框',default='9'))
    pg.hotkey("win","q")
    time.sleep(1)
    pyperclip.copy("应用: 崩坏：星穹铁道")
    pg.hotkey("ctrl","v")
    time.sleep(1)
    pg.press("enter")
    pg.press("enter")
    pg.press("esc")
   
    ##启动！启动启动全都启动！！！
    
    size_ = pg.size()
    #print(size_)
    global scal_x, scal_y
    scal_x = size_[0]/3840
    scal_y = size_[1]/2160
    
    loc_x, loc_y = arr[0]
    #start_x, start_y = pg.position()
    #print(start_x, start_y)
    #pg.moveTo(start_x, start_y)
    time.sleep(3)
    pg.click(loc_x, loc_y)
    
    start =time.process_time()
    moniter("./picture/start.png")      #等待直到开始界面
    end = time.process_time()
    if ((end - start) < 15):    #判断是否识别过短出错了，根据每个人载入时间而定
        time.sleep(5)
    print("Honkai: Star Rail, START!")
    pg.click()

    time.sleep(10)    
    pg.click()    
    time.sleep(5)
    pg.click()
    time.sleep(5)
    task()

def task():     #执行自动化任务
    pg.press("space")
    time.sleep(1)
    print("login sucess")
    time.sleep(1)
    
    yiqi()
    time.sleep(3)
    #meiri()
    time.sleep(3)
    shutdown()


def zhinan():    #这个是指南
    pg.press("esc")
    time.sleep(2)
    loc_x, loc_y = arr[1]
    pg.click(loc_x, loc_y) 
    time.sleep(1)
    print("zhinan succeed")


def yiqi(repeat = 6):        #这个是遗器，n代表从上往下数第几个遗器本（从1开始）
    zhinan()

    loc_x, loc_y = arr[2]
    pg.click(loc_x, loc_y)  #这个是副本
    time.sleep(1)
    loc_x, loc_y = arr[3]
    pg.click(loc_x, loc_y)  #这个是遗器本
    time.sleep(1)
    
    loc_x, loc_y = arr[4]
    pg.moveTo(loc_x, loc_y)  #这个是第一个遗器
    time.sleep(1)
    
    t = num    
    dy = arr[5][1] - arr[4][1]      #计算两个相邻副本的y值差
    while (t>1):
        pg.mouseDown()
        pg.move(0, -(dy+25), 1)     #由于滚轮有误差，(这里25需要微调)
        time.sleep(1)
        pg.mouseUp()
        pg.moveTo(loc_x, loc_y)
        t-=1
    if (num > 6):  
        pg.moveTo(loc_x, (arr[6][1]-(9-num)*dy))    #从最后一个副本的坐标向上减
    
    time.sleep(1)
    pg.click()
    time.sleep(5)
    
    loc_x, loc_y = arr[7]
    pg.moveTo(loc_x, loc_y)  #副本入口
    pg.click()
    time.sleep(2)
    pg.click()
    
    loc_x, loc_y = arr[8]    
    pg.moveTo(loc_x, loc_y)
    while (repeat>1):       #再来一次
        time.sleep(50)
        moniter('./picture/yiqi1.png')
        pg.click(loc_x, loc_y)
        repeat -= 1
        if (diff('./picture/yiqi2.png') >0.85):
            break;   

    loc_x, loc_y = arr[9]
    pg.moveTo(loc_x, loc_y)
    pg.click()
    time.sleep(1)
    pg.click()
    time.sleep(1)

def zhuzhan():      #这个是助战
    pg.press('esc')
    time.sleep(1)
    loc_x, loc_y = arr[16]
    pg.click(loc_x, loc_y)   #…按钮
    time.sleep(1)
    loc_x, loc_y = arr[17]
    pg.click(loc_x, loc_y)  #漫游签证
    time.sleep(1)
    loc_x, loc_y = arr[18]
    pg.click(loc_x, loc_y)  #助战奖励
    time.sleep(1)
    loc_x, loc_y = arr[19]
    pg.click(loc_x, loc_y)  #退出
    time.sleep(1)
    pg.click()          
    time.sleep(1)
    pg.click()        #退回游戏界面

def weituo():       #这个是委托
    pg.press('esc')
    time.sleep(1)
    loc_x, loc_y = arr[13]
    pg.click(loc_x, loc_y)      #委托
    time.sleep(1)
    loc_x, loc_y = arr[14]
    pg.click(loc_x, loc_y)      #收取委托
    time.sleep(1)
    loc_x, loc_y = arr[15]      #再次派遣
    pg.click(loc_x, loc_y)
    time.sleep(1)  
    pg.press('esc')
    time.sleep(1)
    pg.press('esc')        #退回游戏界面  
    
def meiri():        #这个是每日奖励
    zhinan()
    loc_x, loc_y = arr[10]  #打开每日
    pg.click(loc_x, loc_y)
    time.sleep(1)
    loc_x, loc_y = arr[11]
    pg.moveTo(loc_x, loc_y)     #点击每日任务
    time.sleep(1)
    for i in range(6):
        pg.click()
        time.sleep(1)
    loc_x, loc_y = arr[12]  #点击每日奖励
    pg.click(loc_x, loc_y)
    time.sleep(1)
    pg.press('esc')
    time.sleep(1)
    pg.press('esc')        #退回游戏界面

def shutdown():
    pg.hotkey("alt", "f4")
    
    
    

    
    
    
def loc( file_name):
    return pg.locateOnScreen(file_name)

def moniter(file_name,similar = 0.85, flag = True): #flag 为 true 时判断何时相同， 为false时判断何时不同
    
    #region = (0, 0, self.size[0], self.size[1])  # 示例：左上角(0, 0)，右下角(800, 600)
    # 初始化截图
    #shot = ImageGrab.grab(bbox=region)  # 截取指定区域的屏幕图像，并赋值给shot变量

    while True:          
        similarity = diff(file_name)
        print('similarity: ',similarity)
        if (flag and similarity>similar) or ((not flag) and similarity<similar):
            return
        time.sleep(0.5) 
        
def diff(file_name):        #判断当前屏幕与目标图片相似度
    coef = 0
    shot = ImageGrab.grab()
    shot.save("./tmp/screen.jpg")
    screen = cv2.imread("./tmp/screen.jpg")
    target = cv2.imread(file_name)
    target = cv2.resize(target, (screen.shape[1], screen.shape[0]), interpolation=cv2.INTER_AREA)
    
    gray_target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    coef, _ = ssim(gray_target, gray_screen, full=True)
    return coef

if (__name__ == "__main__"):
    arr = np.load('position.npy')       #读取各个关键坐标
    run();
    
    #test
    time.sleep(3)
    #print(diff('./picture/yiqi2.png'))
    #weituo()
    #zhuzhan()