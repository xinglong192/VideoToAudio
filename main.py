import sys
from concurrent.futures import ThreadPoolExecutor

from PySide6.QtCore import Slot, QCoreApplication
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
from moviepy.video.io.VideoFileClip import VideoFileClip
from proglog import ProgressBarLogger

from ui_mainWindow import Ui_MainWindow


class MyLogger(ProgressBarLogger):
    func = None

    def __init__(self, init_state=None, bars=None, ignored_bars=None,
                 logged_bars='all', min_time_interval=0, ignore_bars_under=0, callback=None):
        super(MyLogger, self).__init__(init_state, bars, ignored_bars,
                                       logged_bars, min_time_interval, ignore_bars_under)
        self.func = callback

    def bars_callback(self, bar, attr, value, old_value=None):
        if self.func:
            self.func(value, self.bars['chunk']['total'])


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.tpool = ThreadPoolExecutor(max_workers=1)

    @Slot()
    def on_btnSrc_clicked(self):
        fd = QFileDialog.getOpenFileNames()
        self.lSrcPath.setText(';'.join(fd[0]))

    @Slot()
    def on_btnSave_clicked(self):
        fd = QFileDialog.getExistingDirectory()
        self.lSavePath.setText(fd)

    @Slot()
    def on_btnCommit_clicked(self):
        sp = self.lSrcPath.text()
        tp = self.lSavePath.text()
        ff = self.boxFormat.currentText()
        d = sp.split(';')

        if not sp or not tp:
            QMessageBox.warning(self, '提示', '请选择源文件' if not sp else '请选择存储文件夹')
            return
        try:
            self.process_file(d, tp, ff)
        except Exception as e:
            QMessageBox.critical(self, '错误', e)

    def process_file(self, src: list, target: str, suffix: str):
        try:
            self.btnSrc.setDisabled(True)
            self.btnSave.setDisabled(True)
            self.btnCommit.setDisabled(True)
            self.boxFormat.setDisabled(True)
            flag = False

            def callProBar(val, total):
                """ 进度条 """
                QCoreApplication.processEvents()
                nonlocal flag
                if not flag:
                    self.progressBar.setMaximum(total)
                    flag = True
                self.progressBar.setValue(val)

            for f in src:
                # 要转换的文件
                video = VideoFileClip(f)
                audio = video.audio
                # 转换为的文件
                saveName = f[f.rfind('/'):f.rfind('.')]
                # 设置状态栏显示
                self.sbV.showMessage(f'正在转换:{saveName}文件')
                log = MyLogger(callback=callProBar)
                audio.write_audiofile(filename=''.join([target, saveName, '.', suffix]), logger=log)
                flag = False
                self.sbV.showMessage(f'{saveName}文件转换完成')
                audio.close()
                video.close()

        except Exception as e:
            QMessageBox.critical(self, '错误', e)
        finally:
            self.sbV.showMessage('完成')
            self.btnSrc.setEnabled(True)
            self.btnSave.setEnabled(True)
            self.btnCommit.setEnabled(True)
            self.boxFormat.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
