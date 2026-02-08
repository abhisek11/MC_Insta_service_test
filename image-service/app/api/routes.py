from fastapi import APIRouter, UploadFile,File,Form,HTTPException
from app.services import s3_service, metadata_service

router=APIRouter()

@router.post("/images")
async def upload(user_id:str=Form(...),
                 description:str=Form(""),
                 tags:str=Form(""),
                 file:UploadFile=File(...)):

    data=await file.read()

    image_id,key=s3_service.upload_image(data,file.filename)
    metadata_service.save(user_id,image_id,key,description,tags)

    return {"image_id":image_id}


@router.get("/images")
def list_images(user_id:str,
                tag:str=None,
                text:str=None,
                limit:int=10):

    items,_=metadata_service.list(user_id,limit)

    if tag:
        items=[i for i in items if tag in i.get("tags","")]

    if text:
        items=[i for i in items if text in i.get("description","")]

    return items


@router.get("/images/{uid}/{iid}")
def download(uid:str,iid:str):

    item=metadata_service.get(uid,iid)
    if not item:
        raise HTTPException(404)

    url=s3_service.generate_download_url(item["s3_key"])
    return {"download_url":url}


@router.delete("/images/{uid}/{iid}")
def delete(uid:str,iid:str):

    item=metadata_service.get(uid,iid)
    if not item:
        raise HTTPException(404)

    s3_service.delete_image(item["s3_key"])
    metadata_service.delete(uid,iid)

    return {"deleted":True}
