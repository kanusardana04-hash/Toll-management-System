# 🚧 Toll Entry Management System

## 📌 Project Overview

The **Toll Entry Management System** is a database management project developed using **Oracle Database 18c, SQL, and PL/SQL**.

The project is designed to manage vehicle entries at toll plazas, calculate toll charges according to vehicle categories, record payment transactions, and maintain an audit log of database activities.

It demonstrates how database concepts such as tables, primary keys, foreign keys, stored procedures, triggers, and transaction management can be implemented in a real-world toll management scenario.

## 🎯 Objectives

* Maintain vehicle information in a structured database.
* Store toll rates according to different vehicle categories.
* Manage multiple toll booths and their locations.
* Automatically calculate toll charges based on vehicle type.
* Record toll transactions and payment modes.
* Maintain an audit log for transaction activities.

## 🛠️ Technologies Used

| Technology           | Purpose                           |
| -------------------- | --------------------------------- |
| Oracle Database 18c  | Database Management               |
| SQL                  | Database operations and queries   |
| PL/SQL               | Stored procedures and triggers    |
| Oracle SQL Developer | Writing and executing SQL queries |

## ⚙️ Key Features

### 1. Vehicle Management

Stores vehicle information, including:

* Vehicle ID
* Vehicle Number
* Owner Name
* Vehicle Type

### 2. Toll Rate Management

Maintains toll charges for different vehicle categories.

| Vehicle Type | Toll Amount |
| ------------ | ----------: |
| Car          |        ₹100 |
| Bike         |         ₹40 |
| Truck        |        ₹250 |
| Bus          |        ₹180 |

### 3. Toll Booth Management

Stores toll plaza details, including booth name and location.

Sample locations:

* Kharar
* Mohali

### 4. Automatic Toll Calculation

The PL/SQL stored procedure `TOLL_ENTRY` automatically:

* Identifies the vehicle type.
* Fetches the corresponding toll rate.
* Creates a toll transaction.
* Generates a transaction ID.
* Displays transaction details.

### 5. Payment Management

Records payment modes associated with toll transactions.

Supported sample payment modes:

* Cash
* Card

### 6. Audit Logging

The database trigger `TOLL_AUDIT_TRIGGER` automatically maintains an audit record whenever a toll transaction is:

* INSERTED
* UPDATED
* DELETED

It stores the transaction ID, action type, date, and description.

## 🗄️ Database Structure

The project contains five main tables:

| Table Name        | Description                            |
| ----------------- | -------------------------------------- |
| VEHICLES          | Stores vehicle and owner details       |
| TOLL_RATES        | Stores toll charges by vehicle type    |
| TOLL_BOOTH        | Stores toll plaza information          |
| TOLL_TRANSACTIONS | Stores toll payment transactions       |
| AUDIT_LOG         | Maintains transaction activity records |

### Database Relationships

* `VEHICLES` is connected to `TOLL_TRANSACTIONS` through `VEHICLE_ID`.
* `TOLL_BOOTH` is connected to `TOLL_TRANSACTIONS` through `BOOTH_ID`.
* `AUDIT_LOG` stores transaction activity information.

## 🔄 Working Process

1. Vehicle details are registered in the VEHICLES table.
2. Toll rates are defined according to vehicle categories.
3. Toll booth information is stored in the database.
4. The `TOLL_ENTRY` procedure is executed with the vehicle ID, booth ID, and payment mode.
5. The procedure identifies the vehicle type and calculates the toll amount.
6. A new transaction is inserted into the TOLL_TRANSACTIONS table.
7. The audit trigger automatically records the transaction activity.
8. Transaction details and audit records can be viewed using SQL SELECT queries.

## 💻 Sample PL/SQL Execution

```sql
BEGIN
    TOLL_ENTRY(2, 1, 'CASH');
    COMMIT;
END;
/
```

This example processes a toll entry for vehicle ID 2 at toll booth ID 1 using cash payment.

The system retrieves the vehicle category and calculates the applicable toll amount automatically.

## 📊 SQL Concepts Implemented

This project demonstrates the following database concepts:

* CREATE TABLE
* INSERT INTO
* SELECT
* UPDATE
* PRIMARY KEY
* FOREIGN KEY
* UNIQUE and NOT NULL constraints
* Stored Procedures
* Database Triggers
* Exception Handling
* Autonomous Transactions
* COMMIT
* Identity Columns
* RETURNING INTO

## 🚀 How to Run the Project

1. Install Oracle Database 18c.
2. Open Oracle SQL Developer.
3. Connect to your Oracle database.
4. Open the project SQL notebook.
5. Execute the SQL statements in the given sequence.
6. Enable DBMS Output to view procedure messages.
7. Execute the `TOLL_ENTRY` procedure.
8. Run the SELECT queries to view the database records and audit logs.

**Note:** Execute the table creation and data insertion statements before creating and testing the stored procedure and trigger.

## 📁 Project File

`Toll management system.sqlnb`

The file contains the SQL and PL/SQL implementation of the Toll Entry Management System.

## 🎓 Learning Outcomes

Through this project, we explored:

* Relational database design and implementation.
* Data storage and management using Oracle SQL.
* Automation using PL/SQL stored procedures.
* Database activity tracking using triggers.
* Implementation of primary and foreign key relationships.
* Exception handling and transaction management.

## 🔮 Future Enhancements

The project can be extended with:

* A graphical user interface for toll operators.
* FASTag and online payment integration.
* Vehicle entry and exit tracking.
* Daily, weekly, and monthly revenue reports.
* Admin login and authentication.
* Real-time toll transaction monitoring.

## 👩‍💻 Project Information

**Project Name:** Toll Entry Management System
**Database:** Oracle Database 18c
**Languages:** SQL and PL/SQL
**Project Type:** Database Management System (DBMS) Mini Project

---

⭐ If you find this project useful, feel free to explore the code and learn from its implementation.
