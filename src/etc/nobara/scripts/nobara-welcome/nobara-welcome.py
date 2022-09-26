import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import subprocess
import os
import os.path
from pathlib import Path

class Application:
    
    ### MAIN WINDOW ###
    def __init__(self):
        self.column_names = False
        self.drop_nan = False
        self.df = None
        
        self.builder = Gtk.Builder()
        self.builder.add_from_file("/etc/nobara/scripts/nobara-welcome/nobara-welcome.ui")
        self.builder.connect_signals(self)
        win = self.builder.get_object("main_Window")
        win.connect("destroy", Gtk.main_quit)
        
        self.window = self.builder.get_object("main_Window")
        self.window.show()
        
        theme_box = self.builder.get_object("theme_box")
        layout_box = self.builder.get_object("layout_box")
        
        desktop_output = subprocess.run(["echo $XDG_SESSION_DESKTOP | grep gnome"], shell=True)
        if (desktop_output.returncode) != 0:
            theme_box.hide()
            layout_box.hide()
        

        
        
        
        
    ### Start up Switch ###
        
        startup_switch = self.builder.get_object("startup_switch")
        
        startup_file = Path('/home/' + os.getlogin() + '/.config/autostart/nobara-welcome.desktop')
        
        if startup_file.is_file():
            startup_switch.set_active(True)
    
    def on_startup_switch(self, switch, state):
        if switch.get_active() == True :
            os.system("mkdir -p ~/.config/autostart/ cp /usr/share/applications/nobara-welcome.desktop ~/.config/autostart/nobara-welcome.desktop && echo 'X-GNOME-Autostart-enabled=true' >> ~/.config/autostart/nobara-welcome.desktop ")
        else:
            os.system("rm ~/.config/autostart/nobara-welcome.desktop")
    
    ### ENTER LOOK WINDOW ###
    def enter_look(self, widget):
        look_window =  self.builder.get_object("look_Window")
        look_window.show()
    ### EXIT LOOK WINDOW ###
    def close_look(self, widget, event):
        return self.builder.get_object("look_Window").hide_on_delete()
    ### ENTER DRIVER WINDOW ###
    def enter_driver(self, widget):
        driver_window =  self.builder.get_object("driver_Window")
        driver_window.show()
    ### EXIT DRIVER WINDOW ###
    def close_driver(self, widget, event):
        return self.builder.get_object("driver_Window").hide_on_delete()
    
    ##### FIRST STEPS ENTRIES #####
    
    #### DRIVER ENTRIES ####
    
    ### NVIDIA ###
    def enter_nvidia(self, widget):
        os.system("/etc/nobara/scripts/nobara-welcome/nvidia.sh")
    ### AMD PRO ###
    def enter_amd(self, widget):
        os.system("/usr/bin/nobara-amdgpu-config")
    ### ROCm ###
    def enter_rocm(self, widget):
        os.system("/etc/nobara/scripts/nobara-welcome/rocm.sh")
    ### XONE ###
    def enter_xone(self, widget):
        os.system("/usr/bin/nobara-controller-config")
   
    #### Apps Entries ####
   
    ### APPS ###
    def enter_apps(self, widget):
        os.system("/etc/nobara/scripts/nobara-welcome/apps.sh")
    ### WEBAPPS ###
    def enter_webapps(self, widget):
        os.system("/usr/bin/webapp-manager")

    ##### QUICK SETUP ENTRIES #####
    
    ### LOGIN MANAGER ###
    def enter_dm(self, widget):
        os.system("/usr/bin/nobara-login-config")
    ### LAYOUTS ###
    def enter_layout(self, widget):
        os.system("/usr/bin/nobara-gnome-layouts")
    ### THEMES ###
    def enter_theme(self, widget):
        os.system("/usr/bin/gnome-tweaks")
    ### PLING ###
    def enter_pling(self, widget):
        os.system("xdg-open https://pling.com/")

    #### TROUBLESHOOT ENTRIES ####
    
    ### Troubleshoot ###
    def enter_troubleshoot(self, widget):
        os.system("xdg-open https://nobaraproject.org/docs/upgrade-troubleshooting/")
    ### Docs ###
    def enter_doc(self, widget):
        os.system("xdg-open https://nobaraproject.org/docs/")
    ### Distro Sync ###
    def enter_distrosync(self, widget):
        os.system("/etc/nobara/scripts/nobara-welcome/refresh.sh")


    #### COMMUNITY ENTRIES ####
    
    ### discord ###
    def enter_discord(self, widget):
        os.system("xdg-open https://discord.gg/6y3BdzC")
    ### reddit ###
    def enter_reddit(self, widget):
        os.system("xdg-open https://www.reddit.com/r/NobaraProject/")
    ### blog ###
    def enter_blog(self, widget):
        os.system("xdg-open https://www.gloriouseggroll.tv/")
    ### twitter ###
    def enter_twitter(self, widget):
        os.system("xdg-open https://twitter.com/GloriousEggroll/")
    ### youtube ###
    def enter_youtube(self, widget):
        os.system("xdg-open https://www.youtube.com/channel/UCUMSHXWczvxHy9e8silnVNw")
        
    #### Contribute ENTRIES ####
    
    ### patreon ###
    def enter_patreon(self, widget):
        os.system("xdg-open https://www.patreon.com/gloriouseggroll")
    ### design ###
    def enter_design(self, widget):
        os.system("xdg-open https://discord.com/channels/110175050006577152/1015154123114549309")
    ### GE GITLAB ###
    def enter_ge_gitlab(self, widget):
        os.system("xdg-open https://gitlab.com/GloriousEggroll")
    ### GE GITHUB ###
    def enter_ge_github(self, widget):
        os.system("xdg-open https://github.com/GloriousEggroll")
    ### COSMO GITHUB ###
    def enter_cosmo_github(self, widget):
        os.system("xdg-open https://github.com/CosmicFusion")

    
Application()
Gtk.main()
