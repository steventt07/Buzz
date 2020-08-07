CREATE TABLE IF NOT EXISTS post_table(
	post_id SERIAL PRIMARY KEY,
	username VARCHAR(256) REFERENCES user_table,
	category_name VARCHAR(256) REFERENCES category_table,
	comment_ids INTEGER[],
	content TEXT,
	zipcode varchar(256),
	date_created DATE,
	votes INTEGER DEFAULT 0,
	is_deleted BOOLEAN DEFAULT false,
	is_reported BOOLEAN DEFAULT false,
	is_edited BOOLEAN DEFAULT false,
	date_edited DATE
);

CREATE INDEX inx_post_id_1 on post_table(post_id)