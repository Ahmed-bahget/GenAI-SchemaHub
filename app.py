from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from utils import generate_text
from schemas.schema1 import schema_1
from schemas.schema2 import schema_2
from schemas.schema3 import schema_3
from schemas.schema4 import schema_4
from schemas.schema5 import schema_5
from schemas.schema6 import schema_6
from schemas.schema11 import schema_11
from schemas.schema12 import schema_12
from schemas.schema13 import schema_13
from schemas.schema14 import schema_14
from schemas.schema15 import schema_15
from schemas.schema16 import schema_16
from schemas.schema17 import schema_17
from schemas.schema18 import schema_18
app = FastAPI()

class UserInput(BaseModel):
    user_text: str
    TemplateId: int

class TextRequest(BaseModel):
    text: str

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Define a root path to verify the server is running
@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")


def select_schema(template_id, user_text):
    schema_functions = {
        1: schema_1,
        2: schema_2,
        3:schema_3,
        4:schema_4,
        5:schema_5,
        6:schema_6,
        11:schema_11,
        12:schema_12,
        13:schema_13,
        14:schema_14,
        15:schema_15,
        16:schema_16,
        17:schema_17,
        18:schema_18

        
    }
    
    schema_function = schema_functions.get(template_id)
    if not schema_function:
        raise HTTPException(status_code=404, detail="Template ID not found")
    
    return schema_function(user_text)

@app.post("/generate-schema")
def generate_schema(user_input: UserInput):
    user_text = user_input.user_text
    template_id = user_input.TemplateId

    selected_schema = select_schema(template_id, user_text)
    return selected_schema

@app.post("/regenerate-text")
def regenerate_text(request: TextRequest):
    text = request.text
    return {"regenerated_text": generate_text(f"rewrite this text: {text}")}

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    import os
    uvicorn.run(app, host="localhost", port=int(os.environ.get("PORT", 8000)))

