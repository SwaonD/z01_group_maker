projects = [
    "ascii-art",
    "ascii-art-fs",
    "ascii-art-output",
    "ascii-art-color",
    "ascii-art-web",
    "ascii-art-web-export-file",
    "ascii-art-web-dockerize",
    "ascii-art-web-stylize",
    "groupie-tracker"
]

def is_project(project_name: str):
    for p in projects:
        if p == project_name:
            return True
    return False