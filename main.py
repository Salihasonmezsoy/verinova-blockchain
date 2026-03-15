#blockchain ve veri tabanı bağlanacak ve veri tabanında değişiklik yapılabşlecek

from fastapi import Depends, FastAPI, HTTPException
from blockchain import _blockchain, Block
from pydantic import BaseModel 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from typing import Dict, Any

#python ve mySQL arasında köprü kuruyor
db_url = "gelecek olan url"

engine = create_engine(db_url)
sessionlocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)
base = declarative_base()
app = FastAPI()

my_blockchain = _blockchain.Blockchain()

class model(BaseModel):
  table_name: str
  datas: Dict[str, Any]



@app.post("/add_data/")
def add_data( process: model):
  new_block = my_blockchain.add_block(new_data = block_data.data)
  return new_block.__dict__

@app.get("/blockchain/")
def get_blockchain():
  chain_json = [block.__dict__ for block in my_blockchain.chain]
  return chain_json

app.get("/validate/")
def validate_blockchain():
  is_valid = my_blockchain.is_chain_valid()

  if is_valid:
    return False
  else:
    raise HTTPException(status_code=400, detail="DİKKAT! Blockchain geçersiz. Verilerle oynanmış olabilir")
  

    
