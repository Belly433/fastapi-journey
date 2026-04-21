1. Why does `DATABASE_URL` use `mongo` instead of `localhost`?
`mongo` is the service name defined in `docker-compose.yml`, and Docker automatically uses it as a hostname for communication between containers.

If we used `localhost`, the FastAPI container would try to connect to itself, not to the MongoDB container.  
As result, connection will fail.

2. What does `depends_on` do? Does it guarantee MongoDB is ready?

`depends_on` ensures that the MongoDB container starts before the FastAPI container.

However, it does NOT guarantee that MongoDB is fully ready to accept connections.  
It only controls startup order.

To guarantee readiness, we would need:
- a mechanism to check if MongoDB is ready before the app starts, or  
- a retry/wait mechanism in the application

3. What is the purpose of the volume in the `mongo` service?

The volume is used to persist MongoDB data outside the container which means data is saved even if the container is removed or restarted. If we remove the volume and run docker compose down, all data will be permanently deleted.

4. Why do we copy `requirements.txt` and run `pip install` before copying the rest of the app code in the Dockerfile?

This is done for Docker layer caching. The requirements.txt is copied first, dependencies are installed then the rest of the code is copied. If the app code changes but requirements.txt does not,Docker reuses the cached layer and skips reinstalling dependencies.