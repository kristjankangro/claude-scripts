#!/usr/bin/env python3
# Parody inspirational quotes for Claude Code startup
# Hook: SessionStart
# Setup: Add to ~/.claude/settings.json under hooks.SessionStart:
#   { "type": "command", "command": "python ~/.claude/startup-quote.py" }
# Also add to ~/.claude/CLAUDE.md:
#   When a SessionStart hook provides a quote in the system context, always display it to the user at the beginning of the conversation.

import random

quotes = [
    '"The code is always greener on the other branch." - Ancient Git Proverb',
    '"Move fast and break things. Then spend 3 sprints fixing them." - Every Startup Ever',
    '"It works on my machine. Ship my machine." - Senior Developer, moments before disaster',
    '"A journey of a thousand bugs begins with a single \'it should be a quick fix\'." - Confucius.js',
    '"Be the semicolon someone forgot to add." - CSS Guru',
    '"In the middle of difficulty lies opportunity... to blame the intern." - Albert Einstacktrace',
    '"The only thing we have to fear is fear itself. And merge conflicts." - Franklin D. Refactorevelt',
    '"Ask not what your codebase can do for you, ask why there are no tests." - John F. Dependency',
    '"That which does not kill the build makes it stronger. Except memory leaks." - Friedrich Nietznode',
    '"To be, or not to be... null. That is the NullReferenceException." - Shakesbug',
    '"I think, therefore I refactor." - Rene Debugcartes',
    '"Give a man a fish and he eats for a day. Give a man Stack Overflow and he copies code forever." - Tech Proverb',
    '"Houston, we have a problem. It says \'works as designed\'." - Apollo Error 13',
    '"You miss 100% of the deployments you don\'t skip on Fridays." - Wayne Gitskey',
    '"First, solve the problem. Then, write the code. Then, realize the problem was different." - John Johnscode',
    '"Stay hungry. Stay foolish. Stay away from regex." - Steve Jobs.yml',
    '"One does not simply mass-assign without validation." - Boromir, Code Reviewer',
    '"The best time to write tests was 20 commits ago. The second best time is after the bug report." - Chinese Developer Proverb',
    '"With great power comes great responsibility. With great responsibility comes great technical debt." - Uncle Ben (the framework uncle)',
    '"I have not failed. I have just found 10,000 ways the build does not compile." - Thomas Edibugson',
    '"We choose to refactor not because it is easy, but because we thought it would be easy." - JFK-8',
    '"Float like a butterfly, sting like a missing semicolon in production." - Muhammad Aliasing',
    '"The unexamined code is not worth deploying." - Sockrates',
    '"Premature optimization is the root of all evil. Regular optimization never happens." - Donald Knuth, probably',
    '"I came, I saw, I mass-reverted." - Julius git-Caesar',
    '"Do or do not. There is no --dry-run." - Yoda, DevOps Master',
    '"It is not the strongest codebase that survives, but the one most responsive to change requests." - Charles Darwinpkg',
    '"If you gaze long enough into the abyss, the abyss sends you a JIRA ticket." - Friedrich Nietznode (again)',
    '"The definition of insanity is doing the same deploy over and over and expecting different results." - Albert Einstacktrace (again)',
    '"Elementary, my dear Watson. The bug was in the config all along." - Sherlock Homescreen',
    '"Reports of my code\'s death are greatly exaggerated. It\'s just deprecated." - Mark Twainscript',
    '"Not all who wander are lost. Some are just navigating a monorepo." - J.R.R. Tokenizer',
    '"Yesterday is history. Tomorrow is a mystery. Today is a gift - that\'s why we call it the present sprint." - Master Oogway, Scrum Master',
    '"A room without books is like a codebase without comments. Actually, that might be fine." - Clean Coders Anonymous',
    '"The only constant in life is change. And breaking changes in minor versions." - Heraclitus of NPMphesus',
    '"My mass grave is a git stash list." - Anonymous, 2am',
    '"The five stages of debugging: denial, anger, bargaining, depression, and printf." - Dr. Elisabeth Kubler-Stacktrace',
    '"There are only two hard things in computer science: cache invalidation, naming things, and off-by-one errors." - Every whiteboard interview',
    '"A QA engineer walks into a bar. Orders 1 beer. Orders 0 beers. Orders 99999999 beers. Orders -1 beers. Orders a lizard. Orders NULL beers." - The Setup (the punchline is production crashes)',
    '"99 little bugs in the code, 99 little bugs. Take one down, patch it around... 127 little bugs in the code." - Programmer Nursery Rhyme',
    '"Deleted production database. It\'s fine. Everything is fine. I didn\'t need this job anyway." - Last words of a junior DBA',
    '"Some people, when confronted with a problem, think \'I know, I\'ll use threads.\' Now have they two problesm." - Nedry Bloch',
    '"My code doesn\'t have bugs. It has surprise features that only trigger in production at 3am on a holiday." - Optimistic Developer',
    '"The code works and nobody knows why. The code breaks and nobody knows why. This is the circle of DevOps." - The Lion Kubernetes',
    '"We replaced our monolith with microservices so that every outage could be a mystery." - CTO, post-mortem #47',
    '"If debugging is the process of removing bugs, then programming must be the process of putting them in." - Edsger W. Dijkstra (actually real, and still hurts)',
    '"Commenting your code is like cleaning your bathroom: nobody wants to do it, but it really surprises everyone when you actually do." - Ryan Campbell, probably',
    '"I don\'t always test my code, but when I do, I do it in production." - The Most Interesting Engineer in the World',
    '"rm -rf / solves all dependency problems. And every other problem." - man who lost everything',
    '"Weeks of coding can save you hours of planning." - Every sprint retrospective',
    '"There is no cloud. It\'s just someone else\'s computer that\'s also on fire." - IT Proverb',
    '"git commit -m \'fixed it\' is a cry for help disguised as version control." - git therapist',
    '"In a room full of top software engineers, if two agree on the same thing, that\'s a bug." - Law of Engineering Consensus',
    '"The S in IoT stands for Security." - Cybersecurity Proverb',
]

print(random.choice(quotes))
