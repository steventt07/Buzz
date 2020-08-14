CREATE TABLE IF NOT EXISTS comment_table(
	comment_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	username VARCHAR(256) REFERENCES user_table,
	content TEXT,
	date_created DATE
);