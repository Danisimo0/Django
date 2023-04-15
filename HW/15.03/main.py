import sys
import cv2
from PyQt6.QtCore import Qt, QTimer
from ui_mainwindow import *
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QImage, QPixmap
# import threading

class App(QWidget):
    def __init__(self):
        super().__init__()


        self.label = QLabel(self)

        # настройка параметров окна
        self.setWindowTitle("Hand Gestures Recognition")
        self.setGeometry(100, 100, 640, 480)

        # создание таймера для обновления изображения
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

        # открытие видео потока
        self.capture = cv2.VideoCapture('Video 1')
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        # распознавания рук
        self.hand_cascade = cv2.CascadeClassifier('hand.xml')

        # переменная для хранения состояния жеста руки
        self.hand_gesture = False

        # запуск главного цикла приложения
        self.show()

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            # преобразование изображения в формат, подходящий для отображения в QLabel
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(image)

            # обнаружение рук на изображении
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hands = self.hand_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in hands:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # проверка текущего состояния жеста руки
                if x < 200 and y < 200:
                    self.hand_gesture = True
                else:
                    self.hand_gesture = False

            # изменение цвета QLabel в зависимости от состояния жеста руки
            if self.hand_gesture:
                self.label.setStyleSheet("background-color: red;")
            else:
                self.label.setStyleSheet("")

            # отображение изображения в QLabel
            self.label.setPixmap(pixmap)
            self.label.setAlignment(Qt.AlignCenter)
        else:
            self.timer.stop()
            self.capture.release()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())

# TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH TRASH


# import cv2
# import sys
# from PyQt6.QtCore import Qt, QTimer
# from PyQt6.QtGui import QImage, QPixmap
# from PyQt6.QtWidgets import QApplication, QMainWindow
# from ui_mainwindow import Ui_MainWindow
#
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         # Инициализация пользовательского интерфейса
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         # Инициализация видеокамеры
#         self.cap = cv2.VideoCapture(0)
#         self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,
#                      self.ui.video_label.setAlignment(Qt.AlignCenter)
#         self.ui.video_label.setScaledContents(True)
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(50)
#
#         # Обработка событий кнопок
#         self.ui.start_button.clicked.connect(self.start_recording)
#         self.ui.stop_button.clicked.connect(self.stop_recording)
#
#         def update_frame(self):
#             # Чтение кадра из видеопотока
#             ret, frame = self.cap.read()
#             if ret:
#                 # Преобразование кадра в изображение Qt
#                 rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 h, w, ch = rgb_frame.shape
#                 bytes_per_line = ch * w
#                 image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
#
#                 # Отображение изображения на виджете QLabel
#                 self.ui.video_label.setPixmap(QPixmap.fromImage(image))
#
#                 # Обработка жестов рукой
#                 gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#                 hand_cascade = cv2.CascadeClassifier('hand.xml')
#                 hands = hand_cascade.detectMultiScale(gray_frame, 1.3, 5)
#                 for (x, y, w, h) in hands:
#                     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
#
#                 # Преобразование кадра с обводкой жеста в изображение Qt
#                 rgb_frame_with_hands = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 h, w, ch = rgb_frame_with_hands.shape
#                 bytes_per_line = ch * w
#                 image_with_hands = QImage(rgb_frame_with_hands.data, w, h, bytes_per_line, QImage.Format_RGB888)
#
#                 # Отображение изображения на виджете QLabel
#                 self.ui.hand_label.setPixmap(QPixmap.fromImage(image_with_hands))
#
#         def start_recording(self):
#         # Код для начала записи видео
#
#         def stop_recording(self):
#     # Код для остановки записи видео
#


# import cv2
# import numpy as np
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QTimer
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(0, 450, 261, 61))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(300, 450, 271, 61))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
#         self.listWidget.setGeometry(QtCore.QRect(30, 30, 511, 311))
#         self.listWidget.setObjectName("listWidget")
#         self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(40, 370, 171, 41))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(360, 370, 171, 41))
#         self.pushButton_4.setObjectName("pushButton_4")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.pushButton.setText(_translate("MainWindow", "VIDEO"))
#         self.pushButton_2.setText(_translate("MainWindow", "WEB-CAMERA"))
#         self.pushButton_3.setText(_translate("MainWindow", "Start"))
#         self.pushButton_4.setText(_translate("MainWindow", "Stop"))
#
#
# class App(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.load_video)
#         self.ui.pushButton_2.clicked.connect(self.open_webcam)
#         self.ui.pushButton_3.clicked.connect(self.start_video)
#         self.ui.pushButton_4.clicked.connect(self.stop_video)
#         self.video_size = QtCore.QSize(511, 291)
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_frame)
#
#     def load_video(self):
#         file_dialog = QtWidgets.QFileDialog(self)
#         file_dialog.setWindowTitle("Open Video File")
#         files_filter = "Video files (*.mp4 *.avi *.mkv);;All files (*.*)"
#         file_dialog.setNameFilter(files_filter)
#         if file_dialog.exec() == QtWidgets.QDialog.Accepted:
#             self.video_path = file_dialog.selectedFiles()[0]
#             self.capture = cv2.VideoCapture(self.video_path)
#             self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
#             self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())
#             self.fps = int(self.capture.get(cv2.CAP_PROP_FPS))
#
#     def open_webcam(self):
#
# #
# #
# #
# #
# #
# #
# #
#
#
#
#
#
# Form implementation generated from reading ui file 'untitled.ui'
# #
# # Created by: PyQt6 UI code generator 6.5.0
# #
# # WARNING: Any manual changes made to this file will be lost when pyuic6 is
# # run again.  Do not edit this file unless you know what you are doing.
#
#
# from PyQt6 import QtCore, QtGui, QtWidgets
#
# #
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(0, 450, 261, 61))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(300, 450, 271, 61))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
#         self.listWidget.setGeometry(QtCore.QRect(30, 30, 511, 311))
#         self.listWidget.setObjectName("listWidget")
#         self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(40, 370, 171, 41))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(360, 370, 171, 41))
#         self.pushButton_4.setObjectName("pushButton_4")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.pushButton.setText(_translate("MainWindow", "VIDEO"))
#         self.pushButton_2.setText(_translate("MainWindow", "WEB-CAMERA"))
#         self.pushButton_3.setText(_translate("MainWindow", "Start"))
#         self.pushButton_4.setText(_translate("MainWindow", "Stop"))
#
#
# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())

# import cv2
# import numpy as np
# from PyQt6 import QtCore, QtGui, QtWidgets
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(0, 450, 261, 61))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(300, 450, 271, 61))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
#         self.listWidget.setGeometry(QtCore.QRect(30, 30, 511, 311))
#         self.listWidget.setObjectName("listWidget")
#         self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(40, 370, 171, 41))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(360, 370, 171, 41))
#         self.pushButton_4.setObjectName("pushButton_4")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.pushButton.setText(_translate("MainWindow", "VIDEO"))
#         self.pushButton_2.setText(_translate("MainWindow", "WEB-CAMERA"))
#         self.pushButton_3.setText(_translate("MainWindow", "Start"))
#         self.pushButton_4.setText(_translate("MainWindow", "Stop"))
#
#
# class VideoGestureDetection(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         self.video_capture = None
#         self.timer = QtCore.QTimer()
#         self.timer.timeout.connect(self.update_frame)
#
#         self.ui.pushButton.clicked.connect(self.open_video_file)
#         self.ui.pushButton_2.clicked.connect(self.open_camera)
#         self.ui.pushButton_3.clicked.connect(self.start_video)
#         self.ui.pushButton_4.clicked.connect(self.stop_video)
#
#         self.hand_cascade = cv2.CascadeClassifier("haarcascade_hand.xml")
#
#     def open_video_file(self):
#         file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video File", "",
#                                                              "Video Files (*.mp4 *.avi *.mov)")
#         if file_name:
#             self.video_capture = cv2.VideoCapture(file_name)
#
#     def open_camera(self):
#         self.video_capture = cv2.VideoCapture(0)
#
#     def start
# import cv2
# import numpy as np
# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtCore import pyqtSlot, QTimer
# from PyQt6.QtGui import QImage, QPixmap
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(0, 450, 261, 61))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(300, 450, 271, 61))
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
#         self.listWidget.setGeometry(QtCore.QRect(30, 30, 511, 311))
#         self.listWidget.setObjectName("listWidget")
#         self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_3.setGeometry(QtCore.QRect(40, 370, 171, 41))
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
#         self.pushButton_4.setGeometry(QtCore.QRect(360, 370, 171, 41))
#         self.pushButton_4.setObjectName("pushButton_4")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.pushButton.setText(_translate("MainWindow", "VIDEO"))
#         self.pushButton_2.setText(_translate("MainWindow", "WEB-CAMERA"))
#         self.pushButton_3.setText(_translate("MainWindow", "Start"))
#         self.pushButton_4.setText(_translate("MainWindow", "Stop"))
#
#
# class App(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.pushButton.clicked.connect(self.load_video)
#         self.ui.pushButton_2.clicked.connect(self.open_webcam)
#         self.ui.pushButton_3.clicked.connect(self.start_video)
#         self.ui.pushButton_4.clicked.connect(self.stop_video)
#         self.video_size = QtCore.QSize(511, 291)
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_frame)
#
#     def load_video(self):
#         file_dialog = QtWidgets.QFileDialog(self)
#         file_dialog.setWindowTitle("Open Video File")
#         files_filter = "Video files (*.mp4 *.avi *.mkv);;All files (*.*)"
#         file_dialog.setNameFilter(files_filter)
#         if file_dialog.exec() == QtWidgets.QDialog.Accepted:
#             self.video_path = file_dialog.selectedFiles()[0]
#             self.capture = cv2.VideoCapture(self.video_path)
#             self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
#             self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())
#             self.fps = int(self.capture.get(cv2.CAP_PROP_FPS))
#

# import sys
# import cv2
# import numpy as np
# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.QtCore import QThread, pyqtSignal, Qt
# from PyQt6.QtGui import QImage, QPixmap
# from PySide6.examples.webenginewidgets.markdowneditor.ui_mainwindow import Ui_MainWindow
#
#
# class VideoThread(QThread):
#     change_pixmap_signal = pyqtSignal(np.ndarray)
#
#     def __init__(self, parent=None):
#         QThread.__init__(self, parent=parent)
#         self.play_video = False
#         self.is_webcam = False
#
#     def start_video(self, is_webcam):
#         self.is_webcam = is_webcam
#         self.play_video = True
#
#     def stop_video(self):
#         self.play_video = False
#
#     def run(self):
#         if self.is_webcam:
#             cap = cv2.VideoCapture(0)
#         else:
#             cap = cv2.VideoCapture('video.avi')
#
#         hand_cascade = cv2.CascadeClassifier('hand.xml')
#
#         while self.play_video:
#             ret, frame = cap.read()
#
#             if ret:
#                 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#                 hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
#
#                 for (x, y, w, h) in hands:
#                     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#                 # Convert frame to RGB format
#                 rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#                 # Emit the signal for display of the frame
#                 self.change_pixmap_signal.emit(rgb_image)
#
#             # Wait for 25 ms before the next iteration
#             cv2.waitKey(25)
#
#         # Release the capture object and exit the thread
#         cap.release()
#         cv2.destroyAllWindows()
#
#
# class App(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         self.video_thread = VideoThread()
#
#         self.ui.pushButton.clicked.connect(self.start_video_file)
#         self.ui.pushButton_2.clicked.connect(self.start_video_webcam)
#         self.ui.pushButton_3.clicked.connect(self.video_thread.start_video)
#         self.ui.pushButton_4.clicked.connect(self.video_thread.stop_video)
#
#         self.video_thread.change_pixmap_signal.connect(self.update_image)
#
#     def start_video_file(self):
#         self.video_thread.start_video(False)
#
#     def start_video_webcam(self):
#         self.video_thread.start_video(True)
#
#     def update_image(self, image):
#         """Updates the image_label with a new opencv image"""
#         qt_image = self.convert_cv_qt(image)
#         self.ui.label.setPixmap(qt_image)
#
#     def convert_cv_qt(self, image):
#         """Convert from an opencv image to QPixmap"""
#         rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         h, w, ch = rgb_image.shape
#         bytes_per_line = ch * w
#         convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         p = convert_to_Qt_format.scaled(self.ui.label.width(), self.ui.label.height(), Qt.KeepAspectRatio)
#         return QPixmap.fromImage(p)
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = App()
#     window.show()
#     sys.exit(app.exec())
