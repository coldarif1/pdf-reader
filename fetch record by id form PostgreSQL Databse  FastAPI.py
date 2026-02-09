16. fetch record by id form PostgreSQL Databse | FastAPI

@app.get("course/{id}")
def get_course(id:int):
    cursor.execute("""Select * From course Where id = %s """, (str(id),))
    course = cursor.fetchone()
    if not course:
        raise HTTPExcption(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Course with id:{id} was not found"
        )
return{"Course_detail": course}


app.put("/couser_name/{id}")
def update_a_cousrse(id:int, update_corse: Course, db:session=Depens(get_db)):
    course_query = db.query(modedels.Course).filter(models.Course. id==id)
    course = course_quer.filter()
    if not course:
        raise HTTPExcption (status_code=sastus.HTTP_404_not_Found=f"course with id: {id} dose not exist")
    update_date = update_couser.model_dump()
    update_date["wesite"] = str(updtae_date[website]
                                )



#define requset body schema
#define request body schema
#define body schema

class Course course (BaseModel):
    name: str
    instructo: str
    duration: float
    website: HttpUrl
    #inpoint n function




