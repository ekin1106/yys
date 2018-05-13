import cv2
import aircv as ac

# print circle_center_pos
def draw_circle(img, pos, circle_radius, color, line_width):
    cv2.circle(img, pos, circle_radius, color, line_width)
    cv2.imshow('objDetect', imsrc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    imsrc = ac.imread('D:\\verysync\\github\\yys\\battle_ready.png')
    imobj = ac.imread('D:\\verysync\\github\\yys\\ready_button.jpg')

    # find the match position
    pos = ac.find_template(imsrc, imobj)
    print(pos)
    circle_center_pos = ()
    x = int(pos['result'][0])

    y = int(pos['result'][1])

    circle_center_pos = (x,y)
    circle_radius = 50
    color = (0,255,0)
    line_width = 10

    # draw circle 里位置的坐标要整数，不能为float
    draw_circle(imsrc, circle_center_pos, circle_radius, color, line_width)
'''构想
    主机需要匹配 准备
    匹配完以后，点击 准备
    匹配打完的图
    匹配 红达摩
    匹配 组队画面
    匹配 组队画面 准备开始

    僚机 匹配 匹配打完的图
    匹配 红达摩
    等待几秒
    '''
