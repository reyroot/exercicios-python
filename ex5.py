usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto:
    print("Usuário correto")
else:
    print("Usuário incorreto")

if senha == senha_correta:
    print("Login realizado")
else:
    print("Senha incorreta")