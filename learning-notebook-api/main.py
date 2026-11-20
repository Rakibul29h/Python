# To create this project first need uv installed 
# Install UV by: curl -LsSf https://astral.sh/uv/install.sh |sh
# Then init a project by uv init 'project name' --bare
# To create the project as a fastapi uv add "fastapi[standard]"
# Run the server by uv run fastapi dev

from fastapi import FastAPI

from pydantic import BaseModel

app= FastAPI()


notes = [
    {
        "id": 1,
        "term": "variable",
        "definition": "A name that stores a value",
        "js_equivalent": "let/const",
        "tags": ["python", "basics"],
        "learned": True
    },
    {
        "id": 2,
        "term": "data_type",
        "definition": "Defines the type of value a variable stores",
        "js_equivalent": "typeof",
        "tags": ["python", "basics"],
        "learned": True
    },
    {
        "id": 3,
        "term": "string",
        "definition": "A sequence of characters",
        "js_equivalent": "String",
        "tags": ["python", "data-types"],
        "learned": True
    },
    {
        "id": 4,
        "term": "integer",
        "definition": "A whole number without decimal points",
        "js_equivalent": "Number",
        "tags": ["python", "data-types"],
        "learned": True
    },
    {
        "id": 5,
        "term": "float",
        "definition": "A number that contains a decimal point",
        "js_equivalent": "Number",
        "tags": ["python", "data-types"],
        "learned": False
    },
    {
        "id": 6,
        "term": "boolean",
        "definition": "A data type with True or False values",
        "js_equivalent": "Boolean",
        "tags": ["python", "data-types"],
        "learned": True
    },
    {
        "id": 7,
        "term": "list",
        "definition": "An ordered and mutable collection of items",
        "js_equivalent": "Array",
        "tags": ["python", "collections"],
        "learned": True
    },
    {
        "id": 8,
        "term": "tuple",
        "definition": "An ordered and immutable collection of items",
        "js_equivalent": "No direct equivalent",
        "tags": ["python", "collections"],
        "learned": False
    },
    {
        "id": 9,
        "term": "dictionary",
        "definition": "A collection of key-value pairs",
        "js_equivalent": "Object / Map",
        "tags": ["python", "collections"],
        "learned": True
    }
]


class Note(BaseModel):
    term:str
    definition: str
    js_equivalent:str | None = None
    tags:list[str]=[]
    learned:bool = False
    
@app.get("/")
def root():
    return {"message":"Successful"}

@app.get("/terms")
def get_terms(tag:str|None=None,q:str |None = None):
    result = []
    for note in notes:
        if tag and tag not in note["tags"]:
            continue
        if q and q.lower() not in note["term"].lower():
            continue
        result.append(note)

    return result

# Dynamic id
@app.get("/term/{term_id}")
def get_term_by_id(term_id:int):
    for note in notes:
        if note["id"] == term_id:
            return note

    return {"message":"Term not found"}



@app.post("/term",status_code=201)
def add_term(note:Note):
    new_note = {"id":len(notes)+1}
    new_note.update(note.model_dump())
    notes.append(new_note)
    return new_note
