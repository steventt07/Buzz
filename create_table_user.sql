CREATE TABLE IF NOT EXISTS user (
	username VARCHAR(256) PRIMARY KEY,
	password VARCHAR(256),
	date_joined DATE
);