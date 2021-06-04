# Product-api
API Rest para CRUD de produtos no banco relacional MySQL 5.7.
##
### Pré-requisitos
* Sistema Operacional Linux
* Minikube v1.13.0
* kubectl
##
### Bibliotecas de terceiros
* Foi utilizado o flask para agilizar requisitos da implantação da API via Python3 e o driver para conectar ao MySQL.
##
### Iniciando aplicação.

* Realize o git clone da aplicação:
```
git clone https://github.com/confelipe/projetohurb.git
```
* Após basta executar como administrador o script **run.sh**
```
sudo bash run.sh
```

**OBS.: Em alguns casos houve demora ao subir o container do MySQL(Devido aos requisitos do meu equipamento serem um pouco fraco para virtualização do minikube), o que ocasionou indisponibilidade da aplicação. O que se fez necessário derrubar o pod da api manualmente e assim ela voltar com conexão corretamente ao BD.**
##
### Rotas
```GET /api/products```

Retorna todos os itens cadastrados no formato JSON.

* Exemplo retorno:
```
{
​"totalCount"​: 1​,
  "items"​: [
    {
      ​"title": "Awesome socks"​,
      "sku"​: "SCK-4511"​,
      "barcodes"​: [​"7410852096307"​],
      ​"description"​: null​,
      ​"attributes"​: [
              {
      ​
                  "name"​: "color"​,
                  "value"​: "Red"​,
              },
              {
      ​            "name": "size"​,
                  "value"​: "39-41"​,
              },
          ],
          ​"price"​: "89.00"​,
    }
  ]
}
```

É possivel passar os argumentos abaixo via url para filtrar os resultados.

| Parâmetro | Descrição | Tipo | Default |
|---|---|---|---|
| start | Inicio do index | int | 0 |
| num | Numero de indexes retornados | int | 10 |
| sku | Filtrar por sku | string | --- |
| barcode | Filtrar por barcode | string |  |
| fields | Campos do produto que serão retornados da resposta | string, separado por vírgulas | --- |
##
```GET /api/products/<product_id>```
```GET /api/products/<sku>/sku```
```GET /api/products/<barcode>/barcode```

Todos os parametros são opcionais

| Parâmetro | Descrição | Tipo | Default |
|---|---|---|---|
| fields | Campos do produto que serão retornados da resposta | string, separado por vírgulas | --- |
##

```POST /api/products```

Os dados do post devem ser enviados no BODY do request conforme modelo abaixo.

Os campos <sku> e <title> são obrigátorios.

```
[
  {
      "title" : "Awesome Socks",
      "sku" : "SCK-4517",
      "barcodes" : 7410852096327,
      "description" : "Varias coisas sobre o item.....",
      "attributes" : [{
          "name" : "color",
          "value" : "red"
      },
      {
          "name" : "size",
          "value" : "37-42"
      }
      ],
      "price": 89.99
  }
]
```

* A API vai retornar o ID do item que foi cadastrado com o status code "201 Created"

```
22
```

##
```PUT /api/products/<product_id>```

Os dados do put devem ser enviados no BODY do request conforme modelo abaixo
Para essa parte não existem campos obrigatórios, porém <sku> ou <barcode> não podem conicidir coám itens já cadastrados pois são campos unicos.

```
[
  {
      "title" : "Awesome Socks",
      "sku" : "SCK-4517",
      "barcodes" : 7410852096327,
      "description" : "Varias coisas sobre o item.....",
      "attributes" : [{
          "name" : "color",
          "value" : "red"
      },
      {
          "name" : "size",
          "value" : "37-42"
      }
      ],
      "price": 89.99
  }
]
```

##

```DELETE /api/products/<product_id>```

Ao executar o metodo de delete, o mesmo retornara o status code "200 OK" em caso de sucesso.
Os atributos e barcode do item são removidos de forma recursiva.
