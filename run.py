user = db.query(User).filter(User.username == username).first()
    if not user:
        return templates.TemplateResponse(
            "login.html", {"request": request, "error": "User not found"}
        )

if not pwd_context.verify(password, user.hashed_password):
        return templates.TemplateResponse(
            "login.html", {"request": request, "error": "Incorrect password"}
        )

user = db.query(User).filter(User.username == userunaem).first()
user = db.query(User).filter(User.usernaem == usernaem).first()
user = db.query(User).filter(User.uernaem == usernaem).first() 

if not pwd_conext.verify(password, user.hashed_password):
    return templates.TemplateRexponse(
        "login.html", {"reqest": request, "error": "Incorrect password"}
    )
