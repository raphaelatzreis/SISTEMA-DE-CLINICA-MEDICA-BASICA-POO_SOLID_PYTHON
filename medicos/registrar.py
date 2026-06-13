from abc import ABC, abstractmethod
from rich import print
from rich.table import Table


class Especialidade(ABC):
    @abstractmethod
    def obter_nome(self) -> str:
        pass

class ClinicoGeral(Especialidade):
    def obter_nome(self):
        return "Clinico Geral"
    
class Cardiologia(Especialidade):
    def obter_nome(self):
        return "Cardiologia"
    
class Endocrinologia(Especialidade):
    def obter_nome(self):
        return "Endocrinologia"

class Ginecologia(Especialidade):
    def obter_nome(self):
        return "Ginecologia"
    
class Dermatologia(Especialidade):
    def obter_nome(self):
        return "Dermatologia"
    
class Psiquiatria(Especialidade):
    def obter_nome(self):
        return "Psiquiatria"
    
class Oftalmologia(Especialidade):
    def obter_nome(self):
        return "Oftalmologia"

class Ortopedia(Especialidade):
    def obter_nome(self):
        return "Ortopedia"

class Pediatria(Especialidade):
    def obter_nome(self):
        return "Pediatria"
    
"""-------------------------------------------------------------------------------------------------------------------"""

class Medico:
    def __init__(self, nome:str , rg:str, cpf:str, crm:str, especialidade: Especialidade):
        self.nome = nome
        self.rg=rg
        self.cpf=cpf
        self.crm = crm
        self.especialidade = especialidade  

class CadastroMedico:
    medicos = []

    @staticmethod
    def cadastrarMedico():
        opcao_especialidade = None
        print("\n ﮩ٨ـﮩﮩ٨ـ  CADASTRO DE MÉDICO   ﮩ٨ـﮩﮩ٨ـ")
        while True:
            
            print("\nEscolha a especialidade:")
            print("\n • (1) Clinico Geral")
            print("\n • (2) Cardiologia")
            print("\n • (3) Endocrinologia")
            print("\n • (4) Ginecologia")
            print("\n • (5) Dermatologia")
            print("\n • (6) Psiquiatria")
            print("\n • (7) Oftalmologia")
            print("\n • (8) Ortopedia") 
            print("\n • (9) Pediatria") 
            
            opcao = input("\nDigite o número da opção referente à especialidade: ")
            
            if opcao == "1":
                opcao_especialidade= ClinicoGeral()
                break
            elif opcao == "2":
                opcao_especialidade= Cardiologia()
                break
            elif opcao == "3":
                opcao_especialidade= Endocrinologia()
                break
            elif opcao == "4":
                opcao_especialidade= Ginecologia()
                break
            elif opcao == "5":
                opcao_especialidade= Dermatologia()
                break
            elif opcao == "6":
                opcao_especialidade= Psiquiatria()
                break
            elif opcao == "7":
                opcao_especialidade= Oftalmologia()
                break
            elif opcao == "8":
                opcao_especialidade= Ortopedia()
                break
            elif opcao == "9":
                opcao_especialidade= Pediatria()
                break
            else:
                print("\n[red]DIGITE UMA OPÇÃO VÁLIDA! --> [/red]escolha um número de 1 a 9.")
                
        print("Especialidade selecionada com sucesso!")
        
        nome = input("\nNome do médico: ")
        while True:
            rg = input("RG do médico: ")
            if rg.isdigit() and 7 <= len(rg) <= 9:
                break
            print("[red]Erro: O RG deve conter apenas números e ter entre 7 e 9 dígitos.[/red]")

        while True:
            cpf = input("CPF do médico: ")
            if cpf.isdigit() and len(cpf) == 11:
                break
            print("[red]Erro: O CPF deve conter exatamente 11 números.[/red]")

        while True:
            crm = input("CRM do médico (6 dígitos): ")
            if crm.isdigit() and len(crm) == 6:
                break
            print("[red]Erro: O CRM deve conter exatamente 6 números.[/red]")

        try:
            medico = Medico(nome, rg, cpf, crm, opcao_especialidade)
            CadastroMedico.medicos.append(medico)
            print("[green]\nMédico cadastrado com sucesso![/green]")
        except ValueError as e:
            print(f"[red]Erro no cadastro do médico! [/red] {e}")
            return
        
        tabela= Table(title=" DADOS DO MÉDICO CADASTRADO ", show_header=True, header_style="bold white")
        tabela.add_column("Nome do médico")
        tabela.add_column("CRM")
        tabela.add_column("Especialidade")
        tabela.add_row(medico.nome,medico.crm,medico.especialidade.obter_nome())
        
        print(tabela)
        print("─ ⊹ ⊱ ⊰ ⊹ ─"*4)

# TESTE --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    medico_teste= CadastroMedico.cadastrarMedico()