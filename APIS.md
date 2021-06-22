## create auth token
GET:  /api/token/
```
{
    "username": <str>, 
    "password": <str>
}
```

RESPONSE: 
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNDQyNTE1MCwianRpIjoiNzQzMzAyNDM3ODkzNGVhZmJiZDU2Mjg5OWZjMTU3ODQiLCJ1c2VyX2lkIjoxfQ.L2MTJOCAabOjknxHV1nFo7uO2BmG3SZkwTNK2BqIOuo",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0MzM5MDUwLCJqdGkiOiJiMzg0ZGM1MjU5MWI0ZmQ2ODNlZDA5MTMyYjMwNzNhYyIsInVzZXJfaWQiOjF9.Ls0PcH4xSQ8t9O5mZQmJsbMCWMDvEG35OGKmmaYt958"
}
```


* Pass access token for all below requests:
* HEADER: `Authorization: Bearer access_token`


## List Tasks:
GET: /tasks/

## Task Details
GET: /tasks/{task-id}/

## Create Task
POST: /tasks/
```
{
    "title": "test task",
    "description": "this is test task",
    "task_date": "2021-06-22T00:52:00Z",
    "status": "pending"
}
```

## Update Task
PUT: /tasks/{task-id}/
```
{
    "title": "test task",
    "description": "this is test task",
    "task_date": "2021-06-22T00:52:00Z",
    "status": "pending"
}
```

## Delete Task
DELETE: /tasks/{task-id}/

## Complete Task
PUT: /tasks/{task-id}/complete_task/

## Assign Task
PUT: /tasks/{task-id}/assign_user/
```
{
	"assigned_to":1
}
```




