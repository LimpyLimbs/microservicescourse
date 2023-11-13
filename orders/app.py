# import sys
# sys.path.append('/home/ec2-user/coding/webapplications/microserviceapis/ch02/')

from fastapi import FastAPI

app = FastAPI(debug=True)

from orders.api import api
