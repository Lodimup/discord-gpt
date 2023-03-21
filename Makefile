default: build run

build:
	docker build -t discordgpt .

run:
	docker run --rm --name discordgpt --env-file .env discordgpt

rq:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
