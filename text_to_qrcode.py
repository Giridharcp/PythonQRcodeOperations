import pyqrcode
from appJar import gui
from pathlib import Path

def QRcode_generator():

    def qrcode_generator(message,output_file):
                  qr=pyqrcode.create(message)
                  output=str(output_file)+".png"
                  qr.png(output,scale=10)
    
                  
                  if(app.questionBox("File Save", "QR code generated. Do you want to quit?")):
                    app.stop()
    
    
    def validate_inputs(src_file, dest_dir, out_file):
    
         errors = False
         error_msgs = []
         if len(src_file)<1:
            errors=True
            error_msgs.append("Please Enter the message")
         if not(Path(dest_dir)).exists():
            errors = True
            error_msgs.append("Please Select a valid output directory")
    
        # Check for a file name
         if len(out_file) < 1:
            errors = True
            error_msgs.append("Please enter a file name")
            
        
         return(errors, error_msgs)  
    
    
    def press(button):
        if button=="Process":
            src_file = app.getEntry("Input_msg")
            dest_dir = app.getEntry("Output_Directory")
            out_file = app.getEntry("Output_name")
            errors, error_msg = validate_inputs(src_file, dest_dir, out_file)
            if errors:
                app.errorBox("Error", "\n".join(error_msg), parent=None)
            else:
               qrcode_generator(src_file,Path(dest_dir,out_file))
        else:
            app.stop()
    
    
    app=gui("QR code generator", useTtk=True)
    app.setTtkTheme('alt')
    app.setSize(500, 200)
    
    # Add the interactive components
    app.addLabel("lb1","Enter the Text/Message: ")
    app.addEntry("Input_msg")
    
    
    app.addLabel("lb2","Select Output Directory")
    app.addDirectoryEntry("Output_Directory")
    
    app.addLabel("Output file name")
    app.addEntry("Output_name")
    
    app.addButtons(["Process", "Quit"],press)
    app.setLabelBg("lb1","red")
    app.go()


QRcode_generator()
