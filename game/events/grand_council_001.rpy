label grand_council_001:
    
    default heard_coin = False
    default heard_palace = False
    default heard_gardens = False

    scene black

    n "A week had already passed in my reign; to me, it felt an eternity."

    n "Days of receiving dignitaries from across the Empire and its subjects, overlooking military parades and citizen gatherings in my honor, attending one lavish banquet after another, only to overnight be convoyed between planets to do everything all over again—it was fatiguing."

    n "That does not touch on how overstimulated I felt." 
    
    n "One can eat only so many lavish dishes and desserts before wishing just for a plain slice of bread with cold cuts. The exclusive vintage alcohol constantly offered in toast to my reign furthermore didn’t help me keep a straight mind throughout the whole ordeal."

    n "Needless to say, I was socially exhausted, physically spent, and longed to lock myself in the palace with nothing but my own company."

    n "Yet upon my return to Isa Bellmaré, I was scheduled to meet for the first time with my Castilles—Suzerain’s Council of Councils, and the highest governing body in the Empire beyond myself."

    n "I was to receive a formal introduction from each of the Pueblidorés, Council Delegates, who collectively represented the Polysynodial administration which made up the Empire."

    n "While I nevertheless held final say in all matters, the Pueblidorés ensured the lifeblood of my domains continued to flow without direct input." 
    
    n "In theory, these Councils were to enforce my will in its absolute definition, yet as I was always reminded growing up, Suzerains, when not having their own wishes satisfied, eventually twist the extents of their duties to me."
    
    n "This I had to remember now that it was me who held the reins."

    n "Nothing would be decided or unveiled from the Councils this particular meeting; that was saved for their official briefings on the state of Suzerain’s wellbeing to be conducted on a later day, thankfully."

    n "But this was still a pivotal moment. I knew the Pueblidorés from seeing them work with my Grandmother, but never got a good feeling for their characters."

    n "Without even a second to rest after my journey home, I was led directly from my shuttle to the Castilles Meeting Chamber, informed along the way by excited and pushy servants how the Pueblidorés were already gathered and waiting for me."

    n "I felt for a moment like things had gotten mixed up—that it shouldn’t have been I rushing to meet with the Council in their time, but rather the other way around. In any case, I sped my way through the palace."

    n "Upon reaching the chamber’s gilded portals, decorated in Suzerish silver and Caetzan jewels, I took one brief breath to recompose myself."

    n "I nodded to the attendant beside me, and he threw open the doors, dramatically announcing me as..."

    n "\"His Imperial Majesty Emperor Pherip IV! Emperor of Suzerain, Grand Duke of Isa Bellmaré, Duke of Mexi Taquonno and Bejár Gemba, First Successor to Empress Sicill the Unifier, Baron of Che, Vines, Bellaciao, and Torus!\""

    n "Et cetera, et cetera."

    n "It felt very unnatural to be received with so many titles. They had all but doubled since my ascension to the throne."

    scene expression Transform(
        "images/Castilles_Background.png",
        xsize=config.screen_width,
        ysize=config.screen_height
    )

    n "Striding across the intricate marble floors, I looked up at the chamber’s barrel-vaulted ceiling, adorned with frescos depicting victories from across Suzerain’s history, ranging from battlefield conquests to development projects."

    n "Across the hall was the Castilles Imperial Throne. Not my main one, perhaps, but regal in its splendor all the same."

    n "Its emerald-green silks, golden armrests, and backrest with the Suzerish coat of arms carved into it felt both inviting and intimidating, yet also allured me in its aura of power."

    n "My Pueblidorés stood at attention from their seats on the rectangular meeting table, crafted of dark wood and carved with designs of gold and silver, watching my every move."

    menu:

        "I made an effort to appear imperious, strutting to my throne without paying mind to the Pueblidorés.":

            $ authority += 1
            $ council_approval -= 1

            n "Though I kept my eyes ahead, I could tell upon majestically turning and taking my seat that the Pueblidorés were in awe at my presence."

            n "The glimmer of respect on their faces was unmistakable. I, to them, was not an equal, but a superior to be served."

        "I attempted to survey the Pueblidorés, giving them an expression of sincerity as I did.":

            $ authority -= 1
            $ council_approval += 1

            n "Shifting my gaze from each Pueblidoré, I saw both young and old, soft and strict, servile and ambitious faces among them staring back at me."

            n "I gave each a smile and nod in acknowledgement, fostering already the beginnings of a connection that I hoped to start off on equal footing."

            n "I could tell they all appreciated my intentions, regardless of the execution."

    n "Having placed myself on the throne, my Councillors followed suit."

    show expression "quixote" as portrait

    n "First to rise again was Lord Councillor Quixote fue Ostamara, Duke of Valensia and the official middleman between myself and the rest of the Council."

    n "His feathers puffed proudly as he addressed me, adjusting his glasses to read off a sheet of paper he held dramatically before everyone."

    show expression "quixote" as portrait
    show expression "quixote" as portrait
    q "By consent of the various Council heads and their chosen Pueblidorés, it is my honor as Lord Councillor to officially commence the first meeting of the Castilles under Emperor Pherip IV."

    q "Long may he reign!"

    n "The other Councillors repeated his declaration."

    q "Furthermore, I would like, as my first act under this reformed Council, to propose a swear of allegiance to His Majesty the Emperor."

    q "All those in favor?"

    n "The rest of my Councillors swiftly opened their trains to only extend slightly beyond their shoulders, a sign of agreement."

    n "Quixote smiled, and turned to face me directly."

    n "With a booming voice of authority, though also a boyish enthusiasm that sat strangely upon a man of his age, Quixote shouted across the halls."

    q "I SWEAR MY ETERNAL ALLEGIANCE TO HIS IMPERIAL MAJESTY, EMPEROR PHERIP IV!"

    q "I SHALL DO MY UTMOST TO SECURE HIS RULE AND ENFORCE HIS WILL ACROSS THE EMPIRE, EVEN AT THE COST OF MY OWN PROSPERITY AND LIFE, SHOULD HE DEMAND!"

    n "Finishing with a dramatic bow, Quixote once again sat down."

    n "I could tell Quixote was certain his gesture went over well with me, though I didn’t figure whether his words were sincere, or just a means of gaining my favor."

    n "I'd have to get better in future at differentiating that."

    menu:
        "Your loyalty to the Crown is to be commended, Lord Councillor. I look forward to working with you throughout my reign.":

            $ quixote_relationship += 2

            p "Your loyalty to the Crown is to be commended, Lord Councillor. I look forward to working with you throughout my reign."

            n "Quixote almost blushed with joy at my praise."

            n "He looked around at the other Pueblidorés in an effort to show off."

        "Quite. Let's move on to more important matters, shall we?":

            $ quixote_relationship -= 1

            p "Quite. Let's move on to more important matters, shall we?"

            n "Quixote's smile gave way to a frown."

            n "He had not expected in a million years that to be my reaction."

            n "He slouched a bit into his chair in embarrassment, trying to hide his emotions."

        "Very well, Lord Councillor. You may leave the keys to your estate on your way out, so is my will.":

            $ furique_relationship += 1

            p "Very well, Lord Councillor. You may leave the keys to your estate on your way out, so is my will."

            n "For a split second, Quixote's eyes widened in fear and bewilderment."

            n "I noticed some others in the Council, namely Furique, grin amusingly at him."

            menu:

                "I was joking, Quixote. Thank you for your gesture of loyalty.":

                    p "I was joking, Quixote. Thank you for your gesture of loyalty."

                    n "Quixote's shoulders relaxed, and Furique let out a short laugh."

                    n "Trying to seem in on the joke, Quixote laughed as well, though it only made him look all the more clueless."

                    q "Yes… How clever, Your Majesty."

                "Relax, Quixote, I'm not after your riches. Not YET, anyway…":

                    $ quixote_relationship -= 1
                    $ furique_relationship -= 1

                    p "Relax, Quixote, I'm not after your riches. Not YET, anyway…"

                    n "Quixote remained tense, and the jovial attitude several of my Pueblidorés once had quickly evaporated."

                "Tough crowd. Remind me not to make you Court Jester anytime soon…":

                    $ furique_relationship += 1

                    p "Tough crowd. Remind me not to make you Court Jester anytime soon…"

                    n "Furique couldn't help but laugh, and the rest of my Pueblidorés rolled their eyes with a grin."

                    n "Quixote, taking a few seconds to understand the joke, laughed louder than everyone else to seem like he got it from the beginning."

                    q "Yes! Very funny indeed, Your Majesty."

        "(Say nothing)":

            $ quixote_relationship += 1

            n "I gave no reaction."

            n "Quixote took my serene neutrality as a sign of approval, and grinned to the other Pueblidorés in triumph."

    n "Quixote, having said his piece, looked around for whoever next wanted to speak."

    n "After realizing Quixote was done talking, Furique Vallitu arose to address me."
    
    hide quixote
    
    show expression "furique" as portrait

    n "He had become renowned as a non-aristocratic man of such immense financial talent that Empress Sicill personally appointed him Haciende of the Treasury and Economy."

    n "Some rumored my Grandmother only did this because she thought Furique to be funny. But none could deny the prosperous times in which we currently lived, nor how Furique had played a large part in them."

    n "Furique gestured to Quixote with a grin."

    show expression "furique" as portrait
    show expression "furique" as portrait
    f "I've always said the theatre was robbed of such a grand performer, Lord Councillor."

    n "Quixote grinned."

    n "Based on no one's astonishment at Furique's lack of propriety, I understood this was far from unusual for him."

    n "Furique turned to me and bowed his head before continuing."

    f "Your Majesty, it is a true pleasure to speak for the first time as your subject. History shall know you to be amongst one of the great Monarchs in the galaxy."

    f "Makes me curious what title shall be ascribed to you when the time comes…"

    menu:

        "Generic, perhaps, but Pherip the Great would be ideal.":

            p "Generic, perhaps, but Pherip the Great would be ideal."

            f "I agree."

            f "If you'd want something more interesting, we could always aim for you being the first Emperor with two titles, eh?"
            
        "Seeing as how my Grandmother preferred Unifier over Conqueror, a martial title sounds appealing.":

            p "Seeing as how my Grandmother preferred Unifier over Conqueror, a martial title sounds appealing."

            n "Furique gestured toward my Captain General, Gaucho fue Léon."

            f "For that, the younger of the fue Léons would be a better consultant."

            f "The only thing I understand about arms is they make heaps of money."

            f "Speaking of, please remind me to elaborate on that at a later date if I forget, Your Majesty."

        "What do you hope my reign will be known for, Haciende?":

            p "What do you hope my reign will be known for, Haciende?"

            f "Me? Hmmm..."

            n "Furique placed a hand to his beak in contemplation."

            f "Call me biased, but 'Emperor Pherip the Golden Touched' has a nice ring to it."

            show expression "gaucho" as portrait
            g "If there's one thing our Empire has no more need of, it's gold, Furique."

            show expression "furique" as portrait
            f "I could say the same of territory, Gaucho."

            show expression "gaucho" as portrait
            g "So long as those Fespians are still a relevant galactic player, our wars are far from complete."

            show expression "quixote" as portrait
            q "Do wait your turn to consult His Majesty, Captain General."

            show expression "gaucho" as portrait
            g "My apologies, Your Grace."

        "My actions shall decide as much. We have naught but to see what will come.":

            p "My actions shall decide as much. We have naught but to see what will come."

            show expression "furique" as portrait
            f "Not fond of speculation, Your Majesty?"

            f "Fair enough. I've seen plenty of investors make life-ruining decisions based purely on speculation to sympathize with being risk-adverse."

            f "Still, whatever it ends up being, I hope it's a good one."

    show expression "furique" as portrait
    f "Though we've still much to talk about, I'll allow my fellows to make themselves known."

    hide furique

    n "Furique sat once again."

    n "Both fue Léon brothers peered at each other, waiting for the other to get up."

    n "After a few moments of their indecisiveness, Marquise Aurgenbia Panzarre, my Indes of Colonial Affairs, let out an annoyed sigh and took the initiative."

    show expression "aurgenbia" as portrait

    show expression "aurgenbia" as portrait
    a "My Emperor, on behalf of the Empire's many Colonies and subjects, let me convey our continued support for the Suzerish Royal Family."

    a "Rest assured, any detractors from this sentiment will be made to conform."

    a "I've crushed a hundred revolts, and shall destroy a thousand more to maintain peace in the realm."

    a "You won't have a single upstart threaten the core worlds, or my name is Aurgenbia Panzrrico."

    n "Panzrrico was a play on the word 'Ricco,' meaning 'Moron.'"

    n "Aurgenbia's curt statements and authoritative aura juxtaposed with her grandmotherly expression."

    n "Having once been Governor for an archipelago colony on Isa Bellmaré, back before our ascension into space redefined 'colonies' as encompassing other planets, she had served my Grandmother longer than some of my Councillors had been alive."

    menu:

        "Your long service to Empress Sicill has earned you this duty. I expect great things from you, Indes.":

            $ aurgenbia_relationship += 1

            p "Your long service to Empress Sicill has earned you this duty. I expect great things from you, Indes."

            a "You flatter me, my Emperor."

            a "I'll ensure your name too is synonymous with \"Order\"."

            a "My only regret is I won't live long enough to see the full extent of your era."

            a "But I suppose that's a good thing, considering the alternative."

            show expression "quixote" as portrait
            q "Most certainly. I hope we all die long before His Majesty."

            show expression "torrez" as portrait
            t "A grim way of putting it. But we understand the point, Your Grace."
            
        "There still is much work to be done for our assimilation programs, Indes. I trust you will see them through.":

            $ aurgenbia_relationship += 1

            p "There still is much work to be done for our assimilation programs, Indes. I trust you will see them through."

            show expression "aurgenbia" as portrait
            a "We hold the same vision, Your Majesty."

            a "Personally, my eyes have been set on finally bringing the Zereck brutes to heel."

            a "If we can take their tropical planets and put them to use for our raw resource production, I'll be a happy woman."

            show expression "furique" as portrait
            f "Spoken like... Well... Myself, Your Grace."

            f "I've already been preparing a regional development project to that exact end, assuming the late Empress's agricultural survey bears fruit."

            f "Literally and figuratively."

            n "Furique threw a grin at Aurgenbia."

            n "Aurgenbia smiled with a short laugh."

            show expression "aurgenbia" as portrait
            a "I'm hoping for more than just fruit, Furique."

        "Our Empire is as diverse as it is large. Remember that is a strength we must rely on, not a weakness.":

            $ aurgenbia_relationship -= 1
            $ torrez_relationship += 1

            p "Our Empire is as diverse as it is large. Remember that is a strength we must rely on, not a weakness."

            a "Respectfully, Your Majesty, in my experience allowing disunity is what breeds resentment to Suzerain's authority."

            a "To YOUR authority."

            a "I'll be sure to explain as much in the near future."

    show expression "aurgenbia" as portrait
    a "Alas. I don't have much more to touch on this meeting."

    a "We'll save most of it for our scheduled Colonial Briefing at Palles Sicillia next week."

    a "On the topic of, are you more of a Zereck or Kammarian cuisine type of man, Your Majesty?"

    menu:

        "Some may think it uncivilized, but there is a certain allure of Zereck fire roasts. I'd have to go with that.":

            $ colony_preference = "zereck"

            p "Some may think it uncivilized, but there is a certain allure of Zereck fire roasts. I'd have to go with that."

            a "I wouldn't have expected, frankly, but also do not disagree in the slightest."

        "Kammarian, no doubt. I recall the seafood dishes served when visiting Evoui always went beyond any expectations.":

            $ colony_preference = "kammarian"

            p "Kammarian, no doubt. I recall the seafood dishes served when visiting Evoui always went beyond any expectations."

            a "Ah. The junior Empress, yes."

            a "You'll be happy to know she remains a content resident here on Isa Bellmaré, awaiting her theoretical reinstatement to the Kammarian throne."

            show expression "gaucho" as portrait
            g "Emphasis on \"theoretical\"."

            menu:

                "What do you mean by that, Your Grace?":

                    p "What do you mean by that, Your Grace?"

                    n "Gaucho straightened up, an expression of intent forming on his face."

                    n "By the shifting in their seats, I understood my other Councillors were nervously bracing for whatever came out of his beak."

                    g "All glory to Her late Majesty, but Empress Sicill's sisterly affection was the only thing which entertained the notion of letting that traitor back on her throne."

                    g "Were it up to me, I'd have organized Evoui's execution days ago."

                    show expression "torrez" as portrait
                    t "For God's sake, Gaucho!"
                    
                    show expression "gaucho" as portrait
                    g "Nuts to it! I'm certain he agrees Evoui's actions during the war were both appalling and underpunished."

                    g "Familial ties or not, it remains the opinion of myself and the officer corps that she be brought to justice once and for all!"

                    n "Torrez appeared like he wanted to strangle Gaucho so as to shut him up."

                    n "The others were mortified at his bluntness. However, from Aurgenbia's more shocked than appalled demeanor, she perhaps also put stock into what was said."

                    n "With a huff, having said his piece, Gaucho got the message that his time to speak freely was over."

                    menu:

                        "Captain General, your position on my Council does not give you the right to insult and even threaten violence against a member of the royal family, scandal or not. You will apologize this instant.":

                            $ gaucho_relationship -= 1

                            p "Captain General, your position on my Council does not give you the right to insult and even threaten violence against a member of the royal family, scandal or not. You will apologize this instant."

                            n "Gaucho narrowed his eyes."

                            g "Or...?"

                            n "Torrez at once opened his beak to intervene, but Aurgenbia held up a hand to stop him."

                            menu:

                                "Or I'll have you flogged, dunked in a barrel of salt, paraded through town wearing shoes of thorns, and thrown into the worst prison camp Quixote can find.":

                                    $ gaucho_relationship += 4

                                    p "Or I'll have you flogged, dunked in a barrel of salt, paraded through town wearing shoes of thorns, and thrown into the worst prison camp Quixote can find."

                                    n "To my and everyone else's surprise, apart from Torrez, Gaucho smiled from ear to ear."

                                    n "He pointed a finger at me while looking to his brother."

                                    g "Now THAT'S an Emperor I can get behind. One not afraid to put even his own Pueblidorés in line."

                                    g "Suzerain's had too many Monarchs in its history willing to back down when an upstart noble forgets their place. I'm proud to see you won't be one of them."

                                    n "Gaucho bowed his head to me."

                                    g "Your most awe-inspiring Majesty, please forgive me for that brief confrontation. Know I am most apologetic for any disrespect shown to you, and it won't happen again."

                                    g "Probably."

                                    show expression "torrez" as portrait
                                    t "Definitely!"

                                    menu:
                                        "Do not test me, Gaucho. I am Emperor, it is not I who must prove themself to YOU.":

                                            p "Do not test me, Gaucho. I am Emperor, it is not I who must prove themself to YOU."

                                            jump aurgenbia_reconvene

                                        "You're on thin ice. Torrez, keep your brother in line from now on.":

                                            p "You're on thin ice. Torrez, keep your brother in line from now on."

                                            t "I try. I really do."

                                            t "Seems I must double my efforts."

                                            jump aurgenbia_reconvene

                                        "A bold play, Your Grace. Lucky for you, I favor the bold.":

                                            $ gaucho_relationship += 1

                                            p "A bold play, Your Grace. Lucky for you, I favor the bold."

                                            show expression "gaucho" as portrait
                                            g "We'll get along swimmingly then. I foresee a strong partnership that'll reshape the galaxy."

                                            jump aurgenbia_reconvene

                                "We'll continue this discussion at a later date, Captain General...":

                                    p "We'll continue this discussion at a later date, Captain General..."

                                    show expression "gaucho" as portrait
                                    g "Come, Your Majesty, don't back down so easily."

                                    g "At least respond with a threat of your own. You can't let people get away with something like that."

                                    n "I didn't understand what was going on."

                                    n "Everyone else seemed to have gotten that impression from my lack of comment."

                                    show expression "torrez" as portrait
                                    t "Please pay him no mind, Your Majesty. My Brother just wants to test the waters."

                                    t "Gaucho's always been of the opinion Nobles, among others, should not think themselves privy to treat the Monarch like another avenue of personal gain."

                                    t "Sometimes his soldier mentality leads him to express that more brashly than he ought to."

                                    n "Gaucho let out a hearty laugh and looked at me with sympathy."

                                    show expression "gaucho" as portrait
                                    g "I can't deny anything he said is inaccurate."

                                    g "I humbly apologize for my \"brash\" behavior, Your Majesty."

                                    g "Simply put, there will be plenty of pawns you'll have to manage who shall wish to turn things around and make you their pawn."

                                    g "That cannot be allowed."

                                    g "My objective then is to condition you from enabling such behavior before it takes root."

                                    show expression "aurgenbia" as portrait
                                    a "Perhaps the Emperor himself should decide whether he is in need of your tutoring, Gaucho."

                                    show expression "gaucho" as portrait
                                    g "A good point, Ma'am."

                                    g "Feel free to take or reject my advice as you wish."

                                    g "Either way my hopes are realized."

                                "Do not push your luck, Captain General. I can and WILL make you the one with a set execution date.":

                                    $ gaucho_relationship += 2

                                    p "Do not push your luck, Captain General. I can and WILL make you the one with a set execution date."

                                    n "To my and everyone else's surprise, apart from Torrez, Gaucho smiled from ear to ear."

                                    n "He pointed a finger at me while looking to his brother."

                                    g "Oof. Missing a bit of flair, but I'll certainly take that fury."

                                    g "Suzerain's had too many Monarchs in its history willing to back down when an upstart noble forgets their place."

                                    g "I'm proud to see you won't be one of them."

                                    n "Gaucho bowed his head to me."

                                    g "Your most awe-inspiring Majesty, please forgive me for that brief confrontation."

                                    g "Know I am most apologetic for any disrespect shown to you, and it won't happen again."

                                    g "Probably."

                                    show expression "torrez" as portrait
                                    t "Definitely!"

                                    jump aurgenbia_reconvene

                        "Putting aside my personal thoughts on Evoui, I won't make a decision on what is to be done with her at this moment. Your report shall shed more light on the subject, Indes.":

                            $ torrez_relationship += 1

                            p "Putting aside my personal thoughts on Evoui, I won't make a decision on what is to be done with her at this moment. Your report shall shed more light on the subject, Indes."

                            n "Everyone let out exhales of relief at my defusion of the situation."

                            n "Torrez seemed especially glad his Brother was let off the hook."

                            show expression "aurgenbia" as portrait
                            a "Naturally."

                            a "The breakdown for which is already sitting on my desk."

                            jump aurgenbia_reconvene

                        "My Great Aunt, while not without fault, shall bear no responsibility for how the Kammarian swayed her during the war. I can't have a member of the royal family officially punished, let alone executed. End of story.":

                            $ gaucho_relationship -= 3
                            $ quixote_relationship += 1

                            p "My Great Aunt, while not without fault, shall bear no responsibility for how the Kammarian swayed her during the war. I can't have a member of the royal family officially punished, let alone executed. End of story."

                            show expression "quixote" as portrait
                            q "Hear! Hear!"

                            show expression "gaucho" as portrait
                            g "But surely you-"

                            n "Torrez leaned over the table and smacked his palm on it, which echoed strongly across the chamber."

                            n "He gave a death-ridden stare to Gaucho."

                            n "Gaucho got the message and leaned back in his chair, beaten but not defeated."

                            g "By your command, my Emperor..."

                            n "A few seconds passed as everyone's heightened tempers died down."

                            n "Aurgenbia cleared her throat."

                            jump aurgenbia_reconvene

                "I expect her fate to be the topic of our meeting too, Aurgenbia.":

                    p "I expect her fate to be the topic of our meeting too, Aurgenbia."

                    show expression "aurgenbia" as portrait
                    a "Naturally."

                    a "The breakdown for which is already sitting on my desk."

                    jump aurgenbia_reconvene


label aurgenbia_reconvene:
    
    show expression "aurgenbia" as portrait

    a "With all that being said, I'll defer to one of the fue Léons."

    a "Ideally you've by now decided who wants to speak first, gentlemen."

    n "Aurgenbia gave a coy grin, and the brothers looked to each other, still unsure."

    n "With the most desynchronized mindset possible, Torrez and Gaucho both stood up and began to make introductions over one another at the exact same time."

    n "A few words in, they both looked to one another, irritated."

    n "Flaring his eyes, Torrez indicated his intention to speak first, and Gaucho acquiesced."

    hide aurgenbia
    show expression "torrez" as portrait

    n "Turning to me once again, Count Torrez fue Léon, my First Envoy of Foreign Affairs and patriarch of the numerically largest Noble family in Suzerain, brushed his head awkwardly and continued to speak."

    show expression "torrez" as portrait
    t "Do excuse that sorry display."

    t "My Brother and I have infamously struggled to be on the same page."

    t "Our chosen offices likely tipped you off to that already."

    menu:

        "Indeed. One sibling leads the war machine, one holds it back. I'd love to hear how you both remain on good terms out of work.":

            p "Indeed. One sibling leads the war machine, one holds it back. I'd love to hear how you both remain on good terms out of work."

            t "Contrary to the peace symbols that line my office, I actually hold no grudge against warhawks like my brother."

            t "Force of arms, as our nation has seen, can be a vital and sometimes necessary tool to achieve that which diplomacy cannot."

            t "In the extremely wise words of Empress Sicill, \"A bayonet against one's chest does wonders to turn them agreeable.\""

            show expression "furique" as portrait
            f "Wasn't it you who drafted that particular speech, Your Grace?"

            show expression "torrez" as portrait

            n "Torrez blushed and smiled, having been caught."

            t "Doesn't make it any less true."

        "I detect an older sibling getting the younger out of trouble dynamic here, Your Grace.":

            p "I detect an older sibling getting the younger out of trouble dynamic here, Your Grace."

            t "Your skills of deduction are quite refined."

            t "I've gotten Gaucho out of enough scrapes to learn a thing or two on talking people down."

            t "At the same time, Gaucho's big mouth occasionally caused trouble past reproach, in which instance knowing how to fight served us well."

            n "To this, Gaucho turned his head to reveal a slash of missing feathers across his lower neck, a nasty scar."

            show expression "gaucho" as portrait
            g "Had Torrez not beaten this one son of a Baron who pulled a knife on me to a bloody pulp, I'd not be alive."

            show expression "torrez" as portrait
            t "Helps to keep peace and violence in equal regard."

    show expression "torrez" as portrait
    t "My role now as peacekeeper is more relevant than ever before."

    t "An Empire of our size may seem unstoppable, but only so long as we can keep the powers that be divided on when they wish to strike back at us."

    t "Better still to point their frustrations at one another instead of us."

    menu:

        "No offense, but I'm more a believer in larger fleets keeping our Empire together than diplomatic maneuvering.":

            p "No offense, but I'm more a believer in larger fleets keeping our Empire together than diplomatic maneuvering."

            show expression "gaucho" as portrait
            g "The fact such a sentiment benefits me and yet I agree with Torrez should speak volumes, Your Majesty."

            g "My fleets and armies strike fear in our neighbors and bend them to our—your—will."

            g "But without kind words to proceed and follow up our thrashings, we'll be in no better a geopolitical position than the Zereck Domain was."

            g "And we saw how that turned out for them, didn't we?"

        "Makes sense. Without your outplay of the Zerecks and Kammarians, Suzerain would've remained a subject of the Ajour Assembly or had its expansion halted, respectively.":

            p "Makes sense. Without your outplay of the Zerecks and Kammarians, Suzerain would've remained a subject of the Ajour Assembly or had its expansion halted, respectively."

            n "Torrez nodded in agreement."

    show expression "torrez" as portrait
    show expression "torrez" as portrait
    t "Precisely."

    t "On which topic, the Captain General should at last make his formal introductions."

    n "Torrez remained standing, and Gaucho, his younger brother and Captain General of War and Security, joined him."

    hide torrez
    show expression "quixote" as portrait

    n "Taking out a watch and peering at it with squinted eyes through his glasses, Quixote spoke up."

    show expression "quixote" as portrait
    q "Do make it quick, Your Grace."

    q "We've already run long overtime. Too many interruptions."

    q "I'm sure the Emperor would love to have dinner before it turns the next day."

    show expression "gaucho" as portrait
    g "As timekeeper, perhaps you should've spoken up quite a bit earlier, Lord Councillor."

    hide quixote
    show expression "furique" as portrait

    show expression "furique" as portrait
    f "Admit it."

    f "You only just noticed how late it is."

    hide furique
    show expression "quixote" as portrait

    show expression "quixote" as portrait
    q "I— O-Of course not!"

    n "Huffing at such an accusation, Quixote tried to think of an excuse, but none came to mind."

    n "I glanced at my own watch and felt deflated at how long we'd spent doing nothing more than saying 'Hello.'"

    n "I mentally braced for the many chatty meetings which lay ahead, and prayed Gaucho kept it to the point so I could eat and go to bed."

    hide quixote

    show expression "gaucho" as portrait
    g "I suppose to make up for lost time..."

    g "Greetings, Your Majesty."

    g "Like my brother clarified, I am the one who ensures Suzerain can hold its own against any threats, external or internal."

    g "In accordance with the entire war staff and its forces, we swear our loyalty and submission before you."

    g "The most powerful army and armada the galaxy has ever laid eyes upon is at your disposal."

    g "Decide how you wish to mold the future, and we'll carve it out for you."

    g "That is all."

    n "Ending with a firm and calculated bow, Gaucho sat down."

    n "Torrez followed along."

    show expression "quixote" as portrait

    n "Quixote grunted in satisfaction at Gaucho taking his request into account, then stood up, fixing his suit as he did."

    show expression "quixote" as portrait
    q "Thank you, everyone, for your kind words to the Emperor."

    q "I sincerely hope they were to your satisfaction, Your Majesty."

    q "Before I can responsibly call this meeting to an end, there is but one more matter left on our agenda."

    q "It is of great interest, I'm sure you will all agree."

    q "That being, the question of what shall formally be Emperor Pherip's first Imperial decree?"

    n "Quixote presumed correctly. My Councillors and I sat up in renewed anticipation."

    n "My first act as Emperor."

    n "I had been waiting for this my whole life."

    n "The time when I'd finally live up to the role prepared for me since birth."

    n "So many thoughts flew through my head at once that I was thankful Quixote didn't leave this task entirely to me."

    n "He whistled, and an attendant approached carrying a notebook."

    n "Fumbling through its pages, Quixote settled on a fully filled-out spread."

    q "Ah."

    q "Here we are."

    q "As you no doubt know, traditionally the first decree of each Suzerish Monarch was a grand gesture spanning the entire Empire. Done to both solidify your all-encompassing authority and display the riches held at your whim."

    q "Given you are the first Emperor to ascend since our galactic expansion, the scale for this is both uncharted and potentially monumental."

    q "How you commit the resources of over a thousand worlds will shape both your own rule and that of future leaders to come."

    q "So best decide wisely."

    show expression "furique" as portrait
    f "Or don't and just go with your gut."

    f "You are the Emperor, after all."

    n "Quixote frowned, but nodded in reluctant agreement."

    show expression "quixote" as portrait
    q "Aptly put, Furique."

    q "I have prepared several suggestions based upon my own opinions and those of the broader Court."

    q "You have no obligation to take any of them should you already have an idea in mind, of course."

    q "Would you like to hear them?"

    menu:

        "By all means.":

            p "By all means."

        "Dinner and sleep are calling to me, but I can spare a few more minutes. Proceed.":

            p "Dinner and sleep are calling to me, but I can spare a few more minutes. Proceed."

            q "My thoughts exactly, Your Majesty. I shall try to be swift."

    label proposal_menu:

    menu:

        "Let's hear the first option." if not heard_coin:

            $ heard_coin = True

            p "Let's hear the first option."

            show expression "quixote" as portrait
            q "Alright, proposal number one, Your Majesty."

            q "Issuance of a new golden Imperial coin, minted with your visage and distributed to every subject above the age of 20!"

            q "This would dually cement your rule as a continuation from your ancestors, given others like Empress Sicill have coins of their own, and spread the idea of your generosity."

            q "The coin could, by Furique's estimates, be ingrained with 150 Veiden Svekrons worth of material. I'm sure the people will be quite grateful for such a gift!"

            q "Families can naturally choose to keep the coin or spend it."

            show expression "furique" as portrait
            f "While I can confirm the practicality of this proposal financially, pumping so much gold into the economy could just as easily devalue our gold reserves as it may stimulate purchases."

            f "Some can argue this is not more than a thinly veiled stimulus package, which, really, it is."

            f "We risk downgrading the overall wealth of those with primary shares in precious metals, who obviously tend to be Nobles."

            show expression "aurgenbia" as portrait
            a "I could have gold extraction quotas decreased from the Colonies to counteract this influx."

            show expression "furique" as portrait
            f "A wise suggestion, but ultimately pointless."

            f "We'll need to, in fact, increase gold mining operations to cover all our subjects."

            f "Including those from the Colonies themselves."

            show expression "gaucho" as portrait
            g "You intend to extend this honor to the colonials too?!?"

            show expression "quixote" as portrait
            q "Without a doubt!"

            q "If we close off the Emperor's benevolence to some of our populace, they will grow more resentful of him, thus negating the entire point."

            show expression "torrez" as portrait
            t "I agree with Quixote on this."

            t "Now is the time to foster brotherhood under the royal family between our subjects, domestic and foreign."

            t "It will keep the Dominions and Colonies from drifting away under new leadership."

            show expression "aurgenbia" as portrait
            a "Under different circumstances I'd have advised against rewarding our foreign subjects without proof of submission."

            a "However, as this will be the first act in ideally a benevolent relationship, it is smart to make the Emperor an initiator."

            show expression "furique" as portrait
            f "That's if the colonials and vassals can be made to ignore the increased tribute we'll have to demand."

            show expression "gaucho" as portrait
            g "And if you can stomach seeing foreigners haggling Suzerish gold..."

            g "I'd be surprised if most of those who actually use the coin aren't predominantly from beyond the core worlds."

            g "Such a relic is to be safeguarded with honors, not spent."

            show expression "furique" as portrait
            f "It's their theoretical coin, Captain General."

            f "They may do with it as they wish."

            jump proposal_menu

        "I'd like to hear option two." if not heard_palace:

            $ heard_palace = True

            p "I'd like to hear option two."

            show expression "quixote" as portrait
            q "This one is a personal favorite."

            q "Beginning a yearly ceremony of opening the palace to the public for one week."

            q "Allowing them to bask in the glory and prestige of the royal household and center of the Empire."

            show expression "gaucho" as portrait
            g "Quixote spoke with me on this before."

            g "Security-wise, any high-functioning courtiers and, of course, the Emperor himself shall be moved to another location until the week's end."

            g "It was suggested your Brother's hunting lodge in the Grail Forests would serve as a suitable holiday escape."

            show expression "furique" as portrait
            f "I'd hardly call it a lodge."

            f "It's a proper palace."

            show expression "gaucho" as portrait
            g "Precisely the point, Furique."

            show expression "torrez" as portrait
            t "Well, I for one love the idea."

            t "Let the masses catch a glimpse of such a historical site, if even for a short time."

            t "It will lead to further cultural enrichment and awe-inspiring respect for the monarchy."

            t "This goes for both domestic subjects and foreigners."

            show expression "aurgenbia" as portrait
            a "I'm not of the same mind."

            a "The monarchy should remain detached from the lower classes, not accessible to them."

            a "If we let them see the palace's opulence, what's to stop them from getting ideas of grandeur for their own chance at disrupting the hierarchy?"

            show expression "gaucho" as portrait
            g "To an extent I agree, but overall think the veneration which the people will come out of such an experience with will outweigh any sense of egalitarianism."

            show expression "furique" as portrait
            f "Plus, think of the gift shop potential."

            f "If you thought tax revenues were immense, you've got another thing coming."

            show expression "gaucho" as portrait
            g "I'd sooner die than let some tacky shop anywhere near ten miles of the palace."

            jump proposal_menu

        "The last idea, if you will." if not heard_gardens:

            $ heard_gardens = True

            p "The last idea, if you will."

            show expression "quixote" as portrait
            q "This one's straight from our First Envoy."

            q "The New Imperial Gardens."

            q "A center of botanical and zoological specimens spanning not just Suzerain's core worlds, but all regions under its domain."

            q "Open to the public, and intended to be a source of respite, education, and inspiration for anyone, Noble to commoner."

            show expression "torrez" as portrait
            t "Nothing says 'I care for my people' quite like a garden, Your Majesty."

            t "For millennia, they've been a means to bring the peoples of our Empire together."

            t "Most sites from even the days of the fue Jaimox monarchs remain in operation over two thousand years later."

            t "Only now, we have the means to create one of unprecedented scale."

            t "Not just our homeworld will be represented, but the entire Empire."

            t "Think of how effectively this will display the reach of our borders, while encouraging pride in your people at what large and diverse an Imperial family they belong to."

            t "Furthermore, admittedly, I am personally quite fond of gardens."

            show expression "gaucho" as portrait
            g "I've caught him spending entire nights sleeping in our family estate's garden."

            g "Would think Torrez a camping man, but it's only in a nice cultivated flowerbed where he can stomach being out of doors."

            show expression "torrez" as portrait
            t "Every flora has its place, and every creature its home."

            t "The wild is simply too, well, untamed."

            show expression "quixote" as portrait
            q "A garden is a great suggestion, I say."

            q "It could represent the regal grace of the Emperor and display his thoughtful nature."

            q "Philosophers and artists for centuries may wander through its trails, concocting the next great innovation."

            show expression "furique" as portrait
            f "If there's one thing which will be great, it's the costs, I can guarantee that much."

            f "Organizing, catching, transporting, and transplanting hundreds if not thousands of plants and animals will take a toll on the treasury."

            f "It's why no one else has ever tried to do it before."

            f "Actually, the Eternal Star did once a few decades back, but it forced a new tax to be implemented which caused a peasant revolt that scrapped the entire project."

            show expression "torrez" as portrait
            t "I'd hoped, as the Haciende, you'd be capable of handling the galaxy's richest treasury for such an endeavor, Furique."

            show expression "aurgenbia" as portrait
            a "Throwing money at the project isn't the only issue."

            a "Our administrative capabilities in the Dominions and Colonies are stretched thin as is."

            a "Adding this grandiose survey and capture order will only further strain things."

            show expression "torrez" as portrait
            t "No one is saying it would be easy, but great works such as this are what will best define the Emperor's coming reign."

            t "If we want to keep the first decree local and small-scale, then we might as well not bother making a fuss at all."

            show expression "aurgenbia" as portrait
            a "Hmmm. That's true."

            a "I simply don't want it to be a defining failure either."

            jump proposal_menu

        "I've heard enough. Respectfully, Quixote, my mind is already made up.":

            p "I've heard enough. Respectfully, Quixote, my mind is already made up."

            jump final_decree_choice

label final_decree_choice:

    show expression "quixote" as portrait
    q "No problem at all."

    q "I imagine this moment was one you've contemplated for many years."

    n "Quixote closed his notebook and looked toward me expectantly."

    q "Now, with all that said and done..."

    q "Your decision, Imperial Majesty...?"

    menu:

        "Mint the Pherip Ascension Coin (-4 Budget)":

            $ treasury -= 4

            # Hidden
            $ popularity += 3
            $ colonial_relations += 1
            $ burgher_approval += 1

            n "I stared at the document before me; my first Imperial Decree."

        "Open the Imperial Palace (-1 Budget, -1 Authority)":

            $ treasury -= 1
            $ authority -= 1

            # Hidden
            $ popularity += 1
            $ noble_approval -= 1
            $ tourism += 1

            n "I stared at the document before me; my first Imperial Decree."

        "Establish the Grand Gardens (-5 Budget)":

            $ treasury -= 5

            # Hidden
            $ popularity += 2
            $ noble_approval += 1
            $ burgher_approval += 1
            $ colonial_relations += 2

            n "I stared at the document before me; my first Imperial Decree."

        "Pass the Act of Clemency (-2 Authority)":

            $ authority -= 2

            # Hidden
            $ popularity += 1
            $ military_approval -= 1
            $ colonial_relations += 1
            $ galactic_reputation += 1

            n "I stared at the document before me; my first Imperial Decree."

        "Declare a Week-Long Holiday (-1 Budget)":

            $ treasury -= 1

            # Hidden
            $ popularity += 2
            $ domestic_production -= 1

            n "I stared at the document before me; my first Imperial Decree."

        "Imperial Armada Salute (-3 Budget)":

            $ treasury -= 3

            # Hidden
            $ popularity += 1
            $ authority += 2
            $ military_approval += 1
            $ colonial_relations += 1
            $ galactic_reputation += 1

            n "I stared at the document before me; my first Imperial Decree."

    n "This was a moment I had dreamed of since I was a child, wondering what legacy I would leave, where I'd follow in Sicill's footsteps, and where I'd forge my own path. Now, it was here before me."

    n "Taking one final second to savor the moment, I signed the papers with a vigorous flourish."

    n "My rule had well and truly begun at last."

    n "I triumphantly passed the approved decree to Quixote, who held it with reverence."

    show expression "quixote" as portrait

    n "Giving a glance toward me of jubilant glee, he held the papers high in the air."

    show expression "quixote" as portrait
    q "Behold! The makings of history!"

    q "His Majesty's commencement as ruler of the Empire, and majority of the known galaxy!"

    n "My Pueblidorés broke out into cheers and polite felicitations, sharing in Quixote's and my excitement."

    n "With all that done, it was my turn to end this occasion with a speech and return an oath of allegiance."

    n "I stood up and began thinking of how to phrase it."

    menu:

        "Pueblidorés, you represent the culmination of the brightest minds Suzerain has to offer...":

            $ authority -= 1
            $ council_approval += 1

            p "Pueblidorés, you represent the culmination of the brightest minds Suzerain has to offer. It is by your merits which the Councils you represent have entrusted the privilege of my full attention."

            p "In the same spirit of respect and loyalty that you have shown unto me, I swear, by God above and the responsibility I've inherited, your voices, your thoughts, your sentiments shall always be heard with an open mind."

            p "You need not fear reproach for disagreeing, and you will find a willing and fair partner in me."

            p "Before us lies the opportunity to reshape the galaxy for the better, and ensure our descendants for countless generations inherit a prospering Empire that knows no quarrel or trouble it cannot overcome."

            p "Only through an Emperor and his Castilles together can we forge that future."

            p "To that end, I swear my loyalty to you and this vision."

            p "Long live the Empire!"

        "My subjects, your vows of loyalty to me and Suzerain's royal family have truly touched my heart...":

            $ authority += 1
            $ council_approval -= 1

            p "My subjects, your vows of loyalty to me and Suzerain's royal family have truly touched my heart."

            p "Our Empire and its many children would not be here today were it not for the wisdom provided by the ancient institution that is the Castilles."

            p "Much like it guided my predecessor to achieve greatness, so too do I expect we shall accomplish once thought inconceivable feats."

            p "With your continued support, I will usher in the promised eternal golden age of Suzerain."

            p "Our foes will be truly smitten, never to rise against us again."

            p "Our allies will grow alongside us, becoming convinced Suzerain's stewardship is the right path for all."

            p "Our people will prosper, with riches that will flow for all eternity."

            p "And the Empire, our Suzerain, never will fall to the obscurities of history."

            p "This and more will be achieved, so long as you stay true to your oaths, and serve your Emperor well."

            p "Long live the Empire!"

    n "\"And long live its Emperor!\" my Councillors shouted back."

    hide quixote

    n "It was truly time to get to work."

$ current_event = "investment_opportunity_001"

$ active_event = True

call screen galaxy_map

return
