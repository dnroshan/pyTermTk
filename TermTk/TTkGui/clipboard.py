# MIT License
#
# Copyright (c) 2022 Eugenio Parodi <ceccopierangiolieugenio AT googlemail DOT com>
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

__all__ = ['TTkClipboard']

import importlib.util
from TermTk.TTkCore.log import TTkLog

class TTkClipboard():
    _clipboard = ''
    __slots__ = ('_setText', '_text')

    def __init__(self) -> None:
        self._setText = None
        self._text = None
        try:
            if importlib.util.find_spec('copykitten'):
                TTkLog.info("Using 'copykitten' as clipboard manager")
                import copykitten as _c
                self._setText = _c.copy
                self._text = _c.paste
            elif importlib.util.find_spec('pyperclip'):
                TTkLog.info("Using 'pyperclip' as clipboard manager")
                import pyperclip as _c
                self._setText = _c.copy
                self._text = _c.paste
            elif importlib.util.find_spec('pyperclip3'):
                TTkLog.info("Using 'pyperclip3' as clipboard manager")
                import pyperclip3 as _c
                self._setText = _c.copy
                self._text = _c.paste
            elif importlib.util.find_spec('clipboard'):
                TTkLog.info("Using 'clipboard' as clipboard manager")
                import clipboard as _c
                self._setText = _c.copy
                self._text = _c.paste
        except Exception as e:
           TTkLog.error("Clipboard error, try to export X11 if you are running this UI via SSH")
           for line in str(e).split("\n"):
               TTkLog.error(line)

    def setText(self, text):
        TTkClipboard._clipboard = text
        if self._setText:
            try:
                self._setText(str(text))
            except Exception as e:
                TTkLog.error("Clipboard error, try to export X11 if you are running this UI via SSH")
                for line in str(e).split("\n"):
                    TTkLog.error(line)

    def text(self):
        if self._text:
            txt = self._text()
            if txt == str(TTkClipboard._clipboard):
                return TTkClipboard._clipboard
            else:
                return self._text()
        return TTkClipboard._clipboard
