# Python django project focused on managing Cows!

**To start the project run command:** 

```docker-compose up```

**Create a distributable package**

poetry build 

**Check swagger documentation:**

localhost:8080/swagger

**Build app package:**
- creating prod env\
poetry install --no-dev
- creating package for prod\
poetry build                    
- creating test env\
poetry install                  

**Some notes:**

docker-compose down\
docker-compose down -v
