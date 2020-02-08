import scene


class TitleScene(scene.Scene):

    def show(self):
        print('show')

    def hide(self):
        print('hide')

    def update(self):
        print('update')

    def draw(self):
        print('draw')

    @property
    def is_finished(self):
        return False

    @property
    def next_scene(self):
        return 'Play'
