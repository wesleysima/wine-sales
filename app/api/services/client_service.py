import requests, json
from api.external_apis.velasquez_api import get_clients, get_history_and_purchases

def sort_by_total_purchases():
    sorted_clients = []
    clients = get_clients()
    history = get_history_and_purchases()
    sum_purchases = 0

    for client in clients:
        filtered_history = history_cpf_filter(history, client['cpf'])
        
        for history_item in filtered_history:
            for item in history_item['itens']:
                sum_purchases += item['preco']
        
        sorted_clients.append({'id': client['id'], 'nome': client['nome'], 'cpf': client['cpf'], 'Valor total em compras': int(sum_purchases)})
        sum_purchases = 0

    sorted_clients = sorted(sorted_clients, key=lambda x: x['Valor total em compras'], reverse=True) # ordenando pelo valor total em compras

    return sorted_clients

def get_biggest_single_purchase():
    clients = get_clients()
    history = get_history_and_purchases()
    sum_unique_purchase = 0
    biggest_value = 0
    biggest_single_client = {}

    for client in clients:
        filtered_history = history_cpf_filter(history, client['cpf'])

        for history_item in filtered_history:
            if '2016' in history_item['data']: # validando se o ano da compra é 2016
                for item in history_item['itens']:
                    sum_unique_purchase += item['preco'] # somando os itens apenas dessa compra
                
                if sum_unique_purchase > biggest_value: # validando se é a maior compra registrada no ano de 2016
                    biggest_value = sum_unique_purchase
                    biggest_single_client = {'id': client['id'], 'nome': client['nome'], 'cpf': client['cpf'], 'Valor total compra unica': int(sum_unique_purchase), 'itens': history_item['itens']}

                sum_unique_purchase = 0
    return biggest_single_client

def get_list_faithful_clients():
    clients = get_clients()
    history = get_history_and_purchases()
    clients_and_purchaes = []

    for client in clients:
        filtered_history = history_cpf_filter(history, client['cpf'])

        clients_and_purchaes.append({'id': client['id'], 'nome': client['nome'], 'cpf': client['cpf'], 'Vezes que comprou na loja de vinhos': len(filtered_history)})

    sorted_clients_and_purchases = sorted(clients_and_purchaes, key=lambda x: x['Vezes que comprou na loja de vinhos'], reverse=True) # ordenando pelo número de vezes que o cliente ele comprou

    return sorted_clients_and_purchases

def get_client_wine_recommendation(client_id):
    clients = get_clients()
    history = get_history_and_purchases()
    client_cpf = {}
    client_wines = []

    for client in clients:
        if client['id'] == int(client_id):
            client_cpf = client['cpf']
            break
    
    filtered_history = history_cpf_filter(history, client_cpf)

    # o codigo adiante, pega todos os vinhos comprados pelo cliente, faz um count de quantas vezes esse vinho apareceu, e retorna o que foi comprado mais vezes
    for history_item in filtered_history:
        for item in history_item['itens']:

            if len(client_wines) == 0:
                client_wines.append({'wine': item['produto'], 'qtd': 1})
            else:
                if item['produto'] not in get_wines_names(client_wines):
                    client_wines.append({'wine': item['produto'], 'qtd': 1})
                else:
                    for idx, wine in enumerate(client_wines):
                        if wine['wine'] == item['produto']:
                            client_wines[idx]['qtd'] += 1

    client_wines = sorted(client_wines, key=lambda x: x['qtd'], reverse=True) # ordenando pela quantidade que que o vinho apareceu nas compras

    return {'Vinho indicado': client_wines[0]['wine']}

# retorna apenas os nomes dos vinhos ja adicionados no array do cliente
def get_wines_names(wines):
    names = []

    for wine in wines:
        names.append(wine['wine'])
    
    return names

def history_cpf_filter(history, cpf):
    filtered_history = []
    for h in history:
        history_cpf = h['cliente'][:12] + '-' + h['cliente'][12+1:] # veixando o cpf no mesmo formato
        if len(history_cpf) == 15: # verificando se tem um zero a mais no cpf
            history_cpf = history_cpf[:0] + history_cpf[1:] # retirando esse zero

        if history_cpf == cpf:
            filtered_history.append(h)
    
    return filtered_history

