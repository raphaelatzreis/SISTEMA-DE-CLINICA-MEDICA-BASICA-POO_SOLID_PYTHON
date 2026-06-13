import os

def limpar_tela():
    """
    Limpa o terminal de forma compatível com Windows (cmd/powershell) e Unix (Linux/macOS).
    """
    os.system('cls' if os.name == 'nt' else 'clear')
