import datetime

# Condtions class. Keeps column to which condition should be applied,
# the function that applies the conditions and the operands involved.
class Condition(object):

    def __init__(self, column, predicate, operands) -> None:
        self.column = column
        self.predicate = predicate
        self.operands = operands

    def apply_condition(self, row):
        if len(self.operands) == 1:
            return self.predicate(row[self.column], self.operands[0])
        elif len(self.operands) == 2:
            return self.predicate(row[self.column], self.operands[0], self.operands[1])
        else:
            return self.predicate(row[self.column], self.operands)


# Table filter class. All condition functions return a TableFilter
# object to allow method chaining. The filter() function applies the
# conditions and returns the filtered table. It should be the last function
# called.
class TableFilter(object):

    def __init__(self, table) -> None:
        self.table = table
        self.conditions = []

    def between(self, value, value1, value2):
        return value1 < value < value2

    def lessThan(self, value, value1):
        return value < value1

    def greaterThan(self, value, value1):
        return value > value1

    def equalTo(self, value, value1):
        return value == value1

    def in_list(self, value, list):
        return value in list

    def not_in_list(self, value, list):
        return value not in list

    def withDateLessThan(self, date1):
        self.conditions.append(Condition(2, self.lessThan, [date1]))
        return self

    def withDateBetween(self, date1, date2):
        self.conditions.append(Condition(2, self.between, [date1, date2]))
        return self

    def withDateGreaterThan(self, date1):
        self.conditions.append(Condition(2, self.greaterThan, [date1]))
        return self

    def withDate(self, date):
        self.conditions.append(Condition(2, self.equalTo, [date]))
        return self

    def withIdLessThan(self, id1):
        self.conditions.append(Condition(0, self.lessThan, [id1]))
        return self

    def withIdBetween(self, id1, id2):
        self.conditions.append(Condition(0, self.between, [id1, id2]))
        return self

    def withIdGreaterThan(self, id1):
        self.conditions.append(Condition(0, self. greaterThan, [id1]))
        return self

    def withId(self, id1):
        self.conditions.append(Condition(0, self.equalTo, [id1]))
        return self

    def withIdIn(self, list):
        self.conditions.append(Condition(0, self.in_list, list))
        return self

    def withIdNotIn(self, list):
        self.conditions.append(Condition(0, self.not_in_list, list))
        return self

    def withUrl(self, url):
        self.conditions.append(Condition(1, self.equalTo, [url]))
        return self

    def withRatingLessThan(self, rating1):
        self.conditions.append(Condition(3, self.lessThan, [rating1]))
        return self

    def withRatingBetween(self, rating1, rating2):
        self.conditions.append(Condition(3, self.between, [rating1, rating2]))
        return self

    def withRatingGreaterThan(self, rating1):
        self.conditions.append(Condition(3, self.greaterThan, [rating1]))
        return self

    def withRating(self, rating1):
        self.conditions.append(Condition(3, self.equalTo, [rating1]))
        return self

    def filter(self):
        result = []
        for entry in self.table:
            conditions_satisfied = True
            for condition in self.conditions:
                conditions_satisfied = conditions_satisfied and condition.apply_condition(entry)
            if conditions_satisfied:
                result.append(entry)
        return result

# Example usages

table = [[1, "www.testurl.com", datetime.datetime(2018,1, 7), 7],
         [2, "www.testurl2.com", datetime.datetime(2017, 4, 5), 2],
         [3, "www.testurl.com", datetime.datetime(2018, 3, 12), 3]]
print(TableFilter(table).withUrl("www.testurl.com").filter())
print(TableFilter(table).withIdIn([1, 2, 5, 6]).withRatingBetween(1, 10).filter())
print(TableFilter(table).withDateBetween(datetime.datetime(2018, 1, 1), datetime.datetime(2018, 1, 3)).withIdLessThan(7).filter())