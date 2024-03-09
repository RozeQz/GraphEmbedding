DROP DATABASE planared;

CREATE DATABASE planared;

COMMENT ON DATABASE planared IS 'Diploma';

\c planared

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'WIN1251';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

CREATE TABLE "Users_data" (
  "id" serial,
  "firstname" varchar(32) NOT NULL,
  "lastname" varchar(32) NOT NULL,
  "midname" varchar(32),
  "email" varchar(64) NOT NULL,
  PRIMARY KEY ("id")
);

CREATE TABLE "Users" (
  "id" serial,
  "login" varchar(32) NOT NULL UNIQUE,
  "password" char(64) NOT NULL,
  "user_data_id" int NOT NULL UNIQUE,
  PRIMARY KEY ("id"),
  CONSTRAINT "FK_User.user_data_id"
        FOREIGN KEY ("user_data_id")
            REFERENCES "Users_data"("id")
);

CREATE TABLE "Groups" (
    "id" serial,
    "name" varchar(32) NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "Users_Groups" (
    "id" serial,
    "user_id" int NOT NULL,
    "group_id" int NOT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT "FK_Users_Group.user_id"
        FOREIGN KEY ("user_id")
            REFERENCES "Users"("id"),
    CONSTRAINT "FK_Users_Group.group_id"
        FOREIGN KEY ("group_id")
            REFERENCES "Groups"("id")
);

CREATE TABLE "Tasks" (
    "id" serial,
    "question" varchar(128) NOT NULL,
    "answer" varchar(128) NOT NULL,
    "type" int NOT NULL,
    "options" varchar(512) NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "Tests" (
    "id" serial,
    "name" varchar(128) NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "Tasks_Tests" (
    "id" serial,
    "test_id" int NOT NULL,
    "task_id" int NOT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT "FK_Tasks_Test.test_id"
        FOREIGN KEY ("test_id")
            REFERENCES "Tests"("id"),
    CONSTRAINT "FK_Tasks_Test.task_id"
        FOREIGN KEY ("task_id")
            REFERENCES "Tasks"("id")
);

CREATE TABLE "Results" (
    "id" serial,
    "user_id" int NOT NULL,
    "test_id" int NOT NULL,
    "points" float NOT NULL,
    "answres" json,
    PRIMARY KEY ("id"),
    CONSTRAINT "FK_Result.user_id"
        FOREIGN KEY ("user_id")
            REFERENCES "Users"("id"),
    CONSTRAINT "FK_Result.test_id"
        FOREIGN KEY ("test_id")
            REFERENCES "Tests"("id"),
    CHECK ("points" >= 0),
);

\c postgres
