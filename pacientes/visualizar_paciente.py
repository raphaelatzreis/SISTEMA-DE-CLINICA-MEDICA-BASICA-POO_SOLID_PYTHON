from rich import print
from rich.table import Table

from pacientes.paciente import CadastroPaciente

class VisualizarPaciente:
    
    @staticmethod
    def exibir_paciente():
        for paciente in CadastroPaciente.pacientes:
            print(f"Nome: {paciente.nome}")
            print(f"RG: {paciente.rg}")
            print(f"CPF: {paciente.cpf}")
            print(f"Email: {paciente.email}")
            print(f"Telefone: {paciente.telefone}")
            print(f"Contato de emergência: {paciente.contato_emergencia}")
            print(f"Tipo sanguíneo: {paciente.tipo_sang}")
            print(f"Peso (kg): {paciente.peso}")
            print(f"Altura (m): {paciente.altura}")
            print(f"Alergias: {paciente.alergias}")
            print(f"Doenças pré-existentes: {paciente.doencas_pre_ex}")
            print(f"Medicações em uso: {paciente.med_em_uso}")
            print(f"Histórico cirúrgico: {paciente.hist_cirurgias}")
            print(f"Convênio médico: {paciente.convenio}")
            print(f"{30 * '-'}")
"""-------------------------------------------------------------------------------------------------------------------"""
class BuscaPaciente:
    
    @staticmethod
    def busca_paciente():
        entrada = input("Digite o CPF ou [0] para cancelar: ")
        
        if entrada == "0":
            print("[yellow]Busca cancelada. Voltando ao menu...[/yellow]")
            return None
            
        encontrado= False
        
        for paciente in CadastroPaciente.pacientes:
            if entrada == paciente.cpf:
                
                tabela= Table(title=" DADOS DO PACIENTE", show_header=True, header_style="bold white")
                
                tabela.add_column("Nome do paciente")
                tabela.add_column("RG")
                tabela.add_column("CPF")
                tabela.add_column("Email")
                tabela.add_column("Telefone")
                tabela.add_column("Contato de emergencia")
                tabela.add_column("Tipo sanguíneo")
                tabela.add_column("Peso (kg)")
                tabela.add_column("Altura (m)")
                tabela.add_column("Alergias")
                tabela.add_column("Doenças pré-existentes")
                tabela.add_column("Medicações em uso")
                tabela.add_column("Histórico cirúrgico")
                tabela.add_column("Convênio")
                
                tabela.add_row(
                    str(paciente.nome), 
                    str(paciente.rg), 
                    str(paciente.cpf), 
                    str(paciente.email), 
                    str(paciente.telefone), 
                    str(paciente.contato_emergencia), 
                    str(paciente.tipo_sang), 
                    str(paciente.peso), 
                    str(paciente.altura), 
                    str(paciente.alergias), 
                    str(paciente.doencas_pre_ex), 
                    str(paciente.med_em_uso), 
                    str(paciente.hist_cirurgias), 
                    str(paciente.convenio)
                )
                
                print(tabela)
                print("─ ⊹ ⊱ ⊰ ⊹ ─"*4)
                
                encontrado= True
                return paciente
                
        print("CPF não encontrado no cadastro pacientes.")
        resp=input("Deseja cadastrar um novo paciente? [S/N]: ").strip().upper()
        
        if resp == "S" or resp == "s": 
            CadastroPaciente.cadastrar_paciente()
        else:
            return None
        return None
