# -*- mode: python -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['/Users/user/Documents/SantosGUI/application'],
             binaries=[],
             datas=[],
             hiddenimports = [
             'packaging.qt',
             'matplotlib.backends.backend_qt4agg',
             'matplotlib_backend',
             'sklearn.neighbors.ball_tree',
             'sklearn.neighbors.kd_tree',
             'sklearn.neighbors.dist_metrics',
             'sklearn.neighbors.typedefs'
             ],
             hookspath=['packaging'],
             runtime_hooks=['packaging/rthook_pyqt4.py',
                            'packaging/rthook_qtapi.py',
                            'packaging/rthook_override_pyface_qt.py'], 
             excludes=['gi.repository.Gio', 'gi.repository.GModule',
                       'gi.repository.GObject', 'gi.repository.Gtk',
                       'gi.repository.Gdk', 'gi.repository.Atk',
                       'gi.repository.cairo', 'gi.repository.GLib',
                       'gobject', 'Tkinter', 'FixTk', 'PyQt5',
                       'PySide', 'PySide.QtCore', 'PySide.QtGui',
                       'PySide.QtNetwork', 'PySide.QtSvg',
                       'pyface.wx', 'traitsui.wx', 'OpenGL',
                       'OpenGL.GLUT', 'OpenGL.platform',
                       'IPython', 'PyQt4.QtAssistant',
                       'PyQt4.QtNetwork', 'PyQt4.QtWebKit',
                       'PyQt4.QtSql', 'PyQt4.QtXml', 'PyQt4.QtTest', 
                       'PyQt4.QtOpenGL', 'wx',
                       'gtk', 'gi', 'sphinx', 'twisted', 'zope',
                       'jinja2', 'httplib2', '_mysql',
                       'sqlalchemy'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='app',
          debug=False,
          strip=False,
          upx=True,
          console=True )
