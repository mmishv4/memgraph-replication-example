[Документация](https://memgraph.com/docs/clustering/replication#set-up-a-replication-cluster)

http://localhost:3001/ - Memgraph Lab

`/usr/bin/mgconsole` для доступа к консоли

На обеих репликах:
```sql
SET REPLICATION ROLE TO REPLICA WITH PORT 10000;
```

Получить ip реплик 
```shell
docker ps 
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' CONTAINER ID
```

Регистрация реплик с мастера:
```sql
REGISTER REPLICA REP1 SYNC TO "172.17.0.3";
REGISTER REPLICA REP2 ASYNC TO "172.17.0.4";
```

Проверка на мастере:
```sql
SHOW REPLICAS;
```

