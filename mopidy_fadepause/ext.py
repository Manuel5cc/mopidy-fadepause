import logging
from mopidy import ext

from .actor import FadePauseCore

logger = logging.getLogger(__name__)

class Extension(ext.Extension):

    dist_name = 'Mopidy-FadePause'
    ext_name = 'fadepause'
    version = '0.1.0'

    def setup(self, registry):
        registry.add('core.listener', FadePauseCore)
