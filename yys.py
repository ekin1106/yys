import os,sys,cv2
import aircv as ac
import time
import random
def draw_circle(img, pos, circle_radius, color, line_width):
    cv2.circle(img, pos, circle_radius, color, line_width)
    cv2.imshow('objDetect', img_src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def capture_screen():
    '''测试 御魂'''
    '''截取手机画面，拉回到本地'''
    start = time.clock()
    os.system('adb shell screencap -p /sdcard/yys/yuhun.png')
    end = time.clock()
    print('capture time:{}'.format(end-start))
    os.system('adb pull /sdcard/yys/yuhun.png d:/verysync/github/yys')

def tansuo():
    img_src = ac.imread('D:\\verysync\\github\\yys\\yuhun.png')
    img_btn = ac.imread('D:\\verysync\\github\\yys\\yun_button.jpg')
    pos = ac.find_template(img_src,img_btn)
    '''pos的结果可以获得图像匹配的坐标，具体的匹配结果的四个角的坐标
       confidence 的值就是匹配程度，匹配失败返回none'''
    return pos

def ready():
    img_src = ac.imread('D:\\verysync\\github\\yys\\yuhun.png')
    img_btn = ac.imread('D:\\verysync\\github\\yys\\ready_button.jpg')
    ready_pos = ac.find_template(img_src,img_btn)
    '''pos的结果可以获得图像匹配的坐标，具体的匹配结果的四个角的坐标
       confidence 的值就是匹配程度，匹配失败返回none'''
    return ready_pos


def tap_angle(pos):
        x_Left = pos['rectangle'][0][0]
        x_Right = pos['rectangle'][2][0]
        y_Left = pos['rectangle'][0][1]
        y_Right = pos['rectangle'][1][1]
        x = random.choice(range(x_Left,x_Right+1))
        y = random.choice(range(y_Left,y_Right+1))
        return x,y
if __name__ == '__main__':
#     print('''选择需要adb连接的机器
# 1. Mumu模拟器 127.0.0.1:7555 Physical size: 2560x1440
# 2. Galaxy S8+
# 3. Moto X''')
#     sel = input('请选择:')
#     if sel == '1':
#         os.system('adb connect 127.0.0.1:7555')
#         print('Mumu connect complete')

    while True:
        capture_screen()
        time.sleep(1)
        if tansuo():
            print(tap_angle(tansuo()))
            os.system('adb shell input tap {0} {1}'.format(tap_angle(tansuo())[0],tap_angle(tansuo())[1]))
        elif ready():
            print(tap_angle(ready()))
            os.system('adb shell input tap {0} {1}'.format(tap_angle(ready())[0],tap_angle(ready())[1]))

    # capture_screen()


    # circle_center_pos = (x,y)
    # circle_radius = 50
    # color = (0,255,0)
    # line_width = 10
    # draw_circle(img_src, circle_center_pos, circle_radius, color, line_width)
