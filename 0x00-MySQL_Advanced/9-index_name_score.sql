-- Creating Multi-Indexing mode for even faster data lookup
CREATE INDEX idx_name_first_score ON names ((name(1)), (score(1)));
