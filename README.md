## Utilização de Celery em aplicação Django

**Escrito por:** [Jordano Paganini](https://github.com/JordanoPaganini)

---

- Instalação:
>   1. É nescessário realizar a instalação, obrigatóriamente, dos pacotes Django e Celery, para tal utilize os comandos listados, respectivamente, a seguir:
>   `pip install django`
>   `pip install celery`
>   2. Para a utilização de redis em conjunto a biblioteca do celery, se faz nescessária a sua instalação em conjunto, a mesma pode ser realizada através do comando: `pip install -U "celery[redis]"`

- Configuração:
>   1. É nescessário configurar um arquivo padrão no diretorio do projeto (`celery.py`)
>   2. Deve ser adicionado a chamada do mesmo ao arquivo `__init__` no diretorio do projeto principal
>   3. No arquivo de configurações (`settings.py`) é preciso configurar as variaveis, sendo a principal `CELERY_BROKER_URL`


- Brokers e Results Backends:
>   1. Recomendação a utilização do broker *RabbitMQ*, a exemplo o disponível online em [https://www.cloudamqp.com/]
>   2. Para o armazenamento dos resustados é recomendado a utilização de um servidor Redis, a exemplo o fornecido pela Railway [https://railway.app/]

- Comandos:
>   1. Para executar um novo worker conectado ao devido broker: `celery -A <project_name> worker -l info`
>   2. Caso a execução do worker occora em um dispositivo com sistema operacional Windows é nescessário, ao final do comando, adicionar: `--pool=solo`

- Monitoramento:
>   1. Utilizando o flower uma página web será gerada automaticamente a qual mostrará informações sobre os Workers e as Tarefas
>   2. Para utilizalo é nescessário instala-lo no ambiente: `pip install flower`
>   3. Para iniciar o monitoramento utilizando flower, execute no terminal: `celery -A <project_name> flower`

### Link da úteis: 
- [Celery Documentation](https://docs.celeryq.dev/en/stable/)
- [Official Django and Celery Integration Tutorial](https://docs.celeryq.dev/en/stable/django/index.html)
- [Django Documentation](https://docs.djangoproject.com/en/5.1/)