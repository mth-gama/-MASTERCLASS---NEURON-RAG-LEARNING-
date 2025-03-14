import random
from datetime import datetime, timedelta, timezone


def get_people():
    def generate_cpf():
        return f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"

    def generate_birthdate():
        tz = timezone(timedelta(hours=-2))
        start_date = datetime(1950, 1, 1, tzinfo=tz)
        end_date = datetime(2005, 12, 31, tzinfo=tz)
        random_days = random.randint(0, (end_date - start_date).days)
        return start_date + timedelta(days=random_days)

    base_person = {
        "nome": "Gaybriel",
        "sobrenome": "Gay",
        "cpf": generate_cpf(),
        "caracteristicas": "Bahiano com cabeça chata, 1.75 magro, pele levemente escura (parda), 23cm para dentro",
        "vivo": True,
        "data_nascimento": generate_birthdate(),
        "descricao": "",
        "casado": True,
        "ocupacao": "gerente de bordel gay."
    }

    people_list = []

    total = 50
    same_person = int(total * 0.05)  # Exatamente igual (5%)
    similar_people = int(total * 0.50)  # Semelhantes (50%)
    different_people = int(total * 0.25)  # Totalmente diferentes (25%)
    same_lastname_occupation = int(total * 0.20)  # Mesmo sobrenome e ocupação (20%)

    # Adiciona pessoas exatamente iguais
    for _ in range(same_person):
        people_list.append(base_person.copy())

    # Adiciona pessoas semelhantes
    for _ in range(similar_people):
        person = base_person.copy()
        person["nome"] = person["nome"][:-1] + random.choice("abcdefghijklmnopqrstuvwxyz")  # Pequena variação no nome
        person["cpf"] = generate_cpf()
        person["data_nascimento"] = generate_birthdate()
        people_list.append(person)

    # Adiciona pessoas completamente diferentes
    for _ in range(different_people):
        person = {
            "nome": random.choice(["Carlos", "Fernanda", "José", "Luciana", "Roberto", "Amanda", "Thiago", "Beatriz"]),
            "sobrenome": random.choice(["Silva", "Pereira", "Costa", "Ferreira", "Rodrigues", "Almeida", "Santos", "Oliveira"]),
            "cpf": generate_cpf(),
            "caracteristicas": random.choice([
                "Alto e loiro", "Baixo e moreno", "Ruivo de olhos verdes", "Negro com cabelo encaracolado", "Asiático de baixa estatura"
            ]),
            "vivo": random.choice([True, False]),
            "data_nascimento": generate_birthdate(),
            "descricao": "",
            "casado": random.choice([True, False]),
            "ocupacao": random.choice(["Médico", "Engenheiro", "Professor", "Advogado", "Empresário", "Artista"])
        }
        people_list.append(person)

    # Adiciona pessoas com mesmo sobrenome e ocupação
    for _ in range(same_lastname_occupation):
        person = {
            "nome": random.choice(["João", "Mariana", "Gabriel", "Camila", "Rodrigo", "Sara", "Eduardo", "Vanessa"]),
            "sobrenome": base_person["sobrenome"],
            "cpf": generate_cpf(),
            "caracteristicas": random.choice([
                "Baixo e forte", "Magro e alto", "Cabelos cacheados", "Cabelo raspado", "Tatuagens pelo corpo"
            ]),
            "vivo": random.choice([True, False]),
            "data_nascimento": generate_birthdate(),
            "descricao": "",
            "casado": random.choice([True, False]),
            "ocupacao": base_person["ocupacao"]
        }
        people_list.append(person)

    return people_list