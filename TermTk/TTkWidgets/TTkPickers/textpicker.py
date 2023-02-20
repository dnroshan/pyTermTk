# MIT License
#
# Copyright (c) 2023 Eugenio Parodi <ceccopierangiolieugenio AT googlemail DOT com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from TermTk.TTkCore.constant import TTkK
from TermTk.TTkCore.cfg import TTkCfg
from TermTk.TTkCore.helper import TTkHelper
from TermTk.TTkCore.signal import pyTTkSlot, pyTTkSignal
from TermTk.TTkCore.string import TTkString
from TermTk.TTkCore.color import TTkColor
from TermTk.TTkGui.textcursor import TTkTextCursor
from TermTk.TTkGui.textdocument import TTkTextDocument
from TermTk.TTkLayouts.gridlayout import TTkGridLayout
from TermTk.TTkLayouts.boxlayout import TTkHBoxLayout
from TermTk.TTkAbstract.abstractscrollview import TTkAbstractScrollView
from TermTk.TTkAbstract.abstractscrollarea import TTkAbstractScrollArea

from TermTk.TTkWidgets.widget import TTkWidget
from TermTk.TTkWidgets.resizableframe import TTkResizableFrame
from TermTk.TTkWidgets.texedit import TTkTextEditView, TTkTextEdit
from TermTk.TTkWidgets.splitter import TTkSplitter
from TermTk.TTkWidgets.button import TTkButton
from TermTk.TTkWidgets.label import TTkLabel
from TermTk.TTkWidgets.checkbox import TTkCheckbox
from TermTk.TTkWidgets.window import TTkWindow
from TermTk.TTkWidgets.TTkModelView.filetree import TTkFileTree
from TermTk.TTkWidgets.TTkModelView.filetreewidgetitem import TTkFileTreeWidgetItem
from TermTk.TTkWidgets.TTkPickers.colorpicker import TTkColorButtonPicker

class _superSimpleHorizontalLine(TTkWidget):
    def paintEvent(self):
        w,h = self.size()
        self._canvas.drawText(pos=(0,h-1), text='┕'+('━'*(w-2))+'┙',color=TTkColor.fg("#888888"))

# List taken from:
# https://emojipicker.com

emoji = {
    'Smileys': "😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😙😚🤗🤔😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌🤓😛😜😝🤤😒😓😔😕🙃🤑😲🙁😖😞😟😤😢😭😦😧😨😩😬😰😱😳😵😡😠😇🤠🤡🤥😷🤒🤕🤢🤧😈👿👹👺💀👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🙈🙉🙊👦👧👨👩👴👵👶👼",
    'Body':    "💪🤳👈👉👆🖕👇🤞🖖🤘🤙✋👌👍👎✊👊🤛🤜🤚👋👏👐🙌🙏🤝💅👂👃👣👀👅👄",
    # 'Flags':   "🇦🇨🇦🇩🇦🇪🇦🇫🇦🇬🇦🇮🇦🇱🇦🇲🇦🇴🇦🇶🇦🇷🇦🇸🇦🇹🇦🇺🇦🇼🇦🇽🇦🇿🇧🇦🇧🇧🇧🇩🇧🇪🇧🇫🇧🇬🇧🇭🇧🇮🇧🇯🇧🇱🇧🇲🇧🇳🇧🇴🇧🇶🇧🇷🇧🇸🇧🇹🇧🇻🇧🇼🇧🇾🇧🇿🇨🇦🇨🇨🇨🇩🇨🇫🇨🇬🇨🇭🇨🇮🇨🇰🇨🇱🇨🇲🇨🇳🇨🇴🇨🇵🇨🇷🇨🇺🇨🇻🇨🇼🇨🇽🇨🇾🇨🇿🇩🇪🇩🇬🇩🇯🇩🇰🇩🇲🇩🇴🇩🇿🇪🇦🇪🇨🇪🇪🇪🇬🇪🇭🇪🇷🇪🇸🇪🇹🇪🇺🇫🇮🇫🇯🇫🇰🇫🇲🇫🇴🇫🇷🇬🇦🇬🇧🇬🇩🇬🇪🇬🇫🇬🇬🇬🇭🇬🇮🇬🇱🇬🇲🇬🇳🇬🇵🇬🇶🇬🇷🇬🇸🇬🇹🇬🇺🇬🇼🇬🇾🇭🇰🇭🇲🇭🇳🇭🇷🇭🇹🇭🇺🇮🇨🇮🇩🇮🇪🇮🇱🇮🇲🇮🇳🇮🇴🇮🇶🇮🇷🇮🇸🇮🇹🇯🇪🇯🇲🇯🇴🇯🇵🇰🇪🇰🇬🇰🇭🇰🇮🇰🇲🇰🇳🇰🇵🇰🇷🇰🇼🇰🇾🇰🇿🇱🇦🇱🇧🇱🇨🇱🇮🇱🇰🇱🇷🇱🇸🇱🇹🇱🇺🇱🇻🇱🇾🇲🇦🇲🇨🇲🇩🇲🇪🇲🇫🇲🇬🇲🇭🇲🇰🇲🇱🇲🇲🇲🇳🇲🇴🇲🇵🇲🇶🇲🇷🇲🇸🇲🇹🇲🇺🇲🇻🇲🇼🇲🇽🇲🇾🇲🇿🇳🇦🇳🇨🇳🇪🇳🇫🇳🇬🇳🇮🇳🇱🇳🇴🇳🇵🇳🇷🇳🇺🇳🇿🇴🇲🇵🇦🇵🇪🇵🇫🇵🇬🇵🇭🇵🇰🇵🇱🇵🇲🇵🇳🇵🇷🇵🇸🇵🇹🇵🇼🇵🇾🇶🇦🇷🇪🇷🇴🇷🇸🇷🇺🇷🇼🇸🇦🇸🇧🇸🇨🇸🇩🇸🇪🇸🇬🇸🇭🇸🇮🇸🇯🇸🇰🇸🇱🇸🇲🇸🇳🇸🇴🇸🇷🇸🇸🇸🇹🇸🇻🇸🇽🇸🇾🇸🇿🇹🇦🇹🇨🇹🇩🇹🇫🇹🇬🇹🇭🇹🇯🇹🇰🇹🇱🇹🇲🇹🇳🇹🇴🇹🇷🇹🇹🇹🇻🇹🇼🇹🇿🇺🇦🇺🇬🇺🇲🇺🇳🇺🇸🇺🇾🇺🇿🇻🇦🇻🇨🇻🇪🇻🇬🇻🇮🇻🇳🇻🇺🇼🇫🇼🇸🇽🇰🇾🇪🇾🇹🇿🇦🇿🇲🇿🇼",
}

class _emojiPickerView(TTkAbstractScrollView):
    __slots__ = ('_btns', '_labels', 'emojiClicked')
    def __init__(self, *args, **kwargs):
        self.emojiClicked = pyTTkSignal(str)
        super().__init__(*args, **kwargs)
        self.viewChanged.connect(self._viewChangedHandler)
        self._btns = {}
        self._labels = {}
        for t in emoji:
            self._btns[t]=[]
            self._labels[t] = TTkLabel(parent=self, text=t,size=(len(t),1))
            for e in emoji[t]:
                self._btns[t].append(btn := TTkButton(parent=self, text=e,size=(4,3),border=True))
                def _cbEmoji(ch):
                    def _ccb(): self.emojiClicked.emit(ch)
                    return _ccb
                btn.clicked.connect(_cbEmoji(e))

    def resizeEvent(self, w, h):
        self._placeEmojis()
        return super().resizeEvent(w, h)

    def _placeEmojis(self):
        x,y=0,0
        w,h=self.size()
        for t in self._btns:
            if x:
                y+=3
            self._labels[t].move(0,y)
            x=0
            y+=1
            for e in self._btns[t]:
                e.move(x,y)
                if x+7>=w:
                    x=0
                    y+=3
                else:
                    x+=4

    @pyTTkSlot()
    def _viewChangedHandler(self):
        x,y = self.getViewOffsets()
        self.layout().setOffset(-x,-y)

    def viewFullAreaSize(self) -> (int, int):
        _,_,w,h = self.layout().fullWidgetAreaGeometry()
        return w , h

    def viewDisplayedSize(self) -> (int, int):
        return self.size()

    def maximumWidth(self):   return 0x10000
    def maximumHeight(self):  return 0x10000
    def minimumWidth(self):   return 0
    def minimumHeight(self):  return 0

class _emojiPickerArea(TTkAbstractScrollArea):
    __slots__ = ('_areaView')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'parent' in kwargs: kwargs.pop('parent')
        self._areaView = _emojiPickerView(*args, **kwargs)
        self.setFocusPolicy(TTkK.ClickFocus)
        self.setViewport(self._areaView)

class _emojiPicker(TTkResizableFrame):
    __slots__ = ('emojiClicked')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs|{'layout':TTkGridLayout()})
        self.layout().addWidget(epa := _emojiPickerArea())
        self.emojiClicked = epa.viewport().emojiClicked

class TTkTextDialogPicker(TTkWindow):
    __slots__ = ('_textEdit', '_autoSize')
    def __init__(self, *args, **kwargs):
        self._autoSize = kwargs.get('autoSize',False)
        super().__init__(*args, **kwargs)
        fontLayout = TTkGridLayout(columnMinWidth=1)
        # Char Fg/Bg buttons
        fontLayout.addWidget(cb_fg := TTkCheckbox(text=" FG"),0,0)
        fontLayout.addWidget(btn_fgColor := TTkColorButtonPicker(border=True, enabled=False, maxSize=(7,3), minSize=(7,3)),1,0)

        fontLayout.addWidget(cb_bg := TTkCheckbox(text=" BG"),0,2)
        fontLayout.addWidget(btn_bgColor := TTkColorButtonPicker(border=True, enabled=False, maxSize=(7,3), minSize=(7,3)),1,2)

        # Char style buttons
        fontLayout.addWidget(btn_bold          := TTkButton(border=True, maxSize=(5,3), minSize=(5,3), checkable=True, text=TTkString( 'a' , TTkColor.BOLD)        ),1,4)
        fontLayout.addWidget(btn_italic        := TTkButton(border=True, maxSize=(5,3), minSize=(5,3), checkable=True, text=TTkString( 'a' , TTkColor.ITALIC)      ),1,5)
        fontLayout.addWidget(btn_underline     := TTkButton(border=True, maxSize=(5,3), minSize=(5,3), checkable=True, text=TTkString(' a ', TTkColor.UNDERLINE)   ),1,6)
        fontLayout.addWidget(btn_strikethrough := TTkButton(border=True, maxSize=(5,3), minSize=(5,3), checkable=True, text=TTkString(' a ', TTkColor.STRIKETROUGH)),1,7)

        fontLayout.addWidget(btn_emoji := TTkButton(border=True, maxSize=(6,4), minSize=(6,3), text=TTkString('😎')),1,9)

        fontLayout.addWidget(_superSimpleHorizontalLine(),0,10,2,1)

        self._textEdit = TTkTextEdit(document=kwargs.get('document',TTkTextDocument()))
        self._textEdit.setReadOnly(False)
        self._textEdit.setLineWrapMode(TTkK.WidgetWidth)
        self._textEdit.setLineNumber('\n' in self._textEdit.toPlainText())

        @pyTTkSlot()
        def _showEmojiPicker():
            ep = _emojiPicker(size=(40,10))
            def _addEmoji(e):
                self._textEdit.textCursor().insertText(e)
                self._textEdit.textCursor().movePosition(TTkTextCursor.Right)
            ep.emojiClicked.connect(_addEmoji)
            TTkHelper.overlay(btn_emoji, ep, 0, 0)

        btn_emoji.clicked.connect(_showEmojiPicker)

        @pyTTkSlot(TTkColor)
        def _currentColorChangedCB(format):
            if fg := format.foreground():
                cb_fg.setCheckState(TTkK.Checked)
                btn_fgColor.setEnabled()
                btn_fgColor.setColor(fg.invertFgBg())
            else:
                cb_fg.setCheckState(TTkK.Unchecked)
                btn_fgColor.setDisabled()

            if bg := format.background():
                cb_bg.setCheckState(TTkK.Checked)
                btn_bgColor.setEnabled()
                btn_bgColor.setColor(bg)
            else:
                cb_bg.setCheckState(TTkK.Unchecked)
                btn_bgColor.setDisabled()

            btn_bold.setChecked(format.bold())
            btn_italic.setChecked(format.italic())
            btn_underline.setChecked(format.underline())
            btn_strikethrough.setChecked(format.strikethrough())
            # TTkLog.debug(f"{fg=} {bg=} {bold=} {italic=} {underline=} {strikethrough=   }")

        self._textEdit.currentColorChanged.connect(_currentColorChangedCB)

        def _setStyle():
            color = TTkColor()
            if cb_fg.checkState() == TTkK.Checked:
                color += btn_fgColor.color().invertFgBg()
            if cb_bg.checkState() == TTkK.Checked:
                color += btn_bgColor.color()
            if btn_bold.isChecked():
                color += TTkColor.BOLD
            if btn_italic.isChecked():
                color += TTkColor.ITALIC
            if btn_underline.isChecked():
                color += TTkColor.UNDERLINE
            if btn_strikethrough.isChecked():
                color += TTkColor.STRIKETROUGH
            cursor = self._textEdit.textCursor()
            cursor.applyColor(color)
            cursor.setColor(color)
            self._textEdit.setFocus()

        cb_fg.stateChanged.connect(lambda x: btn_fgColor.setEnabled(x==TTkK.Checked))
        cb_bg.stateChanged.connect(lambda x: btn_bgColor.setEnabled(x==TTkK.Checked))
        cb_fg.clicked.connect(lambda _: _setStyle())
        cb_bg.clicked.connect(lambda _: _setStyle())

        btn_fgColor.colorSelected.connect(lambda _: _setStyle())
        btn_bgColor.colorSelected.connect(lambda _: _setStyle())

        btn_bold.clicked.connect(_setStyle)
        btn_italic.clicked.connect(_setStyle)
        btn_underline.clicked.connect(_setStyle)
        btn_strikethrough.clicked.connect(_setStyle)

        layout = TTkGridLayout()

        layout.addItem(fontLayout,0,0)
        layout.addWidget(self._textEdit,1,0)
        self.setLayout(layout)

        self._textEdit.viewport().viewChanged.connect(self._textPickerViewChanged)

    def focusTextEdit(self):
        self._textEdit.setFocus()

    @pyTTkSlot()
    def _textPickerViewChanged(self):
        w,h = self.size()
        self.resize(w,h)

    def resize(self, w: int, h: int):
        tw,th = self._textEdit.viewport().viewFullAreaSize()
        self._textEdit.setLineNumber(th>1)
        if not self._autoSize:
            return super().resize(w,h)
        t,b,l,r = self.getPadding()
        return super().resize(w, th+t+b+4)


class TTkTextPicker(TTkWidget):
    '''TTkTextPicker
    .. note:: This is an early unstable prototype
              Do not use it unless you know what you are doing
              And I've no idea what I am doing
    '''
    __slots__ = ('_teButton','_textEdit', 'documentViewChanged', 'textChanged', '_autoSize')
    def __init__(self, *args, **kwargs):
        self.documentViewChanged = pyTTkSignal(int,int)
        self._autoSize = kwargs.get('autoSize',False)
        super().__init__(*args, **kwargs|{'layout':TTkHBoxLayout()})
        self._textEdit = TTkTextEdit(pos=(0,0), size=(self.width()-2,self.height()))
        self._textEdit.setText(kwargs.get('text',''))
        self._textEdit.setReadOnly(False)
        self._textEdit.setLineWrapMode(TTkK.WidgetWidth)
        self.textChanged = self._textEdit.textChanged
        self._teButton = TTkButton(border=True, text='◉', borderColor=TTkColor.fg("#AAAAFF")+TTkColor.bg("#002244") ,
                            pos=(self.width()-2,0),
                            size=(2,self.height()), minSize=(3,1),maxWidth=3)
        self.layout().addWidget(self._textEdit)
        self.layout().addWidget(self._teButton)

        @pyTTkSlot()
        def _showTextDialogPicker():
            w,h = self.size()
            tdp = TTkTextDialogPicker(size=(50,8+h), document=self._textEdit.document(), autoSize=self._autoSize)
            TTkHelper.overlay(self, tdp, -1, -7, modal=True)
            tdp.focusTextEdit()

        self._teButton.clicked.connect(_showTextDialogPicker)

        self._textEdit.viewport().viewChanged.connect(self._textPickerViewChanged)

    def getTTkString(self):
        return self._textEdit.toRawText()

    @pyTTkSlot()
    def _textPickerViewChanged(self):
        wa,ha = self._textEdit.viewport().viewFullAreaSize()
        tw,th = self._textEdit.size()
        bw,bh = self._teButton.size()
        w,h = self.size()
        self._textEdit.setLineNumber(ha>1)
        self.documentViewChanged.emit(tw+bw,ha)
        if self._autoSize:
            self.resize(w,ha)
