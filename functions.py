import win32api
import win32gui
import win32con
from time import sleep
import random
from ctypes import windll


def click_left():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def move_cur(x, y):
    windll.user32.SetCursorPos(x, y)


def get_cur_pos():
    return win32gui.GetCursorPos()


def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False


# 向右下角沿着随机直线移动鼠标
def move_cur_random_line():
    for item in range(random.randint(100, 200)):
        pos = get_cur_pos()
        flag = random.random()
        if flag < 0.3:
            move_cur(pos[0] + random.randint(0, 5), pos[1] + random.randint(0, 5))
        elif flag < 0.6:
            move_cur(pos[0] + random.randint(0, 5), pos[1] - random.randint(0, 2))
        else:
            move_cur(pos[0] + random.randint(0, 2), pos[1] + random.randint(0, 3))
        sleep(random.uniform(0.001, 0.009))
    click_left()


def move_cur_line(terminal_x, terminal_y):
    # 移动y轴
    current_y = get_cur_pos()[1]
    movement_y = current_y - terminal_y
    for item in range(int(abs(movement_y) / 3)):
        pos = get_cur_pos()
        back_flag = random.random()
        if back_flag < 0.5:
            if movement_y > 0:  # 向上移动
                move_cur(pos[0] - 1, pos[1] - 3)
            elif movement_y < 0:   # 向下移动
                move_cur(pos[0] - 1, pos[1] + 3)
            else:
                break
        else:
            if movement_y > 0:
                move_cur(pos[0] + 1, pos[1] - 3)
            elif movement_y < 0:
                move_cur(pos[0] + 1, pos[1] + 3)
            else:
                break
        sleep(random.uniform(0.001, 0.009))

    # 移动x轴
    current_x = get_cur_pos()[0]
    movement_x = current_x - terminal_x
    for item in range(int(abs(movement_x) / 3)):
        pos = get_cur_pos()
        back_flag = random.random()
        if back_flag < 0.5:
            if movement_x > 0:  # 向左移动
                move_cur(pos[0] - 3, pos[1] + 1)
            elif movement_x < 0:   # 向右移动
                move_cur(pos[0] + 3, pos[1] + 1)
            else:
                break
        else:
            if movement_x > 0:
                move_cur(pos[0] - 3, pos[1] - 1)
            elif movement_x < 0:
                move_cur(pos[0] + 3, pos[1] - 1)
            else:
                break
        sleep(random.uniform(0.001, 0.009))


def start_game(time, x, y):
    sleep(5)
    x_temp = int(x * 0.7)
    y_temp = int(y * 0.7)
    while True:
        # 点一下挑战，刷一次
        x_init = random.randint(x_temp, x_temp + int(x * 0.085))
        y_init = random.randint(y_temp, y_temp + int(y * 0.053))
        count_init = 0
        while get_cur_pos()[0] != x_init or get_cur_pos()[1] != y_init:
            move_cur_line(x_init, y_init)
            count_init += 1
            if count_init >= 10:
                move_cur(x_init, y_init)
                break

        click_left()
        # 随机延时0s-2s
        sleep(random.uniform(0.2, 0.3))

        # 接下来把鼠标随机移动到一些奇怪的地方，再瞎点几下
        move_cur_random_line()

        # 移动完后，把鼠标移回去
        move_cur_line(x_init, y_init)

        click_left()

        if time == 1:
            sleep(random.uniform(9, 10))  # 等待一次刷完

        else:
            sleep(random.uniform(time + 5, time + 7))

        click_left()
        sleep(random.uniform(2.2, 2.5))
        click_left()
        sleep(random.uniform(2.2, 2.5))
        click_left()
        sleep(random.uniform(2.2, 2.5))


def baigui(x, y):
    sleep(5)
    x_temp = int(x * 0.7)
    y_temp = int(y * 0.73)
    while True:
        x_init = random.randint(x_temp, x_temp + int(x * 0.085))
        y_init = random.randint(y_temp, y_temp + int(y * 0.05))
        count_init = 0
        while get_cur_pos()[0] != x_init or get_cur_pos()[1] != y_init:
            move_cur_line(x_init, y_init)
            count_init += 1
            if count_init >= 10:
                move_cur(x_init, y_init)
                break

        click_left()  # 点击开始
        sleep(random.uniform(2.2, 2.5))

        # 选鬼王
        flag = random.random()
        y1 = random.randint(int(y * 0.6), int(y * 0.6) + int(y * 0.1))
        if flag < 0.33:
            x1 = random.randint(int(x * 0.22), int(x * 0.22) + int(x * 0.03))
            move_cur_line(x1, y1)

        elif flag < 0.66:
            x1 = random.randint(int(x * 0.49), int(x * 0.49) + int(x * 0.03))
            move_cur_line(x1, y1)

        else:
            x1 = random.randint(int(x * 0.76), int(x * 0.76) + int(x * 0.03))
            move_cur_line(x1, y1)
        click_left()
        sleep(random.uniform(0.2, 0.3))
        click_left()
        sleep(random.uniform(0.2, 0.3))
        click_left()
        sleep(random.uniform(0.2, 0.3))
        click_left()
        sleep(random.uniform(0.2, 0.3))
        click_left()
        sleep(random.uniform(0.2, 0.3))

        # 移动鼠标到开始位置
        x1 = random.randint(int(x * 0.9), int(x * 0.9) + int(x * 0.05))
        y1 = random.randint(int(y * 0.82), int(y * 0.82) + int(y * 0.09))
        print('移动到开始')
        move_cur_line(x1, y1)
        print(x1, y1)
        click_left()
        sleep(random.uniform(0.3, 0.5))

        # 把每次砸的豆子数量调到最大
        while abs(get_cur_pos()[0] - int(x * 0.3)) > 2 or abs(get_cur_pos()[1] - int(y * 0.93)) > 2:
            move_cur_line(int(x * 0.3), int(y * 0.93))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        move_cur_line(int(x * 0.45), int(y * 0.93))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        print('调整成功')
        sleep(random.uniform(0.3, 0.5))

        # 开始砸豆子
        count = 0
        y1 = random.randint(int(y * 0.68), int(y * 0.68) + int(y * 0.05))
        while count < 35:
            x1 = random.randint(int(x * 0.3), int(x * 0.3) + int(x * 0.3))
            move_cur_line(x1, y1)

            sleep(random.uniform(1.2, 1.3))
            click_left()
            sleep(0.1)
            click_left()
            sleep(0.1)
            click_left()

            count += 1

        y1 = random.randint(int(y * 0.93), int(y * 0.91) + int(y * 0.07))
        move_cur_line(x1, y1)
        click_left()

        move_cur_random_line()
        sleep(random.uniform(1, 2))
