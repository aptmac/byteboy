# Tests

This folder contains buggy Java programs that will be used for the analysis of Byteboy

## Motivation

- In order to evaluate Byteboy, it must be tested on programs that are:
  - Java applications
  - Able to easily reproduce bugs
  - Written by real developers for real-world purposes (work, hobby, education, etc.)

## Method of Collection

Finding bugs in software that are easily and consistently reproducible is a lot harder than it sounds. Many popular applications will likely have their obvious bugs patched already (in the event they make it through the review process in the first place), and many bugs that do exist may be difficult to reproduce or observe due to complications with concurrency. 

Initially, we attempted to use the GitHub search options to find Java repositories with bugs that may be reproducible. However, this returned a massive list of potential bugs (that's good) but the vast majority of them had poor documentation regarding how to reproduce the errors let alone run the program itself (that's bad).

When in doubt, use Google. After investing a solid amount of time into finding bugs and ending up with nothing of use, we used this Google search in an attempt to find at least some kind of buggy programs: [What's wrong with this Java code?](https://www.google.ca/search?q=what%27s+wrong+with+this+java+code)

Without digging  too far through the pages of Google,  we evaluated all of the links on the front page for buggy programs, and selected the ones that would compile. As a result, we have 3 buggy programs we can use (which are listed below), in addition to the motivating example that we have included. While the gathered bugs are not particularly impressive or a part of large scale application, they are representative of our (Byteboy's) potential users: developers (of any skill level) who need to debug their programs. 

## Descriptions of the Bugs

1. A.java (courtesy of Stack Overflow user: RedEyes, [Link to discussion](https://stackoverflow.com/questions/30968231/whats-wrong-with-my-code)
2. BinarySearch.java (courtesy of Dream in Code user: RhettYoungberg, [Link to discussion](http://www.dreamincode.net/forums/topic/196941-whats-wrong-with-my-code/)
3. InfLoop.java (as previously seen in the byteboy/motivating-example folder)
4. Question3.java (courtesy of Dream in Code user: luka0309, [Link to discussion](http://www.dreamincode.net/forums/topic/375232-whats-wrong-with-my-code/)