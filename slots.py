import threading
import functions


def pushButton_click(test):
    if test.comboBox.currentIndex() == 0:
        time = eval(test.time_value.text())
        x = eval(test.win_value_x.text())
        y = eval(test.win_value_y.text())
        game = threading.Thread(target=functions.start_game, args=(time, x, y))
        game.setDaemon(True)
        game.start()

    else:
        x = eval(test.win_value_x.text())
        y = eval(test.win_value_y.text())
        game = threading.Thread(target=functions.baigui, args=(x, y, ))
        game.setDaemon(True)
        game.start()
