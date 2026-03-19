from fastapi import FastAPI, HTTPException, Depends
import mysql.connector
from pydantic import BaseModel
from blockchain import _blockchain, Blockchain

app = FastAPI()

db_config = {
  "host": "localhost",
  "user": "root",
  "password": "12345",
  "database": "kutuphane_db"
}

class BlockData(BaseModel):
  data:str

blockchain_=_blockchain.Blockchain()

def get_valid_blockchain():
  if not blockchain_.is_chain_valid():
    raise HTTPException(status_code=400, detail="The chain is invalid")
  return blockchain_


@app.post("/mine_block/")
def mine_block(block_data: BlockData,
               blockchain: _blockchain.Blockchain = FastAPI.Depends(get_valid_blockchain)):
  return blockchain.mine_block(data = block_data.data)


@app.get("/get_blockchain/")
def get_blockchain(blockchain: _blockchain.Blockchain = FastAPI.Depends(get_valid_blockchain)):
  return {"lenght": len(blockchain.chain), "chain": blockchain.chain}

@app.get("/blockchain/last/")
def get_previous_block(blockchain: _blockchain.Blockchain= FastAPI.Depends(get_valid_blockchain)):
  return blockchain.get_previous_block()

@app.get("/validate")
def is_block_valid():
  is_valid = blockchain_.is_chain_valid()
  return {"is_valid": is_valid}