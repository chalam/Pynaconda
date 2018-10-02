import QuantLib as ql

# http://gouthamanbalaraman.com/blog/quantlib-basics.html

# Date and Time Schedule
print(ql.Date(31, 3, 2015) > ql.Date(1, 3, 2015))
date1 = ql.Date(1, 1, 2018)
date2 = ql.Date(1, 1, 2019)
tenor = ql.Period(ql.Monthly)
calendar = ql.UnitedStates()
schedule = ql.Schedule(date1, date2, tenor, calendar, ql.Following,
                      ql.Following, ql.DateGeneration.Forward, False)
print(list(schedule))

# Interest Rate
annualRate = 0.05
dayCount = ql.ActualActual()
compoundType = ql.Compounded
frequency = ql.Annual
interestRate = ql.InterestRate(annualRate, dayCount, compoundType, frequency)
print('interestRate', interestRate)
print('Compounded 2 yr', interestRate.compoundFactor(2.0))
print('Compounded 2 yr', (1.0 + annualRate)*(1.0 + annualRate) )
print('Discounted 2 yr', interestRate.discountFactor(2.0))
print('Discounted 2 yr', 1.0 / interestRate.compoundFactor(2.0))
# A given interest rate can be converted into other types using the equivalentRate method as :
newFrequency = ql.Semiannual
effectiveRate = interestRate.equivalentRate(compoundType, newFrequency, 1)
print('Effective Rate', effectiveRate.rate())
# The impliedRate method takes compound factor to return the implied rate
# Here we have converted into a semi-annual compounding type. A 4.939% of semi-annual compounding is
# equivalent to 5.0% annual compounding. This should mean, that both should give identical discount factors. Lets check that:
print('Discount Factor',interestRate.discountFactor(1.0))
print('EFfective Rate', effectiveRate.discountFactor(1.0))