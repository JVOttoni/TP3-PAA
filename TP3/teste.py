import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_test_file(filename, text_length, pattern_length, num_queries):
    with open(filename, 'w') as f:
        # Gera uma string principal aleatória
        text = generate_random_string(text_length)
        f.write(f"{text}\n")
        
        # Gera uma substring aleatória
        pattern_start = random.randint(0, text_length - pattern_length)
        pattern = text[pattern_start:pattern_start + pattern_length]
        f.write(f"{pattern}\n")
        
        # Escreve o número de queries
        f.write(f"{num_queries}\n")
        
        # Gera queries aleatórias
        for _ in range(num_queries):
            a = random.randint(0, text_length - 1)
            b = random.randint(a, text_length - 1)
            f.write(f"{a} {b}\n")

if __name__ == "__main__":
    # Parâmetros para gerar os arquivos de teste
    text_length = 10000000 # Tamanho da string principal
    pattern_length = 1  # Tamanho da substring
    num_queries = 10    # Número de queries
    num_files = 1       # Número de arquivos de teste a serem gerados
    
    for i in range(1, num_files + 1):
        filename = f"entrada.txt"
        generate_test_file(filename, text_length, pattern_length, num_queries)
        print(f"Arquivo {filename} gerado com sucesso.")
