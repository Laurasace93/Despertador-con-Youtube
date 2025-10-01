#importamos librerias
import datetime
import time
import webbrowser
import os
import random

#archivo con URLs de youtube
URLS_FILE = "youtube_urls.txt"

#funcion para cargar URLs desde un archivo
def obtener_urls():
    try:
        with open(URLS_FILE, 'r') as f:
            # Filtra las líneas vacías o solo con espacios
            urls = [line.strip() for line in f if line.strip()]
        if not urls:
            print(f"⚠️ El archivo '{URLS_FILE}' está vacío. Asegúrate de añadir URLs.")
            return None
        return urls
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{URLS_FILE}' no se encuentra.")
        print("Crea este archivo y añade URLs de YouTube, una por línea.")
        return None

def establecer_alarma():
    """Permite al usuario establecer la hora de la alarma y la espera."""
    while True:
        try:
            # Pide la hora de la alarma en formato HH:MM (24 horas)
            alarma_tiempo = input("Establece la hora de la alarma (HH:MM, formato 24h): ")
            # Intenta parsear la entrada a un objeto time
            hora_alarma = datetime.datetime.strptime(alarma_tiempo, "%H:%M").time()
            break
        except ValueError:
            print("Formato de hora no válido. Por favor, usa HH:MM (ej: 07:30).")

    urls_disponibles = obtener_urls()
    if not urls_disponibles:
        # Sale si no hay URLs válidas
        return

    print("-" * 30)
    print(f"✅ Alarma configurada para las {hora_alarma.strftime('%H:%M')}.")
    print("El despertador está esperando...")
    print("-" * 30)

    # Bucle principal de la alarma
    alarm_set = False
    while not alarm_set:
        # Obtiene la hora actual
        ahora = datetime.datetime.now()
        
        # Compara solo la hora y minuto
        if ahora.hour == hora_alarma.hour and ahora.minute == hora_alarma.minute:
            # ¡Es hora de despertar!
            
            # 1. Selecciona una URL aleatoria
            url_a_reproducir = random.choice(urls_disponibles)
            print("\n🚨 ¡ALARMA! 🚨")
            print(f"Reproduciendo: {url_a_reproducir}")
            
            # 2. Abre la URL en el navegador por defecto
            try:
                webbrowser.open(url_a_reproducir, new=2) # 'new=2' abre una nueva pestaña del navegador
            except Exception as e:
                print(f"Error al abrir la URL: {e}")

            alarm_set = True # Detiene el bucle

        # Espera 1 segundo antes de volver a comprobar
        time.sleep(1)

if __name__ == "__main__":
    establecer_alarma()




