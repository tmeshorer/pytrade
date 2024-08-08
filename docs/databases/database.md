- Rational db - collection of tables.
- Table - like a spread sheet
- Row = Entity
- Column = attribute of entity
- RDBMS - manage the data , plus security
- example of SQL:
```sql
select name FROM product WHERE price > 20
```
- SQL parts:
  -  SELECT - columns to retrieve
  -  FROM - specifiy the tables
  -  WHERE - condition on the query
- Operation:
  - Filtering - SQL WHERE
  ```sql
  SELECT * 
  FROM product 
  WHERE price < 30 AND 
  manufacturer = 'Mad Inventors Inc.';
  ```
  - Aggregation:
    - COUNT()
    - SUM()
    - AVG()
    - MAX()
    - MIN()
  - ```sql
    SELECT AVG(price) AS avg_price 
    FROM product 
    WHERE manufacturer = 'Mad Inventors Inc.';
    ```
  - GROUP BY
    ```sql
    SELECT COUNT(*) AS product_count, manufacturer
    FROM product
    GROUP BY manufacturer;
    ``` 
 DDL - Table manipulation
```sql
CREATE TABLE product (
  product_id INT PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  price DECIMAL(5, 2) NOT NULL,
  manufacturer TEXT NOT NULL
);
```

- Insert
  ```sql
  INSERT INTO table_name (column1, column2, ...)
  VALUES (value1, value2, ...);
  ```
  
  ```sql
   INSERT INTO product (product_id, name, description, price, manufacturer)
   VALUES (
      1,
      'Atomic Nose Hair Trimmer',
      'Trim your nose hairs... of an atomic clock!',
      19.99,
      'Mad Inventors Inc.'
   );
   ```
  
- Add column
  ```sql
  ALTER TABLE product
  ADD serial_number INT;
  ```
- change column type
  ```sql
  ALTER TABLE product
  ALTER COLUMN serial_number TEXT;
  ```
- remove table
  ```sql
  DROP TABLE product;
  ```
  
# Related Table
  
- `Product` and `Review` Table. Multiple review per product.
-  `product_id` Share by both. one is primary key , the other it is a the forighn key. 
- Join
  ```sql
  SELECT name, review_text
  FROM product 
  JOIN review
  ON product.product_id = review.product_id;
  ```
- General join syntax
  ```sql
    SELECT column1, column2, ...
    FROM table1
    JOIN table2
    ON table1.column = table2.column;
  ```
- If tables share the same name:
  ```sql
    SELECT employee.name, department.name
    FROM employee
    JOIN department
    ON employee.department_id = department.id;
  ```
  
- Type of join:
  - INNER_JOIN - rows with matching values in both tables
  - LEFT JOIN - all row from left , and matching row from right
  - RIGHT_JOIN - all rows from the right and matching from the left
  - FULL OUTER JOIN - all rows from left and right

```sql
SELECT name, review_text
FROM product 
LEFT JOIN review
ON product.product_id = review.product_i
```

```sql

4
5
6
7
8
9
10
11
12
  -- comment: works for MySQL and MariaDB
  -- comment: see the code repo for other RDBMS
CREATE TABLE review (
  review_id INT PRIMARY KEY,
  product_id INT NOT NULL,
  review_text TEXT NOT NULL,
  datetime DATETIME NOT NULL 
    DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_product_review
    FOREIGN KEY (product_id) 
    REFERENCES product (product_id)
);
```

## Database Design

1) Use singluar name
   User
   - username
   - email
   - password
   - first_name
   - last_name
   - phone_number
   - address
2) PK :
    - user table - email
    - product - code
    - review - review_id
    - payment_method - payment_method_id
    - purchase - purchase id
3) Datatype
   - Unifrom Length = CHAR. E.g. US STATE - CHAR(2)
   - Up to 500 charts = VARCHAR. E.g. Name VARCHAR(30)
   - TEXT
4) Int data types:
   - TINYINT
   - SMALLINT
   - INT
   - BIGINT
9) Float data type = DECIMAL (7,2) for example price
10) Datetime:
    - DATE - Only when data need to be store with no time information
    - TIME - Only when time needs to be stored
    - DATETIME - When both data and time needs to be stored.
    - TIMESTAMP - Exact moment across time zone

## Relationships
Relationship:   
    1) User can make multiple purchase
    2) User can review mulitple products
    3) User can have multiple payment methods
    4) Purchase can have more than one product

Between each entities
Cardinaltiy = the number of instances of B that a single instance of A can be associated with:
1) User has zero one or more accounts
2) Account has only one user

### Relationships
One to One:
1) Department and manager. manager_id in department. department_id in manager

One to Many
1) Purcahse has email field.

Many to May
1) Implemented in a sarugate table

 ### Normalization
Orginizing the database in a way that mimimize redundency. 
Normal Forms
- 1NF - Have primary key. Have no multi values column
- 2NF - In 1NF. All non key columns are dependend on the primary key
- 3NF - In 2NF, 