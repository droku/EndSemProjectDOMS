from BeamClass import*
import funcs_for_user_interface
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
pin_joint = True
cantilever = False
class MyWindow:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def __init__(self):
        self.beam=0
    def on_Create_New_Beam_Button_clicked(self,button):
        print('Create New Button has been clicked')
        newBeam=funcs_for_user_interface.getValuesForNewBeam(builder,pin_joint,cantilever)
        self.beam=Beam(newBeam['Length'],newBeam['Support-Type'],'circle',newBeam['E'],0,0,1)
        print(self.beam)
    def on_Discrete_Force_Button_clicked(self, button):
        print("Discrete button has been clicked")
        ForceValues=funcs_for_user_interface.getValuesForDiscreteForce(builder)
        self.beam.getDiscreteForce(ForceValues['Distance'],ForceValues['Magnitude'])
    def on_Display_Graphs_clicked(self,button):
        print('Display Graphs button has been clicked')
        self.beam.calcShearForceEq()
        self.beam.calcBendingMomentEq()
       # self.beam.calcSupportReac()
        self.beam.calcShearForceEq()
        self.beam.calcBendingMomentEq()
        self.beam.calcDeflection()
        self.beam.maxDeflection()
        self.beam.maxBendingStress()
        self.beam.printLoadEquation()
        self.beam.printShearForceEquation()
        self.beam.printBendingMomentEquation()
        self.beam.plotLoadEq()
        self.beam.plotShearEq()
        self.beam.plotBendingMomentEq()
        self.beam.plotDeflection()
    def on_Continuous_Force_Button_clicked(self,button):
        print('Continuous button has been clicked') 
    def on_Moment_Button_clicked(self,button):
        print('Moment button has been clicked')
    def on_gtk_quit_activate(self,button):
        Gtk.main_quit()
    def on_Distance_Of_Discrete_Force_icon_press():
      print('hello world')
    def on_Support_Type_Cantilever_clicked(self,button):
        cantilever=True
        pin_joint=False
    def on_Support_Type_Pin_Joint_clicked(self,button):
        cantilever=False
        pin_joint=True

builder = Gtk.Builder()
builder.add_from_file("user_interface.glade")
builder.connect_signals(MyWindow())
distance=builder.get_object('Distance_Of_Discrete_Force')
magnitude=builder.get_object('Magnitude_Of_Discrete_Force')
window = builder.get_object("window1")
window.show_all()

Gtk.main()