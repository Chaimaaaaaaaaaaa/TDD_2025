"""
Enregistrement de vidéo avec boutons start/stop et molette pour changer le frame rate
"""

from datetime import datetime
from time import sleep
import cv2
import lgpio
from gpiozero import Button


class VideoCapture:
    """
    Classe contenant les fonctions pour le démarrage et l'arrêt de l'enregistrement.
    """
    def __init__(self):
        """
        Initialisation des pins, des boutons et de l'interruption.
        """
        # Chemin d'enregistrement des vidéos
        self.path = '/home/abc/Projet/Videos/'

        # Pins de la molette
        self.gpio = lgpio.gpiochip_open(0)
        self.start_led_pin = 17
        self.record_led_pin = 21

        lgpio.gpio_claim_output(self.gpio, self.start_led_pin)  # LED de démarrage
        lgpio.gpio_claim_output(self.gpio, self.record_led_pin)  # LED d'enregistrement

        # Boutons
        self.button_on_pin = 3
        self.button_off_pin = 2
        self.button_on = Button(self.button_on_pin)
        self.button_off = Button(self.button_off_pin, bounce_time=0.2)

        self.enregistrement = True

        # Interruption pour le bouton stop
        self.button_off.when_pressed = self.stop_record


    def set_led(self, pin, etat):
        """
        Allume ou éteint la LED d'enregistrement.
        1 pour allumer, 0 pour éteindre.
        """
        lgpio.gpio_write(self.gpio, pin, etat)


    def blink_led(self, pin, times, interval):
        """
        Fait clignoter une LED un certain nombre de fois avec un intervalle donné.
        """
        for _ in range(times):
            self.set_led(pin, 1)
            sleep(interval)
            self.set_led(pin, 0)
            sleep(interval)


    def molette(self):
        """
        Retourne la valeur choisie par la molette + 1.
        """
        valeur_inv = [lgpio.gpio_read(self.gpio, pin) for pin in [14, 15, 23, 24, 25]]
        valeur = [0 if inv else 1 for inv in valeur_inv]
        valeur_ = valeur[0] * 1 + valeur[1] * 2 + valeur[2] * 4 + valeur[3] * 8 + valeur[4] * 8 + 1
        return valeur_


    def stop_record(self):
        """
        Fonction appelée par l'interruption, met la variable enregistrement à false
        pour sortir de la boucle d'enregistrement.
        """
        self.enregistrement = False
        # Clignote 3 fois pour indiquer que l'enregistrement est terminé
        self.blink_led(self.start_led_pin, 3, 0.2)
        # La LED verte reste s'eteint pour indiquer que l'enregistrement est terminé
        self.set_led(self.record_led_pin, 0)


    def start_record(self):
        """
        Démarre l'enregistrement de la vidéo.
        """
        self.enregistrement = True
        self.blink_led(self.start_led_pin, 3, 0.2)
        self.set_led(self.record_led_pin, 1)

        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nom_fichier = self.path + date_now + '.avi'
        video = cv2.VideoCapture(0) # pylint: disable=no-member


        if not video.isOpened():
            print("Erreur de lecture du fichier")
            return

        frame_width = int(video.get(3))
        frame_height = int(video.get(4))
        size = (frame_width, frame_height)
        fps = self.molette()
        print("Frame rate sélectionné: ", fps)

        result = cv2.VideoWriter(   # pylint: disable=no-member
            nom_fichier,
            cv2.VideoWriter_fourcc(*'MJPG'),    # pylint: disable=no-member
            fps,
            size
        )

        while self.enregistrement: # Boucle d'enregistrement
            print("Enregistrement en cours")
            ret, frame = video.read()
            if ret:
                result.write(frame)
            else:
                break

        # Relâcher tout à la fin
        video.release()
        result.release()
        print("Vidéo enregistrée\n")



def main():
    """
    Boucle principale du programme.
    """
    video_capture = VideoCapture()

    video_capture.blink_led(video_capture.start_led_pin, 2, 0.1)

    while True:
        if video_capture.button_on.is_pressed:
            video_capture.start_record()


if __name__ == "__main__":
    main()
