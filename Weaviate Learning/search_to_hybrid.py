import weaviate
import os

from dotenv import load_dotenv
import time
import weaviate.classes.query as wq
from weaviate.classes.init import Auth
from weaviate.classes.query import Filter

load_dotenv()

wcd_url = os.getenv("WCD_URL")
wcd_apikey = os.getenv("WCD_API_KEY")
openai_apikey = os.getenv("OEPANAI_API_KEY")

MAGENTA = '\033[35m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'
headers = {
    "X-OpenAI-Api-Key": openai_apikey
}  # Replace with your OpenAI API key

try:
    start_time = time.time()
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=wcd_url,  # Replace with your WCD URL
        auth_credentials=Auth.api_key(
        wcd_apikey
        ),
        headers=headers
    )

    colletion = client.collections.get("People")
    
    pesquisa="Gaybrien"

    # PESQUISA HIBRIDA QUE COMBINA PALAVRAS CHAVE E SEMANTICA
    response = colletion.query.near_text(
        query=pesquisa, 
        limit=4, 
        distance=0.7,
        return_metadata=wq.MetadataQuery(distance=True),
        filters=Filter.by_property("cpf").equal("607.501.262-98"),
    )


    # Inspect the response
    for o in response.objects:
        print(f" > Nome             : [{MAGENTA}{o.properties['nome']}{RESET}]" )  # Print the title
        print(f" > Sobrenome        : [{MAGENTA}{o.properties['sobrenome']}{RESET}]" )  # Print the title
        print(f" > cpf              : [{MAGENTA}{o.properties['cpf']}{RESET}]" )  # Print the title
        print(f" > caracteristicas  : [{MAGENTA}{o.properties['caracteristicas']}{RESET}]" )  # Print the title
        print(f" > vivo             : [{MAGENTA}{o.properties['vivo']}{RESET}]" )  # Print the title
        print(f" > data_nascimento  : [{MAGENTA}{o.properties['data_nascimento']}{RESET}]" )  # Print the title
        print(f" > descricao        : [{MAGENTA}{o.properties['descricao']}{RESET}]" )  # Print the title
        print(f" > casado           : [{MAGENTA}{o.properties['casado']}{RESET}]" )  # Print the title
        print(f" > ocupacao         : [{MAGENTA}{o.properties['ocupacao']}{RESET}]" )  # Print the title
        print(f" > %                : [{MAGENTA}{o.metadata.distance}{RESET}]" )  # Print the title

        print("-"*20)

    #print(response.generated)
        
except Exception as ex:
    print("ERRRRRRO")
    print(ex)
finally:
    client.close()

end_time = time.time()  # Fim da medição do tempo
execution_time = end_time - start_time
print(f"Tempo de execução: {execution_time:.2f} segundos")