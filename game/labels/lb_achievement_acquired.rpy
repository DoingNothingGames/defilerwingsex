label lb_achievement_acquired:
    python:
        if u"Easter bunny" not in persistent.achievements.keys():            
            for egg in persistent.easter_eggs:
                data.achieve_target(egg, "easter_eggs")
    $ achieved = data.store_achievements(persistent.achievements)
    $ names_list = achieved.keys()
    while len(names_list) != 0:
        $ achievement_name = names_list.pop()
        $ achievement_description = achieved[achievement_name]
        "Achievement unlocked: [achievement_name]: [achievement_description]"
    nvl clear
    return
label lb_achievements_list:
    python:
        if len(persistent.achievements) > 0:
            achievements_text = "\n".join(["%s: %s"%(name, desc) for name, desc in persistent.achievements.items()])
        else:
            achievements_text = "You failed to unlock any achievements"
    "[achievements_text]"
    nvl clear
screen sc_achievements_list:
    python:
        if len(persistent.achievements) > 0:
            achievements_text = "\n".join(["%s: %s"%(name, desc) for name, desc in persistent.achievements.items()])
        else:
            achievements_text = "You have not unlocked any achievements"
    window:
        xmaximum 960
        xalign 0.0
        text "[achievements_text]"
        key "K_SPACE" action Hide("sc_achievements_list")
        key 'K_RETURN' action Hide("sc_achievements_list")
        key 'K_KP_ENTER' action Hide("sc_achievements_list")
        key 'mouseup_1' action Hide("sc_achievements_list")