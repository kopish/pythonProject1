class BrowserWindow:
    def open(self, link):
        self.current_link = link
        print(f"Link '{link}' was opened!")


class Computer:
    def go_online(self):
        return BrowserWindow()

    def open_itvdn_lesson(self):
        browser_window = self.go_online()
        browser_window.open("itvdn.com")

        return browser_window


my_own_computer = Computer()
browser = my_own_computer.open_itvdn_lesson()
