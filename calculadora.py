def ler_numero(mensagem: str) -> float:
    """Lê um número do usuário com validação usando try/except."""
    while True:
        try:
            return float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Erro: valor inválido. Por favor, digite um número (ex: 10, 2.5).")


def escolher_operacao(operacoes: dict) -> str:
    """Exibe o menu dinamicamente e retorna a chave escolhida (ou '' se inválida)."""
    print("\nEscolha uma operação:")

    op_keys = list(operacoes.keys())
    print("\n".join([f"{i + 1} - {operacoes[op_keys[i]]['nome']}" for i in range(len(op_keys))]))

    escolha = input("\nDigite o número da operação: ").strip()

    if not escolha.isdigit():
        return ""

    idx = int(escolha) - 1
    if 0 <= idx < len(op_keys):
        return op_keys[idx]

    return ""


def main():
    operacoes = {
        "soma": {"nome": "Soma", "fn": lambda a, b: a + b},
        "sub":  {"nome": "Subtração", "fn": lambda a, b: a - b},
        "mult": {"nome": "Multiplicação", "fn": lambda a, b: a * b},
        "div":  {"nome": "Divisão", "fn": lambda a, b: a / b},
    }

    while True:
        a = ler_numero("Insira o primeiro número: ")
        b = ler_numero("Insira o segundo número: ")

        op = escolher_operacao(operacoes)

        if not op:
            print("Erro: operação inválida. Tente novamente.")
            continue

        print(f"\nVocê escolheu: {operacoes[op]['nome']}")

        if op == "div":
            while b == 0:
                print("Divisão por zero não é permitida.")
                b = ler_numero("Por favor, insira outro número (divisor): ")

        resultado = operacoes[op]["fn"](a, b)
        print(f"\nO resultado é: {resultado}")

        continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()
        if continuar != "S":
            print("Encerrando a calculadora. Auf Wiedersehen!")
            break


if __name__ == "__main__":
    main()
