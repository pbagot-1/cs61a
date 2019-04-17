CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
   SELECT name, size from dogs, sizes where height > min and height <= max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
    SELECT distinct a.child from parents as a, dogs as b where a.parent = b.name order by -b.height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as col1, b.child as col2 from parents as a, parents as b where b.parent = a.parent and a.child < b.child;

-- Sentences about siblings that are the same size

CREATE TABLE helper AS
SELECT col1, col2, a.size as size1, b.size as size2 from siblings, size_of_dogs as a ,size_of_dogs as b where a.size = b.size and a.name = col1 and b.name = col2 order by col1;

CREATE TABLE sentences AS
SELECT col1 || " and " || col2 || " are " || size1 || " siblings" FROM helper;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);


-- Add your INSERT INTOs here
INSERT INTO stacks_helper SELECT name as name, height as height, height as lastheight from dogs;

INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height from stacks_helper as a, dogs as b where a.last_height < b.height;
INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height from stacks_helper as a, dogs as b where a.last_height < b.height;
INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT a.dogs || ", " || b.name, a.stack_height + b.height, b.height from stacks_helper as a, dogs as b where a.last_height < b.height;

CREATE TABLE stacks_unique AS
SELECT DISTINCT * from stacks_helper;

CREATE TABLE stacks AS
  SELECT dogs,stack_height from stacks_unique where stack_height >= 170 order by stack_height;
