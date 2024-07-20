def reservaDeSalas():
    sair = False
    reservas = []


    while (sair == False):
        try:
            print("Sejam bem vindos ao Sistema G4. \nPara acessar nossos serviços, informe a opção desejada:\n1 - Registrar sua reserva \n2 - Cancelar reservas \n3 - Visualizar reservas \n4 - Consultar disponibilidades \n5 - Sair do sistema" )
            op = int(input())
            if (op == 1):
              if len(reservas) >= 10:
                print("Todas as salas estão reservadas. Não é possível registar mais reservas")
              else:
                reserva = int(input("Informe o número da sua reserva (1 a 10):"))
                if reserva < 1 or reserva > 10:
                  print("Número de reserva inválido. Por favor, insira um número entre 1 e 10.")
                elif reserva in reservas:
                  print("A reserva de nº: "+ str(reserva) +" já está registrada. Por favor, escolha outro número")
                else:
                  reservas.append(reserva)
                  print("Aguarde um momento. Estamos registrando sua reserva...")
                  print("Reserva nº: " +  str(reserva) + " efetuada com sucesso!")
            elif (op == 2):
                reserva = int(input("Informe o nº da sua reserva: "))
                if (reserva in reservas):
                    reservas.remove(reserva)
                    print("Aguarde um momento. Estamos cancelando a sua reserva....")
                    print("Reserva de nº: " + str(reserva) + " cancelada com sucesso!")
                else:
                    print("Reserva de nº " +str(reserva) + " não encontrada!")
            elif (op == 3):
                if reservas:
                    print("Reservas existentes:")
                    for reserva in reservas:
                        print("Você tem uma reserva de nº: " + str(reserva))
                else:
                    print("Não há reservas no momento.")
            elif (op == 4):
                totalSalas = 10
                salasDisponiveis = totalSalas - len(reservas)
                print("Verificando nº de salas disponíveis para reserva. Aguarde...")
                print("Temos " + str(salasDisponiveis) + " salas disponíveis para reserva.")
            elif (op == 5):
                print("Você está saindo do sistema. Obrigada pela visita!")
                sair = True
            else:
                print("Escolha uma opção válida para prosseguir!")
        except ValueError:
            print("Por favor, insira um número válido.")

reservaDeSalas()