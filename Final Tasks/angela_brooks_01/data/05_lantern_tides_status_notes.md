# Lantern Tides - status notes (my rough guess, STALE)

Written from memory, late, probably wrong in places. Do not quote these numbers back to me as
fact - verify against the repo (lantern-tides), Sentry, and the playtest analytics. This is a
Godot 4.x pixel-art narrative puzzle game, 1970s small-town magical-realism, 7 chapters planned,
vertical slice is the thing I am demoing at the Showcase.

## What it is, in case I forget why I am killing myself over it
It is a story about a grandmother in a small 1970s town, and it is quietly about Grandma Ruth even
though she does not know that yet - that reveal is a Thanksgiving thing, not a devlog thing. Art is
mine in Aseprite, code and design and writing are mine, Ravi does audio and music. Lore and the
messy narrative outline live in a private Obsidian vault, not the repo. Chapter 4 (The Railyard) is
supposed to use the night-sky reference stills I have been saving for the mood; that is an art task
for later, not a demo blocker.

## Chapters
- Chapter 1 - The Lantern Walk: solid. Feels basically shippable. Scene-transition mechanic is
  clean. Board says done, and for once I believe it.
- Chapter 2 - The Radio Room: mostly there, minus the radio thing that keeps coming back. The
  puzzle works; the radio state just does not persist between scenes the way it should.
- Chapter 3 - The Post Office: maybe ~50% done? The board says it is basically finished but that
  does not match how it feels when I playtest it. The dialogue-tree segment at the Post Office
  door is where it gets rough, and that is exactly the part testers keep bailing on.
- Chapters 4-7 - The Railyard, The Harbor, The Long Night, Morning: drafted on paper, not built.
  Mechanics sketched (puzzle, scene-transition, dialogue-tree, scene-transition) but no scenes.

## Known rough spots (from memory, IDs may be wrong)
- Post Office door - crashes sometimes. There is a ticket for it, I forget the number. This is the
  one that scares me for the demo.
- Clerk conversation soft-locks if you back out mid-line.
- Postbox gives double feedback, feels buggy.
- Chapter 2 radio state does not persist between scenes.

## What is authoritative, what is not
The board (Trello) is the optimistic version of reality. The commits, Sentry crashes, and the
playtest funnel are the honest version. Where they disagree, the honest version wins and I want to
hear it bluntly. Ravi owns audio on a separate repo (lantern-tides-audio); the Post Office stem is
the one blocking, and there is a main-theme pass sitting in a PR waiting on my review.

## Vibe check
The demo has to be *stable* for 5 minutes in front of judges at 7pm. I would rather cut content
than crash. Freeze the build early, run the loop clean, and if the board and the commit history
disagree, trust the commits and tell me straight.
