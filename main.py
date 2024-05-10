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
    pg.hotkey("win","q")
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
    start_x = 2470*scal_x
    start_y = 1410*scal_y
    #start_x, start_y = pg.position()
    #print(start_x, start_y)
    #pg.moveTo(start_x, start_y)
    time.sleep(3)
    pg.click(start_x, start_y)
    
    start =time.process_time()
    moniter("./picture/start.png")
    end = time.process_time()
    if ((end - start) < 15):    #判断是否识别出错了，根据每个人载入时间而定
        time.sleep(5)
    print("Honkai: Star Rail, START!")
    pg.click()
    
    time.sleep(10)
    task()

def task():     #执行自动化任务
    pg.press("space")
    time.sleep(1)
    print("login sucess")
    time.sleep(1)
    
    yiqi()
    
    meiri()
    
    over()
    
def zhuzhan():      #这个是助战
    return    

def zhinan():    #这个是指南
    pg.press("esc")
    time.sleep(2)
    loc_x = 2686 * scal_x
    loc_y = 1512 * scal_y
    pg.click(loc_x, loc_y) 
    time.sleep(1)
    print("zhinan succeed")
    
def weituo():       #这个是委托
    loc_x = 3450 * scal_x
    loc_y = 728 * scal_y
    pg.click(loc_x, loc_y)


def yiqi(num=1, repeat = 6):        #这个是遗器，n代表从上往下数第几个遗器本（从1开始）
    zhinan()
    loc_x = 1195 * scal_x
    loc_y = 430 * scal_y
    pg.click(loc_x, loc_y)  #这个是副本
    time.sleep(1)
    loc_x = 877 * scal_x
    loc_y = 1738 * scal_y
    pg.click(loc_x, loc_y)  #这个是遗器本
    time.sleep(1)
    
    loc_x = 3103 * scal_x
    loc_y = 836 * scal_y
    pg.moveTo(loc_x, loc_y)  #这个是第一个遗器
    time.sleep(1)
    
    num = 9
    t = num
    
    while (t>1):
        pg.mouseDown()
        pg.move(0, int(-420*scal_y), 1)
        time.sleep(1)
        pg.mouseUp()
        pg.moveTo(loc_x, loc_y)
        t-=1
    if (num > 6):  
        pg.moveTo(loc_x, (922+(num-7)*395) * scal_y)  
    
    time.sleep(1)
    pg.click()
    time.sleep(5)
    
    loc_x = 3236 * scal_x
    loc_y = 1967 * scal_y
    pg.moveTo(loc_x, loc_y)  #副本入口
    pg.click()
    time.sleep(2)
    pg.click()
    
    loc_x = 2450 * scal_x
    loc_y = 1890 * scal_y
    pg.moveTo(loc_x, loc_y)
    while (repeat>1):       #再来一次
        time.sleep(90)
        pg.click()
        repeat -= 1
    
    loc_x = 1423 * scal_x
    loc_y = 1895 * scal_y
    pg.moveTo(loc_x, loc_y)
    pg.click()
    time.sleep(1)
    pg.click()
    time.sleep(1)
    
def meiri():        #这个是每日
    zhinan()
    loc_x = 870 * scal_x
    loc_y = 1652 * scal_y
    pg.moveTo(loc_x, loc_y)
    for i in range(5):
        pg.click()
        time.sleep(1)

def over():
    pg.hotkey("alt", "f4")
    
    
    

    
    
    
def loc( file_name):
    return pg.locateOnScreen(file_name)

def moniter( file_name, flag = True): #flag 为 true 时判断何时相同， 为false时判断何时不同
    
    #region = (0, 0, self.size[0], self.size[1])  # 示例：左上角(0, 0)，右下角(800, 600)
    # 初始化截图
    #shot = ImageGrab.grab(bbox=region)  # 截取指定区域的屏幕图像，并赋值给shot变量
    similarity = 0
    
    shot = ImageGrab.grab()
    shot.save("./tmp/screen.png")
    screen = cv2.imread("./tmp/screen.png")
    target = cv2.imread(file_name)
    target = cv2.resize(target, (screen.shape[1], screen.shape[0]), interpolation=cv2.INTER_AREA)
    
    gray_target = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    while True:          
        similarity, _ = ssim(gray_target, gray_screen, full=True)
        #print(similarity)
        if (flag and similarity>0.85) or ((not flag) and similarity<0.7):
            return
        time.sleep(1)
        shot = ImageGrab.grab()
        shot.save("./tmp/screen.png", "PNG")
        screen = cv2.imread("./tmp/screen.png")
        gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

def diff(img1, img2):
    coef, _ = ssim(img1, img2, full=True)
    return coef

if (__name__ == "__main__"):
    run();
