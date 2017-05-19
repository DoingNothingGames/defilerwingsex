# coding=utf-8
screen sc_container_editor(object, data_list):
    # Экран для редактирования  объекта Container
    # object - Контейнер который мы редактируем
    # data_list - список контенеров из которых берется дата для контейнера object
    
    python:
        class delete_object(Action):
            def __init__(self, source, item):
                self._source = source
                self._item = item

            def __call__(self):
                del self._source[self._item]
                renpy.restart_interaction()

        class add_object(Action):
            def __init__(self, source, target, item):
                self._source = source
                self._target = target
                self._item = item

            def __call__(self):
                self._target.add(self._item, self._source[self._item])
                renpy.restart_interaction()
    
    vbox:
        text("Instructions:\n"
             "Click on the object in the current container to remove it.\n"
             "Click on the object in the list to add it to the current container.") 
        hbox:
            vbox:
                text "Current container:"
                for i in object:
                    textbutton object[i].name action delete_object(object, i)
            for d in data_list:
                vbox:
                    text "Container:" % (data_list.index(d) + 1)
                    for i in d:
                        if i not in object:
                            textbutton d[i].name action add_object(d, object, i)
