from __future__ import division, print_function
import re
import itertools

# https://xkcd.com/1313/
# peter novig reimagines
# https://www.safaribooksonline.com/oriole/regex-golf-with-peter-norvig

def words(text): return set(text.split())

winners = words('''washington adams jefferson jefferson madison madison monroe 
    monroe adams jackson jackson van-buren harrison polk taylor pierce buchanan 
    lincoln lincoln grant hayes garfield cleveland harrison cleveland mckinley
    mckinley roosevelt taft wilson wilson harding coolidge hoover roosevelt 
    roosevelt roosevelt roosevelt truman eisenhower eisenhower kennedy johnson nixon 
    nixon carter reagan reagan bush clinton clinton bush bush obama obama''')

losers = words('''clinton jefferson adams pinckney pinckney clinton king adams 
    jackson adams clay van-buren van-buren clay cass scott fremont breckinridge 
    mcclellan seymour greeley tilden hancock blaine cleveland harrison bryan bryan 
    parker bryan roosevelt hughes cox davis smith hoover landon willkie dewey dewey 
    stevenson stevenson nixon goldwater humphrey mcgovern ford carter mondale 
    dukakis bush dole gore kerry mccain romney''')

print(winners & losers)

losers = losers - winners

def mistakes(regex, winners, losers):
    "The set of mistakes made by this regex in classifying winners and losers."
    return ({"Should have matched: " + W
             for W in winners if not re.search(regex, W)} |
            {"Should not have matched: " + L
             for L in losers if re.search(regex, L)})

def verify(regex, winners, losers):
    assert not mistakes(regex, winners, losers)
    return True

xkcd = "bu|[rn]t|[coy]e|[mtg]a|j|iso|n[hl]|[ae]d|lev|sh|[lnd]i|[po]o|ls"

print(mistakes(xkcd, winners, losers))

alternative_losers = {'fillmore'} | losers - {'fremont'}

print(verify(xkcd, winners, alternative_losers))

def findregex(winners, losers, k=4):
    "Find a regex that matches all winners but no losers (sets of strings)."
    # Make a pool of regex parts, then pick from them to cover winners.
    # On each iteration, add the 'best' part to 'solution',
    # remove winners covered by best, and keep in 'pool' only parts
    # that still match some winner.
    pool = regex_parts(winners, losers)
    solution = []
    def score(part): return k * len(matches(part, winners)) - len(part)
    while winners:
        best = max(pool, key=score)
        solution.append(best)
        winners = winners - matches(best, winners)
        pool = {r for r in pool if matches(r, winners)}
    return OR(solution)

def matches(regex, strings):
    "Return a set of all the strings that are matched by regex."
    return {s for s in strings if re.search(regex, s)}

OR = '|'.join # Join a sequence of strings with '|' between them

def regex_parts(winners, losers):
    "Return parts that match at least one winner, but no loser."
    wholes = {'^' + w + '$'  for w in winners}
    parts = {d for w in wholes for p in subparts(w) for d in dotify(p)}
    return wholes | {p for p in parts if not matches(p, losers)}

def subparts(word, N=4):
    "Return a set of subparts of word: consecutive characters up to length N (default 4)."
    return set(word[i:i+n+1] for i in range(len(word)) for n in range(N))

def dotify(part):
    "Return all ways to replace a subset of chars in part with '.'."
    choices = map(replacements, part)
    return {cat(chars) for chars in itertools.product(*choices)}

def replacements(c): return c if c in '^$' else c + '.'

cat = ''.join

solution = findregex(winners, losers)
print(verify(solution, winners, losers))

print(len(solution), solution)


def tests():
    assert subparts('^it$') == {'^', 'i', 't', '$', '^i', 'it', 't$', '^it', 'it$', '^it$'}
    assert subparts('this') == {'t', 'h', 'i', 's', 'th', 'hi', 'is', 'thi', 'his', 'this'}
    subparts('banana') == {'a', 'an', 'ana', 'anan', 'b', 'ba', 'ban', 'bana',
                           'n', 'na', 'nan', 'nana'}

    assert dotify('it') == {'it', 'i.', '.t', '..'}
    assert dotify('^it$') == {'^it$', '^i.$', '^.t$', '^..$'}
    assert dotify('this') == {'this', 'thi.', 'th.s', 'th..', 't.is', 't.i.', 't..s', 't...',
                              '.his', '.hi.', '.h.s', '.h..', '..is', '..i.', '...s', '....'}
    assert regex_parts({'win'}, {'losers', 'bin', 'won'}) == {
        '^win$', '^win', '^wi.', 'wi.',  'wi', '^wi', 'win$', 'win', 'wi.$'}
    assert regex_parts({'win'}, {'bin', 'won', 'wine', 'wit'}) == {'^win$', 'win$'}
    regex_parts({'boy', 'coy'},
                {'ahoy', 'toy', 'book', 'cook', 'boycott', 'cowboy', 'cod', 'buy', 'oy',
                 'foil', 'coyote'}) == {'^boy$', '^coy$', 'c.y$', 'coy$'}

    assert matches('a|b|c', {'a', 'b', 'c', 'd', 'e'}) == {'a', 'b', 'c'}
    assert matches('a|b|c', {'any', 'bee', 'succeed', 'dee', 'eee!'}) == {
        'any', 'bee', 'succeed'}

    assert OR(['a', 'b', 'c']) == 'a|b|c'
    assert OR(['a']) == 'a'

    assert words('this is a test this is') == {'this', 'is', 'a', 'test'}

    assert findregex({"ahahah", "ciao"},  {"ahaha", "bye"}) == 'a.$'
    assert findregex({"this", "that", "the other"}, {"one", "two", "here", "there"}) == 'h..$'
    assert findregex({'boy', 'coy', 'toy', 'joy'}, {'ahoy', 'buy', 'oy', 'foil'}) == '^.oy'

    assert not mistakes('a|b|c', {'ahoy', 'boy', 'coy'}, {'joy', 'toy'})
    assert not mistakes('^a|^b|^c', {'ahoy', 'boy', 'coy'}, {'joy', 'toy', 'kickback'})
    assert mistakes('^.oy', {'ahoy', 'boy', 'coy'}, {'joy', 'ploy'}) == {
        "Should have matched: ahoy",
        "Should not have matched: joy"}
    return 'tests pass'

tests()

def report(winners, losers):
    "Find a regex to match A but not B, and vice-versa.  Print summary."
    solution = findregex(winners, losers)
    verify(solution, winners, losers)
    trivial  = '^(' + OR(winners) + ')$'
    print('Characters: {}, Parts: {}, Competitive ratio: {:.1f}, Winners: {}, Losers: {}'.format(
          len(solution), solution.count('|') + 1, len(trivial) / len(solution) , len(winners), len(losers)))
    return solution

print(report(winners, losers))

boys  = words('jacob mason ethan noah william liam jayden michael alexander aiden')
girls = words('sophia emma isabella olivia ava emily abigail mia madison elizabeth')

print(report(boys, girls))

drugs = words('lipitor nexium plavix advair ablify seroquel singulair crestor actos epogen')
cities = words('paris trinidad capetown riga zurich shanghai vancouver chicago adelaide auckland')

print(report(drugs, cities))

def phrases(text, sep='/'): return {line.upper().strip() for line in text.split(sep)}

starwars = phrases('''The Phantom Menace / Attack of the Clones / Revenge of the Sith /
                      A New Hope / The Empire Strikes Back / Return of the Jedi''')

startrek = phrases('''The Wrath of Khan / The Search for Spock / The Voyage Home /
                      The Final Frontier / The Undiscovered Country / Generations / 
                      First Contact / Insurrection / Nemesis''')

print(report(starwars, startrek))


