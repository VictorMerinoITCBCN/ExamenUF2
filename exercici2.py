from fastapi import FastAPI
from exercici1 import User

app = FastAPI()

@app.post("/register")
async def register(user: User):
    add_user(user)

def add_user(user: User):
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        INSERT INTO User
            (name, lastName, email, description, course, year, postalCode, password)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            user.name,
            user.last_name,
            user.email,
            user.description,
            user.course,
            user.year,
            user.postal_code,
            user.password
        )

        cursor.execute(query, values)
        conn.commit()

        return {"status": "ok", "msg": "User created"}
    except Exception as e:
        return {"status": "error", "error": e}
    finally:
        Connection.close()