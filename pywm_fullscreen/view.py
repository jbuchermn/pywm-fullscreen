from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar

import logging

from pywm import PyWMView, PyWMViewDownstreamState
from pywm.pywm_view import PyWMViewUpstreamState

if TYPE_CHECKING:
    from .compositor import Compositor
else:
    Compositor = TypeVar('Compositor')

logger = logging.getLogger(__name__)

class View(PyWMView[Compositor]):
    def __init__(self, wm: Compositor, handle: int):
        PyWMView.__init__(self, wm, handle)
        logger.debug("New view - %s" % self.up_state)

    def init(self) -> PyWMViewDownstreamState:
        if self.up_state is None:
            return PyWMViewDownstreamState()

        res = PyWMViewDownstreamState(self._handle, (self.wm.layout[0].pos[0] - self.up_state.offset[0], self.wm.layout[0].pos[1] - self.up_state.offset[1], self.wm.layout[0].width, self.wm.layout[0].height), accepts_input=True)
        res.size = self.wm.layout[0].width, self.wm.layout[0].height

        self.focus()

        return res

    def process(self, up_state: PyWMViewUpstreamState) -> PyWMViewDownstreamState:
        return self.init()

    def destroy(self) -> None:
        self.wm.destroy_view(self)
