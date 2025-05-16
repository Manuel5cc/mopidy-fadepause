import time
from mopidy import core

class FadePauseCore(core.CoreListener):

    def __init__(self, config, core):
        self.config = config
        self.core = core
        self.original_volume = None
        self.fading = False

    def on_event(self, event, **kwargs):
        if event == 'pause' and not self.fading:
            self.handle_fade_pause()

    def handle_fade_pause(self):
        self.fading = True

        try:
            current_volume = self.core.mixer.get_volume().get()
            self.original_volume = current_volume

            seconds = int(self.config['fadepause'].get('fade_duration', 10))
            steps = seconds
            delay = 1  # 1 second per step
            volume_step = current_volume / steps if steps > 0 else current_volume

            for i in range(steps):
                new_volume = max(0, int(current_volume - (volume_step * (i + 1))))
                self.core.mixer.set_volume(new_volume).get()
                time.sleep(delay)

            self.core.playback.pause().get()
            self.core.mixer.set_volume(self.original_volume).get()
        finally:
            self.fading = False
