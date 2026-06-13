import sys
from pacientes.paciente import CadastroPaciente
from pacientes.visualizar_paciente import BuscaPaciente, VisualizarPaciente
from medicos.registrar import CadastroMedico
from medicos.visualizar import VisualizarMedico, BuscaMedico
from consultas.consultas import GerenciadorConsultas
from receitas.receitas import Receita, GerenciadorReceitas
from notificacao.notificacao import Notificacao
from limparterminal.limpador import limpar_tela

def menu():
    while True:
        limpar_tela()
        print("\n=== MENU CLÍNICA MÉDICA ===")
        print("1. Cadastrar Paciente")
        print("2. Cadastrar Médico")
        print("3. Agendar Consulta")
        print("4. Emitir Receita Médica")
        print("5. Listar Pacientes")
        print("6. Listar Médicos")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        limpar_tela()
        
        if opcao == "1":
            CadastroPaciente.cadastrar_paciente()
            input("\nPressione Enter para voltar ao menu...")
            
        elif opcao == "2":
            CadastroMedico.cadastrarMedico()
            input("\nPressione Enter para voltar ao menu...")
            
        elif opcao == "3":
            GerenciadorConsultas.agendar_consultas()
            if GerenciadorConsultas.consultas:
                ultima_consulta = GerenciadorConsultas.consultas[-1]
                Notificacao.enviarConfirmacaoConsulta(ultima_consulta)
            input("\nPressione Enter para voltar ao menu...")
                
        elif opcao == "4":
            GerenciadorReceitas.criar_receita()
            if GerenciadorReceitas.receitas:
                ultima_receita = GerenciadorReceitas.receitas[-1]
                ultima_receita.exibir_receita()
                
                Notificacao.enviarNotificacaoReceita(ultima_receita)
                
            input("\nPressione Enter para voltar ao menu...")
                
        elif opcao == "5":
            print("\n--- Lista de Pacientes ---")
            VisualizarPaciente.exibir_paciente()
            input("\nPressione Enter para voltar ao menu...")
            
        elif opcao == "6":
            print("\n--- Lista de Médicos ---")
            VisualizarMedico.exibir_medicos()
            input("\nPressione Enter para voltar ao menu...")
            
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("\nPressione Enter para voltar ao menu...")


if __name__ == "__main__":
    menu()
