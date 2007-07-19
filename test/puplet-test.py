import os, sys

import gtk

import dbus
import dbus.glib

def check_updates(*args):
    bus = dbus.SystemBus()
    remote_object = bus.get_object("edu.duke.linux.yum", "/Updatesd")
    iface = dbus.Interface(remote_object, "edu.duke.linux.yum")

    remote_object.CheckNow(dbus_interface="edu.duke.linux.yum")

def kill_daemon(*args):
    bus = dbus.SystemBus()
    remote_object = bus.get_object("edu.duke.linux.yum", "/Updatesd")
    iface = dbus.Interface(remote_object, "edu.duke.linux.yum")

    remote_object.ShutDown(dbus_interface="edu.duke.linux.yum")

def update_info(*args):
    bus = dbus.SystemBus()
    remote_object = bus.get_object("edu.duke.linux.yum", "/Updatesd")
    iface = dbus.Interface(remote_object, "edu.duke.linux.yum")

    r = remote_object.GetUpdateInfo(dbus_interface="edu.duke.linux.yum")
    for (new, old) in r:
        print "new: %s; old: %s" %(new, old)
    print "Total of %d updates" %(len(r),)

def quit(*args):
    sys.exit(0)


w = gtk.Window()
vbox = gtk.VBox()
w.add(vbox)

l = gtk.Label("don't know about updates")
vbox.pack_start(l)
b = gtk.Button("Check for updates now")
b.connect("clicked", check_updates)
vbox.pack_start(b)

b = gtk.Button("Get update info")
b.connect("clicked", update_info)
vbox.pack_start(b)

b = gtk.Button("kill daemon")
b.connect("clicked", kill_daemon)
vbox.pack_start(b)

w.show_all()
w.connect("destroy", quit)

bus = dbus.SystemBus()

def updates_avail_handler(str):
    print "Received signal about updates and it says", str

bus.add_signal_receiver(updates_avail_handler, "UpdatesAvailableSignal", dbus_interface="edu.duke.linux.yum")



gtk.main()


sys.exit(0)
