from search import search_prompt
import time


def main():
    try:
        pergunta = input("Faça sua pergunta: ")
    except EOFError:
        print("\nEntrada finalizada.")
        return

    pergunta = pergunta.strip()
    if not pergunta:
        print("Nenhuma pergunta fornecida. Saindo.")
        return

    print("Processando sua pergunta, por favor aguarde...")

    try:
        resposta = search_prompt(pergunta)
    except Exception as e:
        print(f"Erro ao executar a busca: {e}")
        return

    print(".")
    time.sleep(2)
    print("..")
    time.sleep(3)
    print("...")

    print("\nPERGUNTA: {}\n".format(pergunta))
    print("RESPOSTA: {}".format(resposta))


if __name__ == "__main__":
    main()
