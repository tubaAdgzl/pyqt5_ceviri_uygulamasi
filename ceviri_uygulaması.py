import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from ceviri import Ui_MainWindow
from textblob import TextBlob

class Ceviri(QMainWindow):
    def __init__(self):
        super(Ceviri, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.rd_entr.setChecked(True)

        self.ui.btn_cevir.clicked.connect(self.Cevir)

    def Cevir(self):

        if self.ui.rd_entr.isChecked():

            cümle1 = self.ui.txt_en.text()
            text1 = TextBlob(cümle1)
            cevir1 = text1.translate(to='tr')
            cevir1 = str(cevir1)
            self.ui.lbl_ceviri.setText(cevir1)

        elif self.ui.rd_tren.isChecked():
            cümle2 = self.ui.txt_tr.text()
            text2 = TextBlob(cümle2)
            cevir2 = text2.translate(from_lang='tr', to ='en')
            cevir2 = str(cevir2)
            self.ui.lbl_ceviri.setText(cevir2)

def Pencere():
    uyg = QApplication(sys.argv)
    pen = Ceviri()
    pen.show()
    sys.exit(uyg.exec_())

Pencere()