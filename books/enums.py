class EnumBookRates:
    @staticmethod
    def _generate_book_rate(one_number):
        return (one_number, one_number)

    @staticmethod
    def book_rates():
        return tuple(map(EnumBookRates._generate_book_rate, range(0, 11)))
