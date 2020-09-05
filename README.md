# What is it?
This is an example of a python application for sending a mail message to Gmail. 
The code is executed asynchronously based on the Rest API and Uvicorn.
# How to use
1. Enable unsafe app in gmail account
1. Create .env file in root directory. Use .env.example for example! Don't push .env in git .
1. Start server from console
```
uvicorn main:app --reload --log-level "debug"
```
or use code
```python
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```
1. Use microservice as http://127.0.0.1:8000/docs
# Info
## ASGI server
http://www.uvicorn.org/deployment/  
## Fast API
https://fastapi.tiangolo.com/  
## Unsafe apps are blocked - enable
https://myaccount.google.com/lesssecureapps