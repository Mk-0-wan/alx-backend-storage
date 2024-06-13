-- Creating Multi-Indexing mode for even faster data lookup
CREATE INDEX idx_name_first_score ON names (SUBSTRING(name, 1, 1), score));
