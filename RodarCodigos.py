import subprocess
import os

comando_base = "!kitt"
nome = "KITT"
maquina = "--"
usuario = ">>"
texto = f"""--{nome}--"""

def criar_caixa(texto):
    linhas = texto.split("\n")
    largura = max(len(linha.strip()) for linha in linhas) + 4

    borda = "+" + "-" * largura + "+"
    espaco_vazio = "|" + " " * largura + "|"

    print(borda)
    print(espaco_vazio)
    for linha in linhas:
        linha_centralizada = linha.strip().center(largura - 2)
        print(f"| {linha_centralizada} |")  
    print(espaco_vazio)
    print(borda)

interpreters = {
    ".py": "python",
    ".exe": "",
    ".sh": "bash",
    ".bat": "cmd /c",
    ".java": "java",
}

def rodar_codigo(file_name):
    file_path = os.path.abspath(file_name)
    _, ext = os.path.splitext(file_name)

    if ext == ".cs":
        print("--Rode o .csproj e nao o .cs")

    if not os.path.exists(file_path):
        print(f"Erro: Arquivo '{file_name}' não encontrado.")
        return

    if ext not in interpreters and ext != ".csproj":
        print(f"Erro: Não sei como executar '{file_name}'")
        return

    if ext == ".csproj":
        project_dir = os.path.dirname(file_path)
        print(f"-- Detectado projeto .NET! Executando `dotnet run` em {project_dir} --")
        
        run_cmd = ["dotnet", "run"]
        subprocess.run(run_cmd, cwd=project_dir, shell=True)
        
        return
    command = interpreters[ext]
    full_command = f"{command} {file_path}" if command else file_path

    try:
        print(f"Executando {file_name}...")
        process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()

        print("-"*50)
        print("Saída:")
        criar_caixa(output)

        if error:
            print("Erros:")
            print(error)

    except Exception as e:
        print(f"Erro ao executar {file_name}: {e}")

def pedir_ajuda():
    print(f"\n{maquina}Usuario pediu ajuda!")
def canal_criador():
    print(f"\n{maquina}Canal do criador:")
def rodar_funcao_cdg():
    try:
        path_file = comando.split(" ")[2]
        print(f"\n{maquina}{comando.split(" ")[2]}")
        rodar_codigo(path_file)
    except Exception as ex:
        print(f"\n{maquina}Erro: {ex}")
def catar_path_txt():
    with open("path.txt","r",encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    print(f"\n{maquina}{conteudo.split(' ')[1]}")
def sair():
    global rodando
    rodando = False

rodando = True
while rodando:
    if os.path.exists("path.txt"):
        comandos_dicionario = {
            f"{comando_base} help": pedir_ajuda,
            f"{comando_base} channel": canal_criador,
            f"{comando_base} run_p <path>": rodar_funcao_cdg,
            f"{comando_base} run_t": catar_path_txt,
            f"{comando_base} leave": sair,
        }
        for com in comandos_dicionario:
            texto += f"\n{com}"
        criar_caixa(texto)
        comando = input(f"\n{usuario}").lower().strip()
        comando_real = " ".join(comando.split(" ")[:2])
        if comando_real in comandos_dicionario:
            comandos_dicionario[comando_real]()
        else:
            print(f"\n{maquina}Comando '{comando_real}' nao encontrado")
    else:
        comandos_dicionario = {
            f"{comando_base} help": pedir_ajuda,
            f"{comando_base} channel": canal_criador,
            f"{comando_base} run_p <path>": rodar_funcao_cdg,
            f"{comando_base} leave": sair,
        }
        for com in comandos_dicionario:
            texto += f"\n{com}"
        criar_caixa(texto)
        comando = input(f"\n{usuario}").lower().strip()
        comando_real = " ".join(comando.split(" ")[:2])
        if comando_real in comandos_dicionario:
            comandos_dicionario[comando_real]()
        else:
            print(f"\n{maquina}Comando '{comando_real}' nao encontrado")
print(f"\n{maquina}Finalizando ...")