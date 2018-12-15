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
        self.thickness = 10

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
        self.initNavigator()
        self.initColorManager()
        self.initLayerManager()
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def initMenuBar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self, self.menubar)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self, self.statusbar)

        self.actionNavigator = QtWidgets.QAction(self)
        self.actionNavigator.setCheckable(True)
        self.actionNavigator.setObjectName("actionNavigator")

        self.actionColor_management = QtWidgets.QAction(self)
        self.actionColor_management.setCheckable(True)
        self.actionColor_management.setObjectName("actionColor_management")

        self.actionTools = QtWidgets.QAction(self)
        self.actionTools.setCheckable(True)
        self.actionTools.setObjectName("actionTools")

        self.actionLayers = QtWidgets.QAction(self)
        self.actionLayers.setCheckable(True)
        self.actionLayers.setObjectName("actionLayers")

        self.actionLayers_2 = QtWidgets.QAction(self)
        self.actionLayers_2.setCheckable(True)
        self.actionLayers_2.setObjectName("actionLayers_2")

        self.actionUndo = QtWidgets.QAction(self)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.triggered.connect(self.undo)
        self.actionUndo.setShortcut('Ctrl+Z')

        self.actionRedo = QtWidgets.QAction(self)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRedo.triggered.connect(self.redo)
        self.actionRedo.setShortcut('Ctrl+Y')

        self.actionSelect_all = QtWidgets.QAction(self)
        self.actionSelect_all.setObjectName("actionSelect_all")

        self.actionDeselect = QtWidgets.QAction(self)
        self.actionDeselect.setObjectName("actionDeselect")

        self.actionInvert_selection = QtWidgets.QAction(self)
        self.actionInvert_selection.setObjectName("actionInvert_selection")

        self.actionNew = QtWidgets.QAction(self)
        self.actionNew.setObjectName("actionNew")

        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save)

        self.actionQuit = QtWidgets.QAction(self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.close)

        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_all)
        self.menuEdit.addAction(self.actionDeselect)
        self.menuEdit.addAction(self.actionInvert_selection)
        self.menuView.addAction(self.actionNavigator)
        self.menuView.addAction(self.actionColor_management)
        self.menuView.addAction(self.actionTools)
        self.menuView.addAction(self.actionLayers)
        self.menuView.addAction(self.actionLayers_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

    def initToolbox(self):
        self.toolBox = QtWidgets.QDockWidget(self)
        self.toolBox.setObjectName("toolBox")
        self.tools = QtWidgets.QWidget()
        self.tools.setObjectName("tools")
        self.toolBox.setWidget(self.tools)
        MainWindow.addDockWidget(self, QtCore.Qt.DockWidgetArea(1), self.toolBox)

    def initToolProperties(self):
        self.toolProperties = QtWidgets.QDockWidget(self)
        self.toolProperties.setObjectName("toolProperties")
        self.properties = QtWidgets.QWidget()
        self.properties.setObjectName("properties")
        self.toolProperties.setWidget(self.properties)
        MainWindow.addDockWidget(self, QtCore.Qt.DockWidgetArea(1), self.toolProperties)

    def initNavigator(self):
        self.navigatorDock = QtWidgets.QDockWidget(self)
        self.navigatorDock.setObjectName("navigatorDock")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.navigatorDock.setWidget(self.widget)
        MainWindow.addDockWidget(self, QtCore.Qt.DockWidgetArea(2),
                                 self.navigatorDock)

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

    def initLayerManager(self):
        self.layerManagement = QtWidgets.QDockWidget(self)
        self.layerManagement.setObjectName("layerManagement")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layersContainer = QtWidgets.QScrollArea(self.dockWidgetContents_5)
        self.layersContainer.setWidgetResizable(True)
        self.layersContainer.setObjectName("layersContainer")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 226, 87))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layersContainer.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.layersContainer)
        self.layerManagement.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(self, QtCore.Qt.DockWidgetArea(2),
                                 self.layerManagement)

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.toolBox.setWindowTitle(_translate("MainWindow", "Tools"))
        self.toolProperties.setWindowTitle(_translate("MainWindow", "Tool properties"))
        self.navigatorDock.setWindowTitle(_translate("MainWindow", "Navigator"))
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
        self.layerManagement.setWindowTitle(_translate("MainWindow", "Layers and channels"))
        self.actionNavigator.setText(_translate("MainWindow", "Navigator"))
        self.actionNavigator.setToolTip(_translate("MainWindow", "Your current position relative to the image"))
        self.actionColor_management.setText(_translate("MainWindow", "Color management"))
        self.actionColor_management.setToolTip(_translate("MainWindow", "Color preset palette and custom color sliders"))
        self.actionTools.setText(_translate("MainWindow", "Tools"))
        self.actionTools.setToolTip(_translate("MainWindow", "Drawing tools"))
        self.actionLayers.setText(_translate("MainWindow", "Tool properties"))
        self.actionLayers.setToolTip(_translate("MainWindow", "Properties for currently selected tool"))
        self.actionLayers_2.setText(_translate("MainWindow", "Layers"))
        self.actionLayers_2.setToolTip(_translate("MainWindow", "Layer management (visibility, masks, channels)"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setToolTip(_translate("MainWindow", "Undo last action"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setToolTip(_translate("MainWindow", "Redo last reverted action"))
        self.actionSelect_all.setText(_translate("MainWindow", "Select all"))
        self.actionSelect_all.setToolTip(_translate("MainWindow", "Select all pixels"))
        self.actionDeselect.setText(_translate("MainWindow", "Deselect"))
        self.actionDeselect.setToolTip(_translate("MainWindow", "Reset selection"))
        self.actionInvert_selection.setText(_translate("MainWindow", "Invert selection"))
        self.actionInvert_selection.setToolTip(_translate("MainWindow", "Selects only currently unselected pixels"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "Create a new file and open it immediately"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Load an existing file"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save current file"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Shutdown program"))

    def load_image(self, image):
        if image is None:
            image = QtGui.QPixmap(500, 500)
            image.fill(QtGui.QColor(255, 255, 255, 0))
            image = image.toImage()
        self.scene.load_image(image)
        self.viewport.setMaximumSize(image.size())

    def save(self):
        title = 'Pick a place to save your file'
        files = 'Image Files (*.png *.jpg *.jpeg *.bmp *.ppm *.xbm *.xpm)'
        path, ok = QtWidgets.QFileDialog.getSaveFileName(self.parent(), caption=title,
                                                         filter=files)
        if ok:
            self.scene.image.save(path)

    def undo(self):
        try:
            self.scene.undo()
        except IndexError:
            pass
        except TypeError:
            pass

    def redo(self):
        try:
            self.scene.redo()
        except IndexError:
            pass


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
        self.view_btn = QtWidgets.QPushButton(NewFileDialog)
        self.view_btn.setObjectName("view_btn")
        self.view_btn.clicked.connect(self.setSourceFile)
        self.view_btn.hide()
        self.gridLayout.addWidget(self.view_btn, 7, 2, 1, 1)
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
        self.view_btn.setText(_translate("NewFileDialog", "View"))
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
        self.view_btn.hide()

    def showInput(self):
        self.source_input.show()
        self.view_btn.show()

    def accept(self):
        super().accept()
        self.parent().load_image(self.source_input.text() if self.open_radio.isChecked() else None)


class OpacityFillDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        self.setWindowTitle('Alpha layers is not supported')
        Dialog.setObjectName("OpacityFillDialog")
        Dialog.resize(300, 120)
        self.color = QtGui.QColor(255, 255, 255)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAcceptDrops(False)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.filler_color_btn = QtWidgets.QPushButton(Dialog)
        self.filler_color_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.filler_color_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.filler_color_btn.setText("")
        self.filler_color_btn.setObjectName("pushButton")
        self.filler_color_btn.setStyleSheet('background-color: #FFFFFF')
        self.filler_color_btn.clicked.connect(self.setColor)
        self.gridLayout.addWidget(self.filler_color_btn, 0, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setColor(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.filler_color_btn.setStyleSheet('background-color: ' + color.name())
            self.color = color

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("OpacityFillDialog", "Alpha layer is not supported"))
        self.label.setText(_translate("Dialog", "Chosen format does not support alpha-channels (opacity). You can save the ."))

    def accept(self):
        super().accept()
        return self.color
