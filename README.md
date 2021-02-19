Flask Blue Print Demo

### Author

- Jclian91

### Code Structure

```
/flask
├── /view
│   └── api.py
│   └── api_redis.py
├── /static
└── main.py
```

### Start Log

```
--> Map([<Rule '/redis/show' (GET, OPTIONS, HEAD) -> app_redis.show>,
 <Rule '/new/app2' (GET, OPTIONS, HEAD) -> app2.show>,
 <Rule '/test' (GET, OPTIONS, HEAD) -> test>,
 <Rule '/' (GET, OPTIONS, HEAD) -> index>,
 <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>])
```