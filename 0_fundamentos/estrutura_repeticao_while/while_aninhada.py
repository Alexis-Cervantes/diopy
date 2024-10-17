"""O Sistema pede as 03 notas de 03 alunos e mostra a MEDIA de cada um deles"""
num_alunos = 3
num_notas = 3
# Contador para o número de alunos
aluno = 0

while aluno < num_alunos:
    print(f"Anotando as notas do aluno {aluno + 1}")
    # Contador para o número de notas de cada aluno
    nota = 0
    total_notas = 0

    while nota < num_notas:
        nota_atual = float(input(f"Digite a nota {nota + 1} do aluno {aluno + 1}: "))
        total_notas += nota_atual
        nota += 1

    media = total_notas / num_notas
    print(f"A média do aluno {aluno + 1} é: {media:.2f}\n")

    aluno += 1

# Mensagem final após todas as médias serem recebidas
print("Todas as médias foram recebidas!")