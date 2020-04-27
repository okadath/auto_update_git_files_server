para ignorar la salida estandar y prevenir que el archivo se apague, aunque habra que reiniciarlo con cada commit, quiza baste con un comando de AWS-EB
```python
nohup python3 autocommit.py  > logs_commit.txt &

```