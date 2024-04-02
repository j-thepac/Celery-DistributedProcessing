

Pre-Req:
- Install Dependencies to Linux      
        sudo apt-get install -y --no-install-recommends \
                autoconf \
                automake \
                pkg-config \
                libtool \
                libffi-dev \
                libssl-dev
        pip install "celery[librabbitmq]"
- Make sure RabbitMQ is up and copy URL
```docker run -d -p 5672:5672 rabbitmq```
- Make sure MongoDB is UP and copy URL
            - use Cloud or 
            - Use docker
           
                       docker run -d -p 27017:27017  mongo
                       docker ps -a
                       docker exec -it containerid bash
                              mongosh
                              use company
                              db.employee.insertOne( { name: "mark" } );
                              db.employee.find().forEach(printjson)
                              exit
- use Docker if needed
        
                docker run -d -p 5672:5672 rabbitmq
                docker run -d -p 6379:6379 redis
Steps:
- Open Terminal 1
  - cd to current folder
          
          celery -A filename worker --loglevel=INFO
- Open terminal 2
  - cd to current folder
  - open python shell (not ipython) 

          from example import add
          res=add.delay(1,2)
          res.status
          res.get()
        

