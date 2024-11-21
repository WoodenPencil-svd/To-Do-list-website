from dataclasses import dataclass

@dataclass
class Task:
    #id = int 
    name:str
    description:str
    user_id:int
    status:str
    # created_at = datetime
    # updated_at = datetime
    