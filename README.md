# Kitt Script Runner

Um script que permite rodar outros scripts de diferentes linguagens diretamente pelo terminal.

## 📌 Funcionalidades
- `!kitt help` → Exibe a ajuda com os comandos disponíveis.
- `!kitt credits` → Mostra os créditos do criador.
- `!kitt run_p <path>` → Roda o script localizado no caminho especificado.
- `!kitt run_t` → Se existir um arquivo `path.txt` no diretório do script, executa o código conforme o caminho definido nesse arquivo.
- `!kitt leave` → Sai do programa.

### 📂 Extensões suportadas
O `Kitt Script Runner` suporta a execução de arquivos com as seguintes extensões:
- `.py` → Python
- `.exe` → Arquivos executáveis
- `.sh` → Shell Script
- `.bat` → Arquivos Batch (Windows)
- `.java` → Arquivos Java compilados
- `.csproj` → Projetos .NET (executa `dotnet run` automaticamente)

## 📦 Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd seu-repositorio
   ```
3. Certifique-se de ter Python instalado na máquina.

## 🚀 Uso
Execute o script e utilize os comandos conforme necessário:
```sh
python kitt.py
```
Depois, utilize os comandos disponíveis no terminal.

## ⚠️ Observações
- Para rodar arquivos `.cs`, utilize o `.csproj` correspondente.
- Se um `path.txt` estiver presente no diretório do script, o comando `!kitt run_t` usará o caminho contido nele automaticamente.
- O script cria caixas de saída para facilitar a leitura dos resultados.

## 🛠 Requisitos
- Python instalado na máquina
- Dependendo do tipo de script que deseja rodar, pode ser necessário ter o interpretador correspondente instalado (Java, .NET, etc.)

## 📜 Licença
Este projeto está sob a licença MIT. Para mais detalhes, consulte o arquivo `LICENSE`.

---
Desenvolvido por Wellington Coelho Pedroso 🚀
