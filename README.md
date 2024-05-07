# RestAPI 

## Endpoints

- `GET /tasks/`: provide a list of stored tasks.
- `GET /tasks/{task_id}`: get the task by ID.
- `POST /tasks/`: create a new task.
- `PUT /tasks/{task_id}`: update the task by ID.
- `DELETE /tasks/{task_id}`: delete the task by ID.

## Error Handling

- `404 Not Found`: Task not found.
- `201 Created`: Task has been Created.
- `400 Bad Request`: ID already exist.
- `204 No Content`: Task has been Successfully deleted.
