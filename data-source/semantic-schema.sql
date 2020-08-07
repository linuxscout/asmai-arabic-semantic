CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE "derivations" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE ,
 "verb" varchar NOT NULL , "transitive" BOOL NOT NULL  DEFAULT 1,
 "derived" VARCHAR NOT NULL , "type" VARCHAR NOT NULL );
;
CREATE TABLE "relations" ("id" INTEGER PRIMARY KEY  NOT NULL ,"first" VARCHAR NOT NULL  DEFAULT ('') ,"second" VARCHAR NOT NULL  DEFAULT ('') ,"rule" VARCHAR NOT NULL  DEFAULT (0) );
CREATE INDEX "idx_derived" ON "derivations" ("derived" ASC);
CREATE INDEX "idx_relation" ON "relations" ("first" ASC, "second" ASC);
