import os
from dotenv import load_dotenv;
from supabase import create_client, Client

load_dotenv();

# Initialize Supabase client
SUPABASE_URL = os.environ.get("SUPABASE_URL")  # Replace with your Supabase URL
SUPABASE_KEY = os.environ.get("SUPABASE_KEY");  # Replace with your Supabase Key
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def register_user(email, password):
    try:
        response = supabase.auth.sign_up({
            'email': email,
            'password': password
        })
        return response
    except Exception as e:
        print(f"Error during registration: {e}")
        return None

def login_user(email, password):
    try:
        response = supabase.auth.sign_in_with_password({
            'email': email,
            'password': password
        })
        return response
    except Exception as e:
        print(f"Error during login: {e}")
        return None

def insert_prompt(user_id, prompt):
    try:
        response = supabase.table('prompts').insert({
            'prompt': prompt,
            'user_id': user_id
        }).execute()
        return response
    except Exception as e:
        print(f"Error inserting prompt: {e}")
        return None

def get_prompts():
    try:
        response = supabase.table('prompts').select('*').execute()
        return response.data
    except Exception as e:
        print(f"Error fetching prompts: {e}")
        return None

def main():
    logged_in_user = None

    while True:
        if logged_in_user is None:
            print("\n-- Not Logged In --")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                email = input("Enter email: ")
                password = input("Enter password: ")
                response = register_user(email, password)
                if response is not None:
                    print("Registration successful")
                else:
                    print("Registration failed")

            elif choice == '2':
                email = input("Enter email: ")
                password = input("Enter password: ")
                response = login_user(email, password)
                if response != None:
                    logged_in_user = response.user
                    print(f"Logged in as {logged_in_user.email}")
                else:
                    print("Login failed")

            elif choice == '3':
                print("Exiting...")
                supabase.auth.sign_out()
                break

            else:
                print("Invalid choice")

        else:
            print("\n-- Logged In --")
            print("1. Create Prompt")
            print("2. List Prompts")
            print("3. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                prompt = input("Enter your prompt: ")
                response = insert_prompt(logged_in_user.id, prompt)
                if response is not None:
                    print("Prompt added successfully")
                else:
                    print("Failed to add prompt")

            elif choice == '2':
                prompts = get_prompts()
                if prompts is not None:
                    for prompt in prompts:
                        print(prompt)
                else:
                    print("Failed to retrieve prompts")

            elif choice == '3':
                logged_in_user = None
                print("Logged out")

            else:
                print("Invalid choice")

if __name__ == "__main__":
    main()
    
    
    