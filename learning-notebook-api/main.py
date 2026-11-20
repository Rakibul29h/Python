# To create this project first need uv installed 
# Install UV by: curl -LsSf https://astral.sh/uv/install.sh |sh
# Then init a project by uv init 'project name' --bare
# To create the project as a fastapi uv add "fastapi[standard]"
# Run the server by uv run fastapi dev

from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def root():
    return {"message":"Successful"}

