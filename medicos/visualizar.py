try:
    from registrar import CadastroMedico, Medico
except ModuleNotFoundError:
    from medicos.registrar import CadastroMedico, Medico
from rich import print
from rich.table import Table

class VisualizarMedico:
    @staticmethod
    def exibir_medicos():
        print("\nﮩ٨ـﮩﮩ٨ـ  LISTA DE MÉDICOS ﮩ٨ـﮩﮩ٨ـ ")
        for medico in CadastroMedico.medicos:
            print(f"Nome: {medico.nome}")
            print(f"CRM: {medico.crm}")
            print(f"Especialidade: {medico.especialidade.obter_nome()}")
            print("-" * 30)
"""-------------------------------------------------------------------------------------------------------------------"""

class BuscaMedico:
    @staticmethod
    def busca_medico():
        print("\nﮩ٨ـﮩﮩ٨ـ BUSCA DE MÉDICO ﮩ٨ـﮩﮩ٨ـ ")
        while True:
            crm = input("CRM (6 dígitos) ou [0] para cancelar: ")
            
            if crm == "0": 
                print("[yellow]Busca cancelada.[/yellow]")
                return None
                
            if crm.isdigit() and len(crm) == 6:
                break
            print("[red]CRM INVÁLIDO, insira novamente.[/red]")
            
        for medico in CadastroMedico.medicos:
            if medico.crm == crm:
                tabela= Table(title=" DADOS DO MÉDICO", show_header=True, header_style="bold white")
                tabela.add_column("Nome do médico")
                tabela.add_column("CRM")
                tabela.add_column("Especialidade")
                tabela.add_row(medico.nome, medico.crm, medico.especialidade.obter_nome())
                print(tabela)
                print("─ ⊹ ⊱ ⊰ ⊹ ─"*4)
                return medico
            print("Médico não encontrado!")
            return None
        
