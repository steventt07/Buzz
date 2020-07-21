CREATE TABLE IF NOT EXISTS comment (
	comment_id SERIAL PRIMARY KEY,
	username VARCHAR(256) REFRENCES user,
	commnet TEXT
);

CREATE INDEX inx_comment_id_1 on comment(comment_id)