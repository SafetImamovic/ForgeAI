import os
from dotenv import load_dotenv
from supabase import create_client, Client
from gotrue.errors import AuthApiError


load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

# data = (supabase
#         .table("todo")
#         .select("id, name")
#         .execute())

# data = (supabase
#         .table("todo")
#         .insert({"name": "Todo 2"})
#         .execute())

users_email: str = "safet.imamovic.22@size.ba"
users_password: str = "<PASSWORD>"
# user = supabase.auth.sign_up({"email": users_email, "password": users_password})

session = None

try:
        session = supabase.auth.sign_in_with_password({"email": users_email, "password": users_password})
except AuthApiError:
        print("Login failed")

print(session)

supabase.auth.sign_out()

# print(data)
