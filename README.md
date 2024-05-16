### employee-api
Api build by using FastAPI

#### What is FastAPI?
FastAPI is a simple and lightweight Python framework which used to build a small scalable web application. It follows `ASGI` and can handle API requests asynchronously. This allows tasks to be completed at their own pace and does not require that they wait for other tasks to be completed. By default the FastAPI app will run in the port of 8000.

#### Dependcies
 + python3.8 >
 + fastapi
 + uvicorn
 
#### Install Command
```
pip3 install fastapi
```
```
pip3 install uvicorn
```

##### Run Command
``uvicorn myAPI:app --reload``

##### To access the API in UI
http://127.0.0.1:8000/docs

##### Alternative API doc
http://127.0.0.1:8000/redoc

This API was deployed, use the link https://employee-fastapi.herokuapp.com/docs (This link expried since the herokuapp expried) 
