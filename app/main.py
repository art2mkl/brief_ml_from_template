#basic
from fastapi import FastAPI
import pandas as pd
import numpy as np
import json

#scrap
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get('/')

async def root():
    
    return None
