from unittest import TestCase

# Assumption: Prices are always positive

def find_largest_loss(pricesLst):
    num_of_prices = len(pricesLst)
    min_so_far = pricesLst[num_of_prices - 1]
    max_loss = pricesLst[num_of_prices - 1] - pricesLst[num_of_prices - 2]
    for i in range(num_of_prices - 2, -1, -1):
        if min_so_far - pricesLst[i] < max_loss:
            max_loss = min_so_far - pricesLst[i]
        if pricesLst[i] < min_so_far:
            min_so_far = pricesLst[i]
    return max_loss

class TestFindLargestLoss(TestCase):
    def test_all_prices_equal(self):
        self.assertEqual(find_largest_loss(pricesLst=[1, 1, 1, 1, 1]), 0)

    def test_buying_with_max_price_does_not_give_max_loss(self):
        pricesLst = [4, 3, 1, 12, 11, 11, 11]
        self.assertEqual(find_largest_loss(pricesLst), -3)

    def test_selling_with_min_price_does_not_give_max_loss(self):
        pricesLst = [1, 2, 4, 10, 3]
        self.assertEqual(find_largest_loss(pricesLst), -7)

    def test_large_list_with_increasing_prices(self):
        pricesLst = []
        for i in range(1, 1000000):
            pricesLst.append(i)
        self.assertEqual(find_largest_loss(pricesLst), 1)

    def test_large_list_with_decreasing_prices(self):
        pricesLst = []
        for i in range(10000000, 0, -1):
            pricesLst.append(i)
        self.assertEqual(find_largest_loss(pricesLst), -9999999)
