# coding=utf-8
screen sc_list_editor(object, data_list):
    # Экран для редактирования list'ов
    # object - list который мы редаткируем
    # data_list - список списков/словарей из которых берется дата для списка object
    
    # FIY Вообще должно работать, но нигде не используется.
    
    python:
        class delete_object(Action):
            def __init__(self, source, item):
                self._source = source
                self._item = item

            def __call__(self):
                del self._source[self._item]
                renpy.restart_interaction()

        class add_object(Action):
            def __init__(self, target, item):
                self._target = target
                self._item = item

            def __call__(self):
                target.append(item)
                renpy.restart_interaction()
    
    vbox:
        text("Instructions:\n"
             "Click an object in the current container to remove it.\n"
             "Click an object in the list to add it to the current container.")
        hbox:
            vbox:
                text "Current list:"
                for i in range(0, len(object)):
                    textbutton object[i] action delete_object(object, i)
            for d in data_list:
                vbox:
                    text "Container: %d:" % (data_list.index(d) + 1)
                    for i in d:
                        textbutton d[i] action add_object(object, i)