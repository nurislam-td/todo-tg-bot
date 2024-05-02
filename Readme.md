# Bot features

- add tasks to task list
- show task list

**bot links**
https://t.me/anverali_td_bot

# To launch the application

#### Clone git repo

```shell
git clone https://github.com/nurislam-td/em-path_backend.git
```

#### Add environment variables

for example run command

```shell
export MODE=DEV
export BOT_TOKEN=<past your bot api key>
export DB_NAME=todo_tg_bot_db
export DB_USER=username
export DB_PASSWORD=some-random-pass
export DB_HOST=localhost
export DB_PORT=5432
```

**or past this variables in .env file** (without "export")

#### Install docker, docker-compose if you don't have one and run

```shell
docker compose up -d
```
