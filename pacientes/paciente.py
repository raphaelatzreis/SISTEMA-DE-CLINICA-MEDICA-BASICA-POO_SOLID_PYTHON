from rich import print
from rich.table import Table 

class Paciente:
    def __init__(self, nome, rg, cpf, email, telefone, contato_emergencia, tipo_sang: str = "Não informado", peso = "Não informado", altura = "Não informado", alergias: str = "Não informado", doencas_pre_ex: str = "Não informado", med_em_uso: str = "Não informado", hist_cirurgias = "Não informado", convenio: str = "Não informado"):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.contato_emergencia = contato_emergencia
        self.tipo_sang = tipo_sang
        self.peso = peso
        self.altura = altura
        self.alergias = alergias
        self.doencas_pre_ex = doencas_pre_ex
        self.med_em_uso = med_em_uso
        self.hist_cirurgias = hist_cirurgias
        self.convenio = convenio
        
        
    

    @property
    def rg(self):
        return self.__rg #privado
    
    @rg.setter
    def rg(self, valor):
        if valor.isdigit() and 7 <= len(valor) <= 9:
            self.__rg = valor
        else:
            raise ValueError("RG deve conter apenas números e ter entre 7 e 9 dígitos.")

    @property
    def cpf(self):
        return self.__cpf #privado
    
    @cpf.setter
    def cpf(self, valor):
        if valor.isdigit() and len(valor) == 11:
            self.__cpf = valor
        else:
            raise ValueError("CPF deve conter exatamente 11 números.")
        
"""-------------------------------------------------------------------------------------------------------------------"""

class CadastroPaciente:
    pacientes = []

    @staticmethod
    def cadastrar_paciente():
        nome = input("Nome do paciente (ou digite '0' para cancelar): ")
        if nome == "0":
            print("[yellow]Cadastro cancelado. Voltando ao menu...[/yellow]")
            return
        
        while True:
            rg = input("RG do paciente(ou digite '0' para cancelar): ")
            
            if rg == '0':
                print("[yellow]Cadastro cancelado. Voltando ao menu...[/yellow]")
                return
                
            if rg.isdigit() and 7 <= len(rg) <= 9:
                break
                
            print("[red]Erro: O RG deve conter apenas números e ter entre 7 e 9 dígitos.[/red]")
            
        while True:
            cpf = input("CPF do paciente (ou digite '0' para cancelar): ")
            if cpf.isdigit() and len(cpf) == 11:
                break
            print("[red]Erro: O CPF deve conter exatamente 11 números.[/red]")

        email = input("E-mail: ")
        telefone = input("Telefone / Celular: ")
        contato_emergencia = input("Contato de emergência: ")
        
        tipo_sang = input("Tipo Sanguíneo [A+, A-, B+, B-, AB+, AB-, O+, O-] (ou Enter para pular): ") or "Não informado"
        
        peso_input = input("Peso em KG (ou Enter para pular): ")
        peso = int(peso_input) if peso_input.isdigit() else "Não informado"
        
        altura = input("Altura (ex: 1.75) (ou Enter para pular): ") or "Não informado"
        alergias = input("Alergias (ou Enter para pular): ") or "Não informado"
        doencas_pre_ex = input("Doenças pré-existentes (ou Enter para pular): ") or "Não informado"
        med_em_uso = input("Medicações em uso (ou Enter para pular): ") or "Não informado"
        hist_cirurgias = input("Histórico de cirurgias (ou Enter para pular): ") or "Não informado"
        convenio = input("Convênio médico (ou Enter para pular): ") or "Não informado"
        
        try:
            paciente = Paciente(nome, rg, cpf, email, telefone, contato_emergencia, tipo_sang, peso, altura, alergias, doencas_pre_ex, med_em_uso, hist_cirurgias, convenio)
            CadastroPaciente.pacientes.append(paciente)
            print("[green]Paciente cadastrado com sucesso![/green]")
        except ValueError as e:
            print(f"[red]Erro no cadastro! [/red] {e}")


            
