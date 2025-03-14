import os
import weaviate

from weaviate.classes.init import Auth



from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta
from example import get_people


# Criando um fuso horário UTC-2
tz = timezone(timedelta(hours=-2))

# Obtendo a data e hora atual com o fuso horário
current_time = datetime.now(tz)


load_dotenv()


wcd_url = os.getenv("WCD_URL")
wcd_apikey = os.getenv("WCD_API_KEY")
openai_apikey = os.getenv("OEPANAI_API_KEY")


people = get_people()

try:

    headers = {
        "X-OpenAI-Api-Key": openai_apikey
    }


    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,
        auth_credentials=Auth.api_key(wcd_apikey),
       
        headers=headers
    )

    colletion = client.collections.get("People")

    with colletion.batch.dynamic() as batch:
        for indice, person in enumerate(people, 1):
            print(f"[{indice}] Cadastrando pessoa {person.get("nome")}")

            batch.add_object(
                properties=person
            )

    if len(colletion.batch.failed_objects) > 0:
        print(f"Falou aqui ó {len(colletion.batch.failed_objects)}")

except Exception as ex:
    print(ex)

finally:
    client.close()