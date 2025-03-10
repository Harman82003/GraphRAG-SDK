from openai import OpenAI
from .models.openai import OpenAiGenerativeModel
from graphrag_sdk.fixtures.prompts import (
    CREATE_ONTOLOGY_SYSTEM,
    CREATE_ONTOLOGY_PROMPT,
    FIX_ONTOLOGY_PROMPT,
    FIX_JSON_PROMPT,
    BOUNDARIES_PREFIX,
)


class Ontologycreate(OpenAiGenerativeModel):
 
 def OCR(self,file:str):
    client=OpenAI(api_key=self.api_key,base_url=self.base_url)
    completion1 = client.chat.completions.create(
        model=self.model_name,
        messages=[
            {"role":"user","content":file},
            {"role": "user", "content": str(CREATE_ONTOLOGY_SYSTEM)}
        ]
    )
    draft_onto=str(completion1.choices[0].message.content)
    completion2 = client.chat.completions.create(
        model=self.model_name,
        messages=[
            {"role":"user","content":file},
            {"role":"user","content":draft_onto},
            {"role": "user", "content": str(FIX_ONTOLOGY_PROMPT)}
        ]
    )
    return completion2.choices[0].message.content




