"""
Temos aqui um exemplo de código para ler os arquivos xml

"""
import xml.etree.ElementTree as ET

# Carrega o arquivo XML
tree = ET.parse(r'D:\\projetos_python\\read_xml\\data\\Consulta_Importacao_Alterados_202309261424.xml')
root = tree.getroot()

# Itera sobre os elementos do XML
for solicitacao_exame in root.findall('.//SolicitacaoExame'):
    ano = solicitacao_exame.find('Ano').text
    numero = solicitacao_exame.find('Numero').text
    numero_atend = solicitacao_exame.find('NumeroAtend').text
    data_atendimento = solicitacao_exame.find('dataAtendimento').text
    tipo_atendimento = solicitacao_exame.find('tipoAtendimento').text
    idQuarto = solicitacao_exame.find('idQuarto').text
    idLeito = solicitacao_exame.find('idLeito').text
    id_solicitacao = solicitacao_exame.find('ID').text
    idPaciente = solicitacao_exame.find('idPaciente').text
    idProfissional = solicitacao_exame.find('idProfissional').text
    print("Solicitação de Exame:")
    print("\tAno:", ano)
    print("\tNúmero:", numero)
    print("\tNúmero de Atendimento:", numero_atend)
    print("\tId do Paciente:", idPaciente)
    print("\tId do Profissional:", idProfissional)
    print("\tId da Solicitação:", id_solicitacao)
    print("\tId do Quarto:", idQuarto)
    print("\tId do Leito:", idLeito)

    print("\tData de Atendimento:", data_atendimento)
    print("\tTipo de Atendimento:", tipo_atendimento)
    


    exames = solicitacao_exame.find('Exames')
    if exames is not None:
        print("\tExames:")
        for exame in exames.findall('.//SolicitacaoExameItem'):
            id_exame = exame.find('ID').text
            situacao = exame.find('Situacao').text
            data_previsao = exame.find('dataPrevisao').text
            idMaterialColeta = exame.find('idMaterialColeta').text
            idProcedimento = exame.find("idProcedimento").text
            print("\t\tID do Exame:", id_exame)
            print("\t\tSituação:", situacao)
            print("\t\tData de Previsão:", data_previsao)
            print("\t\tData de Previsão:", idMaterialColeta)
            print("\t\tData de Previsão:", idProcedimento)
