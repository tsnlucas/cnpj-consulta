
# CNPJ Consulta e Padronização

Este projeto permite a consulta de CNPJs usando uma API e a padronização de arquivos Excel com CNPJs. O projeto utiliza uma interface gráfica (GUI) construída com **PyQt5**.

## Funcionalidades

- **Consulta de CNPJs**: Através de um arquivo Excel contendo CNPJs, o programa consulta uma API para retornar informações sobre cada CNPJ.
- **Padronização de CNPJs**: Padroniza arquivos Excel removendo formatações incorretas de CNPJs e garantindo que tenham 14 dígitos.

## Requisitos

Para rodar o projeto localmente, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.x** (recomendado Python 3.8 ou superior)
- **Bibliotecas Python**:
    - `PyQt5`
    - `pandas`
    - `openpyxl`
    - `requests`

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/cnpj-consulta.git
   cd cnpj-consulta
   ```

2. **Instale as dependências**:
   Execute o comando abaixo na pasta raiz do projeto para instalar as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o programa**:
   Para rodar a aplicação, use o seguinte comando:
   ```bash
   python main.py
   ```

## Estrutura do Projeto

- **`main.py`**: Arquivo principal para iniciar o programa.
- **`cnpj_consulta_app.py`**: Interface gráfica para consulta e padronização de CNPJs.
- **`cnpj_consulta_thread.py`**: Lida com a consulta de CNPJs em segundo plano (multithreading).
- **`padronizador_cnpj.py`**: Lógica de padronização dos CNPJs.
- **`instrucoes_tab.py`**: Aba com instruções adicionais.
- **`README.md`**: Este arquivo, que contém instruções de instalação e uso.
- **`LICENSE.txt`**: Termos de licença do projeto.

## Uso

### 1. Consulta de CNPJs

1. Na interface gráfica, selecione a aba "Consulta de CNPJs".
2. Clique em "Iniciar Consulta" e selecione um arquivo Excel que contenha CNPJs na coluna `CNPJ`.
3. O programa processará os CNPJs e exibirá os resultados na interface.

### 2. Padronização de CNPJs

1. Na aba "Padronização de CNPJs", clique em "Selecionar Arquivo Excel" e escolha um arquivo Excel.
2. Clique em "Padronizar e Salvar" para gerar um novo arquivo com os CNPJs padronizados (14 dígitos, sem formatação).

## Contribuição

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie um branch com suas alterações: `git checkout -b minha-feature`.
3. Faça um commit das suas alterações: `git commit -m 'Minha nova feature'`.
4. Envie para o branch: `git push origin minha-feature`.
5. Abra um pull request.

## Sobre o Projeto

Este projeto foi desenvolvido como parte de meus estudos para melhorar minhas habilidades de programação e desenvolvimento de software. Durante o processo, utilizei a ajuda de **inteligência artificial** para auxiliar na criação da lógica e no desenvolvimento da interface gráfica, bem como na implementação da consulta e padronização de CNPJs.

O uso de IA foi uma maneira de acelerar o processo de aprendizagem, permitindo-me explorar diferentes soluções e melhorar minha capacidade de resolver problemas.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE.txt).
