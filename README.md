[![Python application](https://github.com/Wheatly99/Project_SE/actions/workflows/python-app.yml/badge.svg)](https://github.com/Wheatly99/Project_SE/actions/workflows/python-app.yml)
## Software Engineering Project
*Hello, this repository is for creating an application that implements an API for a machine learning model.*

**Creators:**
- Markin Mikhail, РИМ-120907;
- Zenkov Miroslav, РИМ-120906;
- Solomein Aleksandr, РИМ-120907;
- Kolomenskii Viktor, РИМ-120907.

**Comments:**  

To run on Yandex Cloud, two virtual machines are created: one runs a server with an API application, the other runs a Web application.   

The machine learning model is located on a virtual machine with an API application. When entering a string from the Web interface, an API server is accessed, which predicts the missing word and returns the result to the Web interface.

**How to run?**

For a VM with an API application: uvicorn main:app --host 0.0.0.0   
For a VM with a Web application: streamlit rum web_with_api.py [ip_api] [port_api]   
*(P.S. ip_api and port_api - optional parameters. Their default values are: ip_api = 127.0.0.1, port_api = 8000)*