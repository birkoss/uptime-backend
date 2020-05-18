API Endpoints
=============

POST */api/auth/login/*

*Parameters*
- email = string, required
- password = string, required

*Response*
Status: 200 OK
```
{
    "id": 1,
    "email": "email@domain.com",
    "is_active": true,
    "is_staff": false,
    "token": "*** HIDDEN ***"
}
```


POST */api/auth/register/*

*Parameters*
- email = string, required, unique
- password = string, required

*Response*
Status: 201 Created
```
{
    "id": 2
    "email": "email2@domain.com",
    "is_active": true,
    "is_staff": false,
    "auth_token": "*** HIDDEN ***"
}
```


POST */api/auth/change_password/*

*Parameters*
- current_password = string, required, match current password
- new_password = string, required

*Response*
Status: 204 No-Content

