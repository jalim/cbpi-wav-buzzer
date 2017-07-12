import time
from thread import start_new_thread
from modules import cbpi

class Buzzer(object):

    def beep(self):
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("./modules/plugins/beeper/beep.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        print("BEEP")

@cbpi.initalizer(order=2)
def init(cbpi):
    cbpi.buzzer = Buzzer()
    cbpi.beep()
    cbpi.app.logger.info("INIT BEEPER")
