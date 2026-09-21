largura = 50


def ler_texto(mensagem, obrigatorio=True):
    while True:
        valor = input(mensagem).strip()
        if valor or not obrigatorio:
            return valor
        print("Erro: este campo não pode ficar vazio.")


def ler_preco(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            preco = float(entrada.replace(",", "."))
            if preco <= 0:
                print("Erro: o preço deve ser maior que zero.")
                continue
            return round(preco, 2)
        except ValueError:
            print("Erro: valor inválido. Digite apenas números (ex.: 19,90).")


def ler_inteiro(mensagem, minimo=0):
    while True:
        entrada = input(mensagem).strip()
        try:
            numero = int(entrada)
            if numero < minimo:
                print(f"Erro: o valor deve ser no mínimo {minimo}.")
                continue
            return numero
        except ValueError:
            print("Erro: valor inválido. Digite um número inteiro.")


def formatar_preco(valor):
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def cadastrar_produto(produtos):
    print("\n" + "=" * largura)
    print("CADASTRAR PRODUTO".center(largura))
    print("=" * largura)

    nome = ler_texto("Nome do produto: ")

    if any(p["nome"].lower() == nome.lower() for p in produtos):
        print(f"Erro: já existe um produto chamado '{nome}'.")
        return

    categoria = ler_texto("Categoria (opcional): ", obrigatorio=False) or "Geral"
    preco = ler_preco("Preço (R$): ")
    quantidade = ler_inteiro("Quantidade em estoque: ")

    produto = {
        "id": len(produtos) + 1,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade,
    }
    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!")
    print("-" * largura)
    print(f"ID:         {produto['id']}")
    print(f"Nome:       {produto['nome']}")
    print(f"Categoria:  {produto['categoria']}")
    print(f"Preço:      {formatar_preco(produto['preco'])}")
    print(f"Quantidade: {produto['quantidade']}")
    print("-" * largura)


def main():
    produtos = []

    try:
        while True:
            cadastrar_produto(produtos)
            outro = input("\nCadastrar outro produto? (s/n): ").strip().lower()
            if outro != "s":
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\nCadastro interrompido.")

    print(f"\nTotal de produtos cadastrados: {len(produtos)}")


if __name__ == "__main__":
    main()
