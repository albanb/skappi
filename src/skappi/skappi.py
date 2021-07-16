#!/usr/bin/env python
# -*-coding:utf-8 -*
"""
Main module.
"""

import sys
from PySide6 import QtCore, QtWidgets, QtQuick, QtQml, QtGui


class ConnectionList():
    """
    This class aim at serving the list of all connection list to other actors.
    """

    def __init__(self):
        self.list = ["xls", "other"]

    def get_list(self):
        """
        Get the list of all possible connection.

        :return: list of connection.
        :rtype: list

        """
        return self.list

        
class Connection(QtCore.QAbstractListModel):
    """
    This class define the data model for the combobox widget listing all possible
    connection.
    """

    def __init__(self):
        super().__init__()
        con_list = ConnectionList()
        self._items = con_list.get_list()

    def rowCount(self, parent=QtCore.QModelIndex()):
        """
        Count the number of connection. This is one of the basic method to be
        implemented subclassing QAbstractListModel.

        :param parent: index of the parent item.
        :type parent: QModelIndex
        :return: the number of items in the list.
        :rtype: int
        """
        return len(self._items)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        """
        Compute the information to be displayed depending on the requested role.

        :param index: requested index.
        :type index: QModelIndex
        :param role: requested role.
        :type role: int
        :return: data to be displayed.
        :rtype: QVariant
        """
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
