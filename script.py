import openai
from dotenv import load_dotenv
import os

def main():

    # Coloca tu clave de API aquí
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Crea una función que toma un mensaje y devuelve una respuesta de la API
    def generate_response(prompt):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content.strip()
    
    # Inicia un bucle de entrada/salida para enviar y recibir mensajes
    while True:
        user_message = input("User: ")
        response = generate_response(user_message)
        print("ChatGPT: " + response)


if __name__ == '__main__':
    main()



