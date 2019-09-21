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
    step = mdb.openStep('C:\Users\scadscad\Desktop\\filesfornewpc\implant\Deneme\\Assembly.STEP', scaleFromFile=OFF)
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
    p1 = mdb.models['Model-1'].parts['Assembly-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-1', toName='cortical')
    p1 = mdb.models['Model-1'].parts['Assembly-2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-2',
        toName='trabecular')
    p1 = mdb.models['Model-1'].parts['Assembly-3']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-3', toName='implant')
    p1 = mdb.models['Model-1'].parts['Assembly-4']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-4', toName='abutment')
    p1 = mdb.models['Model-1'].parts['Assembly-5']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-5', toName='screw')
    p1 = mdb.models['Model-1'].parts['Assembly-6']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    mdb.models['Model-1'].parts.changeKey(fromName='Assembly-6', toName='crown')
    p = mdb.models['Model-1'].parts['crown']
    s = p.edges
    side1Edges = s.getSequenceFromMask(mask=('[#4 ]', ), )
    p.Surface(side1Edges=side1Edges, name='crowntop')
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
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
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial', nlgeom=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON,
        constraints=ON, connectors=ON, engineeringFeatures=ON,
        adaptiveMeshConstraints=OFF)
    mdb.models['Model-1'].StdContactControl(name='ContCtrl-1',
        stabilizeChoice=AUTOMATIC)
    mdb.models['Model-1'].ContactProperty('friction')
    mdb.models['Model-1'].interactionProperties['friction'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF,
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0,
        table=((0.5, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION,
        fraction=0.005, elasticSlipStiffness=None)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['cortical-1'].edges
    '''side1Edges1 = s1.findAt(((0.0, 1.575, 0.0), ), ((2.5, 0.0, 0.0), ), ((10.0,
        8.75, 0.0), ), ((8.019914, 35.0, 0.0), ), ((2.074515, 34.910225, 0.0),
        ), ((2.062034, 34.620906, 0.0), ), ((2.152733, 34.58804, 0.0), ), ((
        2.416877, 34.532965, 0.0), ), ((2.233368, 34.21196, 0.0), ), ((
        2.063265, 34.208422, 0.0), ), ((2.030044, 34.133839, 0.0), ), ((
        2.027667, 34.020906, 0.0), ), ((2.118365, 33.98804, 0.0), ), ((
        2.382509, 33.932965, 0.0), ), ((2.199001, 33.61196, 0.0), ), ((
        2.028898, 33.608422, 0.0), ), ((1.995677, 33.533839, 0.0), ), ((
        1.993299, 33.420906, 0.0), ), ((2.083998, 33.38804, 0.0), ), ((
        2.348142, 33.332965, 0.0), ), ((2.164633, 33.01196, 0.0), ), ((1.99453,
        33.008422, 0.0), ), ((1.962155, 32.948614, 0.0), ), ((3.444528, 32.9,
        0.0), ), ((7.9, 25.2, 0.0), ), ((5.925, 2.1, 0.0), ))'''

    side1Edges1 = s1.getByBoundingBox(-5,-5,-5,80,80,80)

    s2 = a.instances['trabecular-1'].edges
    '''side1Edges2 = s2.findAt(((0.0, 18.737063, 0.0), ), ((1.975, 2.1, 0.0), ), ((
        7.9, 9.8, 0.0), ), ((6.414843, 32.9, 0.0), ), ((1.958525, 32.885225,
        0.0), ), ((1.958931, 32.820906, 0.0), ), ((2.04963, 32.78804, 0.0), ),
        ((2.313774, 32.732965, 0.0), ), ((2.130266, 32.41196, 0.0), ), ((
        1.960163, 32.408422, 0.0), ), ((1.926942, 32.333839, 0.0), ), ((
        1.924564, 32.220906, 0.0), ), ((2.015263, 32.18804, 0.0), ), ((
        2.279407, 32.132965, 0.0), ), ((2.095898, 31.81196, 0.0), ), ((
        1.925795, 31.808422, 0.0), ), ((1.892574, 31.733839, 0.0), ), ((
        1.890196, 31.620906, 0.0), ), ((1.980895, 31.58804, 0.0), ), ((
        2.245039, 31.532965, 0.0), ), ((2.061531, 31.21196, 0.0), ), ((
        1.891428, 31.208422, 0.0), ), ((1.858207, 31.133839, 0.0), ), ((
        1.855829, 31.020906, 0.0), ), ((1.946528, 30.98804, 0.0), ), ((
        2.210672, 30.932965, 0.0), ), ((2.027163, 30.61196, 0.0), ), ((1.85706,
        30.608422, 0.0), ), ((1.823839, 30.533839, 0.0), ), ((1.821461,
        30.420906, 0.0), ), ((1.91216, 30.38804, 0.0), ), ((2.176304,
        30.332965, 0.0), ), ((1.992796, 30.01196, 0.0), ), ((1.822693,
        30.008422, 0.0), ), ((1.789471, 29.933839, 0.0), ), ((1.787094,
        29.820906, 0.0), ), ((1.877793, 29.78804, 0.0), ), ((2.141937,
        29.732965, 0.0), ), ((1.958428, 29.41196, 0.0), ), ((1.788325,
        29.408422, 0.0), ), ((1.755104, 29.333839, 0.0), ), ((1.752726,
        29.220906, 0.0), ), ((1.843425, 29.18804, 0.0), ), ((2.107569,
        29.132965, 0.0), ), ((1.924061, 28.81196, 0.0), ), ((1.753958,
        28.808422, 0.0), ), ((1.720736, 28.733839, 0.0), ), ((1.718359,
        28.620906, 0.0), ), ((1.809058, 28.58804, 0.0), ), ((2.073202,
        28.532965, 0.0), ), ((1.889693, 28.21196, 0.0), ), ((1.71959,
        28.208422, 0.0), ), ((1.686369, 28.133839, 0.0), ), ((1.683991,
        28.020906, 0.0), ), ((1.77469, 27.98804, 0.0), ), ((2.038834,
        27.932965, 0.0), ), ((1.855325, 27.61196, 0.0), ), ((1.685223,
        27.608422, 0.0), ), ((1.652001, 27.533839, 0.0), ), ((1.649624,
        27.420906, 0.0), ), ((1.740323, 27.38804, 0.0), ), ((2.004466,
        27.332965, 0.0), ), ((1.820958, 27.01196, 0.0), ), ((1.650855,
        27.008422, 0.0), ), ((1.617634, 26.933839, 0.0), ), ((1.615256,
        26.820906, 0.0), ), ((1.705955, 26.78804, 0.0), ), ((1.970099,
        26.732965, 0.0), ), ((1.78659, 26.41196, 0.0), ), ((1.616488,
        26.408422, 0.0), ), ((1.583266, 26.333839, 0.0), ), ((1.580889,
        26.220906, 0.0), ), ((1.671587, 26.18804, 0.0), ), ((1.935731,
        26.132965, 0.0), ), ((1.752223, 25.81196, 0.0), ), ((1.58212,
        25.808422, 0.0), ), ((1.548899, 25.733839, 0.0), ), ((1.546521,
        25.620906, 0.0), ), ((1.63722, 25.58804, 0.0), ), ((1.901364,
        25.532965, 0.0), ), ((1.717855, 25.21196, 0.0), ), ((1.547753,
        25.208422, 0.0), ), ((1.50705, 25.003228, 0.0), ), ((1.456345,
        24.427259, 0.0), ), ((0.922269, 24.282751, 0.0), ))'''

    side1Edges2 = s2.getByBoundingBox(-5,-5,-5,80,80,80)


    s3 = a.instances['implant-1'].edges
    '''side1Edges3 = s3.findAt(((0.307423, 24.282751, 0.0), ), ((1.322049, 24.300436,
        0.0), ), ((1.488538, 24.680045, 0.0), ), ((1.520893, 25.183058, 0.0),
        ), ((1.616768, 25.21196, 0.0), ), ((1.901364, 25.267035, 0.0), ), ((
        1.724673, 25.58804, 0.0), ), ((1.573701, 25.592125, 0.0), ), ((1.54535,
        25.67188, 0.0), ), ((1.555261, 25.783058, 0.0), ), ((1.651135,
        25.81196, 0.0), ), ((1.935731, 25.867035, 0.0), ), ((1.75904, 26.18804,
        0.0), ), ((1.608068, 26.192125, 0.0), ), ((1.579717, 26.27188, 0.0), ),
        ((1.589628, 26.383058, 0.0), ), ((1.685503, 26.41196, 0.0), ), ((
        1.970099, 26.467035, 0.0), ), ((1.793408, 26.78804, 0.0), ), ((
        1.642436, 26.792125, 0.0), ), ((1.614085, 26.87188, 0.0), ), ((
        1.623996, 26.983058, 0.0), ), ((1.71987, 27.01196, 0.0), ), ((2.004466,
        27.067035, 0.0), ), ((1.827775, 27.38804, 0.0), ), ((1.676803,
        27.392125, 0.0), ), ((1.648452, 27.47188, 0.0), ), ((1.658363,
        27.583058, 0.0), ), ((1.754238, 27.61196, 0.0), ), ((2.038834,
        27.667035, 0.0), ), ((1.862143, 27.98804, 0.0), ), ((1.711171,
        27.992125, 0.0), ), ((1.68282, 28.07188, 0.0), ), ((1.692731,
        28.183058, 0.0), ), ((1.788605, 28.21196, 0.0), ), ((2.073202,
        28.267035, 0.0), ), ((1.89651, 28.58804, 0.0), ), ((1.745538,
        28.592125, 0.0), ), ((1.717187, 28.67188, 0.0), ), ((1.727099,
        28.783058, 0.0), ), ((1.822973, 28.81196, 0.0), ), ((2.107569,
        28.867035, 0.0), ), ((1.930878, 29.18804, 0.0), ), ((1.779906,
        29.192125, 0.0), ), ((1.751555, 29.27188, 0.0), ), ((1.761466,
        29.383058, 0.0), ), ((1.85734, 29.41196, 0.0), ), ((2.141937,
        29.467035, 0.0), ), ((1.965245, 29.78804, 0.0), ), ((1.814273,
        29.792125, 0.0), ), ((1.785922, 29.87188, 0.0), ), ((1.795834,
        29.983058, 0.0), ), ((1.891708, 30.01196, 0.0), ), ((2.176304,
        30.067035, 0.0), ), ((1.999613, 30.38804, 0.0), ), ((1.848641,
        30.392125, 0.0), ), ((1.82029, 30.47188, 0.0), ), ((1.830201,
        30.583058, 0.0), ), ((1.926075, 30.61196, 0.0), ), ((2.210672,
        30.667035, 0.0), ), ((2.03398, 30.98804, 0.0), ), ((1.883008,
        30.992125, 0.0), ), ((1.854658, 31.07188, 0.0), ), ((1.864569,
        31.183058, 0.0), ), ((1.960443, 31.21196, 0.0), ), ((2.245039,
        31.267035, 0.0), ), ((2.068348, 31.58804, 0.0), ), ((1.917376,
        31.592125, 0.0), ), ((1.889025, 31.67188, 0.0), ), ((1.898936,
        31.783058, 0.0), ), ((1.994811, 31.81196, 0.0), ), ((2.279407,
        31.867035, 0.0), ), ((2.102716, 32.18804, 0.0), ), ((1.951743,
        32.192125, 0.0), ), ((1.923393, 32.27188, 0.0), ), ((1.933304,
        32.383058, 0.0), ), ((2.029178, 32.41196, 0.0), ), ((2.313774,
        32.467035, 0.0), ), ((2.137083, 32.78804, 0.0), ), ((1.986111,
        32.792125, 0.0), ), ((1.95776, 32.87188, 0.0), ), ((1.967671,
        32.983058, 0.0), ), ((2.063546, 33.01196, 0.0), ), ((2.348142,
        33.067035, 0.0), ), ((2.171451, 33.38804, 0.0), ), ((2.020478,
        33.392125, 0.0), ), ((1.992128, 33.47188, 0.0), ), ((2.002039,
        33.583058, 0.0), ), ((2.097913, 33.61196, 0.0), ), ((2.382509,
        33.667035, 0.0), ), ((2.205818, 33.98804, 0.0), ), ((2.054846,
        33.992125, 0.0), ), ((2.026495, 34.07188, 0.0), ), ((2.036406,
        34.183058, 0.0), ), ((2.132281, 34.21196, 0.0), ), ((2.416877,
        34.267035, 0.0), ), ((2.240186, 34.58804, 0.0), ), ((2.089213,
        34.592125, 0.0), ), ((2.06423, 34.730675, 0.0), ), ((1.954657, 35.0,
        0.0), ), ((1.497243, 34.275, 0.0), ), ((1.0875, 32.1, 0.0), ), ((0.6,
        31.425, 0.0), ), ((0.45, 29.4, 0.0), ), ((0.0, 28.120688, 0.0), ))'''

    side1Edges3 = s3.getByBoundingBox(-5,-5,-5,80,80,80)



    s4 = a.instances['abutment-1'].edges
    '''side1Edges4 = s4.findAt(((0.6, 35.9625, 0.0), ), ((0.7625, 32.1, 0.0), ), ((
        1.346624, 32.95, 0.0), ), ((1.539871, 35.9375, 0.0), ), ((1.0875,
        37.25, 0.0), ))'''

    side1Edges4 = s4.getByBoundingBox(-5,-5,-5,80,80,80)
    #side1Edges4=s4.findAt(edges1)


    s5 = a.instances['screw-1'].edges
    '''side1Edges5 = s5.findAt(((0.0, 33.975, 0.0), ), ((0.15, 29.4, 0.0), ), ((0.6,
        30.925, 0.0), ), ((0.45, 35.5, 0.0), ))'''
    side1Edges5 = s5.getByBoundingBox(-5,-5,-5,80,80,80)





    s6 = a.instances['crown-1'].edges
    '''side1Edges6 = s6.findAt(((0.7625, 37.25, 0.0), ), ((1.25, 37.375, 0.0), ), ((
        1.0875, 37.75, 0.0), ), ((0.6, 37.625, 0.0), ))'''
    side1Edges6 = s6.getByBoundingBox(-5,-5,-5,80,80,80)




    region=a.Surface(side1Edges=side1Edges1+side1Edges2+side1Edges3+side1Edges4+\
        side1Edges5+side1Edges6, name='Surf-1')



    #region=a.Surface(side1Edges=side1Edges1+side1Edges2+side1Edges3+side1Edges4+\
    #    side1Edges5+side1Edges6, name='Surf-1')




    mdb.models['Model-1'].SelfContactStd(name='Int-1', createStepName='Step-1',
        surface=region, interactionProperty='friction', thickness=ON,
        contactControls='ContCtrl-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
        predefinedFields=ON, interactions=OFF, constraints=OFF,
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=88.8179,
        farPlane=96.7446, width=39.7839, height=20.3699, viewOffsetX=-1.39888,
        viewOffsetY=10.6927)





    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['crown-1'].surfaces['crowntop']
    mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1',
        region=region, distributionType=UNIFORM, field='', magnitude=21.1,
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
