# M5 - S2 - Entrega - Kopa do Mundo

Nesse projeto, feito como entrega avaliativa no módulo 5 do curso de desenvolvedor Full Stack da Kenzie Academy Brasil, é montado um CRUD que gerencia informações sobre as seleções na Copa do Mundo.

Na aplicação foi utilizado Python com Django e DjangoRestFramework, além de trabalhar também com ORM.

No projeto são utilizados métodos POST, GET, PATCH e DELETE para cadastrar, listar, atualizar e deletar seleções e suas respectivas estatísticas de desempenho na Copa do Mundo.

## Como rodar os testes localmente

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:
```shell
pip list
```
- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:
```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
```

A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

3. Instale o pacote `pytest-testdox`:
```shell
pip install pytest-testdox pytest-django
```

4. Rodar os testes no diretório principal do projeto:
```shell
pytest --testdox -vvs
```


