# -*- coding: utf-8 -*-
import sip
sip.setapi('QString', 2)
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

class Ui_play_widget(object):
    def setupUi(self, play_widget):
        play_widget.setObjectName("play_widget")
        play_widget.setWindowModality(QtCore.Qt.NonModal)
        play_widget.setEnabled(True)
        play_widget.resize(435, 275)
        play_widget.setMinimumSize(QtCore.QSize(435, 275))
        play_widget.setMaximumSize(QtCore.QSize(435, 275))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./image/webicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        play_widget.setWindowIcon(icon)
        play_widget.setWindowOpacity(2.0)
        play_widget.setAutoFillBackground(False)
        play_widget.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"border:0px solid")
        play_widget.setInputMethodHints(QtCore.Qt.ImhNone)
        # 无边框
        play_widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.music_picture = QtGui.QLabel(play_widget)
        self.music_picture.setGeometry(QtCore.QRect(30, 20, 131, 131))
        self.music_picture.setPixmap(QtGui.QPixmap("./image/webicon.png"))

        self.horizontalLayoutWidget = QtGui.QWidget(play_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 180, 412, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.paused_Button = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.paused_Button.setStyleSheet("border-style:flat")
        self.paused_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./image/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.paused_Button.setIcon(icon1)
        self.paused_Button.setIconSize(QtCore.QSize(50, 50))
        self.paused_Button.setObjectName("paused_Button")
        self.horizontalLayout.addWidget(self.paused_Button)
        self.start_Button = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.start_Button.setSizeIncrement(QtCore.QSize(2, 2))
        self.start_Button.setMouseTracking(True)
        self.start_Button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.start_Button.setAcceptDrops(True)
        self.start_Button.setAutoFillBackground(False)
        self.start_Button.setStyleSheet("border-style:flat;\n"
"hover{border-image: url(:/image/play_on_ico.png);}")
        self.start_Button.setInputMethodHints(QtCore.Qt.ImhNone)
        self.start_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./image/play_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("./image/play_on_ico.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.start_Button.setIcon(icon2)
        self.start_Button.setIconSize(QtCore.QSize(50, 50))
        self.start_Button.setShortcut("")
        self.start_Button.setCheckable(False)
        self.start_Button.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.start_Button.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.start_Button.setAutoRaise(False)
        self.start_Button.setObjectName("start_Button")
        self.horizontalLayout.addWidget(self.start_Button)
        self.next_Button = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.next_Button.setStyleSheet("border-style:flat")
        self.next_Button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./image/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_Button.setIcon(icon3)
        self.next_Button.setIconSize(QtCore.QSize(50, 50))
        self.next_Button.setObjectName("next_Button")
        self.horizontalLayout.addWidget(self.next_Button)
        self.out_Button = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.out_Button.setStyleSheet("border-style:flat")
        self.out_Button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./image/out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.out_Button.setIcon(icon4)
        self.out_Button.setIconSize(QtCore.QSize(50, 50))
        self.out_Button.setObjectName("out_Button")
        self.horizontalLayout.addWidget(self.out_Button)
        self.musictime = QtGui.QLCDNumber(play_widget)
        self.musictime.setGeometry(QtCore.QRect(200, 90, 191, 61))
        self.musictime.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.musictime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.musictime.setInputMethodHints(QtCore.Qt.ImhNone)
        self.musictime.setObjectName("musictime")
        self.musicname = QtGui.QLabel(play_widget)
        self.musicname.setGeometry(QtCore.QRect(190, 20, 201, 48))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.musicname.setFont(font)
        self.musicname.setObjectName("musicname")
        #拖动条
        self.seekSlider = Phonon.SeekSlider(self)        
        self.seekSlider.setGeometry(QtCore.QRect(0, 170, 435, 8))
        self.seekSlider.setAcceptDrops(True)
        self.seekSlider.setStyleSheet("border: 0px;\n"
"border-radius: 2px;\n"
"background-color: rgb(218, 218, 218);\n"
"margin: #CD96CD;")

        self.retranslateUi(play_widget)
        QtCore.QMetaObject.connectSlotsByName(play_widget)

    def retranslateUi(self, play_widget):
        play_widget.setWindowTitle("music player")
        self.next_Button.setWhatsThis("<html><head/><body><p>next music</p></body></html>")
        self.musicname.setText("music name")

    #重写事件，鼠标拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
  
    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and QtCore.Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
  
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
        

        
        

class music_player(QtGui.QWidget,Ui_play_widget):
    def __init__(self):
        super(QtGui.QWidget, self).__init__()
        self.setupUi(self)
        self.filelist = []

        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory,self)
        self.mediaObject = Phonon.MediaObject(self)
        self.informedia = Phonon.MediaObject(self)
        #拖动条
        self.seekSlider.setMediaObject(self.mediaObject)
        self.mediaObject.setTickInterval(1000)
        Phonon.createPath(self.mediaObject, self.audioOutput)

        self.informedia.stateChanged.connect(self.metaStateChanged)
        self.mediaObject.tick.connect(self.tick)
        self.mediaObject.aboutToFinish.connect(self.aboutToFinish)
        self.musictime.display("00:00") 
        self.start_Button.clicked.connect(self.clickplay)
        self.paused_Button.clicked.connect(self.clickpaused)
        self.out_Button.clicked.connect(self.close)
        self.next_Button.clicked.connect(self.clicknext)



    def clickplay(self):
        if self.filelist:
            self.mediaObject.play()
            #self.showtitle()
    	
        
    def clickpaused(self):
      	if self.mediaObject.state() == Phonon.PlayingState:
        	self.mediaObject.pause()


    def clicknext(self):
        if not self.filelist:
            self.addFiles()
            self.mediaObject.setCurrentSource(self.filelist[0])
            self.informedia.setCurrentSource(self.filelist[0])
        else:
            index = self.filelist.index(self.mediaObject.currentSource()) + 1
            if index == len(self.filelist):
                self.addFiles()
            else:
                self.mediaObject.setCurrentSource(self.filelist[index])
                self.informedia.setCurrentSource(self.filelist[index])
                self.clickplay()                

    def tick(self,time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.musictime.display(displayTime.toString('mm:ss'))

    def aboutToFinish(self):
        self.mediaObject.enqueue(Phonon.MediaSource(self.filelist))

    def addFiles(self):
        files = QtGui.QFileDialog.getOpenFileNames(self, "Select Music",
                QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation))
        for string in files:
            self.filelist.append(Phonon.MediaSource(string))

    def showtitle(self):
        metaData = self.informedia.metaData()
        title = metaData.get('TITLE', [''])[0]
        artist = metaData.get('ARTIST', [''])[0]
        self.musicname.setText(title+'\n '+artist)
        filename = self.informedia.currentSource().fileName()
        self.setWindowTitle(filename)

    #the method of metainformation media changed
    def metaStateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            QtGui.QMessageBox.warning(self, "Error opening files",
                    self.metaInformationResolver.errorString())
            while self.filelist and self.filelist.pop() != self.metaInformationResolver.currentSource():
                pass
            return
        if newState != Phonon.StoppedState and newState != Phonon.PausedState:
            return
        if self.informedia.currentSource().type() == Phonon.MediaSource.Invalid:
            return
        self.showtitle()





def main():
    if  __name__=='__main__':
        import sys
        app = QtGui.QApplication(sys.argv)
        widget = music_player()
        widget.show()
        sys.exit(app.exec_())

main()
