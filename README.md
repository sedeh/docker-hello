# docker hello world

This repo demonstrates a basic docker app. 
 
Clone the repo and follow these steps to build and run the app:

1. Move into `main`: `cd /path/to/repo/main` (pseudo-code, please change)
2. Build the app: `docker build --tag helloapp:1.0 .`
3. Run the app `docker run --detach -p 5000:8080 --name test helloapp:1.0`

This binds port 8080 of the container to TCP port 5000 on 127.0.0.1 of the host machine. 

If successful, `curl http://127.0.0.1:5000/` will output the following:

```
{"message":"Hello from Docker!"}
```

4. View a log of the running app: `docker logs --follow test`

5. Stop and remove the app: `docker stop test && docker rm test`

# References
- Install docker: https://docs.docker.com/get-docker/
