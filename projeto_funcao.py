import time

def registar_reserva(reservas):
    if len(reservas) >= 10:
       print("Todas as salas estão reservadas. Não é possível registrar mais reservas")
    else:
        try:
          reserva = int(input("Informe um número da sua reserva (1 a 10): "))
          if reserva < 1 or reserva > 10:
             print("Número de reserva inválido, por favor, insira um número entre 1 e 10")
          elif reserva in reservas:
             print(f"A reserva de nº {reserva}, já está registrada, tente outra sala")
          else:
             reservas.append(reserva)
             print("Aguarde um momento, estamos registrando sua reserva...")
             time.sleep(7)
             print(f"Reserva de nº {reserva} efetuada com sucesso!")
        except ValueError:
          print("Por favor, insira um número válido.")
                        

def cancelar_reserva(reservas):
  try:
      reserva = int(input("Informe o nº da sua reserva: "))
      if reserva in reservas:
          reservas.remove(reserva)
          print("Aguarde um momento, estamos cancelando sua reserva...")
          time.sleep(7)
          print(f"Reserva de nº: {reserva} cancelada com sucesso!") 
  except ValueError:
           print("Por favor, insira un número válido.")

def visualizar_reservas(reservas):
    if reservas:
      print("Verificando reservas existentes...:")
      for reserva in reservas:
        print(f"Você tem uma reserva de número: {reserva}")
        time.sleep(5)
    else:
        print("Não há reservas no momento.")

def consultar_disponibilidade (reservas):
      total_salas = 10
      salas_disponives = total_salas - len(reservas)
      print("Verificando o número de salas disponíveis para reserva. Aguarde...") 
      time.sleep(7)
      print(f"Temos {salas_disponives} salas diponísves para reserva")

def menu():
  print("Para acessar nossos serviços, informe a opção desejada:")
  print("1 - Resgistrar sua reserva")
  print("2 - Cancelar reservas")
  print("3 - Visualizar reservas")
  print("4 - Consultar disponibilidade")
  print("5 - Sair do sistema")

def reserva_de_salas():
    sair = False
    reservas = []
    print("Sejam todos bem vindos ao Sistema G4")

    while not sair:
      menu()
      try:
        op = int(input())
        if op == 1:
           registar_reserva(reservas)
        elif op == 2:
           cancelar_reserva(reservas)
        elif op == 3:
           visualizar_reservas(reservas)
        elif op == 4:
          consultar_disponibilidade(reservas)
        elif op == 5:
           print("Você está saindo do sistema. Obrigado pela visita!!")
           sair = True
        else:
           print("Escolha uma opção válida para prosseguir!")
      except ValueError:
          print("Por favor, insira um número válido")

reserva_de_salas()           