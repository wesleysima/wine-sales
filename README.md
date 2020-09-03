# WINE-SALES

### Pré-requisitos

```
docker
```

```
docker-compose
```

### Iniciar projeto em desenvolvimento.

Entre na pasta raiz do projeto e builde o container:

```
docker-compose build
```

Após o build estar finalizado, suba o container:

```
docker-compose up -d
```

Se quiser derrubar o container:

```
docker-compose down -d
```

### Para ver os logs do api:.

```
docker logs -f --tail 100 wine-sales
```

### Para acessar o container:

```
docker exec -it wine-sales sh
```

### Documentação simplificada API:

* **Listar os clientes ordenados pelo maior valor total em compras:** 

```
http://localhost:5600/clients/sort-by-total-purchases
```

* **Mostar o cliente com a maior compra única em 2016:** 

```
http://localhost:5600/clients/biggest-single-purchase
```

* **Listar os cliente mais fiéis:** 

```
http://localhost:5600/clients/list-faithful-clients
```

* **Recomendar um vinho para um determinado cliente:** 

```
http://localhost:5600/clients/${IdCliente}/wine-recommendation
```
    
## Author

* **Wesley Sima** 



