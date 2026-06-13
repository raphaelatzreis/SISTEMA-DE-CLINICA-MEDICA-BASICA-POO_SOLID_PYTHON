from rich import print
from rich.table import Table
from medicos.registrar import Medico, CadastroMedico, ClinicoGeral
from medicos.visualizar import BuscaMedico
from pacientes.visualizar_paciente import BuscaPaciente
from datetime import datetime, timedelta

class Consultas:
    def __init__(self,paciente,medico,data,horario,data_hora_completa):
        self.paciente=paciente # <--- composição
        self.medico=medico # <--- composição
        self.data=data 
        self.horario=horario
        self.data_hora_completa = data_hora_completa

class GerenciadorConsultas:
    consultas= []
    
    @staticmethod
    def agendar_consultas():
        print("\n[bold white] * * * * Agendamento de Consulta * * * *[/bold white] ")
        
        paciente=BuscaPaciente.busca_paciente()
        if not paciente:
            print("[red]Paciente não encontrado![/red]\n")
            input()
            return
        
        medico= BuscaMedico.busca_medico()
        if not medico:
            print("[red]Médico não encontrado![/red]\n")
            input()
            return
        
        while True:
            data=input("Digite a data da consulta |DD/MM/AA| : ")
            try:
                data_objeto=datetime.strptime(data, "%d/%m/%y")
                break
            except ValueError:
                print("Data inválida! Formato correto: DD/MM/AA")
                
        while True:
            horario=input("Digite o horário da consulta |HH:MM| : ")
            try:
                horario_objeto=datetime.strptime(horario,"%H:%M")
                break
            except ValueError:
                print("Horário inválido! Formato correto: HH:MM")
                
        data_hora_completa = data_objeto.replace(hour=horario_objeto.hour, minute=horario_objeto.minute)
        nova_consulta = Consultas(paciente, medico, data, horario, data_hora_completa)
        GerenciadorConsultas.consultas.append(nova_consulta)
        
        tabela=Table(title="INFORMAÇÕES DA CONSULTA")
        tabela.add_column("Paciente")
        tabela.add_column("Médico")
        tabela.add_column("Data")
        tabela.add_column("Horário")
        tabela.add_row(paciente.nome, medico.nome, data, horario )
        print(tabela)
        
        # Teste --------------------------------------------------------------------------------------------------
if __name__== "__main__":
    from medicos.registrar import Medico, CadastroMedico, Especialidade
    from pacientes.paciente import Paciente, CadastroPaciente
    
    print("[yellow]* Inserindo consulta de teste *[/yellow]")
    
    CadastroMedico.medicos.append(Medico("Dr. House", "1234567", "12345678901", "666666", ClinicoGeral()))
    CadastroPaciente.pacientes.append(Paciente("Prof. Tiago", "1234567", "12345678901", "proftiago@gmail.com", "21912121212", "99999999"))
    
    GerenciadorConsultas.agendar_consultas()
