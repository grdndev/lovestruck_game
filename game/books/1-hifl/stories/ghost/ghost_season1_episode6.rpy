
label ghost_season1_episode6:
    $tbc = False
    scene bg undergrass at bg
    play music suspense

    pause

    #Leave these guys right here! Or things will get weird.
    $ hidetextbox = True
    $ renpy.block_rollback()
    $ hideborders = False

    #And now you're free to do pretty much whatever, so long as you leave resets() at the bottom.
    
    "I expect everything to go black, but that's not even close to what happens."
    "Shapes and colors begin to race across my vision, faster than I can even try to focus on them."
    "There's so much {i}stuff{/i} underground- apparently, it's not just dirt."
    "Obviously there's roots, pale and wiggly things that quickly fade from sight as I fall ever deeper."
    "There's rocks, and worms, and little tunnels, and maybe even a few bones- but it all looks completely flat, like a cross-section from a science textbook."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(I can see underground, now?)"
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(No, come on, that doesn't even make sense!)"
    hide ghostmc
    "Though fascinating, my ability to see without light doesn't help to arrest my fall."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Am I just going to keep falling until I get to the earth's core?)"
    "(Is that a common problem for ghosts!?)"
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(Why does gravity even work on me? It's not like I weigh anything.)"
    hide ghostmc
    "And just like that, as if I've slammed an emergency stop button, I shudder to a stop."
    "Everything is still."
    "I've fallen so far below the surface that I'm surrounded by nothing but dark, lifeless rock- and I'm just floating in place."
    "Something clicks into place."
    show ghostmc casual_cu basic_cu at hiflmc_cu
    "(Oh. I get it.)"
    "(I was only falling because that's what I expected to happen.)"
    "(That's why I could walk on the ground, too- I was making my body act human.)"
    show ghostmc casual_cu angry_cu at hiflmc_cu
    "(But I'm not human anymore.)"
    "(And I think it's about time I got back to work.)"
    hide ghostmc
    show bg bowling with dissolve
    stop music fadeout 0.5
    pause 0.5
    play music getitdone
    "No sooner have I finished that thought than I find myself back at the bowling alley."
    show ghostmc casual_cu surprised_cu at hiflmc_cu
    "(Razi was right! I really can teleport.)"
    show ghostmc casual_cu sarcastic_cu at hiflmc_cu
    "(...And I guess Liliane was right, too.)"
    "(Unless I've recently hit a growth spurt.)"
    show ghostmc casual basic at gcentre
    show razi casual surprised at right4 behind ghostmc
    show jd casual surprised at left4 behind ghostmc
    "My landing zone puts me directly between- and slightly above- a very surprised Razi and JD."
    show razi casual surprised at right5
    show jd casual surprised at left5
    with ease
    "They both jerk back, JD nearly tripping over a bar stool that hadn't quite been pushed back in."
    jd "Holy- {i}[genericfn]{/i}?"
    show jd casual angry at left3
    show ghostmc casual basic at gright3
    hide razi
    jd "Could you not!?"

    show ghostmc casual surprised
    ghostmc "Sorry!"
    show ghostmc casual sarcastic
    ghostmc "I don't really know how to drive this thing."
    jd "Well, warn a person before doing ghost stuff!"
    show jd casual smirk
    jd "Rattle some chains, at least."
    hide ghostmc
    show razi casual angry at right3
    ra "I'm going to go ahead and say that it's still too soon for ghost jokes, Jordan."
    hide razi
    hide jd
    show ghostmc 
    ghostmc "Anyway, what are you all doing?"
    ghostmc "Because things got a little weird in the forest."
    hide ghostmc
    hide jd
    show mac cop basic at left3
    show diego glassesdoctor basic at right3
    "Mac and Diego "
    
    $ tobecontinued()
    show bg hifltbc at bg with fade
    pause

    $ resets()
