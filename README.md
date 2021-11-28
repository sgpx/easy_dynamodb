# easy_dynamodb

Simple and easy-to-use module for AWS DynamoDB. Simplify common AWS DynamoDB operations with helpful wrappers. Requires [`boto3`](https://pypi.org/project/boto3/).

- Get All items: Get all items in a table with `get_all_items()`.

- Get Table Item Counts: Calculate the number of items in a table with `count_all_items()`. DynamoDB table counts update approximately every 6 hours. `dynamodb_client.describe_table()` can return old counts which can cause problems.

- Create a table: Create a table simply with `create_table`. (See notes below)

---

### Examples

#### Get all items in a table (recursively work around 1 MB scan return limit)

```
import easy_dynamodb as edb
items = edb.get_all_items(table_name="my_table")
```

#### Count all items in a table

```
import easy_dynamodb as edb
item_count = edb.count_all_items(table_name="my_table")
```

### Create a table

```
import easy_dynamodb as edb

edb.create_table("my_table")
edb.create_table("my_second_table", hash_key="key1", range_key="key2")
```
### Delete a table

```
edb.delete_table("my_table")
```

### List all tables

```
edb.list_tables()
# returns a list of table names as output
# like ["my_table","my_second_table"]
```


---

### FAQ

Q: Why does `count_all_items_alt()` exist?

A: Curiosity. I wanted to check if there are inconsistencies with the `Count` provided in request results.

---

### TODO

- automatic marshalling

---

### notes

- `create_table` without any optional arguments creates a table with a default hash key name of `hash_key` ~~and default range key name `range_key`~~ with a default read/write capacity of 5. 
