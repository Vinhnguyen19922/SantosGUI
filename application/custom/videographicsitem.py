#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2013 Digia Plc and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt5.QtCore import QDir, QSize, QSizeF, Qt, QUrl, QRectF
from PyQt5.QtGui import QTransform
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem
from PyQt5.QtWidgets import (QApplication, QFileDialog, QGraphicsScene,
        QGraphicsView, QHBoxLayout, QPushButton, QSlider, QStyle, QVBoxLayout,
        QWidget, QSizePolicy, QPlainTextEdit)

import os
import sys
# add parent folder to python path
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from video import get_video_resolution

WIDTH = 600.0
WIGGLE = 40.0

class VideoPlayer(QWidget):
    """
    Arguments
    ---------
    parent: QWidget, the parent widget of VideoPlayer
    display_status: bool, default False, will show the status of the media player in the gui
    """

    def __init__(self, parent=None, display_status=False):
        super(VideoPlayer, self).__init__(parent)

        self.display_status = display_status

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.videoItem = QGraphicsVideoItem()

        scene = QGraphicsScene(self)
        graphicsView = QGraphicsView(scene)

        scene.addItem(self.videoItem)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        if self.display_status:
            self.status_mapping = {
                QMediaPlayer.UnknownMediaStatus: "UnknownMediaStatus",
                QMediaPlayer.NoMedia: "NoMedia",
                QMediaPlayer.LoadingMedia: "LoadingMedia",
                QMediaPlayer.LoadedMedia: "LoadedMedia",
                QMediaPlayer.StalledMedia: "StalledMedia",
                QMediaPlayer.BufferingMedia: "BufferingMedia",
                QMediaPlayer.BufferedMedia: "BufferedMedia",
                QMediaPlayer.EndOfMedia: "EndOfMedia",
                QMediaPlayer.InvalidMedia: "InvalidMedia"
            }
            self.statusText = QPlainTextEdit()
            self.statusText.setReadOnly(True)
            self.statusText.setFixedHeight(25)
            self.statusText.setFixedWidth(150)
            self.mediaPlayer.mediaStatusChanged.connect(self.mediaStatusChanged)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)
        if self.display_status:
            controlLayout.addWidget(self.statusText)

        layout = QVBoxLayout()
        layout.addWidget(graphicsView)
        layout.addLayout(controlLayout)
        self.setFixedWidth(WIDTH + WIGGLE)

        self.setLayout(layout)

        self.mediaPlayer.setVideoOutput(self.videoItem)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

    def openFile(self, fileName):
        if fileName != '' or fileName is not None:
            self.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile(fileName)))

            # set resolution
            res_orig = get_video_resolution(fileName)
            self.aspect_ratio = float(res_orig[0]) / res_orig[1]
            self.videoItem.setSize(QSizeF(WIDTH,
                                          WIDTH / self.aspect_ratio))
            self.setFixedHeight(WIDTH / self.aspect_ratio + 2*WIGGLE)

            self.playButton.setEnabled(True)

            # trick to show screenshot of the first frame of video
            self.mediaPlayer.play()
            self.mediaPlayer.pause()

    def closeFile(self):
        self.mediaPlayer.setMedia(QMediaContent())

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def mediaStatusChanged(self, status):
        self.statusText.setPlaceholderText(self.status_mapping[status])

    def positionChanged(self, position):
        self.positionSlider.setValue(position)
        #print self.positionSlider.value()

        # if position slider has reached the end, let's stop the video
        if self.positionSlider.value() >= self.positionSlider.maximum() - 1:
            self.mediaPlayer.stop()

            # play/pause hack to show the first frame of video
            self.mediaPlayer.play()
            self.mediaPlayer.pause()

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    player = VideoPlayer()
    player.show()

    sys.exit(app.exec_())

