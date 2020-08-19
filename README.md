## Demonstration of [Zappa issue #2154](https://github.com/Miserlou/Zappa/issues/2154) 

This repo contrains a minimal viable example to showcase [this issue (#2154)](https://github.com/Miserlou/Zappa/issues/2154) for [Zappa](https://github.com/Miserlou/Zappa).



#### Create a virtualenv 
```
virtualenv -p python3.8 .venv && source .venv/bin/activate && pip install -r requirements.txt 
```

#### Deploy the code to an AWS Lambda and API Gateway
```
zappa deploy dev
```

#### Test it!

Sync function 
```
curl -v https://jqeestl886.execute-api.eu-central-1.amazonaws.com/dev/demo \
-H 'Content-Type: application/json' \
-d '{"foo":"Hello", "bar":"world!"}'

# --> HTTP 202
```

Async function
```
curl -v https://jqeestl886.execute-api.eu-central-1.amazonaws.com/dev/asyncdemo \
-H 'Content-Type: application/json' \
-d '{"foo":"Hello", "bar":"world!"}'

# --> HTTP 500
# botocore.exceptions.SSLError: SSL validation failed for https://lambda.eu-central-1.amazonaws.com/2015-03-31/functions/zappa-error-demo-dev/invocations [Errno 2] No such file or directory
```
