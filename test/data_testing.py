ARGS_LIST_CONTACTS: list = [
    {
        "id": 1,
        "firstname": "first_name",
        "lastname": "first_last_name",
        "address": ["Cortes, San Pedro Sula", "Siguatepeque, Las Lomas"],
        "telephone": ["+504 9234-0934"],
    },
    {
        "id": 2,
        "firstname": "second_name",
        "lastname": "second_last_name",
        "address": ["Ciudad de la Ceiba"],
        "telephone": ["+504 9234-5934", "+503 9345-9567"],
    },
    {
        "id": 3,
        "firstname": "threeth_name",
        "lastname": "three_last_name",
        "address": [
            "SPS, 7 avenida, 14 calle",
            "Residencial Palos Verdes",
            "Mexico D.F.",
        ],
        "telephone": [],
    },
    {
        "id": 4,
        "firstname": "fourth_name",
        "lastname": "fourth_last_name",
        "address": [],
        "telephone": ["+504 3394-9942"],
    },
    {
        "id": 5,
        "firstname": "Paolo",
        "lastname": "Brand",
        "address": ["Cortes"],
        "telephone": [],
    },
    {
        "id": 6,
        "firstname": "Juan",
        "lastname": "Hernandez",
        "address": [],
        "telephone": [],
    },
    {
        "id": 7,
        "firstname": "Juan",
        "lastname": "Manueles",
        "address": [],
        "telephone": [],
    },
    {
        "id": 8,
        "firstname": "Marcos",
        "lastname": "Fernandez",
        "address": [],
        "telephone": ["9234-9234"],
    },
    {
        "id": 9,
        "firstname": "Jorge",
        "lastname": "Lozano",
        "address": ["Los angeles"],
        "telephone": [],
    },
    {
        "id": 10,
        "firstname": "Rodolfo",
        "lastname": "Manzanares",
        "address": ["San Francisco"],
        "telephone": [],
    },
    {"id": 11, "firstname": "Raul", "lastname": "Vega", "address": [], "telephone": []},
    {
        "id": 12,
        "firstname": "Paco",
        "lastname": "Menbreño",
        "address": [],
        "telephone": [],
    },
]


ARGS_LIST_ADDRESS = []
for arg in ARGS_LIST_CONTACTS:
    for address in arg["address"]:
        ARGS_LIST_ADDRESS.append(
            dict(zip(["contact_id", "address"], [arg["id"], address]))
        )

ARGS_LIST_TELEPHONE = []
for arg in ARGS_LIST_CONTACTS:
    for telephone in arg["telephone"]:
        ARGS_LIST_TELEPHONE.append(
            dict(zip(["contact_id", "telephone"], [arg["id"], telephone]))
        )
