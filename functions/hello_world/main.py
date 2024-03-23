import json
from dataclasses import dataclass

@dataclass
class Input:
    pass

@dataclass
class Output:
    message: str


def lambda_handler(event, context):

    data = {
	"story_id": "6060ec3a-6b8c-478e-9a9a-331ea3e625ce",
	"character_image_url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-pADpEhLbKeKYQSV1lwh7BwxB/user-F2K1ftTzZTvhgeopase4ul5P/img-DsmiZWM8diIuPRdR50xoiapk.png?st=2024-03-22T12%3A24%3A42Z&se=2024-03-22T14%3A24%3A42Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-21T21%3A40%3A25Z&ske=2024-03-22T21%3A40%3A25Z&sks=b&skv=2021-08-06&sig=o/MT6lEhnev8fU8tCPwCwYFbNuXmKS8MxXldUtQZeyc%3D",
	"scene": {
		"description": "Sabrina chegou à cidade de Arcádia, conhecida por sua grande torre de magos e mercados repletos de itens mágicos. Nas ruas movimentadas, ela observa vendedores oferecendo poções e pergaminhos, enquanto guildas de magos praticam feitiços para os transeuntes curiosos.",
		"npcs": [
			{
				"name": "Merlinho, o Mercador de Poções",
				"description": "Um velho mago de barba branca, vestido com roupas coloridas e um chapéu pontudo.",
				"image_url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-pADpEhLbKeKYQSV1lwh7BwxB/user-F2K1ftTzZTvhgeopase4ul5P/img-oC4M9AJpazjClxohFO9vxWpz.png?st=2024-03-22T12%3A25%3A07Z&se=2024-03-22T14%3A25%3A07Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-21T21%3A05%3A03Z&ske=2024-03-22T21%3A05%3A03Z&sks=b&skv=2021-08-06&sig=1au/M8PwBFluUsADloYWIpabg646XB3GuvfBXuzcqcw%3D"
			},
			{
				"name": "Eliana, a Jovem Feiticeira",
				"description": "Uma feiticeira de aparência misteriosa, com olhos faiscantes e um cajado adornado com gemas brilhantes.",
				"image_url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-pADpEhLbKeKYQSV1lwh7BwxB/user-F2K1ftTzZTvhgeopase4ul5P/img-PgreljLETcTHhvKrFjEGa0Hp.png?st=2024-03-22T12%3A25%3A31Z&se=2024-03-22T14%3A25%3A31Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-21T21%3A13%3A20Z&ske=2024-03-22T21%3A13%3A20Z&sks=b&skv=2021-08-06&sig=b2ZRGfWSocaTSUlbhUT497IZPkmHv73JHCBIMB8e6ao%3D"
			}
		],
		"location": {
			"name": "Arcádia",
			"description": "Uma cidade mágica repleta de guildas de magos, mercados de itens arcanos e uma atmosfera vibrante de magia no ar.",
			"time": "Tarde",
			"weather": "Ensolarado",
			"image_url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-pADpEhLbKeKYQSV1lwh7BwxB/user-F2K1ftTzZTvhgeopase4ul5P/img-xrq2O4FT5orXjqVC4ge2PZMD.png?st=2024-03-22T12%3A25%3A51Z&se=2024-03-22T14%3A25%3A51Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-03-21T21%3A00%3A10Z&ske=2024-03-22T21%3A00%3A10Z&sks=b&skv=2021-08-06&sig=NpWvA4FjubrGD/VjPHUjAfZICwe%2BsNY%2BDMtlKSjNtrU%3D"
		},
		"dialog": [],
		"options": [
			"Explorar o mercado de itens mágicos",
			"Visitar a grande torre dos magos",
			"Procurar por livros de magia na biblioteca",
			"Conversar com Merlinho, o Mercador de Poções",
			"Observar os feiticeiros praticando feitiços na praça"
		],
		"text": "Sabrina é uma jovem maga em busca de conhecer e dominar novas magias. Criada por uma família de magos renomados, ela decidiu partir em jornada solo para provar seu valor e descobrir seu lugar no mundo mágico. Sabrina chegou à cidade de Arcádia, conhecida por sua grande torre de magos e mercados repletos de itens mágicos. Nas ruas movimentadas, ela observa vendedores oferecendo poções e pergaminhos, enquanto guildas de magos praticam feitiços para os transeuntes curiosos. O que Sabrina deseja fazer em Arcádia?. "
    }
    }

    return {
        "statusCode": 200,
        "body": json.dumps({"data": data})
    }
