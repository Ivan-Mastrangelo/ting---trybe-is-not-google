## Sobre

Este projeto foi desenvolvido como parte da avaliação do módulo Ciência da Computaçãocurso do curso Desenvolvimento Web da escola Trybe e foi desenvolvido em Python.

Nele implementei um programa que simula um algoritmo de indexação de documentos similar ao do Google. O programa deve ser capaz de identificar ocorrências de termos em arquivos _TXT_.
  
Para tanto, o programa possui dois módulos:
- Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato _TXT_) e;
- Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.

### Habilidades exercitadas:

 - Manipular Pilhas;
 - Manipular Deque;
 - Manipular Nó & Listas Ligadas e;
 - Manipular Listas Duplamente Ligadas.

### Para executar o projeto localmente:

- Clone o repositório
```
  git clone git@github.com:Ivan-Mastrangelo/ting---trybe-is-not-google.git
```
- Entre na pasta do repositório que você acabou de clonar:
```
  cd ting---trybe-is-not-google
  ```
- Crie o ambiente virtual para o projeto
```
  python3 -m venv .venv && source .venv/bin/activate
 ```
- Instale as dependências
```
  python3 -m pip install -r dev-requirements.txt
  ```
#### Teste Manual
  
  Abra um terminal Python importando as funções de interesse através do comando:
  ```
  python3 -i tech_news/arquivo_de_interesse.py
  ```