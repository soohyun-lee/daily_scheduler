import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise
from pydantic import BaseSettings

from daily.db import schema
from daily.routes import repost_list


app = FastAPI()

class Settings(BaseSettings):
    db_url: str

    class Config:
        env_file = '.env'

settings = Settings()

TORTOISE_ORM = {
    'connections' : {
        'default' : settings.db_url
    },
    'apps' : {
        'models' : {
            'models' : [
                'daily.db.schema',
                'aerich.models'
            ],
            'default_connection' : 'default'
        },
    }
}


async def init():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)
app.include_router(repost_list.app, prefix='/api/reports')

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)