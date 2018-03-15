# Game server

## processing communication

message format

```python
class msg(object):
    '''
    id: int: msg send to room id
	src: str: whom msg's from, 'client' or 'arena' or any other
	data: dict: msg data
    '''
    def __init__(self, id, src, data):
        self.id = id
        self.src = src
        self.data = data
```





## inner protocol

进程间通信协议，在实例一个 msg 时，msg.src = 'arena'，msg.data 格式为：

```python
{
    "cmd": "cmd" # "add guest",...
    "data": "any data"
}
```

### new guest

To Room
```python
{
    "cmd": "add guest",
    "data": {
        "userId": 12345
    }
}
```
Room 回信时也要吧 msg.src 设置成发信方，比如 new guest 成功后的反馈， msg.src == 'arena'


## protocol with client
