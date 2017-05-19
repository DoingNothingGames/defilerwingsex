# coding=utf-8
#checked and proofread
init python:
    from pythoncode.utils import get_random_image
    
label lb_event_mobilization_increase:
    show expression get_random_image("img/scene/mobilization") as bg
    nvl clear
    "Rulers of the Free Kingdoms are concerned with dragon raids. The level of mobilization rises."
    return

label lb_event_poverty_increase:
    show expression get_random_image("img/scene/poverty") as bg
    nvl clear
    "The dragon\'s evil deeds lead to devastation throughout the Free Kingdoms. Poverty rises and the ability to mobilize diminishes."
    return
    
label lb_event_no_thief:
    "There is no thief in this land who wants to take the paltry treasures of [game.dragon.fullname]."
    return

label lb_event_no_knight:
    "[game.dragon.fullname] is not famous enough to attract questing knights."
    return

label lb_event_sleep_start:
    '[game.dragon.fullname] sleeps...'
    nvl clear
    return

label lb_event_sleep_new_year:
    return

label lb_event_sleep_end:
    nvl clear
    '[game.dragon.fullname] rises from his slumber!'
    return
