from BeamClass import*
import funcs_for_user_interface
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
    def __init__(self):
        self.beam=0
        self.pin_joint=True
        self.cantilever=False
    def on_Create_New_Beam_Button_clicked(self,button):
        print('Create New Button has been clicked')
        newBeam=funcs_for_user_interface.getValuesForNewBeam(builder,self.pin_joint,self.cantilever)
        self.beam=Beam(newBeam['Length'],newBeam['Support-Type'],'circle',newBeam['E'],0,0,1)
        if(self.pin_joint):
            support_window.show_all()
        print(self.cantilever)
        print(self.beam)
    def on_Discrete_Force_Button_clicked(self, button):
        print("Discrete button has been clicked")
        ForceValues=funcs_for_user_interface.getValuesForDiscreteForce(builder)
        self.beam.getDiscreteForce(ForceValues['Distance'],ForceValues['Magnitude'])
    def on_Display_Graphs_clicked(self,button):
        print('Display Graphs button has been clicked')
        self.beam.calcShearForceEq()
        self.beam.calcBendingMomentEq()
        self.beam.calcSupportReac()
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
        resValues=funcs_for_user_interface.getValuesForContinuousForce(builder)
        resValues['Equation'].replace('-','+-')
        resValues['Equation']=resValues['Equation'].split('+')
        for everypart in resValues['Equation']:
            self.beam.getContinuousForce(resValues['Left Distance'],resValues['Right Distance'],everypart)
    def on_Moment_Button_clicked(self,button):
        print('Moment button has been clicked')
        ForceValues=funcs_for_user_interface.getValuesForMoment(builder)
        self.beam.getBendingMoment(ForceValues['Distance'],ForceValues['Magnitude'])
    def on_gtk_quit_activate(self,button):
        Gtk.main_quit()
    def on_Distance_Of_Discrete_Force_icon_press():
      print('hello world')
    def on_Support_Type_Cantilever_clicked(self,button):
        self.cantilever=True
        self.pin_joint=False
        print(self.cantilever)
    def on_Support_Type_Pin_Joint_clicked(self,button):
        self.cantilever=False
        self.pin_joint=True
    def on_Support_Submit_clicked(self,button):
        self.beam.support1=float(builder.get_object('Support_X_Distance').get_text())
        self.beam.support2=float(builder.get_object('Support_Y_Distance').get_text())
        support_window.destroy()




builder = Gtk.Builder()
builder.add_from_file("user_interface.glade")
builder.connect_signals(MyWindow())
distance=builder.get_object('Distance_Of_Discrete_Force')
magnitude=builder.get_object('Magnitude_Of_Discrete_Force')
window = builder.get_object("window1")
support_window=builder.get_object('support_window')

window.show_all()


Gtk.main()