from js import document

def display_info(event=None):
    name = document.getElementById("name").value.strip()
    age = document.getElementById("age").value.strip()
    school = document.getElementById("school").value.strip()
    if not name or not age or not school:
        message = "Please fill in all fields."
    else:
        message = f"""{name} is {age} years old and studies at {school}. This message was generated through input fields and displayed using a multiline string in Python via Pyscript."""

    # innerText to preserve line breaks in most browsers
    document.getElementById("output").innerText = message

def clear_content(event=None):
    for field in ["output", "name", "age", "school"]:
        element = document.getElementById(field)
        if field == "output":
            element.innerText = ""
        else:
            element.value = ""