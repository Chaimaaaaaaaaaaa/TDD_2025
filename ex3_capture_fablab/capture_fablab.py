"""
Enregistrement de vidéo avec boutons start/stop et molette pour changer le frame rate
"""

from datetime import datetime
from time import sleep
import cv2
from gpiozero import Button
import lgpio

# Chemin d'enregistrement des vidéos
PATH = '/home/abc/Projet/Videos/'

# Pins de la molette
GPIO = lgpio.gpiochip_open(0)
START_LED_PIN = 17
RECORD_LED_PIN = 21

lgpio.gpio_claim_output(GPIO, START_LED_PIN)  # LED de démarrage
lgpio.gpio_claim_output(GPIO, RECORD_LED_PIN)  # LED d'enregistrement

# Boutons
BUTTON_ON_PIN = 3
BUTTON_OFF_PIN = 2

button_on = Button(BUTTON_ON_PIN)
button_off = Button(BUTTON_OFF_PIN, bounce_time=0.2)

ENREGISTREMENT = True


def set_led(pin, etat):
    """
    Allume ou éteint la LED d'enregistrement.
    1 pour allumer, 0 pour éteindre.
    """
    lgpio.gpio_write(GPIO, pin, etat)


def blink_led(pin, times, interval):
    """
    Fait clignoter une LED un certain nombre de fois avec un intervalle donné.
    """
    for _ in range(times):
        set_led(pin, 1)
        sleep(interval)
        set_led(pin, 0)
        sleep(interval)


def molette():
    """
    Retourne la valeur choisie par la molette + 1.
    """
    valeur_inv = [lgpio.gpio_read(GPIO, pin) for pin in [14, 15, 23, 24, 25]]
    valeur = [0 if inv else 1 for inv in valeur_inv]
    valeur_ = valeur[0] * 1 + valeur[1] * 2 + valeur[2] * 4 + valeur[3] * 8 + valeur[4] * 8 + 1
    return valeur_


def init():
    """
    Interruption pour le bouton stop.
    """
    button_off.when_pressed = stop_record


def stop_record():
    """
    Fonction appelée par l'interruption, met la variable enregistrement à false
    pour sortir de la boucle d'enregistrement.
    """
    global ENREGISTREMENT
    ENREGISTREMENT = False
    # Clignote 3 fois pour indiquer que l'enregistrement est terminé
    blink_led(START_LED_PIN, 3, 0.2)
    # La LED verte reste s'eteint pour indiquer que l'enregistrement est terminé
    set_led(RECORD_LED_PIN, 0)


def start_record():
    """
    Démarre l'enregistrement de la vidéo.
    """
    global ENREGISTREMENT
    ENREGISTREMENT = True
    blink_led(START_LED_PIN, 3, 0.2)
    set_led(RECORD_LED_PIN, 1)

    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nom_fichier = PATH + date_now + '.avi'
    video = cv2.VideoCapture(0) # pylint: disable=no-member
    
    if not video.isOpened():
        print("Erreur de lecture du fichier")
        return
    
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)
    fps = molette()
    print("Frame rate sélectionné: ", fps)
    
    result = cv2.VideoWriter(   # pylint: disable=no-member
        nom_fichier,
        cv2.VideoWriter_fourcc(*'MJPG'),    # pylint: disable=no-member
        fps,
        size
    )
    
    while ENREGISTREMENT: # Boucle d'enregistrement
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
    while True:
        if button_on.is_pressed:
            start_record()


if __name__ == "__main__":
    # Clignote 2 fois pour indiquer que le programme est lancé
    blink_led(START_LED_PIN, 2, 0.1)
    init()
    main()
    