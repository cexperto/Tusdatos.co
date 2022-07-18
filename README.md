
# Tusdatos.co

project challenge for Tusdatos.co


option:
For do more easy process execute:

./cli 

When the server already runing yo can pass to step 5 and 7 ignore 6 step


1. clone this repo
2. get in folder
3. run:

python -m venv venv

source venv/scripts/activate


pip install -r requirements.txt


python manage.py runserver

4. run 
python manage.py makemigrations
python manage.py migrate

5. create user, run:
python manage.py createsuperuser

insert username

example: 

username: admin

email: admin@mail.com

password: password

In the browser insert your credentials:
http://localhost:8000/admin/

6. Now you have to run the scraper
run:

cd ecommerce/

Run command:

scrapy crawl allinone

7. In the browser:
http://localhost:8000/df/











## API Reference

#### login

```http
  GET /admin/
  http://localhost:8000/admin/
```
#### logout

```http
  GET /admin/logout/
  http://localhost:8000/admin/logout/
```

#### insert data in DB

```http
  GET /df/
  http://localhost:8000/df/
```


#### Get all items

```http
  GET /products/
  http://localhost:8000/products/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `products` | `string` | **Required**. |

#### Get item

```http
  GET /products/<id>/
  example:
  http://localhost:8000/products/1/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |

#### Get items order by field

```http
  GET /products/<string>
  example:
  http://localhost:8000/products/order/index/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `field`      | `string` | **Required**. field name for order by field, |

list values avalibles 'index', 'titles', 'categories', 'price', 'description', 'images', 'reviews', 'ratings'

## Authors

- [@cexperto](https://github.com/cexperto)


## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

