
import os
from supabase import create_client, Client

x: str = os.environ.get("https://vohvbmlpnjkadszsdajy.supabase.co")
y: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZvaHZibWxwbmprYWRzenNkYWp5Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxOTg0MTk5NiwiZXhwIjoyMDM1NDE3OTk2fQ.xK7BopIgFl77HSPGNrYOtYd_BP7Lq97oMFRTl3FOIUY")
supabase: Client = create_client(x, y)



response = supabase.table("Libary").select("*").execute()
print('test11')
print(response)