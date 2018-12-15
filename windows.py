from PyQt5 import QtCore, QtGui, QtWidgets
from classes import FlowLayout, Canvas

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        dialog = NewFileDialog(self)

    def setupUi(self, MainWindow):
        self.setWindowTitle('PyCasso')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)

        self.current_color = QtGui.QColor(0, 0, 0)
        self.thickness = 1
        self.fill_color = QtGui.QColor(255, 255, 255)

        self.scene = Canvas(self)
        self.viewport = QtWidgets.QGraphicsView(self.scene)
        self.viewport.setMinimumSize(300, 300)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.central_layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.central_layout.addWidget(self.viewport)
        MainWindow.setCentralWidget(self.centralwidget)

        self.initMenuBar()
        self.initToolbox()
        self.initToolProperties()
        self.initColorManager()
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def initMenuBar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self, self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self, self.statusbar)

        self.actionNew = QtWidgets.QAction(self)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(self.ask_for_file)

        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save)

        self.actionQuit = QtWidgets.QAction(self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.close)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

    def initToolbox(self):
        self.toolBox = QtWidgets.QDockWidget(self)
        self.toolBox.setObjectName("toolBox")
        self.tools = QtWidgets.QWidget()
        self.tools.setObjectName("tools")
        self.tools_grid = FlowLayout(self.tools)
        self.toolBox.setWidget(self.tools)
        names = ['Pencil', 'Line', 'Rectangle', 'Ellipse']
        self.tool_buttons = []
        for i in range(4):
            btn = QtWidgets.QPushButton(names[i], self)
            btn.clicked.connect(self.set_tool)
            self.tools_grid.addWidget(btn)
            btn.setCheckable(True)
            self.tool_buttons.append(btn)
        self.tool_buttons[0].setChecked(True)
        MainWindow.addDockWidget(self, QtCore.Qt.DockWidgetArea(1), self.toolBox)

    def initToolProperties(self):
        self.toolProperties = QtWidgets.QDockWidget(self)
        self.toolProperties.setObjectName("toolProperties")

        self.properties = QtWidgets.QWidget()
        self.properties.setObjectName("properties")

        self.properties_form = QtWidgets.QFormLayout(self.properties)
        self.thickness_lbl = QtWidgets.QLabel('Thickness', self)

        self.thickness_slider = QtWidgets.QSlider(self)
        self.thickness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.thickness_slider.setMinimum(1)
        self.thickness_slider.setMaximum(50)
        self.thickness_slider.valueChanged.connect(self.set_thickness)
        self.properties_form.addWidget(self.thickness_lbl)
        self.properties_form.addWidget(self.thickness_slider)
        self.toolProperties.setWidget(self.properties)
        MainWindow.addDockWidget(self, QtCore.Qt.DockWidgetArea(1), self.toolProperties)

    def initColorManager(self):
        self.colorManagement = QtWidgets.QDockWidget(self)
        self.colorManagement.setObjectName("colorManagement")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")

        # Сетка, содержащая элементы управления цветом
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40,
                                           QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Создание виджета со вкладками
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")

        # Лейаут для RGB-палитры
        self.rgb_color_sliders = QtWidgets.QWidget()
        self.rgb_color_sliders.setObjectName("rgb_color_sliders")
        self.formLayout = QtWidgets.QFormLayout(self.rgb_color_sliders)
        self.formLayout.setObjectName("formLayout")

        # Red-канал для RGB-палитры
        self.red_lbl = QtWidgets.QLabel(self.rgb_color_sliders)
        self.red_lbl.setObjectName("red_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.red_lbl)
        self.red_slider = QtWidgets.QSlider(self.rgb_color_sliders)
        self.red_slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_slider.setObjectName("red_slider")
        self.red_slider.setMaximum(255)
        self.red_slider.sliderMoved.connect(self.adjustColorSliders)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.red_slider)

        # Green-канал для RGB-палитры
        self.green_lbl = QtWidgets.QLabel(self.rgb_color_sliders)
        self.green_lbl.setObjectName("green_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.green_lbl)
        self.green_slider = QtWidgets.QSlider(self.rgb_color_sliders)
        self.green_slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_slider.setObjectName("green_slider")
        self.green_slider.setMaximum(255)
        self.green_slider.sliderMoved.connect(self.adjustColorSliders)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.green_slider)

        # Blue-канал для RGB-палитры
        self.blue_lbl = QtWidgets.QLabel(self.rgb_color_sliders)
        self.blue_lbl.setObjectName("blue_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.blue_lbl)
        self.blue_slider = QtWidgets.QSlider(self.rgb_color_sliders)
        self.blue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blue_slider.setObjectName("blue_slider")
        self.blue_slider.setMaximum(255)
        self.blue_slider.sliderMoved.connect(self.adjustColorSliders)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.blue_slider)

        # Альфа-канал для RGB-палитры
        self.alpha_lbl_rgb = QtWidgets.QLabel(self.rgb_color_sliders)
        self.alpha_lbl_rgb.setObjectName("alpha_lbl_rgb")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alpha_lbl_rgb)
        self.alpha_rgb_slider = QtWidgets.QSlider(self.rgb_color_sliders)
        self.alpha_rgb_slider.setOrientation(QtCore.Qt.Horizontal)
        self.alpha_rgb_slider.setObjectName("alpha_rgb_slider")
        self.alpha_rgb_slider.setMaximum(255)
        self.alpha_rgb_slider.setValue(255)
        self.alpha_rgb_slider.sliderMoved.connect(self.adjustColorSliders)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.alpha_rgb_slider)
        self.tabWidget.addTab(self.rgb_color_sliders, "")

        # Лейаут для слайдеров HSV-палитры
        self.hsv_color_sliders = QtWidgets.QWidget()
        self.hsv_color_sliders.setObjectName("hsv_color_sliders")
        self.formLayout_2 = QtWidgets.QFormLayout(self.hsv_color_sliders)
        self.formLayout_2.setObjectName("formLayout_2")

        # Hue-канал для HSV-палитры
        self.hue_lbl = QtWidgets.QLabel(self.hsv_color_sliders)
        self.hue_lbl.setObjectName("hue_lbl")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hue_lbl)
        self.hue_slider = QtWidgets.QSlider(self.hsv_color_sliders)
        self.hue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.hue_slider.setObjectName("hue_slider")
        self.hue_slider.setMaximum(359)
        self.hue_slider.sliderMoved.connect(self.adjustColorSliders)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hue_slider)

        # Saturation-канал для HSV-палитры
        self.saturation_lbl = QtWidgets.QLabel(self.hsv_color_sliders)
        self.saturation_lbl.setObjectName("saturation_lbl")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.saturation_lbl)
        self.saturation_slider = QtWidgets.QSlider(self.hsv_color_sliders)
        self.saturation_slider.setOrientation(QtCore.Qt.Horizontal)
        self.saturation_slider.setObjectName("saturation_slider")
        self.saturation_slider.setMaximum(255)
        self.saturation_slider.sliderMoved.connect(self.adjustColorSliders)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.saturation_slider)

        # Value-канал для HSV-палитры
        self.value_lbl = QtWidgets.QLabel(self.hsv_color_sliders)
        self.value_lbl.setObjectName("value_lbl")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.value_lbl)
        self.value_slider = QtWidgets.QSlider(self.hsv_color_sliders)
        self.value_slider.setOrientation(QtCore.Qt.Horizontal)
        self.value_slider.setObjectName("value_slider")
        self.value_slider.setMaximum(255)
        self.value_slider.sliderMoved.connect(self.adjustColorSliders)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.value_slider)

        # Альфа-канал для HSV-палитры
        self.alpha_lbl_hsv = QtWidgets.QLabel(self.hsv_color_sliders)
        self.alpha_lbl_hsv.setObjectName("alpha_lbl_hsv")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alpha_lbl_hsv)
        self.alpha_hsv_slider = QtWidgets.QSlider(self.hsv_color_sliders)
        self.alpha_hsv_slider.setOrientation(QtCore.Qt.Horizontal)
        self.alpha_hsv_slider.setObjectName("alpha_hsv_slider")
        self.alpha_hsv_slider.setMaximum(255)
        self.alpha_hsv_slider.setValue(255)
        self.alpha_hsv_slider.sliderMoved.connect(self.adjustColorSliders)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                    self.alpha_hsv_slider)
        self.tabWidget.addTab(self.hsv_color_sliders, "")

        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40,
                                            QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 3)

        # Кнопка с текущим цветом
        self.current_color_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_color_btn.sizePolicy().hasHeightForWidth())
        self.current_color_btn.setSizePolicy(sizePolicy)
        self.current_color_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.current_color_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.current_color_btn.setText("")
        self.current_color_btn.setObjectName("color_preview_btn")
        self.current_color_btn.setStyleSheet('background-color: #000000')
        self.gridLayout.addWidget(self.current_color_btn, 2, 1, 1, 1)
        self.color_pick_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        self.color_pick_btn.setObjectName("color_pick_btn")
        self.color_pick_btn.clicked.connect(self.getColorWithDialog)
        self.gridLayout.addWidget(self.color_pick_btn, 1, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0,
                                            QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        # Палитра готовых цветов
        self.colorPalette = FlowLayout()

        # Набор цветов для кнопок
        sampleColors = [QtGui.QColor(255, 255, 255),
                        QtGui.QColor(0, 0, 0),
                        QtGui.QColor(127, 127, 127),
                        QtGui.QColor(195, 195, 195),
                        QtGui.QColor(136, 0, 21),
                        QtGui.QColor(185, 122, 87),
                        QtGui.QColor(237, 28, 36),
                        QtGui.QColor(255, 174, 201),
                        QtGui.QColor(255, 127, 39),
                        QtGui.QColor(255, 201, 14),
                        QtGui.QColor(255, 242, 0),
                        QtGui.QColor(239, 228, 176),
                        QtGui.QColor(34, 177, 76),
                        QtGui.QColor(181, 230, 29),
                        QtGui.QColor(0, 162, 232),
                        QtGui.QColor(153, 217, 234),
                        QtGui.QColor(63, 72, 204),
                        QtGui.QColor(112, 146, 190),
                        QtGui.QColor(163, 73, 164),
                        QtGui.QColor(200, 191, 231)]

        # Создание кнопок
        for i in range(20):
            btn = QtWidgets.QPushButton("", self)
            btn.setMaximumSize(20, 20)
            # Смена цвета кнопки
            btn.setStyleSheet('background-color: ' + sampleColors[i].name())
            btn.clicked.connect(self.setCurrentColor)
            btn.show()
            self.colorPalette.addWidget(btn)
        # Занесение палитры в общий блок управления цветом
        self.gridLayout_2.addLayout(self.colorPalette, 1, 0, 1, 3)
        self.colorManagement.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(self, QtCore.Qt.DockWidgetArea(2), self.colorManagement)

    def adjustColorSliders(self):
        rgb = {self.red_slider, self.green_slider, self.blue_slider, self.alpha_rgb_slider}
        hsv = {self.hue_slider, self.saturation_slider, self.value_slider, self.alpha_hsv_slider}
        if self.sender() in rgb:
            red = self.red_slider.value()
            green = self.green_slider.value()
            blue = self.blue_slider.value()
            alpha = self.alpha_rgb_slider.value()
            color = QtGui.QColor(red, green, blue, alpha)
            if color.isValid():
                self.current_color_btn.setStyleSheet('background-color: ' + color.name())
                self.current_color = color
                hsv_color = color.toHsv()
                self.hue_slider.setValue(hsv_color.hue())
                self.saturation_slider.setValue(hsv_color.saturation())
                self.value_slider.setValue(hsv_color.value())
                self.alpha_hsv_slider.setValue(hsv_color.alpha())
        elif self.sender() in hsv:
            hue = self.hue_slider.value()
            saturation = self.saturation_slider.value()
            value = self.value_slider.value()
            alpha = self.alpha_hsv_slider.value()
            color = QtGui.QColor.fromHsv(hue, saturation, value, alpha)
            if color.isValid():
                self.current_color_btn.setStyleSheet('background-color: ' + color.name())
                self.current_color = color
                rgb_color = color.toRgb()
                self.red_slider.setValue(rgb_color.red())
                self.green_slider.setValue(rgb_color.green())
                self.blue_slider.setValue(rgb_color.blue())
                self.alpha_rgb_slider.setValue(rgb_color.alpha())
        else:
            rgb_color = self.current_color.toRgb()
            self.red_slider.setValue(rgb_color.red())
            self.green_slider.setValue(rgb_color.green())
            self.blue_slider.setValue(rgb_color.blue())
            self.alpha_rgb_slider.setValue(rgb_color.alpha())

            hsv_color = self.current_color.toHsv()
            self.hue_slider.setValue(hsv_color.hue())
            self.saturation_slider.setValue(hsv_color.saturation())
            self.value_slider.setValue(hsv_color.value())
            self.alpha_hsv_slider.setValue(hsv_color.alpha())

    def setCurrentColor(self):
        color = QtGui.QColor(self.sender().styleSheet().split()[-1])
        if color.isValid():
            self.current_color = color
            self.current_color_btn.setStyleSheet('background-color: ' + color.name())
            self.adjustColorSliders()

    def getColorWithDialog(self):
        color = QtWidgets.QColorDialog.getColor(self.current_color)
        if color.isValid():
            self.current_color = color
            self.current_color_btn.setStyleSheet('background-color: ' + color.name())
            self.adjustColorSliders()

    def load_image(self, image):
        if image is None:
            image = QtGui.QPixmap(500, 500)
            image.fill(QtGui.QColor(255, 255, 255, 0))
            image = image.toImage()
            self.scene.load_image(image)
            self.viewport.setMaximumSize(image.size())
        else:
            try:
                with open(image):
                    pass
            except FileNotFoundError:
                error = QtWidgets.QErrorMessage(self)
                error.showMessage('Specified file does not exist!')
            else:
                image = QtGui.QImage(image)
                self.scene.load_image(image)
                self.viewport.setMaximumSize(image.size())

    def save(self):
        title = 'Pick a place to save your file'
        files = 'Image Files (*.png *.jpg *.jpeg *.bmp *.ppm *.xbm *.xpm)'
        path, ok = QtWidgets.QFileDialog.getSaveFileName(self.parent(), caption=title,
                                                         filter=files)
        if ok:
            self.scene.image.save(path)

    def set_tool(self):
        for btn in self.tool_buttons:
            btn.setChecked(False)
        self.sender().setChecked(True)
        self.scene.tool = self.sender().text().lower()

    def set_thickness(self):
        self.thickness = self.sender().value()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBox.setWindowTitle(_translate("MainWindow", "Tools"))
        self.toolProperties.setWindowTitle(_translate("MainWindow", "Tool properties"))
        self.colorManagement.setWindowTitle(_translate("MainWindow", "Color Management"))
        self.red_lbl.setText(_translate("MainWindow", "R"))
        self.green_lbl.setText(_translate("MainWindow", "G"))
        self.blue_lbl.setText(_translate("MainWindow", "B"))
        self.alpha_lbl_rgb.setText(_translate("MainWindow", "A"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rgb_color_sliders), _translate("MainWindow", "RGB"))
        self.hue_lbl.setText(_translate("MainWindow", "H"))
        self.saturation_lbl.setText(_translate("MainWindow", "S"))
        self.value_lbl.setText(_translate("MainWindow", "V"))
        self.alpha_lbl_hsv.setText(_translate("MainWindow", "A"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hsv_color_sliders), _translate("MainWindow", "HSV"))
        self.color_pick_btn.setText(_translate("MainWindow", "Pick with dialog"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "Create a new file and open it immediately"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save current file"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Shutdown program"))

    def ask_for_file(self):
        dialog = NewFileDialog(self)

        self.viewport.close()
        self.scene = Canvas(self)
        self.viewport = QtWidgets.QGraphicsView(self.scene, self)
        self.central_layout.addWidget(self.viewport)
        self.viewport.show()
        self.viewport.setMinimumSize(300, 300)


class NewFileDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.show()

    def setupUi(self, NewFileDialog):
        self.setWindowTitle('New file')
        NewFileDialog.setObjectName("NewFileDialog")
        NewFileDialog.resize(280, 100)
        self.gridLayout = QtWidgets.QGridLayout(NewFileDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.browse_btn = QtWidgets.QPushButton(NewFileDialog)
        self.browse_btn.setObjectName("browse")
        self.browse_btn.clicked.connect(self.setSourceFile)
        self.browse_btn.hide()
        self.gridLayout.addWidget(self.browse_btn, 7, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 2, 3, 1)
        self.source_input = QtWidgets.QLineEdit('', NewFileDialog)
        self.source_input.setObjectName("source_input")
        self.source_input.hide()
        self.gridLayout.addWidget(self.source_input, 7, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.open_radio = QtWidgets.QRadioButton(NewFileDialog)
        self.open_radio.setObjectName("open_radio")
        self.open_radio.toggled.connect(self.showInput)
        self.gridLayout.addWidget(self.open_radio, 1, 0, 1, 1)
        self.create_radio = QtWidgets.QRadioButton(NewFileDialog)
        self.create_radio.setChecked(True)
        self.create_radio.setObjectName("radioButton")
        self.create_radio.toggled.connect(self.hideInput)
        self.gridLayout.addWidget(self.create_radio, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 3)

        self.retranslateUi(NewFileDialog)
        self.buttonBox.accepted.connect(NewFileDialog.accept)
        self.buttonBox.rejected.connect(NewFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewFileDialog)

    def retranslateUi(self, NewFileDialog):
        _translate = QtCore.QCoreApplication.translate
        NewFileDialog.setWindowTitle(_translate("NewFileDialog", "New file"))
        self.browse_btn.setText(_translate("NewFileDialog", "Browse"))
        self.open_radio.setText(_translate("NewFileDialog", "Open"))
        self.create_radio.setText(_translate("NewFileDialog", "Create"))

    def setSourceFile(self):
        title = 'Pick an image'
        files = 'Image Files (*.png *.jpg *.jpeg *.bmp *.ppm *.xbm *.xpm *.gif *.pbm *.pgm)'
        path, ok = QtWidgets.QFileDialog.getOpenFileName(self.parent(), caption=title, filter=files)
        if ok:
            self.source_input.setText(path)

    def hideInput(self):
        self.source_input.hide()
        self.browse_btn.hide()

    def showInput(self):
        self.source_input.show()
        self.browse_btn.show()

    def accept(self):
        super().accept()
        self.parent().load_image(self.source_input.text() if self.open_radio.isChecked() else None)
