from rich import print
from datetime import timedelta

class Notificacao:
    @staticmethod
    def enviarConfirmacaoConsulta(consulta):
        momento_do_aviso = consulta.data_hora_completa - timedelta(days=1)
        data_aviso_formatada = momento_do_aviso.strftime("%d/%m/%Y às %H:%M")
        
        
        print("\n" + "═" * 10 + " SISTEMA DE NOTIFICAÇÕES " + "═" * 10)
        print(f"\n[bold green][Notificação] Consulta marcada[/bold green]: Paciente {consulta.paciente.nome} | Médico {consulta.medico.nome} | Dia {consulta.data} às {consulta.horario}")
        print(f"⏳ [yellow]Lembrete de 24h programado para disparo em:{data_aviso_formatada} [/yellow]")
        print("-" * 45)
        
    @staticmethod
    def enviarAvisoCancelamento(consulta):
        print(f"\n[bold red][Notificação] Consulta cancelada[/bold red]: Paciente {consulta.paciente.nome} | Médico {consulta.medico.nome}")

    @staticmethod
    def enviarNotificacaoReceita(receita):
        print("\n" + "═" * 10 + " ENVIO DE RECEITA DIGITAL " + "═" * 10)
        print("\n[bold green]✔ Receita enviada com sucesso![/bold green]")
        print(f"Paciente {receita.paciente.nome} | Medicamentos: {receita.medicamentos}")
        print("-" * 45)

