import re
import os

# STEP 1: Paste your raw, messy transcript here as a string
raw_transcript = """
Full Transcript
Note 00:00:00-00:00:00 ( sec)
No StressLens
[The following transcript was provided by Fox News. It was cross-checked against the source material and confirmed. Transcript and video courtesy and copyright Fox News.]
Sean Hannity 00:00:00-00:00:01 (1 sec)
No StressLens
Mr. President --
Donald Trump 00:00:01-00:00:02 (1 sec)
No StressLens
Thank you.
Sean Hannity 00:00:02-00:00:03 (2 sec)
No StressLens
-- welcome back.
Donald Trump 00:00:03-00:00:05 (2 sec)
No StressLens
Thank you very much.
Sean Hannity 00:00:05-00:00:14 (9 sec)
No Signal (0)
Let's talk about the moment you walked back in this office, this desk, this room, your carpet. How do you feel?
Donald Trump 00:00:14-00:00:41 (27 sec)
No Signal (0.531)
Well, it was a lot of work. And as you know, I felt that we shouldn't have had to necessarily be here. Could have been done. A lot of work could have been -- it would have been over. We wouldn't have inflation. We wouldn't have had the Afghanistan disaster. We wouldn't have October 7th with Israel or so many people were killed and you wouldn't have a Ukraine war going on. But with all that being said, I think it's bigger.
Donald Trump 00:00:41-00:00:46 (5 sec)
No StressLens
It's bigger than if it were more traditional.
Sean Hannity 00:00:46-00:00:48 (2 sec)
No StressLens
Only the second time in history.
Donald Trump 00:00:48-00:00:48 (1 sec)
No StressLens
Yes.
Sean Hannity 00:00:48-00:00:51 (2 sec)
No StressLens
Somebody didn't have consecutive terms.
Donald Trump 00:00:51-00:01:09 (18 sec)
No Signal (0.181)
Yes. Well, they say it's historically bigger. I don't know about that. But I can say it showed us a couple of things. It showed us that the radical left, their philosophies and policies are horrible. They don't work. You look at crime, you look at what's gone on the border, you look at what's going to happen to crime.
Donald Trump 00:01:09-00:01:32 (23 sec)
No Signal (0.388)
I mean, the crime that's going to happen, but I think we got there just in the nick of time. But we still have -- you covered better than anybody, we have terrorists in our country by the thousands. We have murderers in our country by the tens of thousands. We have numbers that came out, 11,000 people that murdered are now free and walking around in our country.
Donald Trump 00:01:32-00:01:50 (19 sec)
No Signal (0.589)
And of them, I think 48 percent they say killed more than one person and they're walking around. They came out of jails from other countries. And, you know, people they've emptied their jails. I wouldn't. If I were the president or prime minister or something of another country, I'd empty my jails right into America, into the United States.
Donald Trump 00:01:50-00:02:08 (18 sec)
No Signal (0.366)
Why not? And many of them did it. If you look at Venezuela, their crime rate is down now, 78 percent. Because they took their street gangs and they moved them into the United States. And you're seeing that in Colorado and Los Angeles and other places, and we're going to take care of it.
Sean Hannity 00:02:08-00:02:17 (9 sec)
No Signal (0)
So, did Biden really say to you when you came up to the front of the White House, welcome home?
Donald Trump 00:02:17-00:02:19 (2 sec)
No StressLens
No. Did somebody say that?
Sean Hannity 00:02:19-00:02:20 (2 sec)
No StressLens
I read it somewhere.
Donald Trump 00:02:20-00:02:23 (2 sec)
No StressLens
I don't know. Maybe he did. I really don't know.
Sean Hannity 00:02:23-00:02:29 (6 sec)
No Signal (0)
So, you left him a letter. It was funny with Peter Doocy. And Peter said, oh, Mr. President, did Joe Biden leave you a letter?
Donald Trump 00:02:29-00:02:29 ( sec)
No StressLens
Yes.
Sean Hannity 00:02:29-00:02:30 ( sec)
No StressLens
He did leave you a letter?
Donald Trump 00:02:30-00:02:30 (1 sec)
No StressLens
He did.
Sean Hannity 00:02:30-00:02:35 (5 sec)
No StressLens
And you had left him one, but you've never disclosed either one of them.
Donald Trump 00:02:35-00:02:36 (1 sec)
No StressLens
Well, a lot of people --
Sean Hannity 00:02:36-00:02:37 (1 sec)
No StressLens
Now, would be a great time.
Donald Trump 00:02:37-00:02:58 (20 sec)
No Signal (0.082)
You know, it was interesting, a lot of people thought it was sort of like a set up with Peter Doocy and myself, and I have a lot of respect for Peter, but he just asked me a question about the letter and then I remember that, you know, like a custom, you leave it right in the drawer of that beautiful desk right alongside of us. And so, I opened it up and I actually gave the letter to Peter.
Sean Hannity 00:02:58-00:02:58 (1 sec)
No StressLens
And did he -- he got to read it
Donald Trump 00:02:58-00:03:00 (2 sec)
No StressLens
I guess. I don't -- I haven't --
Sean Hannity 00:03:00-00:03:02 (2 sec)
No StressLens
You don't know if he read it?
Donald Trump 00:03:02-00:03:05 (4 sec)
No StressLens
Yes. I just sent it to him a little while ago.
Sean Hannity 00:03:05-00:03:19 (14 sec)
No Signal (0)
All right. Before we get into this, there's so much substance. You are inheriting a lot of problems, a lot of things that actually scare me. And I want to get to all that, but I want to -- and I will get to all of that. They're --
Donald Trump 00:03:19-00:03:21 (2 sec)
No StressLens
All solvable problems.
Sean Hannity 00:03:21-00:03:22 (1 sec)
No StressLens
I agree.
Donald Trump 00:03:22-00:03:23 (1 sec)
No StressLens
They're all solvable.
Sean Hannity 00:03:23-00:03:24 (1 sec)
No StressLens
Not easy.
Donald Trump 00:03:24-00:03:36 (12 sec)
No Signal (0.353)
With time, effort, money, unfortunately, but they're all solvable problems. We can get our country back. But if we didn't win this race, I really believe our country would have been lost forever.
Sean Hannity 00:03:36-00:04:04 (28 sec)
No Signal (0)
Were there moments -- I mean, when you think of what they threw at you. And I know you signed this declaration about no more weaponization. And we know that the preemptive pardons came up on Joe's way out. But you were facing a civil trial, a criminal trial, conviction, sentencing, Jack Smith, D.C., Florida, Fani Willis.
Sean Hannity 00:04:04-00:04:17 (13 sec)
No Signal (0)
I mean, you fought through all of that to get back right here in this office. What people don't know is over there's a little red button you push. You scare people. People think it's the nuclear button, but it's really, you know --
Donald Trump 00:04:17-00:04:18 (1 sec)
No StressLens
It's something else.
Sean Hannity 00:04:18-00:04:28 (10 sec)
No Signal (0)
You user it for a different purpose. But the question I have was, at any point, did you doubt you would be back here?
Donald Trump 00:04:28-00:04:52 (24 sec)
No Signal (0.451)
So, it's a great question. It's something I don't think about. I never really thought about it. I don't think about, gee, will I be back? I just do it. I get it done. I get things done. I'm good at getting things done. And I set my mind to it. As you know we had a great election in 2016. I had a much better election in 2020. And if I didn't have that election, I wouldn't have run.
Donald Trump 00:04:52-00:05:17 (25 sec)
No Signal (0.549)
If I thought that I didn't get the number of votes -- and it was reported that I got almost 75 million votes and that was their numbers. That wasn't the numbers, that was their numbers. That was more than anybody has gotten in history. Any sitting president had ever gotten and you lost. Had I got -- gotten like 50 million, 40 million or 60 million, I would never have run.
Donald Trump 00:05:17-00:05:23 (6 sec)
No Signal (0.337)
But that was like a poll. So, but I had a different attitude. Too big to rig.
Sean Hannity 00:05:23-00:05:35 (12 sec)
No Signal (0)
Poll came out just in the last 24 hours by Insider Advantage. That's Matt Towery. He nailed 2016, 2020, and 2024. Great pollsters, you know.
Donald Trump 00:05:35-00:05:35 ( sec)
No StressLens
Right.
Sean Hannity 00:05:35-00:05:50 (15 sec)
No Signal (0)
And he gave you a 56 percent approval rating. He also said of Congress, and I had a town hall with members of Congress last night, that 70 percent of respondents want Congress to unite behind your agenda.
Donald Trump 00:05:50-00:06:12 (22 sec)
No Signal (0.784)
I watched that show. It was a great show. And you had some great people in the background. I know every one of them. And they're really patriots. I just saw the love. You know, as the speaker who is doing a terrific job, the speaker is answering questions. And I saw the -- like, the acknowledgement and the love they had, and those are tough people behind him.
Donald Trump 00:06:12-00:06:14 (2 sec)
No StressLens
You know, these are not easy people.
Sean Hannity 00:06:14-00:06:15 (2 sec)
No StressLens
There are others that are tougher.
Donald Trump 00:06:15-00:06:24 (9 sec)
No Signal (0.373)
I said, well, I don't know, this is a tough group, if they want to be. They're not -- nobody much tougher. But they're very unified. I think they're going to do a great job.
Sean Hannity 00:06:24-00:06:46 (22 sec)
No Signal (0)
They have a small majority. You went through over 200 since we've got here and we have breaking news today that we'll get to in a minute. And especially as it relates to the border and some other issues. And -- but you're going to need to do some of these things legislatively. How -- you will probably play the largest role --
Donald Trump 00:06:46-00:06:46 ( sec)
No StressLens
Yes.
Sean Hannity 00:06:46-00:06:53 (7 sec)
No Signal (0)
-- in uniting them both in the House and Senate. Reconciliation, the Senate has very strict, you know, rules governing how they can do it.
Donald Trump 00:06:53-00:06:54 (1 sec)
No StressLens
Sure.
Sean Hannity 00:06:54-00:06:57 (3 sec)
No StressLens
Do you -- one big beautiful bill, two bills, do you care at this point?
Donald Trump 00:06:57-00:07:18 (20 sec)
No Signal (0.114)
I don't care as long as we get to the final answer. I like the concept of the one bill. I guess I said one big, beautiful, and that's what everyone faced. Actually, it's sort of a nice sound to it. But I do like that concept. It could be something else. It could be a smaller bill and a big bill, but as long as we get to the right answer.
Donald Trump 00:07:18-00:07:29 (11 sec)
No Signal (0.217)
Now, I will say that Los Angeles has changed everything because a lot of money is going to be necessary for Los Angeles and a lot of people on the other side want that to happen in --
Sean Hannity 00:07:29-00:07:30 (1 sec)
No StressLens
North Carolina, too.
Donald Trump 00:07:30-00:07:48 (17 sec)
No Signal (0.589)
Well, they don't care about North Carolina. The Democrats don't care about North Carolina. What they've done with FEMA is so bad. FEMA is a whole another discussion, because all it does is complicate everything. FEMA has not done their job for the last four years. You know, I had FEMA working really well.
Donald Trump 00:07:48-00:08:10 (23 sec)
No Signal (0.278)
We had hurricanes in Florida. We had Alabama tornadoes. We -- but unless you have certain types of leadership it's really -- it gets in the way. And FEMA is going to be a whole big discussion very shortly, because I'd rather see the states take care of their own problems. If they have a tornado someplace and if they let that state, Oklahoma is very competent.
Donald Trump 00:08:10-00:08:38 (28 sec)
No Signal (0.299)
I love Oklahoma. 77 out of 77 districts, and that's never been done before. I did it three times. I mean, think of it, three times, never been done. Ronald Reagan had the record 56 out of 77. I got 77 out of 77. So, you have to love a place like that. I love Oklahoma. But you know what, if they get hit with a tornado or something, let Oklahoma fix it. You don't need -- and then the federal government can help them out with the money.
Sean Hannity 00:08:38-00:08:39 (1 sec)
No StressLens
What do you --
Donald Trump 00:08:39-00:08:47 (8 sec)
No Signal (0.762)
The FEMA is getting in the way of everything. And the Democrats actually use FEMA not to help North Carolina.
Sean Hannity 00:08:47-00:08:48 (1 sec)
No StressLens
It makes no sense.
Donald Trump 00:08:48-00:09:07 (19 sec)
No Signal (0.288)
So, I'm stopping -- on Friday, I'm stopping in North Carolina, first up, because those people were treated very badly by Democrats and I'm stopping there. We're going to get that thing straightened out because they're still suffering from a hurricane from months ago. And then, I'm going to then -- I'm going to go to California.
Sean Hannity 00:09:07-00:09:08 (1 sec)
No StressLens
Will you meet with Gavin?
Donald Trump 00:09:08-00:09:29 (22 sec)
No Signal (0.616)
I don't know. I haven't even thought about it. Look Gavin's got one thing he can do, he can release the water that comes from the north. There is massive amounts of water, rainwater and mountain water that comes due with the snow, comes down when -- it as it melts. There's so much water. They're releasing it into the Pacific Ocean.
Donald Trump 00:09:29-00:09:34 (4 sec)
No Signal (0.359)
And I told him for -- it's a political thing for the Democrats. I don't know.
Sean Hannity 00:09:34-00:09:36 (2 sec)
No StressLens
I played the tape, you said it to him in front of him in 2018.
Donald Trump 00:09:36-00:09:54 (18 sec)
No Signal (0.051)
I said it to him in front of the media and everything else and nobody talks about it. The media never picks it up. You pick -- you put it out. I was so happy to see that tape because some people said. is that possible? They have they have water coming down from the Pacific Northwest, which is a lot of water.
Donald Trump 00:09:54-00:10:05 (11 sec)
No Signal (0.671)
So much water that they'd have to let some of it go at some point. They don't need reservoirs, they don't need any, they're spending all this money on these reservoirs, and they're fake reservoirs. You know, they're --
Sean Hannity 00:10:05-00:10:11 (6 sec)
No Signal (0)
But the reservoirs were empty. The hydrants didn't work. And they're not practicing the science of forestry, which is a --
Donald Trump 00:10:11-00:10:19 (8 sec)
No Signal (0.227)
Their sprinklers didn't work in the homes because they had water. Think of it, we have sprinklers, think of it, with no water. They didn't have any water. The fire hydrants --
Sean Hannity 00:10:19-00:10:19 ( sec)
No StressLens
The --
Donald Trump 00:10:19-00:10:28 (9 sec)
No Signal (0.175)
-- hard to believe. The place has sprinklers, it's nice. But you don't want to lose this office. By the way, how do you like it?
Sean Hannity 00:10:28-00:10:32 (4 sec)
No StressLens
It's -- well, I'm glad -- it's great to be back, I'm not going to lie.
Donald Trump 00:10:32-00:10:35 (3 sec)
No StressLens
You know, I've had the biggest people in the world come here.
Sean Hannity 00:10:35-00:10:35 ( sec)
No StressLens
Yes.
Donald Trump 00:10:35-00:10:43 (8 sec)
No Signal (0.02)
And they come into the Oval Office, and they just look. And they want time to look. They're looking around.
Sean Hannity 00:10:43-00:10:43 ( sec)
No StressLens
It's great.
Donald Trump 00:10:43-00:10:46 (3 sec)
No StressLens
George Washington, Honest Abe.
Sean Hannity 00:10:46-00:11:20 (34 sec)
No Signal (0)
One day maybe we can do a tour. We had a conversation, and maybe I shouldn't disclose this, but I will. And it was after the 2020 election and you asked me a question. And we've known each other for 30 years. So, we have a friendship and we have a professional relationship. And the question you asked me, maybe in the end it will be better that if I came back in four years and we talked about history after World War II, Winston Churchill was thrown out, but they brought him back.
Sean Hannity 00:11:20-00:11:31 (11 sec)
No Signal (0)
Grover Cleveland is the only other American president that did not serve consecutive terms. And my answer to you was, I thought it would be bigger if you came back.
Donald Trump 00:11:31-00:11:46 (15 sec)
No Signal (0.193)
It's turning out to be bigger. And I think one thing is happening is people are learning that they can't govern and that their policies are terrible. I mean, they don't want to see a woman get pummeled by a man in a boxing ring.
Sean Hannity 00:11:46-00:11:46 ( sec)
No StressLens
No.
Donald Trump 00:11:46-00:12:08 (22 sec)
No Signal (0.089)
They don't want to see men in women's sports in other ways. They don't want to see men. They don't want to have transgender for everyone. They don't want a child leave home as a boy and come back two days later as a girl. A parent doesn't want to see that. And there are states where that can happen. They don't want to see taxes go through the roof.
Donald Trump 00:12:08-00:12:29 (20 sec)
No StressLens
Like this is the only group of people they want to raise your -- they say, we want to raise your taxes. You know, if they don't work with us on the Trump tax cuts extending, that would mean it would go back to the taxes. We've got the largest tax cut in history. That would mean the taxes would go up more than any tax hike in the history of our country.
Donald Trump 00:12:29-00:12:39 (10 sec)
No Signal (0.26)
And normally, you'd say, that's got to be the easiest negotiation in history, because if they did that, how could they ever win an election? But they'll fight us on that. They fight us on things. It's incredible.
Sean Hannity 00:12:39-00:12:40 (1 sec)
No StressLens
Here -- I ran into --
Donald Trump 00:12:40-00:12:44 (4 sec)
No Signal (0.02)
They don't use common sense. In my opinion, the Democrats don't use common sense, and that's why --
Sean Hannity 00:12:44-00:12:46 (2 sec)
No StressLens
I think common sense won the day in the election.
Donald Trump 00:12:46-00:13:03 (16 sec)
No Signal (0.374)
Yes. But you know the amazing thing? I'm watching now. Now it's time, and you know, a few months have passed, and the election's over and you see what happened and it was a rout. I won all seven swing states and we won by millions of votes, the popular vote, millions. And nobody can even believe some of the numbers.
Donald Trump 00:13:03-00:13:10 (7 sec)
No Signal (0.462)
And how about with African Americans, with Hispanics, with everything, how well we did, nobody can believe the numbers.
Sean Hannity 00:13:10-00:13:10 ( sec)
No StressLens
I was --
Donald Trump 00:13:10-00:13:18 (8 sec)
No Signal (0.061)
How about with youth? I won youth by 36 points. Now, maybe that's because I went on TikTok. I don't know. But I have -- I'm starting to have a very warm spot --
Sean Hannity 00:13:18-00:13:20 (2 sec)
No StressLens
TikTok is going to be sold, right?
Donald Trump 00:13:20-00:13:21 (2 sec)
No StressLens
I think TikTok's going be --
Sean Hannity 00:13:21-00:13:22 (1 sec)
No StressLens
Well, people like senator --
Donald Trump 00:13:22-00:13:25 (2 sec)
No StressLens
I say people want buy it. People want to buy it.
Sean Hannity 00:13:25-00:13:30 (6 sec)
No Signal (0)
I think they do. But those that say they know, say it's a spying app for the Communist Chinese.
Donald Trump 00:13:30-00:13:46 (15 sec)
No Signal (0.739)
I know, but everything -- but you can say that about everything made in China. Look, we have our telephones made in China for the most part. We have so many things made in China, so why don't they mention that? You know, the interesting thing with TikTok though is you're dealing with a lot of young people.
Donald Trump 00:13:46-00:13:46 ( sec)
No StressLens
So --
Sean Hannity 00:13:46-00:13:47 (1 sec)
No StressLens
They love it.
Donald Trump 00:13:47-00:13:53 (5 sec)
No Signal (0.556)
-- is it that important for China to be spying on young people, on young kids watching crazy videos and things?
Sean Hannity 00:13:53-00:13:55 (2 sec)
No StressLens
I don't want China spying on anybody.
Donald Trump 00:13:55-00:14:01 (6 sec)
No Signal (0.831)
No, no. But they make your telephones and they make your computers and they make a lot of other things. Isn't that a bigger threat?
Sean Hannity 00:14:01-00:14:22 (21 sec)
No Signal (0)
I'm sure that'll be part of your discussions with President Xi, which I'm going to talk about in a moment. Let me go to the border. We do have breaking news today. I ran into Tom Homan as I was walking in today. And so far, 308 total arrests, 296 detainees. And the first deployment of military assets to the U.S. border.
Sean Hannity 00:14:22-00:14:27 (5 sec)
No StressLens
The deployment includes active-duty troops and the National Guard.
Donald Trump 00:14:27-00:14:28 (1 sec)
No StressLens
Right.
Sean Hannity 00:14:28-00:14:52 (24 sec)
No Signal (0)
And here's my biggest fear and concern beyond the Iranian assassination squads. Is we now know 14 million -- We don't know how many got aways. We don't know the total number, but we have known terrorists in our country. We have known murderers, rapists. We have violent criminals, cartel members, gang members.
Sean Hannity 00:14:52-00:15:19 (27 sec)
No Signal (0)
Now, I would imagine if you came from Iran and Syria and Egypt and Afghanistan and Russia and China and Venezuela, you didn't come here because you want a better life for your children. I would imagine those known terrorists are planning an attack on our homeland. At a moment's notice, you're going to be in this desk, maybe sitting at this desk or maybe up in the residence and they're going to call you down in the situation room because our homeland is under attack.
Sean Hannity 00:15:19-00:15:35 (16 sec)
No Signal (0)
I would like to be wrong, but when you have known terrorists, you have to believe that they're going to attack a homeland. That would change their trajectory, that moment of your entire presidency. That has to weigh on you.
Donald Trump 00:15:35-00:15:44 (9 sec)
No Signal (0.029)
It could be. Yes, it could be. And I know, I've watched you for a lot of years, and you actually make one statement before you say that. You say, 100 percent certain.
Sean Hannity 00:15:44-00:15:44 ( sec)
No StressLens
I do.
Donald Trump 00:15:44-00:15:45 (1 sec)
No StressLens
That's a pretty big statement.
Sean Hannity 00:15:45-00:15:47 (2 sec)
No StressLens
And then I say, I pray to God I'm wrong.
Donald Trump 00:15:47-00:16:13 (26 sec)
No Signal (0.072)
Yes, I hope you're wrong too. And I won't comment, but I tend to agree with you. It depends. We'll see what happens. Look, we have a lot of great people right now. A lot of great, great people on this situation. This was a gross miscarriage of common sense to allow people to come in. And I believe the number is 21 million people and a large percentage of them are criminals all over the world.
Donald Trump 00:16:13-00:16:21 (8 sec)
No Signal (0.514)
This is not just South America. This isn't -- you know, we talk Venezuela, that's a big abuser. But these are countries from -- these are --
Sean Hannity 00:16:21-00:16:22 (1 sec)
No StressLens
Iran --
Donald Trump 00:16:22-00:16:40 (18 sec)
No Signal (0.385)
-- the countries that you don't even think of. The Congo has emptied their prisons out into the United States. We're not thinking about the Congo, we're thinking about South America. It's much more than South America. But prisons from all over the world have been emptied out into our country by Biden, allowing it to happen.
Donald Trump 00:16:40-00:16:56 (16 sec)
No Signal (0.279)
I don't even know if he knew what the hell was going on. But who would want this? I always say to people, you know, you always like to understand, like in a business, you want to understand the other side, why do they want something, you know, et cetera, et cetera. And you figure it out. And there's usually an answer, almost always.
Donald Trump 00:16:56-00:17:13 (16 sec)
No Signal (0.058)
I don't understand. Why does somebody want open borders where -- and they say the vote, OK? But I did well with the Hispanic vote, if you're looking at Hispanic. They say they do it because they want to think they're going to stay in power. It's going to keep -- pay better for Democrats. I don't really believe that.
Donald Trump 00:17:13-00:17:36 (24 sec)
No Signal (0.212)
Besides that they cheat so much, they don't have to do that. They cheat so well. They're very good at cheating. The only thing they're good at really is cheating. But here's the thing I ask, why would somebody say that open borders are good, where jails and mental institutions from other countries and gang members right off the streets of the toughest cities in the world are being brought to the United States of America and emptied out into our country?
Donald Trump 00:17:36-00:17:55 (19 sec)
No Signal (0.432)
Why would anybody that even likes -- you don't have to love our country, you have to like it, why would anybody that likes our country, the Democrats, allow that to happen? And even now, I watch them on television. They're trying to justify it. You can't justify it. The only reason it can be is two reasons.
Donald Trump 00:17:55-00:18:22 (27 sec)
No Signal (0.109)
You're stupid, and I don't think they're stupid. I think anybody that cheats that much in that well is not stupid. You're either stupid or you hate the country. Those are the only two reasons. Sean, who would ask for open borders with people pouring in, some of whom I won't get into it, but you can look at them and you can say could be trouble, could be trouble.
Donald Trump 00:18:22-00:18:24 (1 sec)
No StressLens
There are people coming in --
Sean Hannity 00:18:24-00:18:25 (2 sec)
No StressLens
There were people with gang tattoos on.
Donald Trump 00:18:25-00:18:31 (6 sec)
No Signal (0.282)
There are people coming in with tattoos all over their face. Their entire face is covered with tattoos.
Sean Hannity 00:18:31-00:18:32 (1 sec)
No StressLens
That identifies --
Donald Trump 00:18:32-00:18:35 (3 sec)
No StressLens
Typically, you know he's not going to be the head of the local bank.
Note 00:18:35-00:18:35 ( sec)
No StressLens
[Commercial break]
Sean Hannity 00:18:35-00:18:48 (13 sec)
No Signal (0)
What do you do sanctuary states, by definition, or sanctuary cities, they're aiding and abetting in the law breaking. OK. They're going to get federal funds.
Donald Trump 00:18:48-00:18:55 (7 sec)
No Signal (0.838)
Yes. We're trying to get rid of them, and we're trying to end them. And a lot of the people in those communities don't want them. You know, California is a big example.
Sean Hannity 00:18:55-00:18:56 (1 sec)
No StressLens
But would you cut off their money
Donald Trump 00:18:56-00:19:17 (21 sec)
No Signal (0.194)
I might have to do that. Sometimes that's the only thing you can do. Look, California is a great example of it. If you actually polled the people, they don't want sanctuary cities, but Gavin Newsom does, and these radical left politicians do. And you know, if you asked them why they couldn't even -- I watched Gavin Newsom try to answer that question, he was unable to even answer.
Donald Trump 00:19:17-00:19:38 (21 sec)
No Signal (0.346)
He looked like an idiot. He was unable to answer. I asked him one other question, why is it that you don't want millions of gallons of water a day pouring throughout California? You know, the farmland in California is they say the equivalent of Iowa, great land, but it's got no water. And you sit there and it's literally -- you can see it burning.
Donald Trump 00:19:38-00:19:39 (1 sec)
No StressLens
It's on flame.
Sean Hannity 00:19:39-00:19:40 (1 sec)
No StressLens
Sure.
Donald Trump 00:19:40-00:19:59 (19 sec)
No Signal (0.148)
All they need is water and that big farmland. And I asked him why -- how is it possible that you're not allowing this water? They diverted out to the Pacific Ocean where it drops into the ocean. And you know what it's like? It's like nothing. To the Pacific Ocean, it's like two glasses of water. It's nothing.
Donald Trump 00:19:59-00:20:34 (35 sec)
No Signal (0.309)
Millions of gallons of water is diverted way up north in California into the Pacific Ocean, that water -- you know, they have the pipes, and it's half pipes. You see him all the time, half pipes. People live in those half pipes now. You know, they have homeless living in those half pipe. But this is water that millions of gallons of water a week and a day in some cases, you know, depending on the flow, so much water, they wouldn't know what to do with it. Your sprinklers would be filled.
Donald Trump 00:20:34-00:20:55 (21 sec)
No Signal (0.219)
They can even -- remember when I took criticism because they said, you have to manage your forest. The head of a country that lives in forest, a number of them actually. Finland told me this, Austria told me this, the head of Austria, head of Finland, and it was beautiful the way they expressed it. They said, we live in a forest.
Donald Trump 00:20:55-00:21:12 (17 sec)
No Signal (0.137)
We are a forest nation. That's beautiful, isn't it, to say that. We have trees that are the most magnificent in the world, far more beautiful than what they have in California and much more flammable. He said, we don't have forest fires. We manage our forest.
Sean Hannity 00:21:12-00:21:13 (1 sec)
No StressLens
You can get a degree in forestry.
Donald Trump 00:21:13-00:21:38 (24 sec)
No Signal (0.079)
Well, they'll do cuts. Yes. Can you imagine? But you don't need much. You have to clean the floors of the forest. You know, when they had forest, I go to see some of the sites, I watched in California, they use billions of dollars of money. And they just said, you know, I mean, look at what happened. Los Angeles, that's like a nuclear weapon went off what's happened to Los Angeles.
Donald Trump 00:21:38-00:21:54 (17 sec)
No StressLens
And you know, that thing went for four or five days. Nobody was even fighting it because they didn't have any water. Their fire departments aren't funded properly. And the firefighters were brave as hell. They were fighting without water. I mean, they turn on a fire hydrant, there's no water that comes out.
Donald Trump 00:21:54-00:22:12 (18 sec)
No Signal (0.506)
And they're sitting -- and the fires are rushing at them at 30, 40 miles an hour. Those firefighters were brave. What happened to that state is incredible. And then you listen to -- I remember when Ron DeSantis and Gavin Newsom were debating on your show.
Sean Hannity 00:22:12-00:22:13 (1 sec)
No StressLens
Yes.
Donald Trump 00:22:13-00:22:32 (19 sec)
No Signal (0.376)
And Newsom's talking like, everything's great, oh, everything's great, just great, just great. More people left California this year than ever have left in history before the fire. But look at it, take a look. And you know, the amazing thing, these are wealthy people, many wealthy people lost their homes.
Donald Trump 00:22:32-00:22:50 (18 sec)
No Signal (0.348)
I saw somebody on television, one of the wealthiest people, one of the most powerful people in the country, being interviewed as though he were a vagrant. His shirt -- and you have to know, he's a mean, horrible human being. He's a tough guy, very tough guy, a horrible person, but he's very rich and --
Sean Hannity 00:22:50-00:22:51 (1 sec)
No StressLens
He's rich, but he's a horrible person.
Donald Trump 00:22:51-00:23:12 (21 sec)
No Signal (0.511)
No, he's a horrible human being. You have rich people that are very nice. But this guy's a terrible person. So, I say that's so and so. I said to Melania, I said, look at it. They were interviewing him as a guy that lost his house. He said they took my house away. And he's literally in his underwear and his t-shirt.
Donald Trump 00:23:12-00:23:19 (7 sec)
No Signal (0.039)
It looked like he just got out of the bedroom. And I say, that's one of the wealthiest guys in the country. Look at this guy. Take a look at it.
Sean Hannity 00:23:19-00:23:19 ( sec)
No StressLens
He lost --
Donald Trump 00:23:19-00:23:22 (3 sec)
No StressLens
Somebody will tell you the name, maybe after the interview.
Sean Hannity 00:23:22-00:23:22 ( sec)
No StressLens
OK.
Donald Trump 00:23:22-00:23:43 (21 sec)
No Signal (0.019)
But you won't even believe it. But he was on television as somebody that -- and he was complaining they wouldn't let him go to his house, which was on fire. They wouldn't let him go, because you know, they don't want him to die. You know, some of the wealthiest, most powerful people lost their homes. And it looked like our country was helpless.
Donald Trump 00:23:43-00:23:55 (12 sec)
No Signal (0.157)
This fire was just raging and then it would catch to another area, another area, another area. There was nothing. It took a week and a half and I've never seen anything like it. We look so weak.
Sean Hannity 00:23:55-00:24:01 (6 sec)
No StressLens
Will you give -- obviously, Americans want to help the other Americans in need. OK.
Donald Trump 00:24:01-00:24:01 ( sec)
No StressLens
Yes.
Sean Hannity 00:24:01-00:24:05 (4 sec)
No Signal (0)
Fair enough. We do that. We got to help the people in North Carolina. They've been suffering.
Donald Trump 00:24:05-00:24:07 (3 sec)
No StressLens
Well, you know, that's what I want to do. That's why I'm stopping there first.
Sean Hannity 00:24:07-00:24:09 (2 sec)
No StressLens
You're going to stop in California?
Donald Trump 00:24:09-00:24:11 (2 sec)
No StressLens
I'm stopping in North Carolina first.
Sean Hannity 00:24:11-00:24:15 (4 sec)
No StressLens
Should the money be contingent on them practicing the science of forestry?
Donald Trump 00:24:15-00:24:26 (11 sec)
No Signal (0.334)
Well, I think this, I'm going to put a statement out today I think, and maybe it's already written, I'd said, I don't think we should give California anything until they let water flow down into their system.
Sean Hannity 00:24:26-00:24:28 (1 sec)
No StressLens
From the north to the south?
Donald Trump 00:24:28-00:24:33 (5 sec)
No Signal (0.556)
This is a political thing. I don't know what it is. You know, they talk about the Delta smelt. It's a little tiny fish like this.
Sean Hannity 00:24:33-00:24:34 (1 sec)
No StressLens
I want to --
Donald Trump 00:24:34-00:24:44 (10 sec)
No Signal (0.293)
They say it's an endangered species. Well, how is it endangered? No wonder it's a danger. It's not getting any water. How do you -- if you have a fish and you're stopping the water, isn't that going to hurt the fish?
Sean Hannity 00:24:44-00:24:49 (5 sec)
No StressLens
I did a show in 2009 from the San Joaquin Valley, Devin Nunes's district.
Donald Trump 00:24:49-00:24:50 (1 sec)
No StressLens
Right.
Sean Hannity 00:24:50-00:24:55 (5 sec)
No StressLens
And they wouldn't give thousands of acres of farmland water to protect that --
Donald Trump 00:24:55-00:24:56 (1 sec)
No StressLens
By the way, you see that now.
Sean Hannity 00:24:56-00:24:57 (1 sec)
No StressLens
It's crazy.
Donald Trump 00:24:57-00:25:09 (12 sec)
No Signal (0.549)
I drove up the highway. I was with Devin Nunes and other Republican congressmen. And I looked at these vast areas of land and it looked like it was just burning. It was dark. It was dry.
Sean Hannity 00:25:09-00:25:09 (1 sec)
No StressLens
Terrible.
Donald Trump 00:25:09-00:25:30 (21 sec)
No Signal (0.52)
And then there'd be a little patch, a little tiny patch of green, beautiful green. And I said, why -- how come all this land has these little patches? They said, that's all that we're allowed to farm because we have no water. I said, are you having a drought? No, they've turned off the water. They turned off the spigot from up north in order to protect the Delta smelt.
Sean Hannity 00:25:30-00:25:31 (1 sec)
No StressLens
Let me move on to the economy.
Donald Trump 00:25:31-00:25:35 (4 sec)
No Signal (0.474)
And by the way, I don't really believe it's the Delta smelt, because nobody could do that.
Sean Hannity 00:25:35-00:25:37 (1 sec)
No StressLens
Just -- well --
Donald Trump 00:25:37-00:25:41 (5 sec)
No StressLens
It's not endangered either. They have it in other locations, et cetera.
Sean Hannity 00:25:41-00:25:47 (6 sec)
No Signal (0)
They're doing seemingly everything they could do. Like New York is, in many ways, to chase people away.
Donald Trump 00:25:47-00:25:49 (2 sec)
No StressLens
No, but can you imagine today --
Sean Hannity 00:25:49-00:25:49 (1 sec)
No StressLens
It's crazy.
Donald Trump 00:25:49-00:26:04 (14 sec)
No Signal (0.104)
-- when people -- and the press doesn't like, when I talk about the water that they're turning into the Pacific, the press never wants to put it on, the fake news. They don't want to put it on, Sean.
Sean Hannity 00:26:04-00:26:37 (33 sec)
No Signal (0)
But you do realize that you are permanently tattooed into the forehead of legacy media the term fake news. You do realize they spent nine years, nine years attacking you from the moment you came down that escalator and they didn't stop. And here's the interesting part to me is that all of the attacks, all the weaponization, all the FISA warrants, all the Russia, Russia and we can go on, all the various venues, the J6 Committee, which kept out a lot of pertinent information.
Donald Trump 00:26:37-00:26:43 (6 sec)
No Signal (0.227)
And how about the J6 Committee? I say -- I call it the unselect. You know, they say it's the select --
Sean Hannity 00:26:43-00:26:43 ( sec)
No StressLens
But they didn't win.
Donald Trump 00:26:43-00:26:47 (4 sec)
No StressLens
No, no, no. What they did was criminal. That's why they got pardoned.
Sean Hannity 00:26:47-00:26:47 (1 sec)
No StressLens
No. I was --
Donald Trump 00:26:47-00:26:52 (4 sec)
No StressLens
They deleted and destroyed all of the information that they collected over two years.
Sean Hannity 00:26:52-00:26:52 (1 sec)
No StressLens
Why else would they need a pardon?
Donald Trump 00:26:52-00:27:06 (14 sec)
No Signal (0.957)
And you know why? Because it proved I was right. All of that information was deleted and destroyed. They deleted all of the information having to do with the 10,000 soldiers that I offered to Nancy Pelosi and she's now on tape admitting it.
Sean Hannity 00:27:06-00:27:22 (16 sec)
No Signal (0)
I have four of the five people on tape, and General Milley was the fifth in writing, all saying that you authorized it in the days leading up. The Capitol Police chief asked for the guard, was begging for the guard. Muriel Bowser, in writing, denied the use of the guard.
Donald Trump 00:27:22-00:27:25 (3 sec)
No StressLens
And Nancy Pelosi even more strongly denied it.
Sean Hannity 00:27:25-00:27:26 (1 sec)
No StressLens
She said that.
Donald Trump 00:27:26-00:27:27 (2 sec)
No StressLens
She was responsible for the --
Sean Hannity 00:27:27-00:27:29 (1 sec)
No StressLens
She took responsibility.
Donald Trump 00:27:29-00:27:41 (12 sec)
No Signal (0.101)
She was responsible. And she took responsibility for her daughter when it was exposed. They found the daughter's tape, a videotape of her mother saying that she was responsible. And you know what? And they tried to lose it.
Sean Hannity 00:27:41-00:27:42 (1 sec)
No StressLens
Let me move on to --
Donald Trump 00:27:42-00:28:06 (24 sec)
No Signal (0.423)
The unselect -- remember this, the unselect committee, these people that were appointed, all Democrats plus two worse than Democrats, that's crying Adam Kinzinger and Liz Cheney who lost her congressional seat by more than any person in the history of Congress. She lost by a number that nobody has ever lost by. You know why?
Donald Trump 00:28:06-00:28:14 (8 sec)
No Signal (0.35)
Because usually when you have a poll and you're down by like 40 or 50 points, you're smart enough to drop out. She should have dropped out, at least she wouldn't have that moniker.
Sean Hannity 00:28:14-00:28:35 (21 sec)
No Signal (0)
Before I go to the economy and foreign policy, let me -- as long as you brought up this topic, Joe Biden, Chuck Schumer, Adam Schiff, who got a preemptive pardon. All these people that got pardoned, Anthony Fauci, did he know that NIH money through the EcoHealth Alliance was funding the Wuhan Virology Lab?
Sean Hannity 00:28:35-00:28:56 (20 sec)
No Signal (0)
There seems to be text and messages and e-mails that went back and forth. The -- you talk about the unselect committee, as you call it, the January 6th Committee, they had a predetermined outcome. General Milley, all these people, the Biden family members. Joe Biden ran and said he would never do preemptive pardons.
Sean Hannity 00:28:56-00:28:58 (2 sec)
No StressLens
It was an issue that came up when you were leaving your first time.
Donald Trump 00:28:58-00:29:14 (16 sec)
No Signal (0.655)
Sure. No, he thought -- he heard that I was going to do it. I didn't want to do it. I was given the option. They said, sir, would you like to pardon everybody, including yourself? I said, I'm not going to pardon anybody. We didn't do anything wrong. And we had people that suffered. They're incredible patriots.
Donald Trump 00:29:14-00:29:42 (28 sec)
No Signal (0.072)
We had people that suffered. You had Bannon put in jail. You had Peter Navarro put in jail. You had people that suffered. And far worse than that, they've lost their fortunes. They've lost their -- whatever their nest egg, paying it to lawyers. And those people -- and people said, you know what -- and they don't even -- they wouldn't have even taken -- most of those people, they wouldn't have even taken a pardon.
Donald Trump 00:29:42-00:29:58 (16 sec)
No Signal (0.264)
This guy went around giving everybody pardons. And you know, the funny thing, maybe the sad thing, is he didn't give himself a pardon. And if you look at it, it all had to do with him. I mean, the money went to him.
Sean Hannity 00:29:58-00:30:00 (2 sec)
No StressLens
Should Congress investigate that?
Donald Trump 00:30:00-00:30:02 (2 sec)
No StressLens
Well, I don't know. It's -- you know, I've always --
Sean Hannity 00:30:02-00:30:02 ( sec)
No StressLens
Will you order the --
Donald Trump 00:30:02-00:30:22 (19 sec)
No Signal (0.532)
I've always been -- look, he didn't give himself a pardon and he didn't give some other people a pardon that needed it. And I heard Schiff went to him and just begged him for a pardon because Schiff is a crook. Schiff is a crooked guy. He's a crooked politician. He made up the story about Russia, Russia, Russia.
Donald Trump 00:30:22-00:30:38 (17 sec)
No Signal (0.133)
He totally made it up. He's a storyteller. And then, after he made it up, they found out that there was a tape of the conversation made by, you know, I guess the State Department, I don't know. When you make calls, they make tapes sometimes, not all the time, but sometimes.
Sean Hannity 00:30:38-00:30:40 (1 sec)
No StressLens
He was the one talking to the Russians.
Donald Trump 00:30:40-00:30:59 (19 sec)
No Signal (0.835)
So, he, in the meantime, made up the conversation, totally made it up, about quid pro quo. There was no quid pro quo, just the -- there was a perfect call. Tim Scott was the first one to come. He read it. He said, this is a perfect call. What are you doing? You're impeaching a man for a perfect call. It was Schiff.
Donald Trump 00:30:59-00:31:15 (17 sec)
No Signal (0.662)
Schiff, Hillary, the whole group. You know what, they should -- Schiff is just a bad, sick. And he went to Biden and he demanded a pardon because he thought he did something. He knew he did something.
Sean Hannity 00:31:15-00:31:19 (4 sec)
No StressLens
Bennie Thompson won the chairman of that committee.
Donald Trump 00:31:19-00:31:30 (12 sec)
No Signal (0.242)
Bennie Thompson destroyed, destroyed -- along with that unselect committee destroyed all of the work that took place over two years. You know why? It showed that I was right.
Note 00:31:30-00:31:30 ( sec)
No StressLens
[Commercial break]
Sean Hannity 00:31:30-00:31:41 (11 sec)
No Signal (0)
So, you did run on a platform. You were very straightforward. You said you would pardon these people that were sentenced for January 6th.
Donald Trump 00:31:41-00:31:42 (1 sec)
No StressLens
Yes, totally.
Sean Hannity 00:31:42-00:31:56 (14 sec)
No Signal (0)
You did. The only criticism or pushback I've seen is about people that were convicted or involved in incidents where they were violent with police. Why did they get a pardon?
Donald Trump 00:31:56-00:32:18 (23 sec)
No StressLens
A number of reasons. Number one, they were in there for three and a half years, a long time. And in many solitary confinement, treated like nobody's ever been treated. Treated so badly. They were treated like the worst criminals in history. And you know what they were there for? They were protesting the vote because they knew the election was rigged and they were protesting the vote.
Donald Trump 00:32:18-00:32:24 (5 sec)
Strong (2.572)
1 of 138 paragraphs scored.
And that, you know, should be allowed to protest a vote. You should be allowed to. You know, the day -- when the day comes --
Sean Hannity 00:32:24-00:32:26 (2 sec)
No StressLens
But you shouldn't be able to invade the Capitol.
Donald Trump 00:32:26-00:32:47 (21 sec)
No Signal (0.447)
Yes. Ready? Most of the people were absolutely innocent. OK. But forgetting all about that, these people have served horribly a long time. It would be very, very cumbersome to go and -- look, you know, how many people are talking about? 1,500 people. Almost all of them are -- should not have been -- this should not have happened.
Donald Trump 00:32:47-00:33:02 (15 sec)
No Signal (0.61)
And the other thing is this, some of those people with the police, true, but they were very minor incidents. OK. You know, they get built up by that a couple of fake guys that are on CNN all the time.
Sean Hannity 00:33:02-00:33:03 (2 sec)
No StressLens
Nobody watching it.
Donald Trump 00:33:03-00:33:22 (18 sec)
No Signal (0.13)
They were very minor incidents. And it was time. You have murderers in Philadelphia. You have murderers in Los Angeles that don't even get any time. They don't even collect them and they know they're there to be collected. And then they go on television and act holier than thou about this one or that one.
Donald Trump 00:33:22-00:33:46 (24 sec)
No Signal (0.213)
You had 1,500 people that suffered. That's a lot of people. You know, they were looking for new people two weeks ago. They were looking -- wait a minute, they were looking to charge new people. They have a woman who's 76 years old that they said was -- made a statement that was a little bit out of line years after the fact.
Donald Trump 00:33:46-00:34:10 (24 sec)
No Signal (0.423)
This was a political hoax. And you know what, those people -- and I'm not saying in every single case, but there was a lot of patriotism with those people, a lot of patriotism. You know, they did a recording and you know, I -- they asked me if I do the voiceover and I did, do you know it was the number one selling whatever you call it nowadays, album, song --
Sean Hannity 00:34:10-00:34:10 ( sec)
No StressLens
CD?
Donald Trump 00:34:10-00:34:26 (15 sec)
No Signal (0.635)
-- whatever you call it, you don't know it changes every year, right? But it was the number one selling song, number one on billboard, number one on everything, on everything for so long, people get it. They wanted to see those people.
Sean Hannity 00:34:26-00:34:28 (2 sec)
No StressLens
American people were -- you told them what you would do.
Donald Trump 00:34:28-00:34:29 (2 sec)
No StressLens
Well, they voted for me.
Sean Hannity 00:34:29-00:34:34 (5 sec)
No Signal (0)
Joe Biden said he would not do it. Let me move on to the economy. This is so important.
Donald Trump 00:34:34-00:34:35 (1 sec)
No StressLens
But -- Excuse me.
Sean Hannity 00:34:35-00:34:37 (2 sec)
No StressLens
It was such a big -- yes.
Donald Trump 00:34:37-00:34:39 (2 sec)
No StressLens
I was very clear about it.
Sean Hannity 00:34:39-00:34:39 (1 sec)
No StressLens
Very clear.
Donald Trump 00:34:39-00:34:48 (9 sec)
No Signal (0.593)
I said I was going to release him. And probably very quickly. And they voted for me and I won in a landslide. And that was only one of the many reasons.
Sean Hannity 00:34:48-00:34:55 (7 sec)
No Signal (0)
And Joe said he would not do preemptive pardons back in 2020. Chuck Schumer said it. Schiff said it. They all said it. The media said it.
Donald Trump 00:34:55-00:35:12 (17 sec)
No Signal (0.001)
The precedent that he said on pardons is amazing. That's a much bigger story, but people don't like talking about it. He pardoned everybody, but he didn't pardon himself. And remember this, those people that he pardoned are now mandated because they got a pardon to testify and they can't take the feds.
Sean Hannity 00:35:12-00:35:14 (2 sec)
No StressLens
Should Congress investigate that
Donald Trump 00:35:14-00:35:17 (3 sec)
No StressLens
I think we'll let Congress decide.
Sean Hannity 00:35:17-00:35:19 (3 sec)
No StressLens
Would you want the attorney general to investigate it?
Donald Trump 00:35:19-00:35:27 (7 sec)
No Signal (0.925)
You know, I was always against that with presidents and Hillary Clinton. I could have had Hillary Clinton a big number done on her.
Sean Hannity 00:35:27-00:35:29 (2 sec)
No StressLens
Have you changed your mind?
Donald Trump 00:35:29-00:35:54 (26 sec)
Weak (1.265)
And I didn't want to -- well, I went through four years of hell by this scum that we had to deal with. I went through four years of hell. I spent millions of dollars in legal fees and I won, but I did it the hard way. It's really hard to say that they shouldn't have to go through it also. It is very hard to say that.
Donald Trump 00:35:54-00:36:01 (6 sec)
No Signal (0.039)
Joe Biden -- remember this, Joe Biden got very bad advice because like he has in everything.
Sean Hannity 00:36:01-00:36:02 (1 sec)
No StressLens
Hunter's --
Donald Trump 00:36:02-00:36:23 (21 sec)
No Signal (0.092)
He got bad advice on Ukraine. He got bad advice that war should have never started. He got bad advice on Israel. He got bad advice on the way he got out of Afghanistan. We should have gotten out with strength and dignity, not like a bunch of losers. Joe Biden has very bad advisers. Somebody advised Joe Biden to give pardons to everybody but him.
Donald Trump 00:36:23-00:36:25 (2 sec)
No StressLens
They wanted to take care --
Sean Hannity 00:36:25-00:36:26 (1 sec)
No StressLens
Let me get to the economy.
Donald Trump 00:36:26-00:36:27 (1 sec)
No StressLens
Yes. But, Sean --
Sean Hannity 00:36:27-00:36:28 (1 sec)
No StressLens
I'm running out of time.
Donald Trump 00:36:28-00:36:30 (2 sec)
No StressLens
-- they wanted to -- I don't care.
Sean Hannity 00:36:30-00:36:31 (1 sec)
No StressLens
They're yelling at me every time.
Donald Trump 00:36:31-00:36:33 (2 sec)
No StressLens
This is more important because --
Sean Hannity 00:36:33-00:36:33 (1 sec)
No StressLens
I agree.
Donald Trump 00:36:33-00:36:35 (2 sec)
No StressLens
-- right now the economy is going to do great.
Sean Hannity 00:36:35-00:36:37 (2 sec)
No StressLens
I want to know about the economy --
Donald Trump 00:36:37-00:36:50 (13 sec)
No Signal (0.044)
You know, I'm here. So, the -- but you have to understand he had bad advisers on almost everything. It's like in the old days when the secretary of state said he never made a correct decision on foreign policy. Joe Biden got very bad advice.
Sean Hannity 00:36:50-00:37:13 (23 sec)
No Signal (0)
You've been through two would-be assassins. You came within a millimeter of losing your life in this whole process. I know you kind of are somebody that compartmentalizes because I've known you so long, but do you ever think -- and you said this in your inaugural, that you really believe God saved your life so that this was your destiny.
Sean Hannity 00:37:13-00:37:14 (1 sec)
No StressLens
Explain that.
Donald Trump 00:37:14-00:37:37 (22 sec)
No Signal (0.388)
Well, I do believe that. I've had people that really know a lot about guns. And they said that gun, that particular gun and that beautiful field, as I called it in Pennsylvania, which it is Butler, that that gun's a very accurate gun. And that a bad shooter would hit the target 100 percent of the time.
Sean Hannity 00:37:37-00:37:38 (1 sec)
No StressLens
You can't miss.
Donald Trump 00:37:38-00:37:39 (2 sec)
No StressLens
OK. From that distance.
Sean Hannity 00:37:39-00:37:39 ( sec)
No StressLens
I'm --
Donald Trump 00:37:39-00:37:58 (18 sec)
Medium (1.749)
Yes, from that distance. I mean, to me, I didn't know -- I don't know as much about it. They said it's like for a golfer sinking a one-foot putt from that distance. And my son Don and my son, both of them, Eric, they're great shooters. Both of them were great shooters. And they said it's amazing. It's a miracle.
Donald Trump 00:37:58-00:38:22 (24 sec)
No Signal (0.474)
I think it affected them because they can't believe that that happened. I turned -- if I didn't turn it -- you know, when -- the turn was like split second, perfect timing. So, something happened and I don't think you can call it just luck. It was -- the chance was like one-eighth of a second or we wouldn't be sitting here.
Donald Trump 00:38:22-00:38:28 (6 sec)
No Signal (0.157)
Think of it, in a volume of time, one-eighth of a second I was in the right position.
Sean Hannity 00:38:28-00:38:38 (10 sec)
No Signal (0)
Do you believe that moment? People say to me, they see a change in you. Do you believe you've changed? Is this, for example, increased your faith in God?
Donald Trump 00:38:38-00:38:55 (17 sec)
No Signal (0.314)
Yes, I think so. I don't think I've changed, but I think that has taken place, yes. Because when you look at statistically, I should never be here. I mean, if I don't turn my -- I'm looking at an immigration chart. My favorite chart ever in history.
Sean Hannity 00:38:55-00:38:56 (1 sec)
No StressLens
Yes.
Donald Trump 00:38:56-00:38:58 (2 sec)
No StressLens
Even if it was a bad -- even if the numbers were bad, I wouldn't --
Sean Hannity 00:38:58-00:39:02 (3 sec)
No StressLens
I mean, we're talking about assassination and you're telling jokes.
Donald Trump 00:39:02-00:39:03 (2 sec)
No StressLens
Can you believe it? No, no. Can you believe it
Sean Hannity 00:39:03-00:39:06 (2 sec)
No StressLens
-- it's terrible. I remember that day like yesterday.
Donald Trump 00:39:06-00:39:23 (17 sec)
No Signal (0.178)
When I turned -- and it had to be at exactly 90-degree angle. And I said, throw down the chart or something to that effect. And they bring the chart, and I'm literally looking exactly at the right angle. I couldn't have even been a little further or a little bit less. It would have whacked. Because it was an eighth of an inch.
Donald Trump 00:39:23-00:39:25 (2 sec)
No StressLens
The entire ride was an eighth of an inch.
Sean Hannity 00:39:25-00:39:37 (12 sec)
No Signal (0)
Will you investigate these assassination attempts? And you stated that you will release the files, all of the files, as it relates to the JFK assassination. And by the way, this is his desk.
Donald Trump 00:39:37-00:39:38 (1 sec)
No StressLens
Yes, that's right.
Sean Hannity 00:39:38-00:39:41 (3 sec)
No StressLens
This is it. This is where John Ken and little John Kennedy --
Donald Trump 00:39:41-00:39:42 (1 sec)
No StressLens
That's a movable door.
Sean Hannity 00:39:42-00:39:43 (1 sec)
No StressLens
Yes.
Donald Trump 00:39:43-00:39:46 (3 sec)
No StressLens
It's a little door there. That's where John John was.
Sean Hannity 00:39:46-00:39:56 (11 sec)
No Signal (0)
John John, yes. And RFK. And also, Martin Luther King Jr. And that you will be transparent. You -- this was going to happen in the first term.
Donald Trump 00:39:56-00:40:22 (25 sec)
No Signal (0.315)
So many people have asked me to do that. And I did it with Kennedy to an extent. But I was asked by some of our government officials not to. And, you know, you have to respect them. I was actually asked by Mike Pompeo, his secretary of state, not to. And he -- I felt he knew something that maybe, you know, when he asks you not to, you sort of say why.
Donald Trump 00:40:22-00:40:45 (23 sec)
No Signal (0.388)
And he felt that it was just not a good time to release him. And you might ask him why, maybe he'll deny that even. But he did. He asked me. And some others also, though, they didn't want the Kennedy stuff released. And they're professionals and I respect them, and they're working for me and the country.
Donald Trump 00:40:45-00:40:56 (11 sec)
No Signal (0.12)
They're working for the country. And so, I didn't release. But I'm going to release them immediately upon getting. We're going to see the information. We're looking at it right now.
"""  # ← Replace this with the full messy transcript from the file or copy-paste

# STEP 2: Use regex to extract (speaker, text) pairs
pattern = re.compile(r'(Sean Hannity|Donald Trump)[^\n]*\n(?:No StressLens|No Signal.*)?\n(.*?)\n', re.DOTALL)
matches = pattern.findall(raw_transcript)

# STEP 3: Format the extracted lines
formatted_lines = [f"{speaker}: {line.strip()}" for speaker, line in matches]

# STEP 4: Set your custom save path
folder_path = "cleaned_text"
filename = "Trump_Hannity_Interview.txt"
full_path = os.path.join(folder_path, filename)

# STEP 5: Create folders if they don’t exist
os.makedirs(folder_path, exist_ok=True)

# STEP 6: Write the cleaned text to file
with open(full_path, "w", encoding="utf-8") as f:
    f.write('\n'.join(formatted_lines))

