
import random

subjects = [
    # Politics
    "The Prime Minister",
    "The Opposition Leader",
    "A Union Minister",
    "A Chief Minister",
    "A State Home Minister",
    "An Election Commission official",
    "A Parliament MP",
    "A Rajya Sabha member",
    "A political strategist",
    "A party spokesperson",

    # Sports
    "The Indian cricket team captain",
    "A former Indian cricketer",
    "An IPL team owner",
    "A star IPL player",
    "The Indian football team coach",
    "A national badminton champion",
    "An Olympic medalist",
    "A cricket commentator",
    "A team selector",
    "A sports federation president",
]

actions = [
    # Politics-style actions
    "announces",
    "suspends",
    "withdraws",
    "defends",
    "criticizes",
    "promises",
    "rejects",
    "approves",
    "postpones",
    "clarifies",

    # Sports-style actions
    "leads",
    "drops",
    "selects",
    "benches",
    "captains",
    "celebrates",
    "questions",
    "backs",
    "reviews",
    "appeals against",
]

places = [
    # Politics
    "inside Parliament",
    "at a press conference in Delhi",
    "during a Lok Sabha session",
    "at a political rally",
    "inside a state assembly",
    "outside the Supreme Court",
    "at the Election Commission office",

    # Sports
    "during an IPL match",
    "at Wankhede Stadium",
    "at Eden Gardens",
    "inside the team dressing room",
    "after a high-pressure final",
    "during a post-match interview",
    "at a packed national stadium",
]

while True:
  subject= random.choice(subjects)
  action= random.choice(actions)
  place= random.choice(places)

  headline = f" Breaking NEWS: {subject} {action} {place}"
  print("\n"+ headline)

  user = input("\n Do you want another headline (Yes/No)").strip().lower()
  if user == "no":
    break
print ("\n Goodbye")
