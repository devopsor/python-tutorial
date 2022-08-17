import QtQuick 2.2
import QtQuick.Window 2.2

Window {
    Image {
        id: background
        source: "6.background.png"
    }
    Image {
        id: wheel
        anchors.centerIn: parent
        source: "6.pinwheel.png"
        Behavior on rotation {
            NumberAnimation {
                duration: 250
            }
        }
    }
    MouseArea {
        anchors.fill: parent
        onPressed: {
            wheel.rotation += 90
        }
    }
    visible: true
    width: background.width
    height: background.height
}