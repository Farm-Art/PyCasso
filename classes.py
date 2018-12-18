from PyQt5 import QtWidgets, QtGui, QtCore


class Canvas(QtWidgets.QGraphicsScene):
    def __init__(self, parent):
        super().__init__()
        self.window = parent
        self.tool = 'pencil'
        self.painter = QtGui.QPainter()
        self.memory = []

    def mousePressEvent(self, event):
        try:
            self.painter.begin(self.image)
            pen = QtGui.QPen(self.window.current_color)
            pen.setWidth(self.window.thickness)
            self.painter.setPen(pen)
            brush = QtGui.QBrush(self.window.fill_color)
            self.painter.setBrush(brush)
            if self.tool == 'pencil':
                self.painter.drawPoint(event.scenePos())
                self.prev_point = event.scenePos()
            elif self.tool == 'rectangle':
                self.rect = QtCore.QRectF(event.scenePos(), event.scenePos())
                self.rect = self.addRect(self.rect)
                self.rect.setPen(pen)
                self.rect.setBrush(brush)
                self.rect.setZValue(1000.0)
            elif self.tool == 'line':
                self.line = QtCore.QLineF(event.scenePos(), event.scenePos())
                self.line = self.addLine(self.line)
                self.line.setPen(pen)
                self.line.setBrush(brush)
                self.line.setZValue(1000.0)
            elif self.tool == 'ellipse':
                self.ellipse = QtCore.QRectF(event.scenePos(), event.scenePos())
                self.ellipse = self.addEllipse(self.ellipse)
                self.ellipse.setPen(pen)
                self.ellipse.setBrush(brush)
                self.ellipse.setZValue(1000.0)
            self.updateImage()
        except AttributeError:
            pass

    def mouseMoveEvent(self, event):
        try:
            if self.tool == 'pencil':
                self.painter.drawPoint(event.scenePos())
                self.painter.drawLine(self.prev_point, event.scenePos())
                self.prev_point = event.scenePos()
            elif self.tool == 'rectangle':
                x1, y1 = min(max(0, self.rect.rect().x()), self.image.size().width() - 1),\
                         min(max(0, self.rect.rect().y()), self.image.size().height() - 1)
                x2, y2 = min(max(0, event.scenePos().x()), self.image.size().width() - 1),\
                         min(max(0, event.scenePos().y()), self.image.size().height() - 1)
                w, h = x2 - x1, y2 - y1
                self.rect.setRect(x1, y1, w, h)
            elif self.tool == 'line':
                x1, y1 = min(max(0, self.line.line().x1()), self.image.size().width() - 1),\
                         min(max(0, self.line.line().y1()), self.image.size().height() - 1)
                x2, y2 = min(max(0, event.scenePos().x()), self.image.size().width() - 1),\
                         min(max(0, event.scenePos().y()), self.image.size().height() - 1)
                self.line.setLine(x1, y1, x2, y2)
            elif self.tool == 'ellipse':
                x1, y1 = min(max(0, self.ellipse.rect().x()), self.image.size().width() - 1),\
                         min(max(0, self.ellipse.rect().y()), self.image.size().height() - 1)
                x2, y2 = min(max(0, event.scenePos().x()), self.image.size().width() - 1),\
                         min(max(0, event.scenePos().y()), self.image.size().height() - 1)
                w, h = x2 - x1, y2 - y1
                self.ellipse.setRect(x1, y1, w, h)
            self.updateImage()
        except AttributeError:
            pass

    def mouseReleaseEvent(self, event):
        try:
            if self.tool == 'pencil':
                self.painter.end()
            elif self.tool == 'rectangle':
                self.removeItem(self.rect)
                self.painter.drawRect(self.rect.rect())
                self.painter.end()
            elif self.tool == 'line':
                self.removeItem(self.line)
                self.painter.drawLine(self.line.line())
                self.painter.end()
            elif self.tool == 'ellipse':
                self.removeItem(self.ellipse)
                self.painter.drawEllipse(self.ellipse.rect())
                self.painter.end()
            self.updateImage()
        except AttributeError:
            pass

    def load_image(self, image):
        self.image = QtGui.QImage(image)
        self.display_image = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(self.image))
        self.addItem(self.display_image)
        self.memory.append(self.image.copy())

    def updateImage(self):
        self.removeItem(self.display_image)
        self.display_image = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(self.image))
        self.addItem(self.display_image)
        self.display_image.setZValue(-1000.0)


class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=-1, hspacing=-1, vspacing=-1):
        super(FlowLayout, self).__init__(parent)
        self._hspacing = hspacing
        self._vspacing = vspacing
        self._items = []
        self.setContentsMargins(margin, margin, margin, margin)

    def __del__(self):
        del self._items[:]

    def addItem(self, item):
        self._items.append(item)

    def horizontalSpacing(self):
        if self._hspacing >= 0:
            return self._hspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        if self._vspacing >= 0:
            return self._vspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)

    def expandingDirections(self):
        return QtCore.Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QtCore.QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        left, top, right, bottom = self.getContentsMargins()
        size += QtCore.QSize(left + right, top + bottom)
        return size

    def doLayout(self, rect, testonly):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        x = effective.x()
        y = effective.y()
        lineheight = 0
        for item in self._items:
            widget = item.widget()
            hspace = self.horizontalSpacing()
            if hspace == -1:
                hspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            vspace = self.verticalSpacing()
            if vspace == -1:
                vspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + hspace
            if nextX - hspace > effective.right() and lineheight > 0:
                x = effective.x()
                y = y + lineheight + vspace
                nextX = x + item.sizeHint().width() + hspace
                lineheight = 0
            if not testonly:
                item.setGeometry(
                    QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))
            x = nextX
            lineheight = max(lineheight, item.sizeHint().height())
        return y + lineheight - rect.y() + bottom

    def smartSpacing(self, pm):
        parent = self.parent()
        if parent is None:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()
