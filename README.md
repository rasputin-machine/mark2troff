# mark2troff

Write amazing documents without pandoc or LaTeX!!!

# Goals

+ Provide markdown-style syntax for writting roff documents.
+ Be simple and easily pipeable.
+ Cover most, if not, all the roff syntax in markdown. 

### Why I wrote this
I started writing this program after discovering that all Linux systems come
pre-installed with a typesetting system.  I was about to say goodbye to LaTeX 
and RMarkdown, when I noticed that the roff syntax sucks. Don't get me wrong, I
love this thing, and I understand the reasoning behind roff's syntax. But the 
syntax is a bitch to read.  I do not think it's necessary to put a word you 
want to bold on its _own fucking line_.

I also figured I could just use pandoc, but that's 442MB!!!!  That's partially
due to downloading the entire haskell language to get it working.  But since I
don't use haskell, that's wasted space.  And don't even get me started on
LaTeX....

That's where this program comes in.

### What does it do?

You write your program using markdown-style syntax, and the program will
convert that into a valid roff document, which is then piped to the family of
roff commands.  Simple!!  Write that paper without looking at a nearly 50 year
old ugly markup language.  This will be designed to be used at the start of 
your roff pipe.

### Why markdown?

From the place where [markdown was birthed][1]:

> Markdown is intended to be as easy-to-read and easy-to-write as is feasible.

### Why python?

To be quite frank, it's the only language I'm really comfortable in.  I'll
write this in Go or C once I get good at either language.  But I am going to

Why reinvent the wheel?



[1]: https://daringfireball.net/projects/markdown/syntax#philosophy
