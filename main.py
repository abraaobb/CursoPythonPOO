import random

if __name__ == '__main__':
    participantes = ["Alessandro Almeida De Souza",
                     "Allan De Oliveira Salgado Gomes",
                     "Apolo Ícaro Silva De Oliveira",
                     "Caio De Matos Barbosa",
                     "Carlos Renan Batista De Oliveira",
                     "Daniel Cordeiro Patricio",
                     "Davi Ferreira Da Silva",
                     "Davi Rodrigues Barbalho",
                     "Gustavo Ramos Pereira",
                     "Ike Kalel Freire Munoz",
                     "João Pedro Paiva Pereira Dos Santos",
                     "Lian Da Silva Marinho",
                     "Luan Silva De Souza",
                     "Lucas Vieira Silva",
                     "Luciano Garcia De Almeida",
                     "Luis Filipi Brandão Osório",
                     "Raquel Paula Cruz",
                     "Renan Da Silva Serrão",
                     "Ryan Victor Rodrigues Ribeiro",
                     "Suell Richard Da Rocha Ribeiro",
                     "Vitor Hugo Da Silva Lima",
                     "Wanna Laura Lima De Aguiar",
                     "Isaac Maximus Neves Taquita",
                     "Kayk Alberth"]

    player1 = random.choice(participantes)
    player2 = random.choice(participantes)

    print(f"A dupla é {player1} e {player2}")
