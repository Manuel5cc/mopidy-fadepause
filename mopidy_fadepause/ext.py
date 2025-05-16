import logging
from mopidy import ext
from .actor import FadePauseCore

logger = logging.getLogger(__name__)

class Extension(ext.Extension):

    dist_name = 'Mopidy-FadePause'
    ext_name = 'fadepause'
    version = '0.1.0'

    def get_default_config(self):
        return ext.read(os.path.join(os.path.dirname(__file__), 'ext.conf'))

    def setup(self, registry):
        def factory(config, core):
            return FadePauseCore(config, core)
        registry.add('core.listener', factory)
