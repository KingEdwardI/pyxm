import sys, spotipy, base64, requests

from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QWidget, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

sp = spotipy.Spotify()

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.lineEdit = QLineEdit()
        self.button = QPushButton('Get Album')
        self.pic = QLabel()
        self.pixmap = QPixmap()

        self.LineItem = QHBoxLayout()
        self.vBox = QVBoxLayout()


        v_box = QVBoxLayout()
        v_box.addWidget(self.pic)
        v_box.addWidget(self.lineEdit)
        v_box.addWidget(self.button)

        self.setLayout(v_box)

        self.setWindowTitle('PyXm Album Cover')

        #  self.button.clicked.connect(search_album(self.lineEdit.text()))

        self.show()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Return:
            album = search_album(self.lineEdit.text())
            image = get_base64_image(album['images'][1]['url'])
            self.pixmap.loadFromData(image)
            self.pic.setPixmap(self.pixmap)


    #  def createLineItems(self, albumData):
        #  self.artistName = QLabel()
        #  self.albumName = QLabel()
        #  self.albumCover = QPixmap()
        #  self.imgWrap = QLabel()

        #  self.artistName.setText(albumData['artists'][0]['name'])
        #  self.albumName.setText(albumData['name'])
        #  self.albumCover.loadFromData(get_base64_image(albumData['images'][1]['url']))
        #  self.imgWrap.setPixmap(self.albumCover)

        #  self.vBox.addWidget(self.imgWrap)

        #  self.LineItem.addWidget(self.artistName)
        #  self.LineItem.addWidget(self.albumName)
        #  self.LineItem.addWidget(self.vBox)

        #  return self.LineItem
        

def search_album(album_query):

    results = sp.search(album_query, type='album', limit=1)
    return results['albums']['items'][0]



def get_base64_image(url):
    base_64 =  base64.b64encode(requests.get(url).content)
    return base64.b64decode(base_64)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec_())

