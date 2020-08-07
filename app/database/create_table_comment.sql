CREATE TABLE IF NOT EXISTS comment_table(
	comment_id SERIAL PRIMARY KEY,
	username VARCHAR(256) REFERENCES user_table,
	content TEXT,
	date_created DATE
);

CREATE INDEX inx_comment_id_1 on comment_table(comment_id)