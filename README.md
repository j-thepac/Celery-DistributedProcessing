

Pre-Req:
- ```docker run -d -p 6379:6379 redis ```

Optional :
- Broker : Redis , RabbitMQ 
- Backend: Redis , RabbitMQ, Mongo 


                
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
        

