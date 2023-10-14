import os
import pickle
import numpy as np
import requests
from dotenv import load_dotenv
from typing import Optional, List
from fastapi import FastAPI, UploadFile, File, Header, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response, PlainTextResponse, RedirectResponse
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html
)
from starlette import status
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from pydantic import BaseModel

API_URL = '/api'
API_VERSION = '/v1'

app = FastAPI(docs_url=None, redoc_url=None)
app.mount('/static', StaticFiles(directory='static'), name='static')
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://120.0.0.1:8080',
        '*'
    ],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class Data(BaseModel):
    bath: int
    sqft: int
    beds: int
    heating: int
    cooling: int
    parking: int
    age: int
    sch_rat_dist: int
    sch_number: int
    status_Active: int
    status_Other: int
    status_New: int
    status_Pending: int
    status_Foreclosure: int
    propertyType_Single_family: int
    propertyType_Townhouse: int
    propertyType_Condo: int
    propertyType_Multifamily: int
    propertyType_Land: int
    stories_Low_Rise: int
    stories_Mid_Rise: int
    stories_0_Stories: int
    stories_High_Rise: int
    state_0: int
    state_1: int
    state_2: int
    state_3: int
    state_4: int
    state_5: int


@app.get('/docs', include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + ' - Swagger UI',
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url='/static/swagger-ui-bundle.js',
        swagger_css_url='/static/swagger-ui.css'
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get('/redoc', include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + ' - ReDoc',
        redoc_js_url='static/redoc.standalone.js'
    )


@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse('/docs')


@app.post(API_URL + API_VERSION + '/predict', status_code=status.HTTP_200_OK)
async def predict(data: Data):
    model_data = [
        data.bath,
        data.sqft,
        data.beds,
        data.heating,
        data.cooling,
        data.parking,
        data.age,
        data.sch_rat_dist,
        data.sch_number,
        data.status_Active,
        data.status_Other,
        data.status_New,
        data.status_Pending,
        data.status_Foreclosure,
        data.propertyType_Single_family,
        data.propertyType_Townhouse,
        data.propertyType_Condo,
        data.propertyType_Multifamily,
        data.propertyType_Land,
        data.stories_Low_Rise,
        data.stories_Mid_Rise,
        data.stories_0_Stories,
        data.stories_High_Rise,
        data.state_0,
        data.state_1,
        data.state_2,
        data.state_3,
        data.state_4,
        data.state_5
    ]
    features = np.array(model_data).reshape(1, -1)
    prediction = round(model.predict(features)[0])
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    import uvicorn
    load_dotenv()
    
    with open('./model/model.pkl', 'rb') as pkl_file:
        model = pickle.load(pkl_file)

    uvicorn.run(app, host=os.environ['APP_HOST'], port=int(os.environ['APP_PORT']))
