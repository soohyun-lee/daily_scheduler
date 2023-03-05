from fastapi import APIRouter
from daily.db.schema import Report

app = APIRouter()

@app.get("")
async def get_reports():
    data = [{
        "content" : report.content
    } for report in await Report.all()]
    
    return data