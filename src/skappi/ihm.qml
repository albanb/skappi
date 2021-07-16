import QtQuick
import QtQuick.Controls

ApplicationWindow {
	id: appWindow

	visible: true
	title: qsTr("Skappy")

	menuBar: MenuBar {
		Menu {
			title: qsTr("&Actions")
			Action { 
				text: qsTr("&Connection")
				onTriggered: load_page("connection")
			}
		}
	}

	header: ToolBar {}

	footer: TabBar {}

	StackView {
		id: stack
		anchors.fill: parent
	}

	Component {
		id: connection
		Rectangle {
			color: "blue"
			ComboBox {
				id: dataType
				model: conModel 
				onActivated: load_page(dataType.displayText)
				textRole: "display"
			}
		}
	}
	
	Component {
		id: xls
		Rectangle {
			color: "green"
		}
	}

	Component {
		id: noConnection
		Rectangle {
			color: "red"
			Text { text: "No other connection is implemented yet" }
		}
	}
	
	function load_page(page) {
		switch(page) {
			case 'connection':
			stack.push(connection);
			break;
			case 'xls':
			stack.push(xls);
			break;
			case 'other':
			stack.push(noConnection);
			break;
		}
	}
}
