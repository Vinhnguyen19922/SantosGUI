# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_create_new_project(object):
    def setupUi(self, create_new_project):
        create_new_project.setObjectName(_fromUtf8("create_new_project"))
        create_new_project.setWindowModality(QtCore.Qt.ApplicationModal)
        create_new_project.resize(568, 406)
        create_new_project.setAutoFillBackground(False)
        create_new_project.setModal(True)
        create_new_project.setWizardStyle(QtGui.QWizard.ClassicStyle)
        create_new_project.setOptions(QtGui.QWizard.NoBackButtonOnLastPage|QtGui.QWizard.NoBackButtonOnStartPage)
        self.newp_p1 = QtGui.QWizardPage()
        self.newp_p1.setObjectName(_fromUtf8("newp_p1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.newp_p1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newp_p1_title = QtGui.QLabel(self.newp_p1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newp_p1_title.setFont(font)
        self.newp_p1_title.setObjectName(_fromUtf8("newp_p1_title"))
        self.verticalLayout.addWidget(self.newp_p1_title)
        self.newp_p1_layout = QtGui.QFormLayout()
        self.newp_p1_layout.setContentsMargins(-1, 8, -1, -1)
        self.newp_p1_layout.setObjectName(_fromUtf8("newp_p1_layout"))
        self.newp_projectname_label = QtGui.QLabel(self.newp_p1)
        self.newp_projectname_label.setObjectName(_fromUtf8("newp_projectname_label"))
        self.newp_p1_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.newp_projectname_label)
        self.newp_projectname_input = QtGui.QLineEdit(self.newp_p1)
        self.newp_projectname_input.setObjectName(_fromUtf8("newp_projectname_input"))
        self.newp_p1_layout.setWidget(0, QtGui.QFormLayout.FieldRole, self.newp_projectname_input)
        self.verticalLayout.addLayout(self.newp_p1_layout)
        self.newp_ldir_label = QtGui.QLabel(self.newp_p1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.newp_ldir_label.setFont(font)
        self.newp_ldir_label.setText(_fromUtf8(""))
        self.newp_ldir_label.setObjectName(_fromUtf8("newp_ldir_label"))
        self.verticalLayout.addWidget(self.newp_ldir_label)
        create_new_project.addPage(self.newp_p1)
        self.newp_p2 = QtGui.QWizardPage()
        self.newp_p2.setObjectName(_fromUtf8("newp_p2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.newp_p2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.newp_p2_add_video_title = QtGui.QLabel(self.newp_p2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newp_p2_add_video_title.setFont(font)
        self.newp_p2_add_video_title.setObjectName(_fromUtf8("newp_p2_add_video_title"))
        self.verticalLayout_2.addWidget(self.newp_p2_add_video_title)
        self.newp_p2_add_vido_description = QtGui.QLabel(self.newp_p2)
        self.newp_p2_add_vido_description.setWordWrap(True)
        self.newp_p2_add_vido_description.setObjectName(_fromUtf8("newp_p2_add_vido_description"))
        self.verticalLayout_2.addWidget(self.newp_p2_add_vido_description)
        self.newp_p2_video_layout = QtGui.QFormLayout()
        self.newp_p2_video_layout.setContentsMargins(-1, 8, -1, -1)
        self.newp_p2_video_layout.setObjectName(_fromUtf8("newp_p2_video_layout"))
        self.newp_video_label = QtGui.QLabel(self.newp_p2)
        self.newp_video_label.setObjectName(_fromUtf8("newp_video_label"))
        self.newp_p2_video_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.newp_video_label)
        self.newp_p2_video_browse_layout = QtGui.QHBoxLayout()
        self.newp_p2_video_browse_layout.setObjectName(_fromUtf8("newp_p2_video_browse_layout"))
        self.newp_video_input = QtGui.QLineEdit(self.newp_p2)
        self.newp_video_input.setObjectName(_fromUtf8("newp_video_input"))
        self.newp_p2_video_browse_layout.addWidget(self.newp_video_input)
        self.newp_video_browse = QtGui.QPushButton(self.newp_p2)
        self.newp_video_browse.setObjectName(_fromUtf8("newp_video_browse"))
        self.newp_p2_video_browse_layout.addWidget(self.newp_video_browse)
        self.newp_p2_video_layout.setLayout(0, QtGui.QFormLayout.FieldRole, self.newp_p2_video_browse_layout)
        self.newp_video_start_time_label = QtGui.QLabel(self.newp_p2)
        self.newp_video_start_time_label.setObjectName(_fromUtf8("newp_video_start_time_label"))
        self.newp_p2_video_layout.setWidget(1, QtGui.QFormLayout.LabelRole, self.newp_video_start_time_label)
        self.newp_video_start_time_input = QtGui.QDateTimeEdit(self.newp_p2)
        self.newp_video_start_time_input.setObjectName(_fromUtf8("newp_video_start_time_input"))
        self.newp_p2_video_layout.setWidget(1, QtGui.QFormLayout.FieldRole, self.newp_video_start_time_input)
        self.newp_video_server_label = QtGui.QLabel(self.newp_p2)
        self.newp_video_server_label.setObjectName(_fromUtf8("newp_video_server_label"))
        self.newp_p2_video_layout.setWidget(2, QtGui.QFormLayout.LabelRole, self.newp_video_server_label)
        self.newp_video_server_input = QtGui.QLineEdit(self.newp_p2)
        self.newp_video_server_input.setObjectName(_fromUtf8("newp_video_server_input"))
        self.newp_p2_video_layout.setWidget(2, QtGui.QFormLayout.FieldRole, self.newp_video_server_input)
        self.newp_video_email_label = QtGui.QLabel(self.newp_p2)
        self.newp_video_email_label.setObjectName(_fromUtf8("newp_video_email_label"))
        self.newp_p2_video_layout.setWidget(3, QtGui.QFormLayout.LabelRole, self.newp_video_email_label)
        self.newp_video_email_input = QtGui.QLineEdit(self.newp_p2)
        self.newp_video_email_input.setObjectName(_fromUtf8("newp_video_email_input"))
        self.newp_p2_video_layout.setWidget(3, QtGui.QFormLayout.FieldRole, self.newp_video_email_input)
        self.verticalLayout_2.addLayout(self.newp_p2_video_layout)
        self.newp_add_aerial_image_title = QtGui.QLabel(self.newp_p2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newp_add_aerial_image_title.setFont(font)
        self.newp_add_aerial_image_title.setObjectName(_fromUtf8("newp_add_aerial_image_title"))
        self.verticalLayout_2.addWidget(self.newp_add_aerial_image_title)
        self.newp_p2_add_aerial_image_description = QtGui.QLabel(self.newp_p2)
        self.newp_p2_add_aerial_image_description.setWordWrap(True)
        self.newp_p2_add_aerial_image_description.setObjectName(_fromUtf8("newp_p2_add_aerial_image_description"))
        self.verticalLayout_2.addWidget(self.newp_p2_add_aerial_image_description)
        self.newp_p2_aerial_layout = QtGui.QFormLayout()
        self.newp_p2_aerial_layout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.newp_p2_aerial_layout.setContentsMargins(-1, 8, -1, -1)
        self.newp_p2_aerial_layout.setObjectName(_fromUtf8("newp_p2_aerial_layout"))
        self.newp_aerial_image_label = QtGui.QLabel(self.newp_p2)
        self.newp_aerial_image_label.setObjectName(_fromUtf8("newp_aerial_image_label"))
        self.newp_p2_aerial_layout.setWidget(0, QtGui.QFormLayout.LabelRole, self.newp_aerial_image_label)
        self.newp_p2_image_browse_layout = QtGui.QHBoxLayout()
        self.newp_p2_image_browse_layout.setObjectName(_fromUtf8("newp_p2_image_browse_layout"))
        self.newp_aerial_image_input = QtGui.QLineEdit(self.newp_p2)
        self.newp_aerial_image_input.setObjectName(_fromUtf8("newp_aerial_image_input"))
        self.newp_p2_image_browse_layout.addWidget(self.newp_aerial_image_input)
        self.newp_aerial_image_browse = QtGui.QPushButton(self.newp_p2)
        self.newp_aerial_image_browse.setObjectName(_fromUtf8("newp_aerial_image_browse"))
        self.newp_p2_image_browse_layout.addWidget(self.newp_aerial_image_browse)
        self.newp_p2_aerial_layout.setLayout(0, QtGui.QFormLayout.FieldRole, self.newp_p2_image_browse_layout)
        self.verticalLayout_2.addLayout(self.newp_p2_aerial_layout)
        create_new_project.addPage(self.newp_p2)
        self.newp_p3 = QtGui.QWizardPage()
        self.newp_p3.setObjectName(_fromUtf8("newp_p3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.newp_p3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.newp_p2_add_video_title_2 = QtGui.QLabel(self.newp_p3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.newp_p2_add_video_title_2.setFont(font)
        self.newp_p2_add_video_title_2.setObjectName(_fromUtf8("newp_p2_add_video_title_2"))
        self.verticalLayout_3.addWidget(self.newp_p2_add_video_title_2)
        self.line = QtGui.QFrame(self.newp_p3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.newp_start_creation = QtGui.QPushButton(self.newp_p3)
        self.newp_start_creation.setObjectName(_fromUtf8("newp_start_creation"))
        self.verticalLayout_3.addWidget(self.newp_start_creation)
        self.newp_creation_progress = QtGui.QProgressBar(self.newp_p3)
        self.newp_creation_progress.setProperty("value", 0)
        self.newp_creation_progress.setObjectName(_fromUtf8("newp_creation_progress"))
        self.verticalLayout_3.addWidget(self.newp_creation_progress)
        self.newp_creation_status = QtGui.QLabel(self.newp_p3)
        self.newp_creation_status.setObjectName(_fromUtf8("newp_creation_status"))
        self.verticalLayout_3.addWidget(self.newp_creation_status)
        create_new_project.addPage(self.newp_p3)

        self.retranslateUi(create_new_project)
        QtCore.QMetaObject.connectSlotsByName(create_new_project)

    def retranslateUi(self, create_new_project):
        create_new_project.setWindowTitle(_translate("create_new_project", "Create New Project", None))
        self.newp_p1_title.setText(_translate("create_new_project", "New Safety Project", None))
        self.newp_projectname_label.setText(_translate("create_new_project", "Project Name", None))
        self.newp_p2_add_video_title.setText(_translate("create_new_project", "Add project video", None))
        self.newp_p2_add_vido_description.setText(_translate("create_new_project", "Browse and select a video file to analyze. Please input the time when the video recording occurred. You may optionally enter an email that should be notified when long-running analysis is finished. You should also enter the IP address or URL of the server that should be used for analysis.", None))
        self.newp_video_label.setText(_translate("create_new_project", "Selected video", None))
        self.newp_video_browse.setText(_translate("create_new_project", "Browse...", None))
        self.newp_video_start_time_label.setText(_translate("create_new_project", "Recording start time", None))
        self.newp_video_server_label.setText(_translate("create_new_project", "Server IP or URL", None))
        self.newp_video_email_label.setText(_translate("create_new_project", "Email", None))
        self.newp_add_aerial_image_title.setText(_translate("create_new_project", "Add aerial image", None))
        self.newp_p2_add_aerial_image_description.setText(_translate("create_new_project", "Browse and select an aerial image of the video\'s target. ", None))
        self.newp_aerial_image_label.setText(_translate("create_new_project", "Aerial image", None))
        self.newp_aerial_image_browse.setText(_translate("create_new_project", "Browse...", None))
        self.newp_p2_add_video_title_2.setText(_translate("create_new_project", "Creating new project", None))
        self.newp_start_creation.setText(_translate("create_new_project", "Click to create project.", None))
        self.newp_creation_status.setText(_translate("create_new_project", "Beginning project creation...", None))

