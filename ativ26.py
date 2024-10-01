# Crie um programa que receba as notas de 5 alunos e as armazene em uma lista. O programa deve exibir a maior nota, a menor nota e a média das notas.

# Exemplo de entrada:
# Nota do aluno 1: 8
# Nota do aluno 2: 6
# Nota do aluno 3: 9
# Nota do aluno 4: 7
# Nota do aluno 5: 5

# Exemplo de saída:
# Maior nota: 9
# Menor nota: 5
# Média das notas: 
Notas = []
for i in range (5):
    nota=float(input(f"diga a nota do aluno: {i+1}"))
    Notas.append(nota)
maior_nota = max(Notas)
menor_nota = min(Notas)
media_notas = sum(Notas) / len(Notas)
print(f"maior nota: {maior_nota}")
print(f"menor nota: {menor_nota}")
print(f"media das notas: {media_notas:.1f}")
