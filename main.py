import xmltodict
import os
import pandas as pd
import json

#def pegar_infos(nome_arquivo, valores):
def pegar_infos():
    #print(f"Pegou as informações {nome_arquivo}")
    with open(r'D:\\projetos_python\\read_xml\\data\\test_integra.xml', "rb") as arquivo_xml:
        print(f"Pegou as informações {arquivo_xml}")
    # with open(r'D:\\projetos_python\\read_xml\\data\\test_integra.xml', "rb") as arquivo_xml:
    #     print(f"Pegou as informações {arquivo_xml}")
        dic_arquivo = xmltodict.parse(arquivo_xml)
        print(json.dumps(dic_arquivo, indent=4))

        if "buscarSolicitacaoExamePeriodoAlteracaoResponse" in dic_arquivo:
            infos_nf = dic_arquivo["buscarSolicitacaoExamePeriodoAlteracaoResponse"]["buscarSolicitacaoExamePeriodoAlteracaoResult"]["SolicitacaoExame"]
        else:
            pass #infos_nf = dic_arquivo['nfeProc']["NFe"]['infNFe']
        numero_nota = infos_nf["ID"]
        lista_de_exames = infos_nf["Exames"]["SolicitacaoExameItem"]
        for valores in lista_de_exames:
            id_exame = valores
            
            # for kesy in exames:
            #     id_exame =  
                # qtd_ex = valor[1]
                # Sequencia = valor[2]
                # Situacao = valor["Situacao"]
                # dataPrevisao = valor["dataPrevisao"]
                # idMaterialColeta = valor["idMaterialColeta"]
                # idProcedimento = valor["idProcedimento"]




        # nome_cliente = infos_nf["dest"]["xNome"]
        # endereco = infos_nf["dest"]["enderDest"]
        # if "vol" in infos_nf["transp"]:
        #     peso = infos_nf["transp"]["vol"]["pesoB"]
        # else:
        #     peso = "Não informado"
#        valores.append([numero_nota, empresa_emissora, nome_cliente, endereco, peso])
        print(f'Id da solictação: {numero_nota}\nLista de Exames: \n{id_exame}')
# lista_arquivos = os.listdir("data")

# colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "endereco", "peso"]
# valores = []
# for arquivo in lista_arquivos:
#     pegar_infos(arquivo, valores)

# tabela = pd.DataFrame(columns=colunas, data=valores)
# tabela.to_excel("NotasFiscais.xlsx", index=False)
pegar_infos()

