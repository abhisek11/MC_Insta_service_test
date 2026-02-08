from pydantic import BaseModel
from typing import Optional

class UploadResponse(BaseModel):
    image_id:str

class ImageMeta(BaseModel):
    image_id:str
    description:Optional[str]
    tags:Optional[str]
    created_at:str
