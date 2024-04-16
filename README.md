# Secret Keeper

The service is an API server for temporary storage of secrets (or any different information).
Access to the secret is unlocked by a special key.

The service is working, compiled into a Docker package.

To start, you need to create a file (.env) and make certain settings (like .env_template) to start and operate the service correctly.

Нou can use default settings:
```
POSTGRES_DB=key_secret
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379
```

To start working with the service from Docker, run the following command
(for default server is running on host _0.0.0.0:8000_):
```
docker-compose up -d --build
```

To work with the service, the following URLs are used:
```
.../secret/generate/
This URL create a secret in DB and return {key_slug}, which is used to access it
```
```
.../secret//secrets/{secret_key}
This URL open a secret
```

The service allows you to store secrets for a certain period of time (30 minutes, 1, 4 or 12 hours, 1 or 7 days).

The service also provides for clearing already opened secrets (you can read it ONLY 1 TIME).

To work with the admin panel, use the command to create a superuser:
_default settings for superuser: login - admin, password - admin_
```
python3 manage.py create_superuser (for use in env)

docker-compose exec key_secret_tracker python3 manage.py create_superuser (for use in Docker)
```

All information about Secrets is stored in DB in encrypted form, you can choose your own password of encryption (_correct .env-file_):
```
CRYPTO_KEY_PASS=
```
