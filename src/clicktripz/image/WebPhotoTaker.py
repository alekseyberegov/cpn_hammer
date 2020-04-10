import uuid
from pathlib import Path

from PyQt5 import QtCore
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QApplication
from functools import partial


class WebPhotoTaker(object):
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        QApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
        QApplication.setAttribute(QtCore.Qt.AA_UseSoftwareOpenGL)
        self.app = QApplication([''])

    def take_photo(self, url):
        file = str(self.output_dir / ".".join([str(uuid.uuid4()), "pdf"]))
        self.capture(url, file)

    def capture(self, url, file):
        view = QWebEngineView()
        view.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        view.loadFinished.connect(partial(self.done, view, file))
        view.load(QUrl(url))
        self.app.exec_()

    def done(self, view, file, ok):
        if ok:
            print(file)
            frame = view.page()
            view.page().pdfPrintingFinished.connect(view.close)
            frame.printToPdf(file)

