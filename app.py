from textwrap import dedent


def main() -> None:
    """
    Função principal
    """
    def menu() -> int:
        """
        Imprime o menu prinpcipal
        """
        print(
            dedent(
                """
                =========================
                |          MENU         |
                =========================
                :: 1 - Jogar novamente ::
                :: 2 - Placar          ::
                :: 0 - Sair            ::
                :::::::::::::::::::::::::
                """
            ), end=''
        )

        # Retorna a escolha feita por um jogador
        return int(input(':: > '))


    def game() -> tuple:
        """
        Recebe as entradas dos jogadores, seta em qual espaço da matriz 
        (tabuleiro) será armazenado a entrada de cada jogador, também 
        verifica se já houve uma jogada naquele espaço e se houve 
        vitória por parte de um jogador.
        """
        rounds = 0

        while True:
            # Armazena um mensagem de erro, quando se já tem uma jogada
            CASA_OCUPADA = 'Casa ocupada!\nTente novamente...'

            # Conta os rounds
            rounds += 1

            # Imprime e define quem está jogando no momento
            print(f'\n  #Jogador: {1 if rounds % 2 else 2} ', end='')

            # Imprime o tabuleiro
            exibir()

            # Imprime em qual round a partida se encontra
            print(f'  > Round: {rounds}\n')

            # Recebe a jogada do jogador
            lance = int(input('Número: '))


            def retornar_jogada() -> int:
                """
                Identifica o jogador e a peça do ultimo lance
                """
                if rounds % 2:
                    return 1
                else:
                    return -1

            # Identifica qual casa o jogador escolheu
            # Identifica se já houve jogada na casa escolhida
            match lance:
                case 1:
                    if not tabuleiro[0][0]:
                        tabuleiro[0][0] = retornar_jogada()
                    else:
                        rounds -= 1
                        print(CASA_OCUPADA)

                case 2:
                    if not tabuleiro[0][1]:
                        tabuleiro[0][1] = retornar_jogada()
                    else:
                        rounds -= 1
                        print(CASA_OCUPADA)

                case 3:
                    if not tabuleiro[0][2]:
                        tabuleiro[0][2] = retornar_jogada()
                    else:
                        rounds -= 1
                        print(CASA_OCUPADA)

                case 4:
                    if not tabuleiro[1][0]:
                        tabuleiro[1][0] = retornar_jogada()
                    else:
                        rounds -= 1
                        print(CASA_OCUPADA)

                case 5:
                    if not tabuleiro[1][1]:
                        tabuleiro[1][1] = retornar_jogada()
                    else:
                        rounds -= 1
                        print(CASA_OCUPADA)

                case 6:
                    if not tabuleiro[1][2]:
                        tabuleiro[1][2] = retornar_jogada()
                    else:
                        rounds -= 1
                        print(CASA_OCUPADA)
                
                case 7:
                    if not tabuleiro[2][0]:
                        tabuleiro[2][0] = retornar_jogada()
                    else:
                        rounds -= 1
                        print(CASA_OCUPADA)

                case 8:
                    if not tabuleiro[2][1]:
                        tabuleiro[2][1] = retornar_jogada()
                    else:
                        rounds -= 1
                        print(CASA_OCUPADA)

                case 9:
                    if not tabuleiro[2][2]:
                        tabuleiro[2][2] = retornar_jogada()
                    else:
                        rounds -= 1
                        print(CASA_OCUPADA)

                case _:
                    rounds -= 1
                    print('Jogada INVÁLIDA!\nTente novamente...')

            # Verifica se houve vitória
            if vitoria():
                return 1, rounds

            # Verifica se houve empate
            elif rounds > 8:
                exibir()
                print('Empate, FIM DE JOGO!')
                return


    def vitoria() -> int:
        """
        Retorna se houve ou não vencedor
        """
        def verificar(value: int, value2: int, value3: int) -> int:
            """
            Através da soma das linhas verifica se houve ou não vitória
            por parte de um jogador
            """

            # Recebe a soma das linhas e colunas
            soma = (
                value
                + value2
                + value3
            ) 

            # Verifica se houve vitória e quem venceu
            if soma == 3 or soma == -3:
                if soma == 3:
                    exibir()
                    print('Jogador 1 VENCEU!')
                else:
                    exibir()
                    print('Jogador 2 VENCEU!')
                return 1


        # Vitória na diagonal (do topo esquerda para direita baixo
        if verificar(
            tabuleiro[0][0], 
            tabuleiro[1][1], 
            tabuleiro[2][2]
        ):
            return 1
        
        # Vitória na diagonal (do topo direita para esquerda baixo)
        if verificar(
            tabuleiro[0][2], 
            tabuleiro[1][1], 
            tabuleiro[2][0]
        ):
            return 1
        
        # Vitórias nas linhas horizontais (coluna fixa linha dinamica)
        for i in range(3):
            if verificar(
                tabuleiro[i][0],
                tabuleiro[i][1],
                tabuleiro[i][2]
            ):
                return 1
        
        # Vitórias nas linhas verticais (coluna dinamica linha fixa)
        for i in range(3):
            if verificar(
                tabuleiro[0][i],
                tabuleiro[1][i],
                tabuleiro[2][i]
            ):
                return 1


    def exibir() -> None:
        """
        Imprime o tabuleiro do jogo
        """

        # Valores mostrados ao usuário
        placeholder = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        # Substitui as entradas pela peça de escolha do jogador
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == 1:
                    placeholder[i][j] = 'X'
                elif tabuleiro[i][j] == -1:
                    placeholder[i][j] = 'O'

        # Imprime o tabuleiro
        print(
            dedent(
                f"""
                :::::::::::::::
                :: {placeholder[0][0]} | {placeholder[0][1]} | """
                f"""{placeholder[0][2]} ::
                ::===========::
                :: {placeholder[1][0]} | {placeholder[1][1]} | """
                f"""{placeholder[1][2]} ::
                ::===========::
                :: {placeholder[2][0]} | {placeholder[2][1]} | """
                f"""{placeholder[2][2]} ::
                :::::::::::::::
                """
            ), end=''
        )


    def exibir_placar() -> None:
        """
        Imprime o placar do jogo e verifica o jogador com mais vitórias
        """

        # Verifica se o jogador 1 venceu
        if ven % 2:
            placar[0].get("jogador1")["vitorias"] += vit

        # Verifica se o jogador 2 venceu
        else:
            placar[1].get("jogador2")["vitorias"] += vit
        
        # Imprime o placar
        print(
            dedent(
                f"""
                :::::::::::::::::::::::
                ::    X    |    O    ::
                :::::::::::::::::::::::
                ::    {placar[0].get("jogador1")["vitorias"]}    |    """
                f"""{placar[1].get("jogador2")["vitorias"]}    ::
                :::::::::::::::::::::::
                """
            )
        )

    # Armazena as vitórias de cada jogador
    placar = [
        {"jogador1": {"vitorias": 0}},
        {"jogador2": {"vitorias": 0}}
    ]

    # Recebe a escolhas dos jogadores referêntes ao menu
    # e aplica o desejo do jogador.
    while True:
        match menu():
            case 1:
                tabuleiro = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]
                vit, ven = game()
            case 2:
                exibir_placar()
            case 0:
                break
            case _:
                print('Opção INVÁLIDA\nTente novamente...')


main()
