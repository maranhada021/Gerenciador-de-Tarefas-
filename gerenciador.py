
tarefas = []

def adicionar_tarefa(descricao, prioridade, tempo): # Função de adicionar a tarefa e colocar ela automatica como nao concluida
    
    if not descricao.strip(): # Comando para verificar se o usuário deixou o input em branco e o .strip para retirar espaços em brancos do inicio e fim
        print("A descrição da tarefa não pode ser vazia.")
        return
    
    for tarefa in tarefas: # Verificador se ja existe a tarefa na lista
        if tarefa['descricao'].lower() == descricao.lower():
            print(f"Tarefa '{descricao}' já existe na lista.")
            return
          
    tarefas.append({"descricao": descricao, 'concluida': False, 'prioridade': prioridade, 'data de validade': tempo}) # Comando para adicionar a tarefa/prioridade e data na lista
    print(f"Tarefa '{descricao}' com prioridade '{prioridade}' e tempo para {tempo} dias adicionada com sucesso!")


def editar_tarefa(indice, nova_descricao): # Comando para editar alguma tarefa da lista
   
   if not nova_descricao.strip():
       print("A nova descrição da tarefa não pode ser vazia.")
       return
   
   if 1 <= indice <= len(tarefas): # Comando pra verificar se o indice do usario existe na tabela
        tarefa_original = tarefas[indice - 1]['descricao']
        tarefas[indice - 1]['descricao'] = nova_descricao
        print(f"Tarefa '{tarefa_original}' editada para '{nova_descricao}' com sucesso!")

   else:
        print('Índice inválido. Por favor, digite um número da lista para editar.')


def listar_tarefa(): # funçao para listar as tarefas da lista
    
    print("\n--- MINHAS TAREFAS ---")

    if not tarefas: # comando para se não tiver tarefa na lista aparecer uma mensagem.
        print("Nenhuma tarefa cadastrada no momento.")
        print("----------------------\n") 
        return

    for i, tarefa in enumerate(tarefas, 1): # comando para listar as tarefas.
        status = 'Concluída' if tarefa['concluida'] else "Pendente" 
        prioridade = tarefa.get('prioridade', 'Não definida') 
        data = tarefa.get('data de validade', 'Não informada')
        print(f'{i}. {tarefa["descricao"]} [{status}] - Prioridade: {prioridade} - tempo: {data} dias')
    print("----------------------\n") # 

def concluir_tarefa(indice): # funçao para declarar as tarefas como concluida
    
    if 1 <= indice <= len(tarefas):
        tarefa_a_concluir = tarefas[indice - 1] 

        if tarefa_a_concluir['concluida']: # comando para verificar se a tarefa ja esta concluida
            print(f"A tarefa '{tarefa_a_concluir['descricao']}' já está concluída.")

        else:
            tarefa_a_concluir['concluida'] = True
            print(f"Tarefa '{tarefa_a_concluir['descricao']}' marcada como concluída!")
    else:
        print('Índice inválido. Por favor, digite um número da lista.')

def remover_tarefa(indice): # funçao para remover as tarefas da lista
    
    if 1 <= indice <= len(tarefas):
        tarefa_removida = tarefas.pop(indice - 1) # comando .pop para remover o indice e retorna o item
        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!") 
    else:
        print('Índice inválido. Por favor, digite um número da lista.')


def editar_prioridade(indice, prioridade): # funçao para definir ou atualizar a prioridade de uma tarefa

    try:
        indice_real = int(indice) # Converte o índice para inteiro
        if not (1 <= indice_real <= len(tarefas)):
            print('Índice inválido ao tentar definir prioridade. Por favor, digite um número da lista.')
            return

        tarefas[indice_real - 1]['prioridade'] = prioridade
        print(f"Prioridade da tarefa {tarefas[indice_real - 1]['descricao']} atualizada para {prioridade}.")

    except ValueError:
        print('Entrada de índice inválida. Por favor, digite um número.')
    
def editar_data(indice, nova_data): # Função para editar a data da tarefa
    try:
        ind = int(indice)
        if not (1 <= ind <= len(tarefas)):
            print('Índice inválido ao tentar definir prioridade. Por favor, digite um número da lista.')
            return
        
        print(f'O tempo {tarefas[ind - 1]['data de validade']} dias atualizada para {nova_data} dias')
        tarefas[ind - 1]['data de validade'] = nova_data
        

    except ValueError:
        print('Entrada de índice inválida. Por favor, digite um número.')

def menu(): # O menu do codigo
    while True:
        print("\n--- GERENCIADOR DE TAREFAS ---") 
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Editar tarefa")
        print("6 - Definir prioridade da tarefa")
        print("7 - Editar tempo restante")
        print("8 - sair")
        print("-----------------------------------------------------")

        opcao = input('Digite o que deseja fazer: ').strip() 

        if opcao == "1": # Adicionar tarefa
            desc = input('Digite a descrição da tarefa: ')

            if not desc.strip():
                print("A descrição não pode ser vazia. Tente novamente.")
                continue

            print("\nEscolha a prioridade:")
            print("1 - Baixa")
            print("2 - Média")
            print("3 - Alta")
            prioridade_escolha = input("Digite o número da prioridade desejada (1, 2 ou 3): ").strip()

            mapa_prioridade = {'1': 'Baixa', '2': 'Média', '3': 'Alta'}
            
            prioridade_final = mapa_prioridade.get(prioridade_escolha) # Usar .get() para evitar KeyError

            try:
                data = input("Digite o tempo para sua tarefa (em dias): ")
                if not data.strip(): # Verifica se a entrada de tempo está vazia
                    print("O tempo não pode ser vazio. Tente novamente.")
                    continue
                data = int(data)
                if data < 0: 
                    print("O tempo não pode ser negativo. Tente novamente.")
                    continue
            except ValueError:
                print('Tempo inválido. Por favor, digite um número inteiro para os dias.')
                continue 

            if prioridade_final:
                adicionar_tarefa(desc, prioridade_final, data)
            else:
                print("Opção de prioridade inválida. A tarefa será adicionada com prioridade 'Não definida'.")
                
                adicionar_tarefa(desc, 'Não definida', data) 
            

        elif opcao == "2": 
            listar_tarefa()

        elif opcao == "3": # Primeiro, verificar se há tarefas antes de listar e pedir índice
            if not tarefas:
                print('Não há tarefas para concluir.')
                continue 

            listar_tarefa() # Mostra as tarefas para o usuário escolher

            try:
                indic = int(input('Qual tarefa deseja concluir (digite o número): '))
                concluir_tarefa(indic)
                
            except ValueError: # Comando validador caso o usuário não digitar um número
                print('Entrada inválida. Por favor, digite um número inteiro para o índice.')
                
            

        elif opcao == "4":
            
            if not tarefas:
                print("Não há tarefas para remover.")
                continue 

            listar_tarefa() 
            try:
                indic = int(input("Qual tarefa deseja remover (digite o número): "))
                remover_tarefa(indic)

            except ValueError: 
                print('Entrada inválida. Por favor, digite um número inteiro para o índice.')

        elif opcao == "5":
            if not tarefas:
                print ("Não há tarefas para editar")
                continue

            listar_tarefa()

            try:
                indic = int(input("Qual tarefa deseja editar?: "))

            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro para o índice.")
                continue   

            nova_tarefa = input("Digite a sua nova tarefa: ")
            editar_tarefa(indic,nova_tarefa)

        elif opcao == "6":
            if not tarefas:
                print("Não há tarefas para definir prioridade.")
                continue

            listar_tarefa()
            
            try:

                idx_prioridade = int(input("Digite o número da tarefa para definir a prioridade: "))
                if not (1 <= idx_prioridade <= len(tarefas)):
                    print("Índice inválido.")
                    continue

                print("\nEscolha a prioridade:")
                print("1 - Baixa")
                print("2 - Média")
                print("3 - Alta")
                prioridade_escolha = input("Digite o número da prioridade desejada (1, 2 ou 3): ").strip()

                mapa_prioridade = {'1': 'Baixa', '2': 'Média', '3': 'Alta'}
                
                if prioridade_escolha in mapa_prioridade:
                    editar_prioridade(idx_prioridade, mapa_prioridade[prioridade_escolha])
                else:
                    print("Opção de prioridade inválida. Escolha 1, 2 ou 3.")

            except ValueError:
                print("Entrada inválida. Por favor, digite um número para o índice da tarefa.")

        elif opcao == '7':
            if not tarefas:
                print("Não há tarefas para editar o tempo.")
                continue

            listar_tarefa()

            try:
                idx = int(input("Digite o número da tarefa para definir o tempo: "))
                if not (1 <= idx <= len(tarefas)):
                    print("Índice inválido.")
                    continue

                nova_data = int(input('digite o novo tempo: '))
                editar_data(idx,nova_data)
                
            except ValueError:
                print("Entrada inválida. Por favor, digite um número para o índice da tarefa.")
                          
        elif opcao == "8":
            print("Encerrando o programa... Até logo!")
            break 

        else:
            print('Opção inválida. Por favor, escolha uma das opções do menu (1 a 8).')

if __name__ == "__main__":
    menu()