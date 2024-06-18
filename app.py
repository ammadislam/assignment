from firebase_admin import credentials, firestore
from fastapi import FastAPI, Body, HTTPException, Query
from pydantic import BaseModel
from unittest.mock import patch
import uuid
import uvicorn
import firebase_admin


cred = credentials.Certificate("assignment-d43d0-firebase-adminsdk-63mo0-76ceb5b9ea.json")
firebase_app = firebase_admin.initialize_app(cred)
db = firestore.client(firebase_app)
app = FastAPI()


def generate_unique_id():
  return str(uuid.uuid4())

class Person(BaseModel):
    id: str
    first_name: str
    last_name: str
    age: int
    # email: str

@app.post("/people")
async def create_person(person: Person = Body(...)):
    person.id = generate_unique_id()  # Generate ID before adding to Firestore
    db.collection("people").add(person.model_dump())
    if person.age < 0:
       raise HTTPException(status_code=400, detail=" Age can not be less than 0 ")
    
    doc_ref = db.collection("people").document()
    try:
       doc_ref.set(person.model_dump())
       return person
    except Exception as e:
       raise HTTPException(status_code=500, detail=f"Error saving person to Firestore: {e}")
    # return person

@app.get("/people")
async def get_people():
   people_ref = db.collection("people")
#    get all people
   docs = people_ref.get()
# convert docs to objects
   people = [Person(**doc.to_dict()) for doc in docs]
   return people


# @patch.object(firestore.Client, 'set')
# def test_create_person(self, mock_set):
#    person = Person(first_name="John", last_name="Doe", age=30)

# # call create_person function 
#    response = create_person(Person)

# # return value
#    assert response == person

# # verify firestore.set was called with correct date
#    mock_set.assert_called_once(person.model_dump())

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
