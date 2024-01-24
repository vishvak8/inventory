create table customer(
    customer_id serial primary key,
    customer_name varchar(100),
    age numeric check(age>0 and age<100),
    email varchar(100) unique,
    cust_data timestamp default current_timestamp
);
insert into customer(customer_name,age,email) values('virat',35,'virat@gmail.com')
select * from customer
select customer_name,age from customer


create table product(
    product_id serial primary key,
    product_name varchar(100)
);

create table inventory(
    inventory_id serial primary key,
    product_id integer references product(product_id),
    quantity numeric check(quantity>=0),
    inventory_update timestamp default current_timestamp
);

create table invoice(
    invoice_id serial primary key,
    customer_id integer references customer(customer_id),
    product_id integer references product(product_id),
    quantity integer check(quantity>=0),
    price integer check (price>0),
    inv_date timestamp default current_timestamp
);

