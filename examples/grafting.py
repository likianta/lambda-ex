from lambda_ex import GRAFTEE
from lambda_ex import grafting


def demo1():
    """
    pip install qtpy
    pip install pyside6
    """
    import os
    os.environ['QT_API'] = 'pyside6'
    
    from qtpy.QtWidgets import QApplication, QWidget, QPushButton
    
    app = QApplication()
    win = QWidget(None)
    btn = QPushButton('click me', win)
    
    cnt = 0
    
    @grafting(btn.clicked.connect)  # noqa
    def on_clicked():
        nonlocal cnt
        cnt += 1
        print('clicked', cnt)
    
    win.show()
    app.exec()


def demo2():
    """
    pip install flet
    """
    from flet import Page, TextField, app
    from flet.control_event import ControlEvent
    from lambda_ex import later
    
    @grafting(app, 'flet demo app', target=GRAFTEE)
    def main(page: Page):
        page.add(TextField(label='name', on_submit=(s := later())))
        
        @s.bind
        def submit(e: ControlEvent):
            print(e.control.value)


if __name__ == '__main__':
    # demo1()
    demo2()
