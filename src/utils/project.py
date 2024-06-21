import discord

projects = [
	"ascii-art",
	"ascii-art-web",
	"groupie-tracker",
 	"lem-in",
]

def is_project(project_name: str):
    for p in projects:
        if p == project_name:
            return True
        
    return False