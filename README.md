# Sistema de Gerenciamento de Clínica Médica

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Rich](https://img.shields.io/badge/Rich-Terminal_UI-purple?style=for-the-badge)

Sistema de gerenciamento de clínica médica via linha de comando (CLI) desenvolvido em Python. O projeto tem como foco a aplicação prática de Programação Orientada a Objetos (POO) para estruturar as entidades do domínio médico e utiliza a biblioteca Rich para a construção da interface no terminal.

## Funcionalidades

- **Gestão de Médicos:** Cadastro de profissionais contendo nome, RG, CPF, CRM e especialidades médicas.
- **Gestão de Pacientes:** Cadastro de pacientes com histórico médico, alergias, tipo sanguíneo e contatos de emergência.
- **Agendamento de Consultas:** Marcação de consultas com validação de cadastros existentes, organizadas por data e horário.
- **Emissão de Receitas:** Geração de receituários vinculando o médico emissor ao paciente, detalhando prescrições e orientações.
- **Sistema de Notificações:** Simulação de lembretes de consultas (aviso de 24h) e alertas de envio de receitas.
- **Interface CLI:** Utilização da biblioteca `rich` para criação de menus interativos e exibição de dados formatados em tabelas.

## Estrutura do Projeto

O código fonte foi modularizado visando a separação de responsabilidades:

- `main.py`: Arquivo principal e gerenciamento do menu de navegação.
- `limparterminal/limpador.py`: Função de utilitário para limpeza do console (multiplataforma).
- `pacientes/`: Contém as classes da entidade (`paciente.py`) e a lógica de exibição/busca (`visualizar_paciente.py`).
- `medicos/`: Contém as classes da entidade e especialidades (`registrar.py`) e a lógica de exibição/busca (`visualizar.py`).
- `consultas/` e `receitas/`: Módulos responsáveis pelas classes associativas que interligam os dados de médicos e pacientes.
- `notificacao/`: Lógica para disparos de avisos no terminal (`notificacao.py`).

## Como executar

Certifique-se de ter o Python 3 instalado no seu ambiente. O projeto possui dependência da biblioteca `rich` para a renderização do terminal.

Siga os comandos abaixo no seu terminal:

```bash
# 1. Clone o repositório
git clone [https://github.com/raphaelatzreis/SISTEMA-DE-CLINICA-MEDICA-BASICA-POO_SOLID_PYTHON.git](https://github.com/raphaelatzreis/SISTEMA-DE-CLINICA-MEDICA-BASICA-POO_SOLID_PYTHON.git)

# 2. Acesse o diretório
cd SISTEMA-DE-CLINICA-MEDICA-BASICA-POO_SOLID_PYTHON

# 3. Instale as dependências
pip install rich

# 4. Execute o arquivo principal
python main.py
