from rich import print
from rich.table import Table
from pacientes.paciente import Paciente
from medicos.visualizar import BuscaMedico
from pacientes.visualizar_paciente import BuscaPaciente
from datetime import datetime

class Receita:
    def __init__(self, medico, paciente, medicamentos:str, orientacoes):
        self.medico=medico
        self.paciente = paciente
        self.medicamentos = medicamentos
        self.orientacoes = orientacoes
        self.data = datetime.now().strftime("%d/%m/%Y")

    def exibir_receita(self):
        print("\n" + "═" * 18 + " RECEITUÁRIO MÉDICO " + "═" * 18)
        
        tabela = Table(title=f"Documento Emitido em: {self.data}", show_header=True)
        tabela.add_column("Emitente (Médico)")
        tabela.add_column("Paciente")
        tabela.add_column("Prescrição & Orientações")
        
        dados_medico = f"[bold]Nome:[/bold] {self.medico.nome}\n[bold]CRM:[/bold] {self.medico.crm}\n[bold]Especialidade:[/bold] {self.medico.especialidade.obter_nome()}"
        dados_paciente = f"[bold]Nome[/bold]: {self.paciente.nome}\n[bold]CPF:[/bold] {self.paciente.cpf}\n[bold]RG:[/bold] {self.paciente.rg}"
        corpo_receita = f"[bold]Medicamentos:[/bold]\n{self.medicamentos}\n\n[bold]Orientações:[/bold]\n{self.orientacoes}"
        
        tabela.add_row(dados_medico, dados_paciente, corpo_receita)
        
        print(tabela)
        print("═" * 56)
        
class GerenciadorReceitas:
    receitas=[]
    
    @staticmethod
    def criar_receita():
        print("\n[bold white]* * * * Emitir Nova Receita * * * *[/bold white]")
        paciente_encontrado = BuscaPaciente.busca_paciente()
        
        if paciente_encontrado is None:
            return
            
        print("\n[bold white]* * * * Dados do Médico * * * *[/bold white]")
        medico_encontrado = BuscaMedico.busca_medico()
        
        if medico_encontrado is None:
            print("[red]Médico não encontrado. [/red]")
            return
            
        medicamentos = input("\nMedicamentos receitados: ")
        orientacoes = input("Orientações médicas: ")
        
        receita=Receita(medico_encontrado,paciente_encontrado,medicamentos,orientacoes)
        GerenciadorReceitas.receitas.append(receita)
        print("[green]\nReceita cadastrada com sucesso![/green]")