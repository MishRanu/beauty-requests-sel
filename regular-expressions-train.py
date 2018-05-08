import re

pattern = re.compile("\S*")
print(pattern.match("za2abc"))

pattern_star = re.compile("a*")
print(pattern_star.match("aaaabbb"))

pattern_star = re.compile("[a-c]*")
print(pattern_star.match("azaaabbbz"))

pattern_plus = re.compile("[a-c]+")
print(pattern_plus.match(""))
print(pattern_plus.match("abcddz"))

#first character here is ? says minimum is 0 and maximum is 1
pattern_question = re.compile("a?b")
print(pattern_question.match("aab"))
print(pattern_question.match("abc"))

# {m.n} = this qualifier means there must at least m repetitions, and at most n
pattern_curly = re.compile("a{2,4}")
print(pattern_curly.match("aaaaa"))

pattern_curly_zero = re.compile("a{0,}")
print(pattern_curly_zero.match("aaaaaaaaaz"))

pattern_start = re.compile("^abc")
print(pattern_start.match("zabc"))
print(pattern_start.match("abcz"))

# | chracter is the operator
pattern_or = re.compile("a|b")
print(pattern_or.match("a"))
print(pattern_or.match("b"))
print(pattern_or.match("cba"))

# $ matches the end of line
pattern_and = re.compile("abc$")
print(pattern_and.match("c"))
print(pattern_and.match("abccc"))
print(pattern_and.match("abc"))