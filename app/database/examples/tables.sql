CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS user_table(
	username VARCHAR(256) PRIMARY KEY,
	password VARCHAR(256) NOT NULL,
	date_joined DATE
);

CREATE TABLE IF NOT EXISTS category_table(
	category_name VARCHAR(256) PRIMARY KEY,
	owner_username VARCHAR(256) REFERENCES user_table,
	date_created DATE
);

CREATE TABLE IF NOT EXISTS comment_table(
	comment_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	username VARCHAR(256) REFERENCES user_table,
	content TEXT,
	date_created DATE
);

CREATE TABLE IF NOT EXISTS post_table(
	post_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	username VARCHAR(256) REFERENCES user_table,
	category_name VARCHAR(256) REFERENCES category_table,
	comment_ids INTEGER[],
	title varchar(256),
	content TEXT,
	zipcode varchar(256),
	date_created DATE,
	up_vote INTEGER DEFAULT 0,
	down_vote INTEGER DEFAULT 0,
	is_deleted BOOLEAN DEFAULT false,
	is_reported BOOLEAN DEFAULT false,
	is_edited BOOLEAN DEFAULT false,
	date_edited DATE
);