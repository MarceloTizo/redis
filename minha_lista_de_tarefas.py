import redis


redis_client = redis.Redis(host='localhost', port=6379, db=0)

def adicionar_tarefa(descricao):
    #cria o id para a tarefa
    id_tarefa = redis_client.incr('tarefa:id')

    # Armazenando a descrição da tarefa como um valor no Redis
    redis_client.set(f'tarefa:{id_tarefa}', descricao)

def listar_tarefas():
    # Obtendo todas as chaves que correspondem a tarefas
    chaves_tarefas = redis_client.keys('tarefa:*')

    tarefas = []

    for chave in chaves_tarefas:
        id_tarefa = chave.decode('utf-8').split(':')[1]
        descricao = redis_client.get(chave).decode('utf-8')
        tarefas.append({'id': id_tarefa, 'descricao': descricao})

    return tarefas

def remover_tarefa(id_tarefa):
    
    redis_client.delete(f'tarefa:{id_tarefa}')


descricao_tarefa = input("Digite a descrição da tarefa: ")
adicionar_tarefa(descricao_tarefa)

print("Lista de tarefas:")
for tarefa in listar_tarefas():
    print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}")


id_tarefa_remover = input("Digite o ID da tarefa a ser removida: ")
remover_tarefa(id_tarefa_remover)

print(f"Tarefa com ID {id_tarefa_remover} removida.")
