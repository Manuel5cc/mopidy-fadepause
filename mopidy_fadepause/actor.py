import time
from mopidy import core

class FadePauseCore(core.CoreListener):

    def __init__(self):
        self.original_volume = None
        self.fading = False

    def on_event(self, event, **kwargs):
        if event == 'pause' and not self.fading:
            self.handle_fade_pause()

    def handle_fade_pause(self):
        self.fading = True

        core = self.core
        try:
            current_volume = core.mixer.get_volume().get()
            self.original_volume = current_volume

            steps = 10
            delay = 1  # seconds
            volume_step = current_volume / steps

            for i in range(steps):
                new_volume = max(0, int(current_volume - (volume_step * (i + 1))))
                core.mixer.set_volume(new_volume).get()
                time.sleep(delay)

            core.playback.pause().get()
            core.mixer.set_volume(self.original_volume).get()
        finally:
            self.fading = False
