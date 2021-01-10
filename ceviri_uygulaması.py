import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox
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
            cümle_en= self.ui.txt_en.toPlainText()
            if cümle_en:
                try:
                    text_en = TextBlob(cümle_en)
                    cevir_en = text_en.translate(to='tr')
                    cevir_en= str(cevir_en)
                    self.ui.txt_ceviri.setText(cevir_en)
                except:
                    self.message("Uyarı","<p style='color:#000;font-size:14px;'>\
                                Lütfen İngilizce bir metin girin!</p>")
            else:
                self.message("Uyarı","<p style='color:#000;font-size:14px;'>\
                            Çevirmek için bir şeyler yazın!</p>")

        elif self.ui.rd_tren.isChecked():
            cümle_tr = self.ui.txt_tr.toPlainText()
            if cümle_tr:
                try:
                    text_tr = TextBlob(cümle_tr)
                    cevir_tr = text_tr.translate(from_lang='tr', to ='en')
                    cevir_tr = str(cevir_tr)
                    self.ui.txt_ceviri.setText(cevir_tr)
                except:
                    self.message("Uyarı","<p style='color:#000;font-size:14px;'>\
                                  Lütfen Türkçe bir metin girin!</p>")
            else:
                self.message("Uyarı", "<p style='color:#000;font-size:14px;'>\
                             Çevirmek için bir şeyler yazın!</p>")


    def message(self,title,text):
        mesaj=QMessageBox(self)
        mesaj.setIcon(QMessageBox.Warning)
        mesaj.setWindowTitle(title)
        mesaj.setText(text)
        mesaj.setStandardButtons(QMessageBox.Ok)
        btn_tamam=mesaj.button(QMessageBox.Ok)
        btn_tamam.setText("Tamam")

        mesaj.exec_()

def Pencere():
    uyg = QApplication(sys.argv)
    pen = Ceviri()
    pen.show()
    sys.exit(uyg.exec_())

Pencere()