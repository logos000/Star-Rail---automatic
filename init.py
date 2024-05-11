import pyautogui as pg
import numpy as np  # 导入numpy模块，用于处理图像数据  
import keyboard     #监听键盘
from pynput import mouse    #监听鼠标

def initial():
   pg.alert(text='请选择想要你更改的坐标,然后移动鼠标到目标坐标并按ctrl', title='请求框', button='OK')
   arr = np.load('position.npy')
   global loc_x, loc_y
   while True:
       botton = pg.confirm(text='请选择你想要更改的坐标',title='初始化坐标',buttons=['启动按钮','指南','副本','遗器本','第一个遗器','第二个遗器', '保存'])
       match  botton:
        case '启动按钮':
            arr[0] = position()     
        case '指南':
            arr[1] = position()
        case '副本':
            arr[2] = position()
        case '遗器本':
            arr[3] = position()
        case '第一个遗器':
            arr[4] = position()
        case '第二个遗器':
            arr[5] = position()
        case '最后一个遗器':
            arr[6] = position()
        case '副本入口按钮':
            arr[7] = position()
        case '再来一次按钮':
            arr[8] = position()
        case '退出按钮':
            arr[9] = position()
        case '每日奖励':
            arr[10] = position()
        case '保存':
            np.save('position', arr)
            return
           
def save_default():
    arr = np.zeros([20,2], int)
    arr[0] = [2470, 1410]       #'启动按钮'
    arr[1] = [2686, 1512]       #'指南'
    arr[2] = [1195, 430]        #'指南-副本'
    arr[3] = [877, 1738]        #'副本-遗器本'
    arr[4] = [3103, 836]        #'第一个遗器'
    arr[5] = [3103, 1231]       #'第二个遗器'
    arr[6] = [3103, 1712]       #'最后一个遗器'
    arr[7] = [3236, 1967]       #'副本入口按钮'
    arr[8] = [2450, 1890]       #'再来一次按钮'
    arr[9] = [1423, 1895]       #'退出按钮'
    arr[10] = [870, 1652]       #'每日奖励'
    arr[11] = [3450, 728]       #'委托'
    np.save('position', arr)

def position():
    keyboard.wait('ctrl')
    return pg.position()

def listen_click():
    listener = mouse.Listener(on_move=on_move,    on_click=on_click,  on_scroll=on_scroll)
    listener.start()

# 移动监听  
def on_move(x, y):
    print('鼠标移动到了：{}'.format((x, y)))

# 滚动监听
def on_scroll(x, y, dx, dy):
    print('滚动中... {} 至 {}'.format('向下：' if dy < 0 else '向上：', (x, y)))

# 点击监听
def on_click(x, y, button, pressed):
 
 if  pressed:
      # 当点击鼠标时停止监听
      print('鼠标按键：{}，在位置处 {}, {} '.format(button, (x, y), '按下了'))
      loc_x = x
      loc_y = y
      return False

if (__name__ == "__main__"):
    save_default()
    botton = pg.confirm(text='确定初始化吗',title='初始化坐标',buttons=['yes','no'])
    if botton == 'yes':
        initial()
        