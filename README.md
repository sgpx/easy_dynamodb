# easy_dynamodb

Helper functions to simplify common AWS DynamoDB operations. Requires [`boto3`](https://pypi.org/project/boto3/).

- Get All items: Get all items in a table with `get_all_items()`.

- Get Table Item Counts: Get the number of items in a table with `count_all_items()`. DynamoDB table counts update approximately every 6 hours. `dynamodb_client.describe_table()` can return old counts which can cause problems.

---

### Examples

#### Get all items in a table (recursively work around 1 MB scan return limit)

```
import easy_dynamodb as edb
print(edb.get_all_items(table_name="my-table"))
```

#### Count all items in a table

```
import easy_dynamodb as edb
print(edb.count_all_items(table_name="my-table"))
```

---

### FAQ

Q: Why does `count_all_items_alt()` exist?

A: Curiosity. I wanted to check if there are inconsistencies with the `Count` provided in request results.

---