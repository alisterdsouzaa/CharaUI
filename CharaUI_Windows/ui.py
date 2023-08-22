import sys
import pyqtgraph as pg
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.graphWidget = None
        self.title = "Chara Ui"
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1000, 600)

        # Adding Icon to Application Logo
        application_icon = QIcon("logo/chara_logo.png")
        self.setWindowIcon(application_icon)

        # Layout of buttons and elements architecture in VBox And then
        # adding all these horizontal layouts add in the main VBox
        mainWindow = QVBoxLayout()
        graphLayout = QHBoxLayout()
        zerothHorizontalLayout = QHBoxLayout()
        firstHorizontalLayout = QHBoxLayout()
        secondHorizontalLayout = QHBoxLayout()
        thirdHorizontalLayout = QHBoxLayout()

        # Creating Graph
        # self.graphWidget = pg.PlotWidget()
        # self.graphWidget.setBackground('w')  # Set background color to white
        # graphLayout.addWidget(self.graphWidget)  # Add the graph to the graphLayout

        # Stretching all the buttons towards the bottom
        mainWindow.addStretch()

        # Zeroth Row Horizontal Elements / Buttons
        dropDownBox1 = QComboBox(self)
        dropDownBox1.addItems(["Serial", "Parallel"])
        zerothHorizontalLayout.addWidget(dropDownBox1)

        samplesSpinBox = QSpinBox()
        samplesSpinBox.setMinimum(1)
        samplesSpinBox.setMaximum(10000)
        samplesSpinBox.setValue(500)
        samplesSpinBox.setSuffix(" samples")
        zerothHorizontalLayout.addWidget(samplesSpinBox)

        start_button = QPushButton("Start")
        zerothHorizontalLayout.addWidget(start_button)

        openParamFile_button = QPushButton("Open Param File")
        zerothHorizontalLayout.addWidget(openParamFile_button)

        update_button = QPushButton("Update")
        zerothHorizontalLayout.addWidget(update_button)

        # First Row Horizontal Buttons
        varLabel = QLabel(self)
        varLabel.setText("PARAM")
        firstHorizontalLayout.addWidget(varLabel)

        varAddressInHex = QLineEdit(self)
        varAddressInHex.setPlaceholderText("Address in Hex")
        firstHorizontalLayout.addWidget(varAddressInHex)

        varDataInInt = QLineEdit(self)
        varDataInInt.setPlaceholderText("Data in Int")
        firstHorizontalLayout.addWidget(varDataInInt)

        varSet_button = QPushButton("Param Set")
        firstHorizontalLayout.addWidget(varSet_button)

        varGet_button = QPushButton("Param Get")
        firstHorizontalLayout.addWidget(varGet_button)

        varGetDisplayField = QLineEdit(self)
        firstHorizontalLayout.addWidget(varGetDisplayField)

        # Second Row Horizontal Buttons --> VAR
        varLabel = QLabel(self)
        varLabel.setText("VAR     ")
        secondHorizontalLayout.addWidget(varLabel)

        varAddressInHex = QLineEdit(self)
        varAddressInHex.setPlaceholderText("Address in Hex")
        secondHorizontalLayout.addWidget(varAddressInHex)

        varDataInInt = QLineEdit(self)
        varDataInInt.setPlaceholderText("Data in Int")
        secondHorizontalLayout.addWidget(varDataInInt)

        varSet_button = QPushButton("Var Set")
        secondHorizontalLayout.addWidget(varSet_button)

        varGet_button = QPushButton("Var Get")
        secondHorizontalLayout.addWidget(varGet_button)

        varGetDisplayField = QLineEdit(self)
        secondHorizontalLayout.addWidget(varGetDisplayField)

        # Third Row Horizontal Buttons / QLine's
        stream1Addr = QLineEdit(self)
        stream1Addr.setPlaceholderText("Stream 1 Addr")
        thirdHorizontalLayout.addWidget(stream1Addr)

        stream2Addr = QLineEdit(self)
        stream2Addr.setPlaceholderText("Stream 2 Addr")
        thirdHorizontalLayout.addWidget(stream2Addr)

        stream3Addr = QLineEdit(self)
        stream3Addr.setPlaceholderText("Stream 3 Addr")
        thirdHorizontalLayout.addWidget(stream3Addr)

        stream4Addr = QLineEdit(self)
        stream4Addr.setPlaceholderText("Stream 4 Addr")
        thirdHorizontalLayout.addWidget(stream4Addr)

        stream5Addr = QLineEdit(self)
        stream5Addr.setPlaceholderText("Stream 5 Addr")
        thirdHorizontalLayout.addWidget(stream5Addr)

        streamTimeInterval = QLineEdit(self)
        streamTimeInterval.setPlaceholderText("Stream Time Interval")
        thirdHorizontalLayout.addWidget(streamTimeInterval)

        updateStream_button = QPushButton(self)
        updateStream_button.setText("Update Stream")
        thirdHorizontalLayout.addWidget(updateStream_button)

        mainWindow.addLayout(graphLayout)
        mainWindow.addLayout(zerothHorizontalLayout)
        mainWindow.addLayout(firstHorizontalLayout)
        mainWindow.addLayout(secondHorizontalLayout)
        mainWindow.addLayout(thirdHorizontalLayout)

        centralWidget = QWidget(self)
        centralWidget.setLayout(mainWindow)
        self.setCentralWidget(centralWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
