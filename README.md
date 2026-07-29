Sistema de Login com Validação
Um simulador de sistema de autenticação construído em Python, com controle de acesso, validação de credenciais e gerenciamento de estado de usuários. Disponível em duas versões: a original via terminal (CLI) e uma interface web simples que reproduz a mesma lógica.
Objetivo
Simular o fluxo completo de um sistema de login seguro, aplicando bloqueio preventivo contra ataques de força bruta (tentativas repetidas de adivinhação de senha).
Funcionalidades
Cadastro de Usuário: criação de conta com validação para impedir nomes de usuário duplicados e senhas vazias.
Autenticação Segura: verificação de credenciais no momento do login.
Controle de Tentativas: o sistema monitora erros de senha.
Bloqueio de Conta: após 3 tentativas incorretas, o usuário é bloqueado e impedido de tentar novamente, simulando uma medida real de segurança.
Estrutura do repositório
```
sistema-login-validacao/
├── cli/
│   └── sistema_login.py   # versão original, via terminal
└── web/
    └── index.html         # interface web (HTML/CSS/JS puro)
```
Versão CLI
Tecnologias e estruturas utilizadas
Python 3.x
Dicionários aninhados: para armazenar o estado de cada usuário — `{"usuario": {"senha": str, "tentativas": int, "bloqueado": bool}}`.
Modularização (funções): código dividido em funções específicas (`cadastrar_usuario`, `realizar_login`, `validar_senha`) para facilitar a manutenção e leitura.
Controle de fluxo: uso de `if/elif/else` para validações e loop `while` para manter a aplicação ativa.
Como executar
```bash
cd cli
python3 sistema_login.py
```
Versão Web
Uma interface simples em HTML/CSS/JS que roda direto no navegador, sem instalação e sem back-end. Reproduz as mesmas validações e mensagens da versão CLI: cadastro, verificação de senha e bloqueio após 3 tentativas. Os dados existem apenas em memória durante a sessão (assim como o dicionário `usuarios` da versão em Python) — ao atualizar a página, o estado é reiniciado.
Como executar
Basta abrir o arquivo `web/index.html` em qualquer navegador (duplo clique ou "Abrir com" o navegador de sua preferência). Não requer servidor.
Autor
Projeto desenvolvido como exercício acadêmico de lógica de programação e estruturas de dados em Python.

LINK: file:///C:/Users/Raul%20Teot%C3%B4nio/Downloads/sistema-login-validacao/sistema-login-validacao/web/index.html
