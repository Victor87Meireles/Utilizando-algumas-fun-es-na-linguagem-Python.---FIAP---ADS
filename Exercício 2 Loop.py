quantidade_transacoes = int(input("Informe a quantidade de transações"))
total_transacoes = 0
for n_transacao in range(1, quantidade_transacoes + 1, 1):
    transacao = float(input("Por favor informe a transação de número {}".format(n_transacao)))
    total_transacoes = total_transacoes + transacao

media = total_transacoes / quantidade_transacoes
print("Neste dia foi gasto um total de R${}, com uma média de R${} por transação".format(total_transacoes, media))