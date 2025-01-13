from fastapi import FastAPI
from exercici3 import user_schema

app = FastAPI()

@app.get("/users")
async def users():
    return get_users()

def get_users():
    try:
        conn = Connection.get()
        cursor = conn.cursor()

        query = """
        SELECT
            name,
            lastName,
            email,
            description,
            course,
            year
        FROM User
        """

        cursor.execute(query)

        users = cursor.fetchall()

        return {"status": "ok", "users": [user_schema(u) for u in users]}
    except Exception as e:
        return {"status": "error", "error": e}
    finally:
        Connection.close()