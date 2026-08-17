DROP TABLE IF EXISTS appointment CASCADE;
DROP TABLE IF EXISTS chatting CASCADE;
DROP TABLE IF EXISTS disease_info CASCADE;
DROP TABLE IF EXISTS doctor CASCADE;
DROP TABLE IF EXISTS users CASCADE;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(100),
    user_email VARCHAR(100),
    password VARCHAR(100),
    user_phone VARCHAR(100),
    user_addr VARCHAR(100)
);


CREATE TABLE doctor (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100),
    age VARCHAR(100),
    gender VARCHAR(100),
    hospital_name VARCHAR(100),
    address VARCHAR(100),
    exp_type VARCHAR(100),
    mobile VARCHAR(100)
);


CREATE TABLE disease_info (
    id SERIAL PRIMARY KEY,
    pname VARCHAR(100),
    email VARCHAR(100),
    age VARCHAR(100),
    gender VARCHAR(100),
    smoking VARCHAR(100),
    days VARCHAR(100),
    infection VARCHAR(100),
    bmi VARCHAR(100),
    image VARCHAR(100),
    disease VARCHAR(100),
    severity VARCHAR(100),
    causes TEXT,
    remedies TEXT,
    date VARCHAR(100),
    time VARCHAR(100)
);


CREATE TABLE chatting (
    id SERIAL PRIMARY KEY,
    sender_email VARCHAR(100),
    receiver_email VARCHAR(100),
    chat_date VARCHAR(100),
    chat_time VARCHAR(100),
    msg VARCHAR(100),
    patient_name VARCHAR(100),
    patient_email VARCHAR(100),
    doctor_email VARCHAR(100)
);


CREATE TABLE appointment (
    id SERIAL PRIMARY KEY,
    pname VARCHAR(100),
    pemail VARCHAR(100),
    age VARCHAR(100),
    gender VARCHAR(10),
    bmi VARCHAR(100),
    infection VARCHAR(100),
    smoking VARCHAR(100),
    days VARCHAR(100),
    image VARCHAR(100),
    disease VARCHAR(100),
    severity VARCHAR(100),
    date VARCHAR(100),
    time VARCHAR(100),
    hname VARCHAR(100),
    address VARCHAR(100),
    dname VARCHAR(100),
    demail VARCHAR(100),
    accepted_date VARCHAR(100) DEFAULT 'Not updated',
    status VARCHAR(100) DEFAULT 'pending',
    feedback TEXT
);