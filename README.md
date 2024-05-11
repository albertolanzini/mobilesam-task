## Initialize Service

1. **Create a Virtual Environment and Activate It**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the Requirements**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Code**

    ```bash
    python main.py
    ```
   Do this to test proper functioning of the code, and proper package installation.

## API Testing with Postman

### Using FastAPI directly

1. Once you have setup your service, you can run the following command to start your locally hosted server:
   ```commandline
   uvicorn segment_image_endpoint:app
   ```
2. It is now possible to send a **POST** request to the endpoint:
   ```commandline
   http://127.0.0.1:8000/segment-image/
   ```
3. A great tool test the endpoint is **Postman**. It is possible to send a **POST** request with a body of type **form-data**.
   Make sure to use *file* as a key and upload the image you'd like to segment as a value.

### Using Docker

1. Make sure Docker is installed on your device. Instructions may depend on the device you are using. Refer to the following link for a guide: https://www.docker.com/get-started/.
2. Run this to build a docker image (it may take a while)
   ```commandline
   export DOCKER_BUILDKIT=1                                                                                                                     
   docker build -t my-fastapi-app .
   ```
3. Run your container with the following command:
   ```commandline
   docker run -p 8000:8000 --name=my-fastapi-app my-fastapi-app
   ```
4. You can now test the endpoint by sending a **POST** request at the following endpoint:
   ```commandline
   http://0.0.0.0:8000/segment-image
   ```
   If you're using Postman, make sure to use *file* as a key in the body of type **form-data** and upload the image you'd like to segment as a value.



   


