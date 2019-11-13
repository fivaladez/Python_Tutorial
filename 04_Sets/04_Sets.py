# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})  # {3, 4, 5}
{1, 2, 3, 4, 5} & {3, 4, 5, 6}  # {3, 4, 5}
# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6})  # {1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5} | {3, 4, 5, 6}  # {1, 2, 3, 4, 5, 6}
# Difference
{1, 2, 3, 4}.difference({2, 3, 5})  # {1, 4}
{1, 2, 3, 4} - {2, 3, 5}  # {1, 4}
# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5})  # {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5}  # {1, 4, 5}
# Superset check
{1, 2}.issuperset({1, 2, 3})  # False
{1, 2} >= {1, 2, 3}  # False
# Subset check
{1, 2}.issubset({1, 2, 3})  # True
{1, 2} <= {1, 2, 3}  # True
# Disjoint check
{1, 2}.isdisjoint({3, 4})  # True
{1, 2}.isdisjoint({1, 4})  # False

# Existence check
2 in {1, 2, 3}  # True
4 in {1, 2, 3}  # False
4 not in {1, 2, 3}  # True
# Add and Remove
s = {1, 2, 3}
s.add(4)  # s == {1,2,3,4}
s.discard(3)  # s == {1,2,4}
s.discard(5)  # s == {1,2,4}
s.remove(2)  # s == {1,4}
s.remove(2)  # KeyError!
