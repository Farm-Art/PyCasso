# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBox = QtWidgets.QDockWidget(MainWindow)
        self.toolBox.setObjectName("toolBox")
        self.tools = QtWidgets.QWidget()
        self.tools.setObjectName("tools")
        self.toolBox.setWidget(self.tools)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.toolBox)
        self.toolProperties = QtWidgets.QDockWidget(MainWindow)
        self.toolProperties.setObjectName("toolProperties")
        self.properties = QtWidgets.QWidget()
        self.properties.setObjectName("properties")
        self.toolProperties.setWidget(self.properties)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.toolProperties)
        self.navigatorDock = QtWidgets.QDockWidget(MainWindow)
        self.navigatorDock.setObjectName("navigatorDock")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.navigatorDock.setWidget(self.widget)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.navigatorDock)
        self.colorManagement = QtWidgets.QDockWidget(MainWindow)
        self.colorManagement.setObjectName("colorManagement")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 10, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, 6, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.rgb_color_sliders = QtWidgets.QWidget()
        self.rgb_color_sliders.setObjectName("rgb_color_sliders")
        self.formLayout = QtWidgets.QFormLayout(self.rgb_color_sliders)
        self.formLayout.setObjectName("formLayout")
        self.red_lbl = QtWidgets.QLabel(self.rgb_color_sliders)
        self.red_lbl.setObjectName("red_lbl")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.red_lbl)
        self.red_slider = QtWidgets.QSlider(self.rgb_color_sliders)
        self.red_slider.setOrientation(QtCore.Qt.Horizontal)
        self.red_slider.setObjectName("red_slider")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.red_slider)
        self.green_lbl = QtWidgets.QLabel(self.rgb_color_sliders)
        self.green_lbl.setObjectName("green_lbl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.green_lbl)
        self.green_rgb_slider = QtWidgets.QSlider(self.rgb_color_sliders)
        self.green_rgb_slider.setOrientation(QtCore.Qt.Horizontal)
        self.green_rgb_slider.setObjectName("green_rgb_slider")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.green_rgb_slider)
        self.blue_lbl = QtWidgets.QLabel(self.rgb_color_sliders)
        self.blue_lbl.setObjectName("blue_lbl")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.blue_lbl)
        self.blue_rgb_slider = QtWidgets.QSlider(self.rgb_color_sliders)
        self.blue_rgb_slider.setOrientation(QtCore.Qt.Horizontal)
        self.blue_rgb_slider.setObjectName("blue_rgb_slider")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.blue_rgb_slider)
        self.alpha_lbl_rgb = QtWidgets.QLabel(self.rgb_color_sliders)
        self.alpha_lbl_rgb.setObjectName("alpha_lbl_rgb")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alpha_lbl_rgb)
        self.alpha_rgb_slider = QtWidgets.QSlider(self.rgb_color_sliders)
        self.alpha_rgb_slider.setOrientation(QtCore.Qt.Horizontal)
        self.alpha_rgb_slider.setObjectName("alpha_rgb_slider")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.alpha_rgb_slider)
        self.tabWidget.addTab(self.rgb_color_sliders, "")
        self.hsv_color_sliders = QtWidgets.QWidget()
        self.hsv_color_sliders.setObjectName("hsv_color_sliders")
        self.formLayout_2 = QtWidgets.QFormLayout(self.hsv_color_sliders)
        self.formLayout_2.setObjectName("formLayout_2")
        self.hue_lbl = QtWidgets.QLabel(self.hsv_color_sliders)
        self.hue_lbl.setObjectName("hue_lbl")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.hue_lbl)
        self.hue_slider = QtWidgets.QSlider(self.hsv_color_sliders)
        self.hue_slider.setOrientation(QtCore.Qt.Horizontal)
        self.hue_slider.setObjectName("hue_slider")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.hue_slider)
        self.saturation_lbl = QtWidgets.QLabel(self.hsv_color_sliders)
        self.saturation_lbl.setObjectName("saturation_lbl")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.saturation_lbl)
        self.saturation_slider = QtWidgets.QSlider(self.hsv_color_sliders)
        self.saturation_slider.setOrientation(QtCore.Qt.Horizontal)
        self.saturation_slider.setObjectName("saturation_slider")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.saturation_slider)
        self.value_lbl = QtWidgets.QLabel(self.hsv_color_sliders)
        self.value_lbl.setObjectName("value_lbl")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.value_lbl)
        self.value_slider = QtWidgets.QSlider(self.hsv_color_sliders)
        self.value_slider.setOrientation(QtCore.Qt.Horizontal)
        self.value_slider.setObjectName("value_slider")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.value_slider)
        self.alpha_lbl_hsv = QtWidgets.QLabel(self.hsv_color_sliders)
        self.alpha_lbl_hsv.setObjectName("alpha_lbl_hsv")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.alpha_lbl_hsv)
        self.alpha_hsv_slider = QtWidgets.QSlider(self.hsv_color_sliders)
        self.alpha_hsv_slider.setOrientation(QtCore.Qt.Horizontal)
        self.alpha_hsv_slider.setObjectName("alpha_hsv_slider")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.alpha_hsv_slider)
        self.tabWidget.addTab(self.hsv_color_sliders, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 3)
        self.current_color_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_color_btn.sizePolicy().hasHeightForWidth())
        self.current_color_btn.setSizePolicy(sizePolicy)
        self.current_color_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.current_color_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.current_color_btn.setText("")
        self.current_color_btn.setObjectName("current_color_btn")
        self.gridLayout.addWidget(self.current_color_btn, 2, 0, 1, 1)
        self.current_secondary_color_btn = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_secondary_color_btn.sizePolicy().hasHeightForWidth())
        self.current_secondary_color_btn.setSizePolicy(sizePolicy)
        self.current_secondary_color_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.current_secondary_color_btn.setMaximumSize(QtCore.QSize(20, 20))
        self.current_secondary_color_btn.setText("")
        self.current_secondary_color_btn.setObjectName("current_secondary_color_btn")
        self.gridLayout.addWidget(self.current_secondary_color_btn, 2, 2, 1, 1)
        self.color_preview = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_preview.sizePolicy().hasHeightForWidth())
        self.color_preview.setSizePolicy(sizePolicy)
        self.color_preview.setMinimumSize(QtCore.QSize(20, 20))
        self.color_preview.setMaximumSize(QtCore.QSize(20, 20))
        self.color_preview.setText("")
        self.color_preview.setObjectName("color_preview")
        self.gridLayout.addWidget(self.color_preview, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.colorManagement.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.colorManagement)
        self.layerManagement = QtWidgets.QDockWidget(MainWindow)
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
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.layerManagement)
        self.actionNavigator = QtWidgets.QAction(MainWindow)
        self.actionNavigator.setCheckable(True)
        self.actionNavigator.setObjectName("actionNavigator")
        self.actionColor_management = QtWidgets.QAction(MainWindow)
        self.actionColor_management.setCheckable(True)
        self.actionColor_management.setObjectName("actionColor_management")
        self.actionTools = QtWidgets.QAction(MainWindow)
        self.actionTools.setCheckable(True)
        self.actionTools.setObjectName("actionTools")
        self.actionLayers = QtWidgets.QAction(MainWindow)
        self.actionLayers.setCheckable(True)
        self.actionLayers.setObjectName("actionLayers")
        self.actionLayers_2 = QtWidgets.QAction(MainWindow)
        self.actionLayers_2.setCheckable(True)
        self.actionLayers_2.setObjectName("actionLayers_2")
        self.actionPreview_color = QtWidgets.QAction(MainWindow)
        self.actionPreview_color.setCheckable(True)
        self.actionPreview_color.setObjectName("actionPreview_color")
        self.actionKeep_projects_loaded = QtWidgets.QAction(MainWindow)
        self.actionKeep_projects_loaded.setCheckable(True)
        self.actionKeep_projects_loaded.setObjectName("actionKeep_projects_loaded")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSelect_all = QtWidgets.QAction(MainWindow)
        self.actionSelect_all.setObjectName("actionSelect_all")
        self.actionDeselect = QtWidgets.QAction(MainWindow)
        self.actionDeselect.setObjectName("actionDeselect")
        self.actionInvert_selection = QtWidgets.QAction(MainWindow)
        self.actionInvert_selection.setObjectName("actionInvert_selection")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionConvert = QtWidgets.QAction(MainWindow)
        self.actionConvert.setObjectName("actionConvert")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionConvert)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
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
        self.menuSettings.addAction(self.actionPreview_color)
        self.menuSettings.addAction(self.actionKeep_projects_loaded)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
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
        self.pushButton.setText(_translate("MainWindow", "Pick with dialog"))
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
        self.actionPreview_color.setText(_translate("MainWindow", "Preview color"))
        self.actionPreview_color.setToolTip(_translate("MainWindow", "Custom color is stored in the preview button instead of being applied immediately"))
        self.actionKeep_projects_loaded.setText(_translate("MainWindow", "Keep files loaded"))
        self.actionKeep_projects_loaded.setToolTip(_translate("MainWindow", "If several files are open, keep all of them loaded instead of only keeping current project in the memory (Increases switch speed, but may impact performance and stability)"))
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
        self.actionConvert.setText(_translate("MainWindow", "Convert"))
        self.actionConvert.setToolTip(_translate("MainWindow", "Convert an existing file into a different format"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save current file"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionSave_as.setToolTip(_translate("MainWindow", "Save current file as a different file"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setToolTip(_translate("MainWindow", "Shutdown program"))


class NewFileDialog(QtWidgets.QDialog):
    def setupUi(self, NewFileDialog):
        NewFileDialog.setObjectName("NewFileDialog")
        NewFileDialog.resize(283, 160)
        self.gridLayout = QtWidgets.QGridLayout(NewFileDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.view_btn = QtWidgets.QPushButton(NewFileDialog)
        self.view_btn.setObjectName("view_btn")
        self.gridLayout.addWidget(self.view_btn, 7, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 2, 3, 1)
        self.source_input = QtWidgets.QLineEdit(NewFileDialog)
        self.source_input.setObjectName("source_input")
        self.gridLayout.addWidget(self.source_input, 7, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.formats_btn = QtWidgets.QPushButton(NewFileDialog)
        self.formats_btn.setMinimumSize(QtCore.QSize(0, 35))
        self.formats_btn.setObjectName("formats_btn")
        self.gridLayout.addWidget(self.formats_btn, 3, 0, 1, 1)
        self.open_radio = QtWidgets.QRadioButton(NewFileDialog)
        self.open_radio.setObjectName("open_radio")
        self.gridLayout.addWidget(self.open_radio, 1, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(NewFileDialog)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.convert_radio = QtWidgets.QRadioButton(NewFileDialog)
        self.convert_radio.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.convert_radio.setObjectName("convert_radio")
        self.gridLayout.addWidget(self.convert_radio, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 3)

        self.retranslateUi(NewFileDialog)
        self.buttonBox.accepted.connect(NewFileDialog.accept)
        self.buttonBox.rejected.connect(NewFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewFileDialog)

    def retranslateUi(self, NewFileDialog):
        _translate = QtCore.QCoreApplication.translate
        NewFileDialog.setWindowTitle(_translate("NewFileDialog", "Dialog"))
        self.view_btn.setText(_translate("NewFileDialog", "View"))
        self.formats_btn.setText(_translate("NewFileDialog", "Supported\n"
"Formats"))
        self.open_radio.setText(_translate("NewFileDialog", "Open"))
        self.radioButton.setText(_translate("NewFileDialog", "Create"))
        self.convert_radio.setText(_translate("NewFileDialog", "Convert"))


class OpacityFillDialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 120)
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
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
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

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Chosen format does not support alpha-channels (opacity). Pick a background color to fill the blank spots, or save the file in another format."))