1. Clone the repository:

```bash
git clone https://github.com/your-username/your-project.git

cd your-project
python3 -m venv env
source env/bin/activate  # for Linux/Mac
env\Scripts\activate.bat  # for Windows

pip install -r requirements.txt

python manage.py runserver

Endpoints

    Endpoint for creating a task:
        URL: /tasks/
        Method: POST
        Description: Create a new task.
        Request Body: JSON data containing task details.

    Endpoint for viewing all tasks:
        URL: /tasks/
        Method: GET
        Description: Retrieve all tasks.

    Endpoint for viewing a single task:
        URL: /tasks/<task_id>/
        Method: GET
        Description: Retrieve details of a specific task.

    Endpoint for updating a task:
        URL: /tasks/<task_id>/
        Method: PUT
        Description: Update details of a specific task.

    Endpoint for deleting a task:
        URL: /tasks/<task_id>/
        Method: DELETE
        Description: Delete a specific task.

    Endpoint for filtering tasks by status:
        URL: /tasks/status/<status>/
        Method: GET
        Description: Retrieve tasks filtered by status (Pending, Completed, Canceled).