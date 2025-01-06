# Enregistrement de vidéo avec boutons start/stop et molette pour changer le frame rate                                                                                                                                                                                                                                                                                                                                
import cv2
from gpiozero import Button
from datetime import datetime
from time import sleep
import lgpio

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

# Pour sortir de la boucle d'enregistrement
stop_enrg = True

# Fait clignoter une LED un certain nombre de fois.
def blink_led(pin, times, interval):
    for _ in range(times):
        lgpio.gpio_write(GPIO, pin, 1)
        sleep(interval)
        lgpio.gpio_write(GPIO, pin, 0)
        sleep(interval)

# Interruption pour le bouton stop
def init():
    button_off.when_pressed = OFF

# Fonction appelée par l'interruption, met la variable stop_enrg à false pour sortir de la boucle d'enregistrement
def OFF():
    global stop_enrg
    stop_enrg = False
    # Clignote 3 fois pour indiquer que l'enregistrement est terminé
    blink_led(17, 3, 0.2)
    # La LED verte reste s'eteint pour indiquer que l'enregistrement est terminé
    lgpio.gpio_write(GPIO, 21, 0)

# Retourne la valeur choisie par la molette + 1
def molette():
    valeur_inv = [lgpio.gpio_read(GPIO, pin) for pin in [14, 15, 23, 24, 25]]
    valeur = [0 if inv else 1 for inv in valeur_inv]
    valeur_ = valeur[0] * 1 + valeur[1] * 2 + valeur[2] * 4 + valeur[3] * 8 + valeur[4] * 8 + 1
    return valeur_

def main():
    global stop_enrg
    while True:
        if button_on.is_pressed:
            stop_enrg = True
            # Lancement de l'enregistrement après 3 clignotements
            blink_led(17, 3, 0.2)
            # La LED verte s'allume pour indiquer que l'enregistrement est en cours
            lgpio.gpio_write(GPIO, 21, 1)
            nom_fichier = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            video = cv2.VideoCapture(0)
            if not video.isOpened():
                print("Erreur de lecture du fichier")
                return
            frame_width = int(video.get(3))
            frame_height = int(video.get(4))
            size = (frame_width, frame_height)
            fps = molette()
            print("______________________frame", fps)
            # Modifier le chemin d'enregistrement des vidéos si necessaire
            result = cv2.VideoWriter('/home/abc/Projet/Videos/' + nom_fichier + '.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, size)
            while stop_enrg:
                print("enrg")
                ret, frame = video.read()
                if ret:
                    result.write(frame)
                else:
                    break
            # Relâcher tout à la fin
            video.release()
            result.release()
            print("Vidéo enregistrée\n")

if __name__ == "__main__":
    # Clignote 2 fois pour indiquer que le programme est lancé
    blink_led(17, 2, 0.1)
    init()
    main()