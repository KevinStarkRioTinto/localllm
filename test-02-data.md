
# Play to Win: Mobile Game Soft Launch Best Practices

[Doug McCracken](https://a16z.com/author/doug-mccracken/) and [Joshua
Lu](https://a16z.com/author/joshua-lu/)

Posted October 17, 2023

We hear a lot of discussion around the best practices for launching a mobile
game, and one particular topic that often comes up is: whether or not to do a
soft launch. And if you do soft launch, how can you tell if your game will be
successful? Much of the mobile games industry has taken the tactic of soft
launching seriously - in September alone, there were more than 100 games soft
launched on the Apple App Store and over 600 on the Google Play Store.

This blog post will explore what a soft launch is and why it can be beneficial
for game studios. We'll also dispel some of the myths that are commonly
associated with soft launches and help you figure out if this strategy is
right for your game. We’ll also address why there are so many more games soft
launched on Google Play (hint: they have more options to support a variety of
soft launch strategies).

## **What Can you Learn from Soft Launch?**

There are a few questions you should seek to answer with a soft launch, though
it’s difficult to answer all of these at a high level of fidelity. If you’re
resource constrained, you should think about prioritizing your goals based on
what’s most important to the team.

**Is the game stable/performant?******

Building a bug-free game is hard, and while your QA team is heroically finding
and triaging bugs, there’s nothing like a soft launch to show you where the
holes are. Acquiring users at scale from lower-cost geographies is a great way
to stress test servers and also get performance data from long-tail devices.
There are a TON of lower-spec Android phones that your QA team won’t have and
should probably not be purchasing. Some metrics to keep in mind for this sort
of testing include: FPS, crash rates/DAU, crashes/crasher, and latency. Google
Play recommends monitoring via their [Android Vitals
Dashboard](https://play.google.com/console/about/vitals/).

**Is the core game fun?**

The most important part of a game experience is the core loop. It’s the atomic
gameplay loop that people will experience over and over and should be HIGHLY
repeatable. If a game’s core loop doesn’t work, players will never stick
around long enough to hit the meta loops that keep them around long term and
can generate revenue. Testing core loops effectively requires getting players
in soft launch that simulate your target audience at scale, so targeting that
audience is important. On the flip side, you can save some energy/money by
remembering you don’t need to target audiences that necessarily monetize or
worry about how players are engaging with other parts of the game. Some
metrics to keep in mind for core loop testing would be:

  * First Time User Experience (FTUE) completion rates (Wooga’s game director, Annelie Biernat, recently shared why “[Optimizing the FTUE is definitely worth it](https://www.deconstructoroffun.com/blog/2022/3/27/how-woogas-switchcraft-aced-the-soft-launch#:~:text=Optimizing%20the%20FTUE%20is%20definitely%20worth%20it)”) 
  * D0 playtime & repeat sessions 
  * D1-D7 retention
  * Sessions/day
  * Minutes played/day

**Does the game have legs?**

If your core loop is working, you’ll want to make sure the game is highly
retentive. Retention is king, and it’s the most important metric in all of
free-to-play. Retention compounds over time and has a large cumulative effect
on DAUs. Retention also leads to organic growth - the longer players stick
around the more chances they’ll have to tell their friends about the game.
Retention also leads to revenue - the more sticky your game is the more likely
it is that a player will support the game by monetizing. One key metric to
look at is D30 retention, but other metrics are important too including elder
system engagement %, DAU/MAU and DAU/WAU. [Google Play
data](https://medium.com/googleplaydev/why-focusing-on-tomorrow-brings-back-
players-in-the-long-run-e57c51bd3481) suggests 50% percentile for top games
DAU/WAU = 55% and DAU/MAU = 31%.

Ideally you want to make sure your D30 retention is strong enough to stand on
its own. Testing D30 retention means that your test will need to run at least
30 days - but to get 30 cohorts of D30 retention your test will have to run at
least 60 days! Additionally, since a smaller % of each install cohort will get
to D30, you’ll need to work backwards to calculate statistical significance
for your install cohorts. Testing D30 retention can be difficult for smaller
developers that don’t have the time or resources to get highly statistically
significant data.

A hack to proxy D30 retention is to look at the ratio of D1:D7:D30 retention –
according to Google Play, the Median DAU return is 77%. Looking at the shape
of your retention curve can help approximate longer-tail retention.
