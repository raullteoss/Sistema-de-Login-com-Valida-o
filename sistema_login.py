# ==========================================
# Sistema de Login com Validação
# Desenvolvido para terminal (CLI)
# ==========================================
#
# Simula o fluxo de um sistema de autenticação:
# cadastro de usuário, verificação de credenciais
# e bloqueio de conta após tentativas incorretas
# repetidas (proteção simples contra força bruta).
#
# Estrutura de dados principal (banco de dados em memória):
# usuarios = {
#     "nome_do_usuario": {
#         "senha": str,
#         "tentativas": int,
#         "bloqueado": bool
#     },
#     ...
# }

MAX_TENTATIVAS = 3  # número de erros permitidos antes do bloqueio


def exibir_menu():
    """Exibe as opções principais do sistema."""
    print("\n" + "=" * 40)
    print("        SISTEMA DE AUTENTICAÇÃO")
    print("=" * 40)
    print("[1] - Cadastrar novo usuário")
    print("[2] - Fazer Login")
    print("[3] - Sair do sistema")
    print("=" * 40)


def cadastrar_usuario(usuarios):
    """Gerencia o cadastro de novos usuários no sistema.

    Validações aplicadas, nesta ordem:
      1. Usuário já cadastrado
      2. Nome de usuário vazio
      3. Senha vazia
    """
    print("\n--- Cadastro de Usuário ---")
    nome_usuario = input("Digite um nome de usuário: ").strip()

    # Validação 1: usuário já existe
    if nome_usuario in usuarios:
        print("Erro: O usuário '{}' já está cadastrado.".format(nome_usuario))
        return

    # Validação 2: nome de usuário vazio
    if not nome_usuario:
        print("Erro: O nome de usuário não pode ser vazio.")
        return

    senha = input("Digite uma senha: ").strip()

    # Validação 3: senha vazia
    if not senha:
        print("Erro: A senha não pode ser vazia.")
        return

    # Novo usuário sempre começa com 0 tentativas e desbloqueado
    usuarios[nome_usuario] = {
        "senha": senha,
        "tentativas": 0,
        "bloqueado": False,
    }

    print("Sucesso: Usuário '{}' cadastrado com sucesso!".format(nome_usuario))


def validar_senha(usuarios, nome_usuario, senha_digitada):
    """Valida a senha informada e controla o contador de tentativas.

    Regras:
      - Senha correta  -> zera o contador de tentativas.
      - Senha incorreta -> incrementa o contador; ao atingir
        MAX_TENTATIVAS, a conta passa a ficar bloqueada.

    Retorna True se a senha estiver correta, False caso contrário.
    """
    dados_usuario = usuarios[nome_usuario]

    if dados_usuario["senha"] == senha_digitada:
        dados_usuario["tentativas"] = 0
        return True

    dados_usuario["tentativas"] += 1
    if dados_usuario["tentativas"] >= MAX_TENTATIVAS:
        dados_usuario["bloqueado"] = True

    return False


def realizar_login(usuarios):
    """Gerencia o fluxo completo de login.

    Ordem de verificação: usuário existe -> conta não está
    bloqueada -> senha confere.
    """
    print("\n--- Login ---")
    nome_usuario = input("Usuário: ").strip()

    if nome_usuario not in usuarios:
        print("Erro: Usuário não encontrado no sistema.")
        return

    if usuarios[nome_usuario]["bloqueado"]:
        print(
            "Acesso Negado: A conta '{}' está bloqueada por excesso de tentativas.".format(
                nome_usuario
            )
        )
        return

    senha_digitada = input("Senha: ").strip()
    login_sucesso = validar_senha(usuarios, nome_usuario, senha_digitada)

    if login_sucesso:
        print("\nSucesso: Login realizado! Bem-vindo(a), {}!".format(nome_usuario))
        return

    # Login falhou: informa quantas tentativas restam ou o bloqueio
    if usuarios[nome_usuario]["bloqueado"]:
        print(
            "Alerta de Segurança: Senha incorreta {} vezes. Sua conta foi BLOQUEADA.".format(
                MAX_TENTATIVAS
            )
        )
    else:
        tentativas_restantes = MAX_TENTATIVAS - usuarios[nome_usuario]["tentativas"]
        print("Erro: Senha incorreta. Você tem mais {} tentativa(s).".format(tentativas_restantes))


def main():
    """Função principal: controla o loop do menu do sistema."""
    usuarios = {}  # banco de dados em memória (perdido ao encerrar o programa)

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            realizar_login(usuarios)
        elif opcao == "3":
            print("\nEncerrando o sistema de autenticação. Até logo!")
            break
        else:
            print("\nErro: Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
