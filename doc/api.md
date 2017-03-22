# API
### Plugins
```python
class plugin_test:
	def __init__(self):
		pass

	def on_msg(self, bot, msg):
		text = msg.text
		return message(text, bot)
```

### Compare

```python
import compare
#compare a string to a pattern
compare.compare(input("text: "), [["hi", "hello", "hey"], ["bot", ""]])
```

#### Patterns
###### Simple Pattern
```python
["hi", "bot"]
```
- hi bot -> true
- hello -> false

###### Other Patterns
```python
[["hi", "hello"], "bot"]
```

- hi bot -> true
- hello bot -> true

```python
[["hi", "hello", ""], "bot"]
```

- hi bot -> true
- bot -> true
