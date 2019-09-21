from abaqus import *
from abaqusConstants import *
import __main__
import time

def Macro3():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.mdbData.summary()
    o1 = session.openOdb(name='C:\Users\scadscad\Desktop\\filesfornewpc\implantanalyses\Job-1.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=88.3021,
        farPlane=132.61, width=34.4301, height=15.2156, viewOffsetX=0.278516,
        viewOffsetY=9.72171)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    leaf = dgo.LeafFromPartInstance(partInstanceName=('CORTICAL-1', ))
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
    leaf = dgo.Leaf(leafType=DEFAULT_MODEL)
    session.viewports['Viewport: 1'].odbDisplay.displayGroup.either(leaf=leaf)
    odb = session.odbs['C:\Users\scadscad\Desktop\\filesfornewpc\implantanalyses\Job-1.odb']
    session.fieldReportOptions.setValues(printXYData=OFF, sort=DESCENDING,
        printTotal=OFF)
    session.writeFieldReport(fileName='shortrpt.rpt', append=OFF,
        sortItem='S.Mises', odb=odb, step=0, frame=1,
        outputPosition=INTEGRATION_POINT, variable=(('S', INTEGRATION_POINT, ((
        INVARIANT, 'Mises'), )), ))






Macro3()


