#!/usr/bin/env python
# -*-coding:utf-8 -*
"""
Main module.
"""

import sys
from PySide6 import QtCore, QtWidgets, QtQuick, QtQml, QtGui


class Connection(QtCore.QAbstractListModel):
    """
    Docstring for Connection.
    """

    def __init__(self):
        """
        TODO: to be defined.
        """
        super().__init__()
        self._items = ["connection", "xls", "c"]

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._items)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self._items[index.row()]
        else:
            return QtCore.Qt.QVariant()


if __name__ == "__main__":
    app = QtGui.QGuiApplication([])
    con = Connection()
    engine = QtQml.QQmlApplicationEngine(parent=app)
    context = engine.rootContext()
    context.setContextProperty("conModel", con)
    url = QtCore.QUrl("ihm.qml")
    engine.load(url)
    sys.exit(app.exec())
