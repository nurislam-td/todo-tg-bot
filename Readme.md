# Bot features

- add tasks to task list
- show task list

# To launch the application

#### Clone git repo

```shell
git clone https://github.com/nurislam-td/em-path_backend.git
```

#### Add environment variables

for example run command

```shell
exoprt MODE=DEV
exoprt BOT_TOKEN=<past your bot api key>
exoprt PYTHONPATH=$PYTHONPATH:$(pwd)/. # if modul named app not defined
exoprt DB_NAME=todo_tg_bot_db
exoprt DB_USER=username
exoprt DB_PASSWORD=some-random-pass
exoprt DB_HOST=localhost
exoprt DB_PORT=5432
```

**or past this variables in .env file** (without "export" of course )

#### Install docker, docker-compose if you don't have one and run

```shell
docker compose up -d
```
