# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
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
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    step = mdb.openStep('C:\Users\scad\Desktop\\filesfornewpc\implant\Deneme\\Assembly.STEP', scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='Assembly-1',
        geometryFile=step, combine=False, dimensionality=AXISYMMETRIC,
        type=DEFORMABLE_BODY)
    mdb.models['Model-1'].PartFromGeometryFile(name='Assembly-2',
        geometryFile=step, bodyNum=2, combine=False,
        dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    mdb.models['Model-1'].PartFromGeometryFile(name='Assembly-3',
        geometryFile=step, bodyNum=3, combine=False,
        dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    mdb.models['Model-1'].PartFromGeometryFile(name='Assembly-4',
        geometryFile=step, bodyNum=4, combine=False,
        dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    mdb.models['Model-1'].PartFromGeometryFile(name='Assembly-5',
        geometryFile=step, bodyNum=5, combine=False,
        dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
    mdb.models['Model-1'].PartFromGeometryFile(name='Assembly-6',
        geometryFile=step, bodyNum=6, combine=False,
        dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)


    p = mdb.models['Model-1'].parts['Assembly-6']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.61312,
        farPlane=2.93305, width=2.15847, height=1.04272, viewOffsetX=0.232343,
        viewOffsetY=-0.0422777)

    p1 = mdb.models['Model-1'].parts['Assembly-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-1', toName='cortical')
    p = mdb.models['Model-1'].parts['cortical']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#3ffffff ]', ), )
    p.Surface(side1Edges=side1Edges, name='cort')

    p1 = mdb.models['Model-1'].parts['Assembly-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-2',
        toName='trabecular')
    p = mdb.models['Model-1'].parts['trabecular']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#ffffffff:2 #7fff ]', ), )
    p.Surface(side1Edges=side1Edges, name='trab')

    p1 = mdb.models['Model-1'].parts['Assembly-3']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-3', toName='implant')
    p = mdb.models['Model-1'].parts['implant']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#ffffffff:3 #7 ]', ), )
    p.Surface(side1Edges=side1Edges, name='imp')






    #faces = p.rootAssembly.faces.getByBoundingBox(-5,-5,-5,80,80,80)
    #region = p.Set(faces=faces, name='Surf-1')

    p = mdb.models['Model-1'].parts['implant']
    s = p.edges
    side1Edges = s.getByBoundingBox(-1,-1,-1,1,1,1)

    p.Surface(side1Edges=side1Edges, name='imp')










    p1 = mdb.models['Model-1'].parts['Assembly-4']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-4', toName='abutment')
    p = mdb.models['Model-1'].parts['abutment']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#1f ]', ), )
    p.Surface(side1Edges=side1Edges, name='abut')

    p1 = mdb.models['Model-1'].parts['Assembly-5']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-5', toName='screw')
    p = mdb.models['Model-1'].parts['screw']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#f ]', ), )
    p.Surface(side1Edges=side1Edges, name='screw')

    p1 = mdb.models['Model-1'].parts['Assembly-6']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-6', toName='crown')
    p = mdb.models['Model-1'].parts['crown']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#f ]', ), )
    p.Surface(side1Edges=side1Edges, name='crown')

    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Surface(side1Edges=side1Edges, name='crowntop')



    mdb.models['Model-1'].Material(name='titanium')
    mdb.models['Model-1'].materials['titanium'].Elastic(table=((110000.0, 0.3), ))
    mdb.models['Model-1'].Material(name='cortical')
    mdb.models['Model-1'].materials['cortical'].Elastic(table=((13700.0, 0.3), ))
    mdb.models['Model-1'].Material(name='trabecular')
    mdb.models['Model-1'].materials['trabecular'].Elastic(table=((1370.0, 0.3), ))
    mdb.models['Model-1'].Material(name='ceramic')
    mdb.models['Model-1'].materials['ceramic'].Elastic(table=((68900.0, 0.28), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='titsec',
        material='titanium', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='corsec',
        material='cortical', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='trabsec',
        material='trabecular', thickness=None)
    mdb.models['Model-1'].HomogeneousSolidSection(name='cersec',
        material='ceramic', thickness=None)
    p = mdb.models['Model-1'].parts['cortical']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['abutment']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['abutment']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['abutment']
    p.SectionAssignment(region=region, sectionName='titsec', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['cortical']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['cortical']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['cortical']
    p.SectionAssignment(region=region, sectionName='corsec', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['crown']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['crown']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['crown']
    p.SectionAssignment(region=region, sectionName='cersec', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['implant']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['implant']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['implant']
    p.SectionAssignment(region=region, sectionName='titsec', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['screw']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['screw']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['screw']
    p.SectionAssignment(region=region, sectionName='titsec', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['Model-1'].parts['trabecular']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['trabecular']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['trabecular']
    p.SectionAssignment(region=region, sectionName='trabsec', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)


    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON,
        constraints=ON, connectors=ON, engineeringFeatures=ON)
    mdb.models['Model-1'].StdContactControl(name='ContCtrl-1',
        stabilizeChoice=AUTOMATIC)
    mdb.models['Model-1'].ContactProperty('friction')
    mdb.models['Model-1'].interactionProperties['friction'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF,
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0,
        table=((0.5, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION,
        fraction=0.005, elasticSlipStiffness=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF,
        constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByThreePoints(coordSysType=CYLINDRICAL, origin=(0.0, 0.0, 0.0),
        point1=(1.0, 0.0, 0.0), point2=(0.0, 0.0, -1.0))
    p = mdb.models['Model-1'].parts['abutment']
    a.Instance(name='abutment-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['cortical']
    a.Instance(name='cortical-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['crown']
    a.Instance(name='crown-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['implant']
    a.Instance(name='implant-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['screw']
    a.Instance(name='screw-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['trabecular']
    a.Instance(name='trabecular-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON,
        constraints=ON, connectors=ON, engineeringFeatures=ON,
        adaptiveMeshConstraints=OFF)



    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['abutment-1'].surfaces['abut']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['crown-1'].surfaces['crown']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-1',
        createStepName='Step-1', master=region1, slave=region2, sliding=FINITE,
        thickness=ON, interactionProperty='friction',
        contactControls='ContCtrl-1', adjustMethod=NONE, initialClearance=OMIT,
        datumAxis=None, clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['abutment-1'].surfaces['abut']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['screw-1'].surfaces['screw']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-2',
        createStepName='Step-1', master=region1, slave=region2, sliding=FINITE,
        thickness=ON, interactionProperty='friction',
        contactControls='ContCtrl-1', adjustMethod=NONE, initialClearance=OMIT,
        datumAxis=None, clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['abutment-1'].surfaces['abut']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['implant-1'].surfaces['imp']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-3',
        createStepName='Step-1', master=region1, slave=region2, sliding=FINITE,
        thickness=ON, interactionProperty='friction',
        contactControls='ContCtrl-1', adjustMethod=NONE, initialClearance=OMIT,
        datumAxis=None, clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['screw-1'].surfaces['screw']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['implant-1'].surfaces['imp']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-4',
        createStepName='Step-1', master=region1, slave=region2, sliding=FINITE,
        thickness=ON, interactionProperty='friction',
        contactControls='ContCtrl-1', adjustMethod=NONE, initialClearance=OMIT,
        datumAxis=None, clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['implant-1'].surfaces['imp']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['cortical-1'].surfaces['cort']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-5',
        createStepName='Step-1', master=region1, slave=region2, sliding=FINITE,
        thickness=ON, interactionProperty='friction',
        contactControls='ContCtrl-1', adjustMethod=NONE, initialClearance=OMIT,
        datumAxis=None, clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['implant-1'].surfaces['imp']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['trabecular-1'].surfaces['trab']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-6',
        createStepName='Step-1', master=region1, slave=region2, sliding=FINITE,
        thickness=ON, interactionProperty='friction',
        contactControls='ContCtrl-1', adjustMethod=NONE, initialClearance=OMIT,
        datumAxis=None, clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['cortical-1'].surfaces['cort']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['trabecular-1'].surfaces['trab']
    mdb.models['Model-1'].SurfaceToSurfaceContactStd(name='Int-7',
        createStepName='Step-1', master=region1, slave=region2, sliding=FINITE,
        thickness=ON, interactionProperty='friction',
        contactControls='ContCtrl-1', adjustMethod=NONE, initialClearance=OMIT,
        datumAxis=None, clearanceRegion=None)





    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['crown-1'].surfaces['crowntop']
    mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1',
        region=region, distributionType=UNIFORM, field='', magnitude=21.1,          ## LOADING
        amplitude=UNSET)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=84.2955,
        farPlane=101.267, width=85.4414, height=43.7472, viewOffsetX=1.18376,
        viewOffsetY=2.49663)


    #a = mdb.models['Model-1'].rootAssembly
    #e1 = a.instances['cortical-1'].edges
    #edges1 = e1.getSequenceFromMask(mask=('[#2 ]', ), )
    #region = a.Set(edges=edges1, name='Set-1')
    #mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1',
    #    region=region, localCsys=None)

    a = mdb.models['Model-1'].rootAssembly
    e1 = a.instances['cortical-1'].edges
    edges1 = e1.findAt(((8, 0.0, 0.0), ))           #####Boundary Conditions
    region = a.Set(edges=edges1, name='Set-1')
    mdb.models['Model-1'].EncastreBC(name='BC-1', createStepName='Step-1',
        region=region, localCsys=None)








    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF,
        bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['trabecular']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['trabecular']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    p = mdb.models['Model-1'].parts['trabecular']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=TRI)
    p = mdb.models['Model-1'].parts['trabecular']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['trabecular']
    p.generateMesh()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=70.9607,
        farPlane=80.2187, width=46.4049, height=23.8187, viewOffsetX=-0.270655,
        viewOffsetY=5.05923)
    p = mdb.models['Model-1'].parts['screw']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['screw']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    p = mdb.models['Model-1'].parts['screw']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=TRI)
    p = mdb.models['Model-1'].parts['screw']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['screw']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['implant']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['implant']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    p = mdb.models['Model-1'].parts['implant']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=TRI)
    p = mdb.models['Model-1'].parts['implant']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['implant']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['crown']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['crown']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    p = mdb.models['Model-1'].parts['crown']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=TRI)
    p = mdb.models['Model-1'].parts['crown']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['crown']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['cortical']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['cortical']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    p = mdb.models['Model-1'].parts['cortical']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=TRI)
    p = mdb.models['Model-1'].parts['cortical']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['cortical']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['abutment']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
    elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD)
    p = mdb.models['Model-1'].parts['abutment']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    pickedRegions =(faces, )
    p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
    p = mdb.models['Model-1'].parts['abutment']
    f = p.faces
    pickedRegions = f.getSequenceFromMask(mask=('[#1 ]', ), )
    p.setMeshControls(regions=pickedRegions, elemShape=TRI)
    p = mdb.models['Model-1'].parts['abutment']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['abutment']
    p.generateMesh()
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF,
        optimizationTasks=ON, geometricRestrictions=ON, stopConditions=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)


Macro1()
