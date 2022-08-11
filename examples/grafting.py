import os
os.environ['QT_API'] = 'pyside6'

from lambda_ex import grafting
from qtpy.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])
win = QWidget()
btn = QPushButton('click me', win)


cnt = 0


@grafting(btn.clicked.connect)  # noqa
def on_clicked():
    global cnt
    cnt += 1
    print('clicked', cnt)


win.show()
app.exec()
