
# 1 - Pessoa Fisica / 2 - Pessoa Juridica / 3 - Sair
# 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Sair
# 1 - Cadastar Pessoa Juridica / 2 - listar Pessoa Juridica / 3 - Sair

from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica



def main():
    lista_pf = []
    lista_pj = []
    while True:
        opcao = int(input("Escolha uma opcao: 1 - Pessoa Fisica / 2- Pessoa Juridica / 0 - Sair " ))
        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 -Listar Pessoa Fisica / 3 - Remover CPF da lista / 4 - Atualizar item da lista / 0 - Voltar ao menu anterior "))
                #  1 - Cadastrar uma Pessoa Fisica 
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa fisica: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente numeros): "))

                    data_nascimento = input("Digite a data de nascimento (dd/MM/aaaa): ") # solicita a data de nascimento
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A Pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")  
                        continue # Retornar ao inicio do loop  

                    # Cadastro do endereco
                    novo_end_pf.logradouro = input("Digite o Logradouro: ")
                    novo_end_pf.numero = input("Digite o numero: ")
                    end_comercial = input("Este endereco e comercial: S/N ?")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S' # define se o endereco e comercial

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!!")

                # Listar pessoa fisica
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereco: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago R$: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para Sair")
                            input()
                    else:
                        print("Lista Vazia")  
                # Remover pessoa fisica          
                elif opcao_pf == 3:
                    cpf_para_remover = input("Digite o CPF da pessoa fisica que deseja remover: ")

                    pessoa_encontrada = False
                
                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_remover:
                            lista_pf.remove(cada_pf)
                            pessoa_encontrada = True  
                            print("Pessoa Fisica removida! ")  

                            break
                    if not pessoa_encontrada:
                        print("Nenhuma pessoa encontrada!")  
                # Atualizar item da lista
                elif opcao_pf == 4:
                    cpf_para_atualizar = input("Digite o CPF que deseja atualizar")
                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_atualizar:
                            pessoa_encontrada = True

                            print("Escolha qual dado deseja atualizar")
                            print("N - Nome")
                            print("R - Rendimento")
                            print("L - Logradouro")
                            print("M - Numero do Endereco")

                            escolha = input("Digite a inicial d atributo que deseja alterar: ").strip(). upper()

                            if escolha == 'N':
                                novo_nome = input(f"O nome atual e {cada_pf.nome}. Digite o novo nome para atualizar: ")
                                cada_pf.nome = novo_nome
                            elif escolha == "R":
                                novo_rendimento = input(f"O rendimento atual e {cada_pf.rendimento}. Digite o novo valor de rendimento: ")   
                                cada_pf.rendimento = novo_rendimento
                            elif escolha == "L":
                                novo_logradouro = input(f"O logradouro atual e {cada_pf.logradouro}. Digite o novo logradouro:  ") 
                            elif escolha == "M":
                                novo_numero = input(f"O numero do endereco atual e {cada_pf.numero}. Digite um novo numero para alterar: ")
                            else:
                                print("Opcao Invalida")  
                                break     

                    if not pessoa_encontrada:
                        print("Nenhuma pessoa com esse CPF foi encontrado")


                   # atualizar_item = int(input("Qual item quer atualizar: 1 - Nome / 2 - CPF / 3 - Rendimento / 4 - Logradouro / 5 - Numero "))
                    #if atualizar_item == 1:
                       # novo_nome = input("Digite o novo nome: ")
                       # novapf.nome = novo_nome
                    #elif atualizar_item == 2:
                        #novo_cpf = input("Digite o novo CPF: ")   
                        #novapf.cpf = novo_cpf
                    #elif atualizar_item == 3:
                        #novo_rendimento = input("Digite o novo rendimento: ")  
                        #novapf.rendimento = novo_rendimento    
                    #lif atualizar_item == 4:
                       # novo_logradouro = input("Digite o novo logradouro: ")
                        #novapf.logradouro = novo_logradouro   
                    #elif atualizar_item == 5:
                       # novo_numero = input("Digie o novo numero: ")  
                        #novapf.numero = novo_numero



                # Sair do menu atual
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")   
                    break      

                else:
                    print("Opcao invalida, por favor digite uma das opcoes indicadas:")   
        elif opcao == 2:
           while True:
               opcao_pj = int(input("Escolha uma opcao: 1- Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Remover Pessoa Juridica da lista / 4- Atualizar item da lista /  0 - Voltar ao menu anterior "))
               # 1 Cadastrar uma Pessoa Juridica
               if opcao_pj == 1:
                   novapj = PessoaJuridica()
                   novapj_end = Endereco()

                   novapj.nome = input("Digite o nome da Pessoa Juridica: ")
                   novapj.cnpj = input("Digite o CNPJ: ")
                   novapj.rendimento = float(input("Digite o rendimento da empresa: ")) 

                   # Cadastro de endereco
                   novapj_end.logradouro = input("Digite o Logradouro: ")
                   novapj_end.numero = input("Digite o numero: ")

                   end_comercialpj = input("Este endereco e comercial: S/N ")
                   novapj_end.endereco_Comercial = end_comercialpj.strip().upper() == 'S' # define se o endereco e comercial
                
                   novapj.endereco = novapj_end

                   lista_pj.append(novapj)

                   print("Cadastro realizado com sucesso !!")

               # 2 Listar pessoa juridica
               elif opcao_pj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                                print(f"Nome: {cada_pj.nome}")
                                print(f"CNPJ: {cada_pj.cnpj}")
                                print(f"Endereco: {cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}")
                                print(f"Imposto a ser pago R$: {cada_pj.calcular_imposto(cada_pj.rendimento)}")
                                print("Digite 0 para ir para o proximo/ para voltar ao menu")
                                input()
                        else:
                            print("Lista Vazia")  

               # 3 Remover pessoa Juridica         
               elif opcao_pj == 3:
                    cnpj_para_remover = input("Digite o CNPJ da empresa que deseja remover: ")

                    empresa_encontrada = False
                
                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == cnpj_para_remover:
                            lista_pj.remove(cada_pj)
                            empresa_encontrada = True  
                            print("Pessoa Juridica removida! ")  
                            break

                    if not empresa_encontrada:
                        print("Nenhuma empresa com o CNPJ foi encontrado! ")

               # 4 Atualizar item da lista
               elif opcao_pj == 4:
                    cnpj_para_atualizar = input("Digite o CNPJ que deseja atualizar")
                    empresa_encontrada = False

                    for cada_pJ in lista_pj:
                        if cada_pJ.cnpj == cnpj_para_atualizar:
                            empresa_encontrada = True

                            print("Escolha qual dado deseja atualizar")
                            print("N - Nome")
                            print("R - Rendimento")
                            print("L - Logradouro")
                            print("M - Numero do Endereco")

                            escolha = input("Digite a inicial d atributo que deseja alterar: ").strip(). upper()

                            if escolha == 'N':
                                novo_nome = input(f"O nome atual e {cada_pj.nome}. Digite o novo nome para atualizar: ")
                                cada_pf.nome = novo_nome
                            elif escolha == "R":
                                novo_rendimento = input(f"O rendimento atual e {cada_pj.rendimento}. Digite o novo valor de rendimento: ")   
                                cada_pf.rendimento = novo_rendimento
                            elif escolha == "L":
                                novo_logradouro = input(f"O logradouro atual e {cada_pj.logradouro}. Digite o novo logradouro:  ") 
                            elif escolha == "M":
                                novo_numero = input(f"O numero do endereco atual e {cada_pj.numero}. Digite um novo numero para alterar: ")
                            else:
                                print("Opcao Invalida")  
                                break     

                        if not empresa_encontrada:
                            print("Nenhuma empresa  com esse CNPJ foi encontrada")



               #elif opcao_pj == 4:
                    #atualizar_item = int(input("Qual item quer atualizar: 1 - Nome / 2 - CNPJ / 3 - Rendimento / 4 - Logradouro / 5 - Numero "))
                    #if atualizar_item == 1:
                        #novo_nome = input("Digite o novo nome: ")
                        #novapj.nome = novo_nome
                    #elif atualizar_item == 2:
                       #novo_cnpj = input("Digite o novo CNPJ: ")   
                        #novapj.cnpj = novo_cnpj
                    #elif atualizar_item == 3:
                        #novo_rendimento = input("Digite o novo rendimento: ")  
                        #novapj.rendimento = novo_rendimento    
                    #elif atualizar_item == 4:
                        #novo_logradouro = input("Digite o novo logradouro: ")
                        #novapj.logradouro = novo_logradouro   
                    #elif atualizar_item == 5:
                        #novo_numero = input("Digie o novo numero: ")  
                        #novapj.numero = novo_numero

               else:
                   print("Opcao Invalida")                      

        elif opcao == 0:
            print("Obrigado por utilizar o nosso sistema! Valeu!")
            break

        else:
            print("Opcao invalida, por favor digite uma das opcoes validas! ")

if __name__ == "__main__": 
    main() # Chama a funcao principal            
