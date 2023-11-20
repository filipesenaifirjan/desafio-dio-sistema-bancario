class ContaBancaria:
  def __init__(self):
      self.saldo = 500
      self.saque_diario = 0
      self.total_saques = 0
      self.extrato = []

  def deposito(self, valor):
      if valor > 0:
          self.saldo += valor
          self.extrato.append(f'Depósito de R$ {valor:.2f}')
          print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
      else:
          print('O valor do depósito deve ser maior que zero.')

  def saque(self, valor):
      if self.total_saques < 3:
          if valor <= self.saldo and valor <= 500 and valor > 0:
              self.saldo -= valor
              self.saque_diario += valor
              self.total_saques += 1
              self.extrato.append(f'Saque de R$ {valor:.2f}')
              print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
          elif valor > self.saldo:
              print('Saldo insuficiente para saque.')
          elif valor <= 0:
              print('Valor inválido para saque.')
          else:
              print('Valor máximo por saque é R$ 500.')
      else:
          print('Limite diário de saques atingido.')

  def extrato_bancario(self):
      print('Extrato Bancário:')
      for movimento in self.extrato:
          print(movimento)
      print(f'Saldo atual: R$ {self.saldo:.2f}')

  def emprestimo(self, valor):
      if valor > 0:
          valor_emprestado = valor * 1.10  # Valor emprestado com 10% de juros
          self.saldo += valor_emprestado
          self.extrato.append(f'Empréstimo de R$ {valor:.2f} (Valor recebido: R$ {valor_emprestado:.2f})')
          print(f'Empréstimo de R$ {valor:.2f} realizado com sucesso.')
      else:
          print('Valor inválido para empréstimo.')


# Uso do sistema bancário
conta = ContaBancaria()

while True:
  print('\nOpções Disponíveis:')
  print('1 - Saque')
  print('2 - Depósito')
  print('3 - Extrato')
  print('4 - Empréstimo')
  print('5 - Sair')

  opcao = input('Escolha uma opção: ')

  if opcao == '1':
      valor_saque = float(input('Digite o valor do saque: '))
      conta.saque(valor_saque)
  elif opcao == '2':
      valor_deposito = float(input('Digite o valor do depósito: '))
      conta.deposito(valor_deposito)
  elif opcao == '3':
      conta.extrato_bancario()
  elif opcao == '4':
      valor_emprestimo = float(input('Digite o valor do empréstimo: '))
      conta.emprestimo(valor_emprestimo)
  elif opcao == '5':
      print('Encerrando o programa.')
      break
  else:
      print('Opção inválida. Escolha novamente.')
