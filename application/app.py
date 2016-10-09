#!/usr/bin/env python
import sys
import shutil
import cv2
from custom.videoplayer import VideoPlayer
from custom.video_frame_player import VideoFramePlayer
from PyQt4 import QtGui, QtCore
from safety_main import Ui_TransportationSafety
from subprocess import call

from plotting.make_object_trajectories import main as db_make_objtraj

##############################################3
# testing feature objects
# import display-trajectories

###############################################

import os
from PyQt4.phonon import Phonon
import ConfigParser
from PyQt4.QtGui import *

import random
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import cvutils
from app_config import AppConfig as ac
import app_config as pm
import pm

import qt_plot


class Organizer(object):  # TODO: Phase out.
    def __init__(self):
        super(Organizer, self).__init__()


class MainGUI(QtGui.QMainWindow):

    def __init__(self):
        super(MainGUI, self).__init__()
        self.ui = Ui_TransportationSafety()
        self.ui.setupUi(self)
        self.newp = pm.ProjectWizard(self)

        # Experimenting with organizational objects
        self.feature_tracking = Organizer()
        self.results = Organizer()

        # Connect Menu actions
        self.ui.actionOpen_Project.triggered.connect(self.open_project)
        self.ui.actionNew_Project.triggered.connect(self.create_new_project)
        self.ui.actionAdd_Replace_Aerial_Image.triggered.connect(self.homography_open_image_aerial)  # TODO: New method. Check which tab is open. Move to homography tab if not already there. Then call open_image_aerial.
        self.ui.actionAdd_Replace_Aerial_Image.triggered.connect(self.homography_open_image_camera)
        self.ui.main_tab_widget.setCurrentIndex(0)  # Start on the first tab

        # Connect button actions
        self.ui.homography_button_open_aerial_image.clicked.connect(self.homography_open_image_aerial)
        self.ui.homography_button_open_camera_image.clicked.connect(self.homography_open_image_camera)

        # Connect back + continue buttons
        self.ui.homography_continue_button.clicked.connect(self.show_next_tab)
        self.ui.feature_tracking_continue_button.clicked.connect(self.show_next_tab)
        self.ui.feature_tracking_back_button.clicked.connect(self.show_prev_tab)

###########################################################################################################################################

        self.ui.roadusers_tracking_back_button.clicked.connect(self.show_prev_tab)
        self.ui.roadusers_tracking_continue_button.clicked.connect(self.show_next_tab)

##########################################################################################################################################

        # Track features page

        self.feature_tracking_video_player = VideoFramePlayer()
        # self.ui.actionOpen_Video.triggered.connect(self.videoplayer.openVideo)
        self.ui.feature_tracking_video_layout.addWidget(self.feature_tracking_video_player)

        # config
        self.configGui_features = configGui_features()
        self.ui.actionOpen_Config.triggered.connect(self.configGui_features.openConfig)
        self.ui.feature_tracking_parameter_layout.addWidget(self.configGui_features)

        # test button
        self.ui.button_feature_tracking_test.clicked.connect(self.test_feature)

##########################################################################################################################################

        # roadusers page

        # video play
        self.roadusers_tracking_video_player = VideoPlayer()
        # self.ui.actionOpen_Video.triggered.connect(self.videoplayer3.openVideo)
        self.ui.roadusers_tracking_video_layout.addWidget(self.roadusers_tracking_video_player)

        # config
        self.configGui_object = configGui_object()
        self.ui.actionOpen_Config.triggered.connect(self.configGui_object.openConfig)
        self.ui.roadusers_tracking_parameter_layout.addWidget(self.configGui_object)

        # test button
        self.ui.button_roadusers_tracking_test.clicked.connect(self.test_object)

        # run button
        self.ui.button_roadusers_tracking_run.clicked.connect(self.run)


        qt_plot.plot_results(self)
###########################################################################################################################################
        # self.ui.track_image.mousePressEvent = self.get_image_position

        ## CONFIGURE HOMOGRAPHY ##
        self.ui.homography_hslider_zoom_camera_image.zoom_target = self.ui.homography_cameraview
        self.ui.homography_hslider_zoom_aerial_image.zoom_target = self.ui.homography_aerialview
        self.ui.homography_hslider_zoom_computed_image.zoom_target = self.ui.homography_results
        self.ui.homography_cameraview.status_label = self.ui.homography_camera_status_label
        self.ui.homography_aerialview.status_label = self.ui.homography_aerial_status_label
        self.ui.homography_compute_button.clicked.connect(self.homography_compute)
        self.show()

######################################################################################################

    def test_feature(self):
        tracking_path = os.path.join(ac.CURRENT_PROJECT_PATH, ".temp", "test", "test_feature", "feature_tracking.cfg")
        db_path = os.path.join(ac.CURRENT_PROJECT_PATH, ".temp", "test", "test_feature", "test1.sqlite")
        if os.path.exists(db_path):
            os.remove(db_path)
        call(["feature-based-tracking", tracking_path, "--tf", "--database-filename", db_path])
        call(["display-trajectories.py", "-i", ac.CURRENT_PROJECT_VIDEO_PATH, "-d", db_path, "-o", ac.CURRENT_PROJECT_PATH + "/homography/homography.txt", "-t", "feature"])
        # displaytrajectories2.makeTrajectories()

    def test_object(self):
        tracking_path = os.path.join(ac.CURRENT_PROJECT_PATH, ".temp", "test", "test_object", "object_tracking.cfg")
        obj_db_path = os.path.join(ac.CURRENT_PROJECT_PATH,".temp", "test", "test_object", "test1.sqlite")
        feat_db_path = os.path.join(ac.CURRENT_PROJECT_PATH, ".temp", "test", "test_feature", "test1.sqlite")
        if os.path.exists(obj_db_path):
            os.remove(obj_db_path)
        shutil.copyfile(feat_db_path, obj_db_path)
        # call(["feature-based-tracking",ac.CURRENT_PROJECT_PATH + "/.temp/test/test_object/object_tracking.cfg","--tf","--database-filename", obj_db_path])
        call(["feature-based-tracking",tracking_path,"--gf","--database-filename", obj_db_path])
        call(["classify-objects.py", "--cfg", tracking_path, "-d", obj_db_path])  # Classify road users
        call(["display-trajectories.py", "-i", ac.CURRENT_PROJECT_VIDEO_PATH,"-d", obj_db_path, "-o", ac.CURRENT_PROJECT_PATH + "/homography/homography.txt", "-t", "object"])


# for the run button
    def run(self):
        """
        Runs TrafficIntelligence trackers and support scripts.
        """
        # create test folder
        if not os.path.exists(ac.CURRENT_PROJECT_PATH + "/run"):
            os.mkdir(ac.CURRENT_PROJECT_PATH + "/run")

        # removes object tracking.cfg
        if os.path.exists(ac.CURRENT_PROJECT_PATH + "/run/run_tracking.cfg"):
            os.remove(ac.CURRENT_PROJECT_PATH + "/run/run_tracking.cfg")

        # creates new config file
        shutil.copyfile(ac.CURRENT_PROJECT_PATH + "/.temp/test/test_object/object_tracking.cfg", ac.CURRENT_PROJECT_PATH + "/run/run_tracking.cfg")

        path1 = ac.CURRENT_PROJECT_PATH + "/run/run_tracking.cfg"

        f = open(path1, 'r')
        lines = f.readlines()
        f.close()
        with open(path1, "w") as wf:
            for line in lines:
                line_param = line.split('=')[0].strip()
                if "frame1" == line_param:  # Replace parameter "frame1"
                    wf.write("frame1 = 0\n")
                elif "nframes" == line_param:  # Remove parameter "nframes"
                    wf.write("nframes = 0\n")
                elif "database-filename" == line_param:
                    wf.write("database-filename = results.sqlite\n")
                else:
                    wf.write(line)

        db_path = os.path.join(ac.CURRENT_PROJECT_PATH, "run", "results.sqlite")
        tracking_path = os.path.join(ac.CURRENT_PROJECT_PATH, "run", "run_tracking.cfg")

        if os.path.exists(db_path):  # If results database already exists,
            os.remove(db_path)  # then remove it--it'll be recreated.
        call(["feature-based-tracking", tracking_path, "--tf", "--database-filename", db_path])
        call(["feature-based-tracking", tracking_path, "--gf", "--database-filename", db_path])

        call(["classify-objects.py", "--cfg", tracking_path, "-d", db_path])  # Classify road users

        db_make_objtraj(db_path)  # Make our object_trajectories db table

        call(["display-trajectories.py", "-i", ac.CURRENT_PROJECT_VIDEO_PATH, "-d", db_path, "-o", ac.CURRENT_PROJECT_PATH + "/homography/homography.txt", "-t", "object"])

################################################################################################
    def homography_load_aerial_image(self):
        pass

    def show_next_tab(self):
        curr_i = self.ui.main_tab_widget.currentIndex()
        new_i = curr_i + 1
        self.ui.main_tab_widget.setCurrentIndex(new_i)
        if new_i is 3:  # If we are moving to the plots page
           qt_plot.plot_results(self)


    def show_prev_tab(self):
        curr_i = self.ui.main_tab_widget.currentIndex()
        self.ui.main_tab_widget.setCurrentIndex(curr_i - 1)

    def results_plot_plot1(self):
        data = [random.random() for i in range(10)]
        # create an axis
        ax = self.figure1.add_subplot(111)
        # discards the old graph
        ax.hold(False)
        # plot data
        ax.plot(data, '*-')
        # refresh canvas
        self.canvas1.draw()

    def results_plot_plot2(self):
        data1 = [random.random() for i in range(50)]
        # create an axis
        ax = self.figure2.add_subplot(111)
        # discards the old graph
        ax.hold(False)
        # plot data
        ax.plot(data1, '*-')
        # refresh canvas
        self.canvas2.draw()

    def open_project(self):
        fname = str(QtGui.QFileDialog.getExistingDirectory(self, "Open Existing Project Folder...", ac.PROJECT_DIR))
        # TODO: Instead of select folder, perhaps select config file?
        if fname:
            pm.load_project(fname, self)
        else:
            pass  # If no folder selected, don't load anything.

    def create_new_project(self):
        self.newp.restart()
        self.newp.show()

    def homography_open_image_camera(self):
        """Opens a file dialog, allowing user to select an camera image file.

        Creates a QImage object from the filename of an camera image
        selected by the user in a popup file dialog menu.
        """
        qi = self.open_image_fd(dialog_text="Select camera image...")
        if qi:
            self.ui.homography_cameraview.load_image(qi)

    def homography_open_image_aerial(self):
        """Opens a file dialog, allowing user to select an aerial image file.

        Creates a QImage object from the filename of an aerial image
        selected by the user in a popup file dialog menu.
        """
        qi = self.open_image_fd(dialog_text="Select aerial image...")
        if qi:
            self.ui.homography_aerialview.load_image(qi)

    def open_image_fd(self, dialog_text="Open Image", default_dir=""):
        """Opens a file dialog, allowing user to select an image file.

        Creates a QImage object from the filename selected by the user in the
        popup file dialog menu.

        Args:
            dialog_text [Optional(str.)]: Text to prompt user with in open file
                dialog. Defaults to "Open Image".
            default_dir [Optional(str.)]: Path of the default directory to open
                the file dialog box to. Defaults to "".

        Returns:
            QImage: Image object created from selected image file.
            None: Returns None if no file was selected in the dialog box.
        """
        fname = QtGui.QFileDialog.getOpenFileName(self, dialog_text, default_dir)  # TODO: Filter to show only image files
        if fname:
            image = QtGui.QImage(fname)
        else:
            image = None
        return image

    def homography_compute(self):
        #TODO: display error message if points are < 4
        px_text = self.ui.unit_px_input.text()
        self.unitPixRatio = float(unicode(px_text))
        self.unscaled_world_pts = (np.array(self.ui.homography_aerialview.list_points()))
        self.worldPts = self.unitPixRatio * self.unscaled_world_pts
        self.videoPts = np.array(self.ui.homography_cameraview.list_points())
        if len(self.worldPts) >= 4:
            if len(self.worldPts) == len(self.videoPts):
                self.homography, self.mask = cv2.findHomography(self.videoPts, self.worldPts)

        if self.homography is None:
            return

        pm.update_project_cfg("homography", "unitpixelratio", str(self
            .unitPixRatio))
        homography_path = os.path.join(ac.CURRENT_PROJECT_PATH, "homography")

        if self.homography.size > 0:
            txt_path = os.path.join(homography_path, "homography.txt")
            np.savetxt(txt_path, self.homography)  # Save computed homography.

        corr_path = os.path.join(homography_path, "point-correspondences.txt")
        points_path = os.path.join(homography_path, "image-points.txt")

        f = open(corr_path, 'w') #save points to be loaded later
        np.savetxt(f, self.worldPts.T)
        np.savetxt(f, self.videoPts.T)
        f.close()

        with open(points_path, 'w') as pp:
            np.savetxt(pp, self.unscaled_world_pts.T)
            np.savetxt(pp, self.videoPts.T)

        self.homography_display_results()

    def homography_display_results(self):
        homography_path = os.path.join(ac.CURRENT_PROJECT_PATH, "homography")
        worldImg = cv2.imread(os.path.join(homography_path, "aerial.png"))
        videoImg = cv2.imread(os.path.join(homography_path, "camera.png"))

        invHomography = np.linalg.inv(self.homography)

        projectedWorldPts = cvutils.projectArray(invHomography, self.worldPts.T).T
        projectedVideoPts = cvutils.projectArray(self.homography, self.videoPts.T).T

        # TODO: Nicer formatting for computed goodness images
        for i in range(self.worldPts.shape[0]):
            # world image
            cv2.circle(worldImg, tuple(np.int32(np.round(self.worldPts[i] / self.unitPixRatio))), 2, cvutils.cvBlue)
            cv2.circle(worldImg, tuple(np.int32(np.round(projectedVideoPts[i] / self.unitPixRatio))), 2, cvutils.cvRed)
            cv2.putText(worldImg, str(i+1), tuple(np.int32(np.round(self.worldPts[i]/self.unitPixRatio)) + 5), cv2.FONT_HERSHEY_PLAIN, 2., cvutils.cvBlue, 2)
            # video image
            cv2.circle(videoImg, tuple(np.int32(np.round(self.videoPts[i]))), 2, cvutils.cvBlue)
            cv2.circle(videoImg, tuple(np.int32(np.round(projectedWorldPts[i]))), 2, cvutils.cvRed)
            cv2.putText(videoImg, str(i+1), tuple(np.int32(np.round(self.videoPts[i]) + 5)), cv2.FONT_HERSHEY_PLAIN, 2., cvutils.cvBlue, 2)
        aerial_goodness_path = os.path.join(homography_path, "homography_goodness_aerial.png")
        camera_goodness_path = os.path.join(homography_path, "homography_goodness_camera.png")

        cv2.imwrite(aerial_goodness_path, worldImg)  # Save aerial goodness image
        cv2.imwrite(camera_goodness_path, videoImg)  # Save camera goodness image

        self.ui.homography_results.load_image(QtGui.QImage(aerial_goodness_path))  # Load aerial goodness image into gui

##########################################################################################################################

class configGui_features(QtGui.QWidget):

    def __init__(self):
        super(configGui_features, self).__init__()
        self.initUI()

    def initUI(self):
        # lbl1.move(15, 10)

        self.btn = QtGui.QPushButton('Set Config', self)
        # self.btn.move(20, 20)
        self.btn.clicked.connect(self.createConfig_features)

        self.label1 = QtGui.QLabel("first frame to process")
        # input box
        self.input1 = QtGui.QLineEdit()
        # self.input1.setMaximumWidth(10)

        self.label2 = QtGui.QLabel("number of frames to process")
        # self.label1.move(130, 22)
        self.input2 = QtGui.QLineEdit()
        # self.le.move(150, 22)

        self.label3 = QtGui.QLabel("Max number of features added at each frame")
        self.input3 = QtGui.QLineEdit()
        self.label4 = QtGui.QLabel("Number of deplacement to test")
        # self.input4 = QtGui.QLineEdit()

        self.label5 = QtGui.QLabel("minimum feature motion")
        self.input5 = QtGui.QLineEdit()

        self.label6 = QtGui.QLabel("Minimum displacement to keep features (px)")
        self.input6 = QtGui.QLineEdit()

        self.label7 = QtGui.QLabel("Max number of iterations")
        # self.input7 = QtGui.QLineEdit()

        self.label8 = QtGui.QLabel("to stop feature tracking")
        self.input8 = QtGui.QLineEdit()

        self.label9 = QtGui.QLabel("Minimum number of frames to consider")
        # self.input7 = QtGui.QLineEdit()

        self.label10 = QtGui.QLabel("a feature for grouping")
        self.input10 = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.label1, 2, 0)
        grid.addWidget(self.input1, 2, 1)

        grid.addWidget(self.label2, 3, 0)
        grid.addWidget(self.input2, 3, 1)

        grid.addWidget(self.label3, 4, 0)
        grid.addWidget(self.input3, 4, 1)

        grid.addWidget(self.label4, 5, 0)

        grid.addWidget(self.label5, 6, 0)
        grid.addWidget(self.input5, 6, 1)

        grid.addWidget(self.label6, 7, 0)
        grid.addWidget(self.input6, 7, 1)

        grid.addWidget(self.label7, 8, 0)

        grid.addWidget(self.label8, 9, 0)
        grid.addWidget(self.input8, 9, 1)

        grid.addWidget(self.label9, 10, 0)

        grid.addWidget(self.label10, 11, 0)
        grid.addWidget(self.input10, 11, 1)

        grid.addWidget(self.btn, 12, 0)

        self.setLayout(grid)

        self.setWindowTitle('Input config')
        # self.show()

        # opens a cofig file
    def openConfig(self):

        # path = QFileDialog.getOpenFileName(self, 'Open File', '/')
        # global path1
        path1= str(path)

        # path1 = "../project_dir/test1"

    def createConfig_features(self, path):
        """
        Create a config file
        """

        # global path1
        # path1= str(path)

        # update test1 name with file chose



        config = ConfigParser.ConfigParser()

        if not os.path.exists(ac.CURRENT_PROJECT_PATH + "/.temp/test"):
            os.mkdir(ac.CURRENT_PROJECT_PATH + "/.temp/test")

        # create test folder
        if not os.path.exists(ac.CURRENT_PROJECT_PATH + "/.temp/test/test_feature"):
            os.mkdir(ac.CURRENT_PROJECT_PATH + "/.temp/test/test_feature")

        # removes feature_tracking.cfg
        if os.path.exists(ac.CURRENT_PROJECT_PATH + "/.temp/test/test_feature/feature_tracking.cfg"):
            os.remove(ac.CURRENT_PROJECT_PATH + "/.temp/test/test_feature/feature_tracking.cfg")

        # creates new config file
        proj_tracking_path = os.path.join(ac.CURRENT_PROJECT_PATH, "tracking.cfg")
        shutil.copyfile(proj_tracking_path, ac.CURRENT_PROJECT_PATH + "/.temp/test/test_feature/feature_tracking.cfg")

        path1 = ac.CURRENT_PROJECT_PATH + "/.temp/test/test_feature/feature_tracking.cfg"


        # add new content to config file
        config.add_section("added")
        config.set("added", "video-filename",ac.CURRENT_PROJECT_VIDEO_PATH)
        config.set("added", "homography-filename",ac.CURRENT_PROJECT_PATH + "/homography/homography.txt")
        config.set("added", "frame1", self.input1.text())
        config.set("added", "nframes", self.input2.text())
        config.set("added", "max-nfeatures", self.input3.text())
        config.set("added", "ndisplacements", self.input5.text())
        config.set("added", "min-feature-displacement", self.input6.text())
        config.set("added", "max-number-iterations", self.input8.text())
        config.set("added", "min-feature-time", self.input10.text())

        try:
            path1
        except NameError:
            # self.player.load(Phonon.MediaSource(""))
            error = QtGui.QErrorMessage()
            error.showMessage('''\
            no config files chosen''')
            error.exec_()
            print "no config chosen"
        else:
            with open(path1, "a") as config_file:
                config.write(config_file)

            # to remove the section header from config file

            # opens the file to read
            f = open(path1, "r")
            lines = f.readlines()
            f.close()
            # opens the file to write
            f = open(path1, "w")
            for line in lines:
                # removes the section header
                if line != "[added]"+"\n":
                    f.write(line)
            f.close()


##########################################################################################################################

class configGui_object(QtGui.QWidget):

    def __init__(self):
        super(configGui_object, self).__init__()
        self.initUI()

    def initUI(self):
        # lbl1.move(15, 10)

        self.btn = QtGui.QPushButton('Set Config', self)
        # self.btn.move(20, 20)
        self.btn.clicked.connect(self.createConfig_objects)


        self.label1 = QtGui.QLabel("first frame to process")
        # input box
        self.input1 = QtGui.QLineEdit()
        # self.input1.setMaximumWidth(10)

        self.label2 = QtGui.QLabel("number of frames to process")
        # self.label1.move(130, 22)
        self.input2 = QtGui.QLineEdit()
        # self.le.move(150, 22)

        self.label3 = QtGui.QLabel("maximum connection-distance")
        self.input3 = QtGui.QLineEdit()

        self.label4 = QtGui.QLabel("maximum segmentation-distance")
        self.input4 = QtGui.QLineEdit()

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.label1, 2, 0)
        grid.addWidget(self.input1, 2, 1)

        grid.addWidget(self.label2, 3, 0)
        grid.addWidget(self.input2, 3, 1)

        grid.addWidget(self.label3, 4, 0)
        grid.addWidget(self.input3, 4, 1)

        grid.addWidget(self.label4, 5, 0)
        grid.addWidget(self.input4, 5, 1)

        grid.addWidget(self.btn, 6, 0)

        # path1 = "3"

        self.setLayout(grid)

        self.setWindowTitle('Input config')
        # self.show()

        # opens a config file
    def openConfig(self):
        path = QFileDialog.getOpenFileName(self, 'Open File', '/')
        # global path1
        path1 = str(path)

    def createConfig_objects(self, path):
        """
        Create a config file
        """
        config = ConfigParser.ConfigParser()
        object_dir = os.path.join(ac.CURRENT_PROJECT_PATH, ".temp", "test", "test_object")
        feature_cfg = os.path.join(ac.CURRENT_PROJECT_PATH, ".temp", "test", "test_feature", "feature_tracking.cfg")
        object_cfg = os.path.join(object_dir, "object_tracking.cfg")

        # create test folder
        if not os.path.exists(object_dir):
            os.mkdir(object_dir)

        # removes object tracking.cfg
        if os.path.exists(object_cfg):
            os.remove(object_cfg)

        # creates new config file
        shutil.copyfile(feature_cfg, object_cfg)

        with open(object_cfg, 'r') as rf:
            lines = rf.readlines()

        with open(object_cfg, 'w') as wf:
            for line in lines:
                line_param = line.split('=')[0].strip()
                if "frame1" == line_param:  # Remove parameter "frame1"
                    pass
                elif "nframes" == line_param:  # Remove parameter "nframes"
                    pass
                else:
                    wf.write(line)

        # add new content to config file

        config.add_section("added")
        config.set("added", "frame1", self.input1.text())
        config.set("added", "nframes", self.input2.text())
        config.set("added", "mm-connection-distance", self.input3.text())
        config.set("added", "mm-segmentation-distance", self.input4.text())

        with open(object_cfg, "a") as config_file:
            config.write(config_file)

        # to remove the section header from config file

        # opens the file to read
        with open(object_cfg, "r") as f:
            lines = f.readlines()
        # opens the file to write
        with open(object_cfg, 'w') as wf:
            for line in lines:
                # removes the section header
                if line != "[added]\n":
                    wf.write(line)

##########################################################################################################################

def main():
    app.exec_()

if __name__ == '__main__':
    ac.load_application_config()
    app = QtGui.QApplication(sys.argv)
    ex = MainGUI()
    sys.exit(main())
