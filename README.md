<h1>Backend-python-wallet</h1>
<h2>Sumário</h2>

* <small><i><a href='#Objetivo'>Objetivo</a></i></small><br>
* <small><i><a href='#Ferramentas utilizadas'>Ferramentas utilizadas</a></i></small><br>
* <small><i><a href='#Como rodar o projeto'>Como rodar o projeto</a></i></small><br>
* <small><i><a href='#Testes'>Testes</a></i></small><br>
* <small><i><a href='#Estudos'>Estudos</a></i></small>



<h2>Objetivo:</h2>

- Criar um endpoint onde valida informações do cliente e calcula o cashback pelo tipo do produto assim enviando as informações a API 
da MaisTodos efetivando a criação do mesmo já calculado.

<h2>Ferramentas utilizadas:</h2>

- Marshmallow
- Psycopg2
- Psycopg2-binary
- Django
- Black
- Isort
- Pytest
- Pytest-django
- Validate-docbr
- Pytest-cov
- Pytest-flake8
- Insomnia

<h2>Como rodar o projeto:</h2>

- Crie um ambiente virtual através do comando python -m venv "Nome da virtual env".

- Ative seu ambiente virtual através do comando:

   - No Linux: source venv/bin/activate 
   - No Windows: cd venv/scripts/.\activate 

   **OBS**: venv é o exemplo do nome da virtual env, esse comando de ativação tem que estar dentro da pasta da virtual env.

<h3>Com a virtual env ativada rode o comando:</h3>

- pip install -r requirements.txt

  Este comando fará com que instale todas as bibliotecas necessárias para rodar o projeto.

  Com todas as dependencias instaladas rode o comando:

  - python manage.py runserver onde irá startar o servidor do projeto assim sendo possivel realizar uma requisição ao endpoint cashback.

  O endpoint espera um dicionário neste formato:

    ```json
    {
        "sold_at": "2026-01-02 00:00:00",
        "customer": {
           "document": "00000000000",
           "name": "JOSE DA SILVA",
        },
        "total": "100.00",
        "products": [
           {
              "type": "A",
              "value": "10.00",
              "qty": 1,
           },
           {
              "type": "B",
              "value": "10.00",
              "qty": 9,
           }
        ],
    }
    ```
    
    <h2>Testes</h2>
    
    - <h3>Testes no código</h3></br>
    
    <img src = https://user-images.githubusercontent.com/38404862/132390652-ddd004e0-6576-4e37-915b-a2e5e3a69107.png width = 700/>
    
    - <h3>Testes utilizando o Insomnia</h3>   
    
    <h3>Cpf inválido</h3>
    
    <img src = https://user-images.githubusercontent.com/38404862/132392701-5e9d40f0-20b8-4045-8dc5-20da13b1cff5.png width = 700/>
    
    <h3>Data inválida</h3>
    
    <img src = https://user-images.githubusercontent.com/38404862/132392754-34dd6ad7-cce4-4121-8610-c24fc3f6307a.png width = 700/>
    
    <h3>Soma errada dos valores</h3>
    
    <img src = https://user-images.githubusercontent.com/38404862/132392808-a5d08701-787c-4404-9f21-12143364a7c1.png width = 700/>
    
    <h3>Tipo fora do formato</h3>
    
    <img src = https://user-images.githubusercontent.com/38404862/132392964-b7b21615-c238-4dad-ab62-47425669ea3a.png width = 700/>
    
    <h3>Requisição válida</h3>
    
    <img src = https://user-images.githubusercontent.com/38404862/132392773-7c84495b-a9c3-4d5c-9840-b6f55837a0e7.png width = 700/>
    
    <h2>Estudos</h2>
    
    Para realizar este projeto foi feito uma grande pesquisa na biblioteca marshmallow que foi usada para validar os dados.
    
    Função oneOf usado para validar o tipo do produto: https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#marshmallow.validate.OneOf
    
    Função post_load usado para validar o valor total após a validação dos dados:         https://marshmallow.readthedocs.io/en/stable/marshmallow.decorators.html#marshmallow.decorators.post_load e 
    https://marshmallow.readthedocs.io/en/stable/marshmallow.decorators.html
    
    Função fields.Method usado para validar o cpf: https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html#marshmallow.fields.Method e 
    https://marshmallow.readthedocs.io/en/stable/custom_fields.html#method-fields
    
    Realizar uma requisição post pra API MaisTodos: 
    https://www.kite.com/python/answers/how-to-send-a-post-request-in-python#:~:text=Use%20requests.,server's%20response%20to%20the%20request.
    
    Django JSONResponse usado para retornar o valor da API criada em Json de maneira customizável: https://docs.djangoproject.com/en/3.2/ref/request-response/#jsonresponse-objects
    
    
    
