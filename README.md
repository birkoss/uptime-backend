API Endpoints
=============

POST */api/auth/login/*

*Parameters*
- email = string, required
- password = string, required

*Response*
Status: **200 OK**
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
Status: **201 Created**
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
Status: **204 No-Content**


GET */api/servers/*

*Response*
Status: **200 OK**
```
[
    {
        "id": 1,
        "hostname": "domain.com",
        "protocol": {
            "id": 1,
            "name": "HTTPS",
            "slug": "https"
        },
        "date_added": "2020-05-18T12:52:40.334790-04:00",
        "date_changed": "2020-05-18T12:52:40.334821-04:00",
        "is_active": true
    },
    {
        "id": 2,
        "hostname": "domain.ca",
        "protocol": {
            "id": 1,
            "name": "HTTPS",
            "slug": "https"
        },
        "date_added": "2020-05-18T18:37:31.783833-04:00",
        "date_changed": "2020-05-18T18:37:31.783866-04:00",
        "is_active": true
    }
]
```

protocols/

servers/1/endpoints/1/