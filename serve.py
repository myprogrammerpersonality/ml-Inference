import os
from fastapi import FastAPI, Request, Response, status
import joblib
import pandas as pd
import uvicorn


model_path = './'
model = joblib.load(os.path.join(model_path, "model.joblib"))


stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"
app = FastAPI(title="MyAwesomeApp", openapi_prefix=openapi_prefix) # Here is the magic

@app.get("/hello")
def hello_world():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return Response(status_code=status.HTTP_200_OK)

@app.post('/boston_predict')
async def basic_predict(request: Request):
    # Getting the JSON from the body of the request
    input_data = await request.json()

    # Converting JSON to Pandas DataFrame
    input_df = pd.DataFrame([input_data]).values

    # Getting the prediction from the Logistic Regression model
    pred = model.predict(input_df)[0]

    return pred


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
