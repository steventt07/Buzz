CREATE TABLE IF NOT EXISTS buzz (
	buzz_id SERIAL PRIMARY KEY,
	username VARCHAR(256) REFRENCES user,
	comment_ids INTEGER[],
	content TEXT,
	zipcode varchar(256),
	date_created DATE,
	votes INTEGER,
);

CREATE INDEX inx_buzz_id_1 on buzz(buzz_id)