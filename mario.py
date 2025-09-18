altura = int(input("Altura: "))

for i in range(1, altura + 1):
    espacos = altura - i
    blocos = i
    print(" " * espacos + "#" * blocos)

input("Pressione Enter para sair...")