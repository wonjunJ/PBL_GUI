import sys
import cv2, imutils
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()
        self.titleBar()
        self.menu_bar_2()
        self.main_layout()

    def init_UI(self):
        self.resize(1180, 900)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet(
            "background-color : rgb(40, 52, 72);"
        )
        self.setMouseTracking(True)

    def titleBar(self):
        self.app_label = QLabel('Camver', self)

        self.app_label.setFont(QFont('Segoe UI', 13))
        self.app_label.setStyleSheet(
            '''
            QLabel{ 
                color : #ffffff;
                background-color : rgb(33, 37, 43); 
                margin-bottom : px; }
            ''')

        self.favicon_label = QLabel(self)
        self.favicon_label.setPixmap(QPixmap('./icon/favicon.png').scaled(25, 25))
        self.favicon_label.setStyleSheet(
            '''
            QLabel{ 
                background-color : rgb(33, 37, 43); 
                margin-right : 10px; 
                margin-left : 2px;
                margin-top : 2px;
                margin-bottom : px; }
            ''')

        self.btn_close = QPushButton(self)
        self.btn_close.setStyleSheet(
            '''
            QPushButton{ 
                background-color : rgb(33, 37, 43); 
                border : 0px; 
                border-radius : 3px;
                margin-top : 2px; }
            QPushButton::hover { background-color : #000000 }
            ''')

        self.btn_close.setIcon(QIcon('./icon/icon_close.png'))
        self.btn_close.setIconSize(QSize(20, 20))
        self.btn_close.clicked.connect(self.btn_close_clicked)

        self.btn_min = QPushButton(self)
        self.btn_min.setStyleSheet(
            '''
            QPushButton{ background-color : rgb(33, 37, 43); 
            border : 0px; 
            border-radius : 3px;
            margin-top : 2px; }
            QPushButton::hover { background-color : #000000 }
            ''')
        self.btn_min.setIcon(QIcon('./icon/icon_min.png'))
        self.btn_min.setIconSize(QSize(20, 20))
        self.btn_min.clicked.connect(self.btn_min_clicked)

        self.btn_max = QPushButton(self)
        self.btn_max.setStyleSheet(
            '''
            QPushButton{ 
                background-color : rgb(33, 37, 43); 
                border : 0px; 
                border-radius : 3px;
                margin-top : 2px; }
            ''')
        self.btn_max.setIcon(QIcon('./icon/icon_max.png'))
        self.btn_max.setIconSize(QSize(20, 20))

        self.btn_max.setCheckable(True)
        # self.btn_max.clicked.connect(self.btn_restore_clicked)
        self.titleFrame = QFrame(self)
        self.titleFrame.setGeometry(0, 0, 1180, 50)
        self.titleFrame.setStyleSheet(
            '''
            QWidget{  
                background-color : rgb(33, 37, 43); }
            '''
        )

        self.titleHBox = QHBoxLayout(self.titleFrame)
        self.titleHBox.addWidget(self.favicon_label)
        self.titleHBox.addWidget(self.app_label)
        self.titleHBox.addStretch(1)
        self.titleHBox.addWidget(self.btn_min)
        self.titleHBox.addWidget(self.btn_max)
        self.titleHBox.addWidget(self.btn_close)

    '''
    def menu_bar(self):
        self.btn_resolution_result = QPushButton("Resolution", self)
        self.btn_resolution_result.setFont(QFont('Segoe UI', 15))
        self.btn_resolution_result.setMaximumSize(150, 163)
        self.btn_resolution_result.setCheckable(True)
        self.btn_resolution_result.setStyleSheet(
            """
            QPushButton{ 
                background-color : rgb(15, 65, 82); 
                border : 0px;
                color : white; 
                border-width : 0px; }
            QPushButton::hover { background-color : rgb(40, 52, 72); }
            """)
        self.btn_resolution_result.clicked.connect(self.btn_resolution_clicked)

        self.btn_vignetting_result = QPushButton("Vignetting", self)
        self.btn_vignetting_result.setFont(QFont('Segoe UI', 15))
        self.btn_vignetting_result.setMaximumSize(150, 162)
        self.btn_vignetting_result.setCheckable(True)
        self.btn_vignetting_result.setStyleSheet(
            """
            QPushButton{ 
                background-color : rgb(15, 65, 82); 
                border : 0px;
                color : white; 
                border-width : 0px; }
            QPushButton::hover { background-color : rgb(40, 52, 72); }
            """
        )
        self.btn_vignetting_result.clicked.connect(self.btn_vignetting_clicked)

        self.btn_whiteBalance_result = QPushButton("WhiteBalance", self)
        self.btn_whiteBalance_result.setFont(QFont('Segoe UI', 15))
        self.btn_whiteBalance_result.setMaximumSize(150, 162)
        self.btn_whiteBalance_result.setCheckable(True)
        self.btn_whiteBalance_result.setStyleSheet(
            """
            QPushButton{ 
                background-color : rgb(15, 65, 82); 
                border : 0px;
                color : white;
                border-width : 0px; }
            QPushButton::hover { background-color : rgb(40, 52, 72); }
            """
        )
        self.btn_whiteBalance_result.clicked.connect(self.btn_WB_clicked)

        self.btn_focus_result = QPushButton("Focus", self)
        self.btn_focus_result.setFont(QFont('Segoe UI', 15))
        self.btn_focus_result.setMaximumSize(150, 163)
        self.btn_focus_result.setCheckable(True)
        self.btn_focus_result.setStyleSheet(
            """
            QPushButton{ 
                background-color : rgb(15, 65, 82); 
                border : 0px;
                color : white; 
                border-width : 0px; }
            QPushButton::hover { background-color : rgb(40, 52, 72); }
            """
        )
        self.btn_focus_result.clicked.connect(self.btn_focus_clicked)

        self.menuFrame = QFrame(self)
        self.menuFrame.setGeometry(0, 150, 150, 650)
        self.menuFrame.setStyleSheet(
            """
            QWidget{  
                background-color : rgb(15, 65, 82); }
            """
        )
        self.menuVBox = QVBoxLayout(self.menuFrame)
        self.menuVBox.setSpacing(0)
        self.menuVBox.setContentsMargins(0, 0, 0, 0)
        self.menuVBox.addWidget(self.btn_resolution_result)
        self.menuVBox.addWidget(self.btn_vignetting_result)
        self.menuVBox.addWidget(self.btn_whiteBalance_result)
        self.menuVBox.addWidget(self.btn_focus_result)
    '''
    def menu_bar_2(self):
        self.btn_resolution_result = QPushButton(self)
        self.btn_resolution_result.setMaximumSize(100, 140)
        self.btn_resolution_result.setCheckable(True)
        self.btn_resolution_result.setIcon(QIcon('./icon/resolution.png'))
        self.btn_resolution_result.setIconSize(QSize(30,30))
        self.btn_resolution_result.setStyleSheet(
            """
            QPushButton{ 
                background-color : rgb(15, 65, 82); 
                border : 0px;
                color : white; 
                border-width : 0px; }
            QPushButton::hover { background-color : rgb(40, 52, 72); }
            """)
        self.btn_resolution_result.clicked.connect(self.btn_resolution_clicked)

        self.btn_vignetting_result = QPushButton(self)
        self.btn_vignetting_result.setMaximumSize(100, 140)
        self.btn_vignetting_result.setCheckable(True)
        self.btn_vignetting_result.setIcon(QIcon('./icon/vignetting.png'))
        self.btn_vignetting_result.setIconSize(QSize(30,30))
        self.btn_vignetting_result.setStyleSheet(
            """
            QPushButton{ 
                background-color : rgb(15, 65, 82); 
                border : 0px;
                color : white; 
                border-width : 0px; }
            QPushButton::hover { background-color : rgb(40, 52, 72); }
            """
        )
        self.btn_vignetting_result.clicked.connect(self.btn_vignetting_clicked)

        '''
        self.btn_whiteBalance_result = QPushButton(self)
        self.btn_whiteBalance_result.setFont(QFont('Segoe UI', 15))
        self.btn_whiteBalance_result.setMaximumSize(100, 125)
        self.btn_whiteBalance_result.setIcon(QIcon('./icon/whitebalance.png'))
        self.btn_whiteBalance_result.setIconSize(QSize(30,30))
        self.btn_whiteBalance_result.setCheckable(True)
        self.btn_whiteBalance_result.setStyleSheet(
            """
            #QPushButton{ 
            #    background-color : rgb(15, 65, 82); 
            #    border : 0px;
            #    color : white;
            #    border-width : 0px; }
            #QPushButton::hover { background-color : rgb(40, 52, 72); }
            """
        )
        self.btn_whiteBalance_result.clicked.connect(self.btn_WB_clicked)
        '''

        self.btn_focus_result = QPushButton(self)
        self.btn_focus_result.setFont(QFont('Segoe UI', 15))
        self.btn_focus_result.setMaximumSize(100, 140)
        self.btn_focus_result.setIcon(QIcon('./icon/focus.png'))
        self.btn_focus_result.setIconSize(QSize(30,30))
        self.btn_focus_result.setCheckable(True)
        self.btn_focus_result.setStyleSheet(
            """
            QPushButton{ 
                background-color : rgb(15, 65, 82); 
                border : 0px;
                color : white; 
                border-width : 0px; }
            QPushButton::hover { background-color : rgb(40, 52, 72); }
            """
        )
        self.btn_focus_result.clicked.connect(self.btn_focus_clicked)

        self.menuFrame = QFrame(self)
        self.menuFrame.setGeometry(0, 265, 100, 420)
        self.menuFrame.setStyleSheet(
            """
            QWidget{  
                border-top-right-radius : 3px;
                border-bottom-right-radius : 3px;
                background-color : rgb(15, 65, 82); }
            """
        )
        self.menuVBox = QVBoxLayout(self.menuFrame)
        self.menuVBox.setSpacing(0)
        self.menuVBox.setContentsMargins(0, 0, 0, 0)
        self.menuVBox.addWidget(self.btn_resolution_result)
        self.menuVBox.addWidget(self.btn_vignetting_result)
        #self.menuVBox.addWidget(self.btn_whiteBalance_result)
        self.menuVBox.addWidget(self.btn_focus_result)

    def main_layout(self):
        self.gridLayoutWidget = QWidget(self)
        self.img_result = QLabel(self)
        self.pass_result = QLabel(self)
        self.gridLayoutWidget.setGeometry(QRect(180, 75, 990, 790))
        self.resolutionGLayout = QGridLayout(self.gridLayoutWidget)
        self.resolutionGLayout.setContentsMargins(0, 0, 0, 0)
        #self.resolutionGLayout.addWidget(self.img_result, 2, 1, 1, 1)
        #self.resolutionGLayout.addWidget(self.pass_result, 2, 2, 1, 1)

    def btn_resolution_clicked(self):
        if self.btn_resolution_result.isChecked() ==1:
            if self.btn_vignetting_result.isChecked() ==1:
                self.btn_vignetting_result.toggle()
                self.btn_vignetting_clicked()
            #if self.btn_whiteBalance_result.isChecked() ==1:
            #    self.btn_whiteBalance_result.toggle()
            #    self.btn_WB_clicked()
            if self.btn_focus_result.isChecked() ==1:
                self.btn_focus_result.toggle()
                self.btn_focus_clicked()

            Result_layout.result_content(self)
            self.resol_Animation()
            self.btn_resolution_result.setStyleSheet(
                """
                QPushButton{
                    border : 5px;
                    color : white;
                    border-style : solid;
                    border-top-color : rgb(40, 52, 72);
                    border-bottom-color : rgb(40, 52, 72);
                    border-right-color : rgb(40, 52, 72);
                    background-color : rgb(40, 52, 72);
                    border-left-color : rgb(100, 0, 0);
                }
                """
            )
        else:
            '''
            self.img_result.setStyleSheet(
                """
                QLabel{
                    border : 0px
                }
                """
            )
            self.pass_result.setText("")
            '''
            self.resol_Animation_down()
            self.btn_resolution_result.setStyleSheet(
                '''
                QPushButton{
                    border : 0px;
                    color: white;
                    background-color : rgb(15, 65, 82);
                }
                QPushButton::hover { background-color : rgb(40, 52, 72); }
                '''
            )


    def btn_vignetting_clicked(self):
        if self.btn_vignetting_result.isChecked() ==1:
            if self.btn_resolution_result.isChecked() ==1:
                self.btn_resolution_result.toggle()
                self.btn_resolution_clicked()
            #if self.btn_whiteBalance_result.isChecked() ==1:
            #    self.btn_whiteBalance_result.toggle()
            #    self.btn_WB_clicked()
            if self.btn_focus_result.isChecked() ==1:
                self.btn_focus_result.toggle()
                self.btn_focus_clicked()

            Result_layout.vig_result_content(self)
            self.btn_vignetting_result.setStyleSheet(
                """
                QPushButton{
                    border : 5px;
                    color : white;
                    border-style : solid;
                    border-top-color : rgb(40, 52, 72);
                    border-bottom-color : rgb(40, 52, 72);
                    border-right-color : rgb(40, 52, 72);
                    background-color : rgb(40, 52, 72);
                    border-left-color : rgb(100, 0, 0);
                }
                """
            )
        else:
            '''
            self.img_result.setStyleSheet(
                """
                QLabel{
                    border : 0px
                }
                """
            )
            self.pass_result.setText("")
            '''
            self.vig_Animation_down()
            self.btn_vignetting_result.setStyleSheet(
                """
                QPushButton{
                    border : 0px;
                    color: white;
                    background-color : rgb(15, 65, 82);
                }
                QPushButton::hover { background-color : rgb(40, 52, 72); }
                """
            )

    '''
    def btn_WB_clicked(self):
        if self.btn_whiteBalance_result.isChecked() ==1:
            if self.btn_resolution_result.isChecked() ==1:
                self.btn_resolution_result.toggle()
                self.btn_resolution_clicked()
            if self.btn_vignetting_result.isChecked() ==1:
                self.btn_vignetting_result.toggle()
                self.btn_vignetting_clicked()
            if self.btn_focus_result.isChecked() ==1:
                self.btn_focus_result.toggle()
                self.btn_focus_clicked()

            Result_layout.result_content(self)
            self.btn_whiteBalance_result.setStyleSheet(
                """
                QPushButton{
                    border : 5px;
                    color : white;
                    border-style : solid;
                    border-top-color : rgb(40, 52, 72);
                    border-bottom-color : rgb(40, 52, 72);
                    border-right-color : rgb(40, 52, 72);
                    background-color : rgb(40, 52, 72);
                    border-left-color : rgb(100, 0, 0);
                }
                """
            )
        else:
            self.img_result.setStyleSheet(
                """
                QLabel{
                    border : 0px
                }
                """
            )
            self.pass_result.setText("")
            self.btn_whiteBalance_result.setStyleSheet(
                """
                QPushButton{
                    border : 0px;
                    color: white;
                    background-color : rgb(15, 65, 82);
                }
                QPushButton::hover { background-color : rgb(40, 52, 72); }
                """
            )
    '''

    def btn_focus_clicked(self):
        if self.btn_focus_result.isChecked() ==1:
            if self.btn_resolution_result.isChecked() ==1:
                self.btn_resolution_result.toggle()
                self.btn_resolution_clicked()
            #if self.btn_whiteBalance_result.isChecked() ==1:
            #    self.btn_whiteBalance_result.toggle()
            #    self.btn_WB_clicked()
            if self.btn_vignetting_result.isChecked() ==1:
                self.btn_vignetting_result.toggle()
                self.btn_vignetting_clicked()

            Result_layout.result_content(self)
            self.focus_Animation()
            self.btn_focus_result.setStyleSheet(
                """
                QPushButton{
                    border : 5px;
                    color : white;
                    border-style : solid;
                    border-top-color : rgb(40, 52, 72);
                    border-bottom-color : rgb(40, 52, 72);
                    border-right-color : rgb(40, 52, 72);
                    background-color : rgb(40, 52, 72);
                    border-left-color : rgb(100, 0, 0);
                }
                """
            )
        else:
            """
            self.img_result.setStyleSheet(
                '''
                QLabel{
                    border : 0px
                }
                '''
            )
            """
            self.focus_Animation_down()
            self.pass_result.setText("")
            self.btn_focus_result.setStyleSheet(
                '''
                QPushButton{
                    border : 0px;
                    color: white;
                    background-color : rgb(15, 65, 82);
                }
                QPushButton::hover { background-color : rgb(40, 52, 72); }
                '''
            )

    def btn_close_clicked(self):
        self.close()

    def btn_min_clicked(self):
        self.showMinimized()

    def resol_Animation(self):
        self.animation = QPropertyAnimation(self.gridLayoutWidget, b"geometry")
        self.animation.setDuration(200)
        self.animation.setStartValue(QRect(100, 335, 0, 0))
        self.animation.setEndValue(QRect(180, 75, 990, 790))
        self.animation.start()

    def resol_Animation_down(self):
        self.animation = QPropertyAnimation(self.gridLayoutWidget, b"geometry")
        self.animation.setDuration(200)
        self.animation.setStartValue(QRect(180, 75, 990, 790))
        self.animation.setEndValue(QRect(100, 335, 0, 0))
        self.animation.start()

    def vig_Animation(self):
        self.animation = QPropertyAnimation(self.gridLayoutWidget, b"geometry")
        self.animation.setDuration(200)
        self.animation.setStartValue(QRect(100, 475, 0, 0))
        self.animation.setEndValue(QRect(180, 75, 990, 790))
        self.animation.start()

    def vig_Animation_down(self):
        self.animation = QPropertyAnimation(self.gridLayoutWidget, b"geometry")
        self.animation.setDuration(200)
        self.animation.setStartValue(QRect(180, 75, 990, 790))
        self.animation.setEndValue(QRect(100, 475, 0, 0))
        self.animation.start()

    def focus_Animation(self):
        self.animation = QPropertyAnimation(self.gridLayoutWidget, b"geometry")
        self.animation.setDuration(200)
        self.animation.setStartValue(QRect(100, 615, 0, 0))
        self.animation.setEndValue(QRect(180, 75, 990, 790))
        self.animation.start()

    def focus_Animation_down(self):
        self.animation = QPropertyAnimation(self.gridLayoutWidget, b"geometry")
        self.animation.setDuration(200)
        self.animation.setStartValue(QRect(180, 75, 990, 790))
        self.animation.setEndValue(QRect(100, 615, 0, 0))
        self.animation.start()


class Result_layout(MyDialog):
    def __init__(self):
        super(Result_layout, self).__init__()

    def result_content(self):
        #self.gridLayoutWidget = QWidget(self)
        #self.img_result = QLabel(self)
        self.resolutionGLayout.addWidget(self.img_result, 2, 1, 1, 1)
        self.resolutionGLayout.addWidget(self.pass_result, 2, 2, 1, 1)
        self.img_result.setAlignment(Qt.AlignCenter)
        #self.img_result.setGeometry(200, 125, 750, 750)
        self.img_result.setMaximumSize(QSize(750, 750))
        self.img_result.setStyleSheet(
            '''
            QLabel{
                border : 3px;
                border-style : dashed;
                border-color : white;
            }
            '''
        )
        #self.pass_result = QLabel(self)
        self.pass_result.setFont(QFont('Segoe UI', 30))
        self.pass_result.setText("Pass")
        self.pass_result.setAlignment(Qt.AlignCenter)
        self.pass_result.setMaximumSize(QSize(150, 16777215))
        self.pass_result.setStyleSheet(
            '''
            color : white;
            '''
        )
        #self.menuAnimation()

    def vig_result_content(self):
        #self.gridLayoutWidget = QWidget(self)
        #self.img_result = QLabel(self)
        self.img_result.setAlignment(Qt.AlignCenter)
        #self.img_result.setGeometry(200, 125, 750, 750)
        self.img_result.setMaximumSize(QSize(750, 750))
        self.img_result.setStyleSheet(
            '''
            QLabel{
                border : 3px;
                border-style : dashed;
                border-color : white;
            }
            '''
        )
        self.pass_result.setText("")
        self.resolutionGLayout.addWidget(self.img_result, 2, 1, 1, 2)
        self.vig_Animation()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyDialog()
    main.show()
    app.exec_()