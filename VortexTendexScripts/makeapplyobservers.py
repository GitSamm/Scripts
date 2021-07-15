
#=================================================================
# This file will make the required ApplyObservers.input file needed
# to generate vortex and tendex lines.
# Created by Haroon, maintained by Sam. So if you have any questions, ask them...
#=================================================================


#=================================================================
# Set the value = 1 to visualize the the lines. If you want to make the lines
# for merger/ringdown, set *C=1 and *A=0 and *B=0
#=================================================================

TendexA=0
TendexB=0
TendexC=0

VortexA=0
VortexB=0
VortexC=0



#=================================================================
# Change the variables below. Default setting should be fine,
# except for the Centers of the holes.
#=================================================================
AbsoluteErrorScale="1.e-6"
MinimumDlambda="1.e-10"
InitialDlambda="1.e-3"
EigenvalueDegeneracyTol="1.e-9"
DeltaT="0.05" # Lower to make the lines smoother. 0.05 DeltaT is already very small, so if the black holes are far apart, increase to make visualization quicker.
Verbosity="2"
TerminateOnLambda="12" # How long do you want the lines to be?
SpatialMetric="Inertialg"
MapPrefixFromGridFrame ="GridToInertial"

NumStreams = "100" # How many lines do you want?
VecAposition="0.0"
VecBposition="1.0"
NumRefinements="5"


# H5 Stuff for the orbital intializer.
H5File = "OrbitDiagnostics.h5"
DataSet = "OrbitalPhase.dat"


#======
# choose how to read in times
# Time: If you want to use a specific time insert value within quotes. Otherwise leave blank.
# TakeTimeFromDataBox: Read time values from data. Use true or false
# DeltaT: Tolerance on Time; default 1.e-10
# TimeFormula: a specific formula to calculate time. If you want first time step in segment do "t+0"
#======

Time = "" ## LEAVE EMPTY IF NOT USING THIS
TimeFormula = "" ## LEAVE EMPTY IF NOT USING THIS
TakeTimeFromDataBox = 0 ## (BOOL) By default this is true. If other options are left blank the code will use this.

DeltaT_header = "1.e-7" #double






#=================================================================
# This block of code lets you decide on the initializer
# (where and how you want to seed the lines).
# Set the value =1 of the initializer  you
# want to use/visualize.
# Depending on which initializer you use you will have to specify which lines.
# For example, the Apparent Horizons initializer seeds the points from the horizons
# so we need to specify AhA, AhB, or AhC.
#
# ApparentHorizon -> seeds the lines from the horizons
# SpecifyPointAndEigenvector -> seeds the lines around the holes based on the given eigenvector
# Drift Velocity -> Seed the lines so they move with the holes. Used to see vortex and tendex lines with the GW's
#
#=================================================================

#CHOOSE INITIALIZER:
ApparentHorizon=0
OrbitalApparentHorizon = 0
SpecifyPointAndEigenvector = 0
DotProduct = 0
DriftVelocity = 0


#...........................................

#SETTINGS FOR APPARENTHORIZON
#======================================
# If you want to seed the lines from the center of the holes
# set the center of the holes.
# The locations of the centers for AhA and AhB are
# ../Run/ApparentHorizons/Ah?Coefs.dat
# The location of the center of AhC is in
# ../GrDomain.input.
# It just usually (0,0,0).
#======================================

CenterA = "()"
CenterB = "()"
CenterC = "()"


#...........................................


#SETTINGS FOR SpecifyPointAndEigenvector
#============================================
# The following block of code is used if you
# want to seed the lines from various points
# around the holes. Choose the eigenvector
# you want and give a set of start points.
# The default start points are just a test, you
# can delete them and put your own if you want.
#============================================

#...........................................
# Change the values to generate the type of line.
TendexSpecEig = 0
VortexSpecEig = 0

#choose a value (0,1,2)
#...........................................
Eigenvector = "1"
SPE_StartPoints = " (-3,-3,-3),(-3,-3,-2),(-3,-3,-1)"
#...........................................
#============================================


#SETTINGS FOR DotProductInitialzer
#=============================================
# The following block of code is meant to allow
# you to be able to have a more control over
# which eigenvector is choosen. The code will 
# find out which of the eigenvectors is closest 
# to, for example, the x plane and then start seeding lines
# that are closest to that plane. Change
# NormalizedVector to one of the planes to choose
# the plane that you want the lines to be closest to.

TendexDotEig = 0
VortexDotEig = 0

#...........................................
Dot_StartPoints = " (-3,-3,-3),(-3,-3,-2),(-3,-3,-1)"
NormalizedVector = " (1,0,0) "
#...........................................
#============================================


# SETTINGS FOR DRIFTVELOCITY
#=============================================
# The drift velocity initializer is used to see the lines as gw's.
# Note that each startpoint needs to have a corrosponding startdirection
#============================================

#...........................................

StartPoints_DriftVel = " (-4,15,-4), (4,15,-4), (-4,15,0), (4,-15,0), (-4,15,4), (4,-15,4), (-4,15,-4), (4,-15,-4), (-4,15,0), (4,-15,0),(-4,15,4), (4,-15,4), (-4,15,-4), (4,-15,-4), (-4,15,0), (4,-15,0), (-4,15,4), (4,15,4), (4,15,-4), (4,-15,-4), (-4,15,0), (4,-15,0), (-4,15,4), (4,-15,4), (-4,15,-4), (4,15,-4), (-4,15,0), (4,-15,0), (-4,15,4), (4,15,4), (4,15,-4), (4,-15,-4)"

StartDirections = "  (1.,1.,0.), (1.,1.,0.), (1.,1.,0.), (1.,1.,0.), (1.,1.,0.), (1.,1.,0.), (0.,1.,1.), (0.,1.,1.), (0.,1.,1.), (0.,1.,1.), (0.,1.,1.), (0.,1.,1.), (1.,0.,1.), (1.,0.,1.), (1.,0.,1.), (1.,0.,1.), (1.,0.,1.), (1.,0.,1.), (-1.,0.,-1.), (-1.,0.,-1.), (-1.,0.,-1.), (-1.,0.,-1.), (-1.,0.,-1.), (-1.,0.,-1.), (-1.,-1.,0.), (-1.,-1.,0.), (-1.,-1.,0.), (-1.,-1.,0.), (-1.,-1.,0.), (-1.,-1.,0.), (-1.,0.,-1.), (-1.,0.,-1.) "
#...........................................

DriftTendex = 0
DriftVortex = 0


semicolon = ");"
comma = "),"

file=open('ApplyObservers.input','w')

#=================================================================
# Create the vectors that the lines are seeded along, for both the
# apparent horizon and orbit initializer.
#=================================================================

Vec1="(0,0,1)"
Vec2="(0,0,-1)"
Vec3="(1,0,0)"
Vec4="(-1,0,0)"

#=================================================================
# This part of the code just deals with the stuff at the top of the
# input file
#=================================================================

timer = ""
if TakeTimeFromDataBox:
     timer = "TakeTimeFromDataBox = yes"
elif Time:
    timer = "Time = " + Time


else:
    if TimeFormula:
        timer = "TimeFormula = " + TimeFormula
    else:
        timer = "TakeTimeFromDataBox = yes"




topoffile="""DataBoxItems =
    ReadFromFile(File=SpatialCoordMap.input),
        Domain(
               Items=
               ReadSurfaceInfoFromFile(
                                       FileName=ApparentHorizons/AhACoefs.dat;
                                       Output = AhA;
                                       """ + timer + """;
                                       DeltaT=""" + DeltaT_header + """;
                                       ),
               ReadSurfaceInfoFromFile(
                                       FileName=ApparentHorizons/AhBCoefs.dat;
                                       Output = AhB;
                                       """ + timer + """;
                                       DeltaT=""" + DeltaT_header + """;
                                       ),
               CoordMappedSurfaceInfo(
                                      Input=AhA;
                                      MapPrefix=DistortedToInertial;
                                      MapGoesToOutputFrame=True;
                                      Recenter=False;
                                      Output=AhAInertial;
                                      ),
               CoordMappedSurfaceInfo(
                                      Input=AhB;
                                      MapPrefix=DistortedToInertial;
                                      MapGoesToOutputFrame=True;
                                      Recenter=False;                                                                                      
                                      Output=AhBInertial;                                                                                                                  
                                     ),  

    """

topoffileAHC="""DataBoxItems =
    ReadFromFile(File=SpatialCoordMap.input),
    Domain(
        Items=
        ReadSurfaceInfoFromFile(
            FileName=ApparentHorizons/AhCCoefs.dat ;
            Output = AhC;
            """ +  timer +""";
            DeltaT=""" + DeltaT_header + """;
        ),
        CoordMappedSurfaceInfo(
                               Input=AhC;
                               MapPrefix=DistortedToInertial;
                               MapGoesToOutputFrame=True;
                               Recenter=False;
                               Output=AhCInertial;
                              ),"""


topoffile_driftvel="""
    ),
    Subdomain
    (Items =
    
    
        ConvertVectorFromMyVectorToTensor(Output=GCoords; Input=GlobalCoords),
        EvaluateScalarFormula(Output=radius; Formula=sqrt(x0*x0+x1*x1+x2*x2);),
        BinaryOp(Output=radialVec; A=GCoords; B=radius; Op=A/B;),
    

    """

top_end="""
        );
        
        Observers =
"""

#============================================



def Observers_block (streamline,**kwargs):
    
    if streamline=="Tendex" or streamline=="tendex":
                SymmetricCovariantTensor="VTWeylE"

    if streamline =="Vortex" or streamline =="vortex":
                SymmetricCovariantTensor="VTWeylB"
    for key, value in kwargs.iteritems():
        if key == 'hole':
            if value == "AhAInertial":
                Center = CenterA
                hole = value
            if value == "AhBInertial":
                Center = CenterB
                hole = value
            if value == "AhCInertial":
                Center = CenterC
                hole = value
        if key == 'VecA':
            VecA = value
        if key == 'VecB':
            VecB = value
        if key == 'Basename':
            Basename = value
        if key == 'initializer':
            initializer = value

    if initializer == "ApparentHorizon":
    
    
        initializer_block ="""ApparentHorizon(
                                    StrahlkorperBasename="""+hole+""";
                                    Center ="""+ Center +""";
                                    VecA = """+ VecA +""";
                                    VecB = """ + VecB +""";
                                    Basename ="""+ Basename+""";
                                    NumStreams ="""+NumStreams+""";
                                    VecAposition="""+VecAposition+""";
                                    VecBposition="""+VecBposition+""";
                                    NumRefinements=""" + NumRefinements +""";
                                );"""
    

    elif initializer == "OrbitalApparentHorizon":
         
         initializer_block ="""OrbAppHorizon(
                                    StrahlkorperBasename="""+hole+""";
                                    Center ="""+ Center +""";
                                    VecA = """+ VecA +""";
                                    VecB = """ + VecB +""";              
                                    Basename ="""+ Basename+""";        
                                    NumStreams ="""+NumStreams+""";
                                    VecAposition="""+VecAposition+""";
                                    VecBposition="""+VecBposition+""";                                                                                                
                                    NumRefinements=""" + NumRefinements +""";
                                    H5File = """ + H5File + """;
                                    DataSet = """ + DataSet +  """;
                                );"""

    elif initializer == "SpecifyPointAndEigenvector":

        initializer_block = """SpecifyPointAndEigenvector(
                                    Basename ="""+streamline+"""_Eigenvector"""+Eigenvector+""";
                                    StartPoints = (""" + SPE_StartPoints + """);
                                        WhichEigenvector =""" + Eigenvector + """ ;
                                        SymmetricCovariantTensor="""+SymmetricCovariantTensor+""";
                                        SpatialMetric="""+SpatialMetric+""";
                                        MapPrefixFromGridFrame="""+MapPrefixFromGridFrame+""";
                                        Verbosity="""+Verbosity+""";
                                
                                );

                                """

    elif initializer == "DotProduct":

         initializer_block = """DotProduct(
                                        StartPoints = (""" + Dot_StartPoints + """);
                                        Basename = """+streamline+"""_Eigenvector"""+Eigenvector+""";
                                        SymmetricCovariantTensor="""+SymmetricCovariantTensor+""";
                                        SpatialMetric="""+SpatialMetric+""";
                                        MapPrefixFromGridFrame="""+MapPrefixFromGridFrame+""";
                                        Verbosity="""+Verbosity+"""; 
                                        NormalizedVector="""+NormalizedVector+""";


                                 );


                             """



    
    elif initializer == "DriftVelocity":
    
        initializer_block = """ DriftVelocity(
            
                                    OneTimeInitializer=SpecifyValues(
                                        Basename=vortex;
                                        StartPoints=(""" + StartPoints_DriftVel+ """);
                                        StartDirections=(""" + StartDirections + """);
                                        
                                        );
                                        
                                VelocityField=radialVec;
                                SymmetricCovariantTensor="""+SymmetricCovariantTensor+""";
                                SpatialMetric="""+SpatialMetric+""";
                                MapPrefixFromGridFrame="""+MapPrefixFromGridFrame+""";
                                Verbosity="""+Verbosity+""";
            
                                    );
    
                            """
                                

        
        
        
                    

    string_block = """
        ObserveInSubdir(
                    Subdir=Streamlines;
                    Observers=
                        ParallelEigenvectorStreamlines
                        (SymmetricCovariantTensor= """+SymmetricCovariantTensor+""";
                        SpatialMetric="""+SpatialMetric+""";
                        MapPrefixFromGridFrame ="""+MapPrefixFromGridFrame+""";
                        AbsoluteErrorScale="""+AbsoluteErrorScale +""";
                        MinimumDlambda=""" + MinimumDlambda+""";
                        InitialDlambda="""+InitialDlambda+""";
                        EigenvalueDegeneracyTol="""+EigenvalueDegeneracyTol+""";
                        DenseTriggerOnLambda=EveryDeltaT(DeltaT=""" +DeltaT+""";);
                        Verbosity="""+Verbosity+""";
                        TerminateOnLambda="""+TerminateOnLambda+""";
                        Initializer= """+initializer_block+"""
                        
                        )
        
"""


    return string_block


################################################################## 
################################################################## 
# Apparent Horizon Tendex Lines
################################################################## 
################################################################## 


#=================================================================
# Tendex lines for hole A
#=================================================================

#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
TendexAhA_1 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhAInertial",VecA=Vec1,VecB=Vec4,Basename="TendexAhA_1")

#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================
TendexAhA_2 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhAInertial",VecA ="(0,0,-1)",VecB="(-1,0,0)",Basename="TendexAhA_2")

#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
TendexAhA_3 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhAInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="TendexAhA_3")

#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
TendexAhA_4 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhAInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="TendexAhA_4")







#=================================================================
# Tendex lines for hole B
#=================================================================


#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
TendexAhB_1 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhBInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="TendexAhB_1")

#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================

TendexAhB_2 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhBInertial",VecA="(0,0,-1)",VecB="(-1,0,0)",Basename="TendexAhB_2")


#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
TendexAhB_3 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhBInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="TendexAhB_3")


#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
TendexAhB_4 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhBInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="TendexAhB_4")




#=================================================================
# Tendex lines for hole C
#=================================================================

#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
TendexAhC_1 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhCInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="TendexAhC_1")


#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================
TendexAhC_2 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhCInertial",VecA="(0,0,-1)",VecB="(-1,0,0)",Basename="TendexAhC_2")

#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
TendexAhC_3 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhCInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="TendexAhC_3")


#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
TendexAhC_4 = Observers_block("Tendex",initializer="ApparentHorizon",hole="AhCInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="TendexAhC_4")




################################################################## 
################################################################## 
# Apparent Horizon Vortex Lines
################################################################## 
################################################################## 



#=================================================================
# Vortex lines for hole A
#=================================================================


#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
VortexAhA_1 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhAInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="VortexAhA_1")

#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================
VortexAhA_2 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhAInertial",VecA ="(0,0,-1)",VecB="(-1,0,0)",Basename="VortexAhA_2")

#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
VortexAhA_3 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhAInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="VortexAhA_3")

#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
VortexAhA_4 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhAInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="VortexAhA_4")








#=================================================================
# Vortex lines for hole B
#=================================================================
                                          
#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
VortexAhB_1 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhBInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="VortexAhB_1")

#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================

VortexAhB_2 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhBInertial",VecA="(0,0,-1)",VecB="(-1,0,0)",Basename="VortexAhB_2")


#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
VortexAhB_3 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhBInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="VortexAhB_3")

#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
VortexAhB_4 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhBInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="VortexAhB_4")









#=================================================================
# Vortex lines for hole C
#=================================================================


#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
VortexAhC_1 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhCInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="VortexAhC_1")


#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================
VortexAhC_2 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhCInertial",VecA="(0,0,-1)",VecB="(-1,0,0)",Basename="VortexAhC_2")

#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
VortexAhC_3 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhCInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="VortexAhC_3")


#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
VortexAhC_4 = Observers_block("Vortex",initializer="ApparentHorizon",hole="AhCInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="VortexAhC_4")



################################################################## 
################################################################## 
# Orbital Initializer Tendex Lines
################################################################## 
################################################################## 


#=================================================================
# Tendex lines for hole A
#=================================================================

#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
TendexAhA_O_1 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhAInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="TendexAhA_1")

#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================
TendexAhA_O_2 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhAInertial",VecA ="(0,0,-1)",VecB="(-1,0,0)",Basename="TendexAhA_2")

#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
TendexAhA_O_3 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhAInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="TendexAhA_3")

#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
TendexAhA_O_4 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhAInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="TendexAhA_4")







#=================================================================
# Tendex lines for hole B
#=================================================================


#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
TendexAhB_O_1 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhBInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="TendexAhB_1")

#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================

TendexAhB_O_2 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhBInertial",VecA="(0,0,-1)",VecB="(-1,0,0)",Basename="TendexAhB_2")


#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
TendexAhB_O_3 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhBInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="TendexAhB_3")


#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
TendexAhB_O_4 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhBInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="TendexAhB_4")




#=================================================================
# Tendex lines for hole C
#=================================================================

#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
TendexAhC_O_1 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhCInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="TendexAhC_1")


#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================
TendexAhC_O_2 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhCInertial",VecA="(0,0,-1)",VecB="(-1,0,0)",Basename="TendexAhC_2")

#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
TendexAhC_O_3 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhCInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="TendexAhC_3")


#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
TendexAhC_O_4 = Observers_block("Tendex",initializer = "OrbitalApparentHorizon",hole="AhCInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="TendexAhC_4")




################################################################## 
################################################################## 

# Orbital Initializer Vortex Lines

################################################################## 
################################################################## 



#=================================================================
# Vortex lines for hole A
#=================================================================


#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
VortexAhA_O_1 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhAInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="VortexAhA_1")

#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================
VortexAhA_O_2 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhAInertial",VecA ="(0,0,-1)",VecB="(-1,0,0)",Basename="VortexAhA_2")

#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
VortexAhA_O_3 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhAInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="VortexAhA_3")

#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
VortexAhA_O_4 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhAInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="VortexAhA_4")








#=================================================================
# Vortex lines for hole B
#=================================================================
                                          
#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
VortexAhB_O_1 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhBInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="VortexAhB_1")

#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================

VortexAhB_O_2 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhBInertial",VecA="(0,0,-1)",VecB="(-1,0,0)",Basename="VortexAhB_2")


#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
VortexAhB_O_3 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhBInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="VortexAhB_3")

#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
VortexAhB_O_4 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhBInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="VortexAhB_4")









#=================================================================
# Vortex lines for hole C
#=================================================================


#===========================
# Quadrant 1 (x=0,z=1 to x=-1,z=0)
#===========================
VortexAhC_O_1 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhCInertial",VecA="(0,0,1)",VecB="(-1,0,0)",Basename="VortexAhC_1")


#===========================
# Quadrant 2 (x=0,z=-1 to x=-1,z=0)
#===========================
VortexAhC_O_2 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhCInertial",VecA="(0,0,-1)",VecB="(-1,0,0)",Basename="VortexAhC_2")

#===========================
# Quadrant 3 (x=0,z=-1 to x=1,z=0)
#===========================
VortexAhC_O_3 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhCInertial",VecA="(0,0,-1)",VecB="(1,0,0)",Basename="VortexAhC_3")


#===========================
# Quadrant 4 (x=0,z=1 to x=1,z=0)
#===========================
VortexAhC_O_4 = Observers_block("Vortex",initializer = "OrbitalApparentHorizon",hole="AhCInertial",VecA="(0,0,1)",VecB="(1,0,0)",Basename="VortexAhC_4")









##################################################################                                                            
##################################################################
# SpecifyPointandEigenVector
##################################################################                                                                                                             
##################################################################                                                                                                                                 

#=================================================================
# Tendex lines seeding from various points (eigenvectors)

#=================================================================

                                          
Tendex_eigenvec = Observers_block("Tendex",initializer="SpecifyPointAndEigenvector")


#=================================================================
# Vortex lines seeding from various points (eigenvectors)

#=================================================================

Vortex_eigenvec = Observers_block("Vortex",initializer="SpecifyPointAndEigenvector")



################################################################## 
################################################################## 
# DotProduct
################################################################## 
################################################################## 
Tendex_dot = Observers_block("Tendex",initializer="DotProduct")
Vortex_dot = Observers_block("Vortex",initializer="DotProduct")





################################################################## 
################################################################## 
# Drift Velocity
################################################################## 
##################################################################



#=================================================================
# Tendex lines seeding from various points using Drift Velocity

#=================================================================


Tendex_driftvel = Observers_block("Tendex",initializer="DriftVelocity")


#=================================================================
# Vortex lines seeding from various points (eigenvectors)

#=================================================================

Vortex_driftvel= Observers_block("Vortex",initializer="DriftVelocity")







#=================================================================
# This part of the code writes to the file.
#
#=================================================================

if ApparentHorizon == 1:

    if (TendexA == 1) or (TendexB == 1) or (VortexA == 1) or (VortexB == 1):
        file.write(topoffile)

    if (TendexC == 1) or (VortexC == 1):
        file.write(topoffileAHC)

    file.write(top_end)

    if TendexA == 1:
        file.write(TendexAhA_1)
        file.write(comma)
        file.write(TendexAhA_2)
        file.write(comma)
        file.write(TendexAhA_3)
        file.write(comma)
        file.write(TendexAhA_4)

        if TendexB == 1 or VortexA == 1 or  VortexB == 1:
            file.write(comma)

    if TendexB == 1:
        file.write(TendexAhB_1)
        file.write(comma)
        file.write(TendexAhB_2)
        file.write(comma)
        file.write(TendexAhB_3)
        file.write(comma)
        file.write(TendexAhB_4)

        if  VortexA == 1 or  VortexB == 1:
            file.write(comma)


    if VortexA == 1:
        file.write(VortexAhA_1)
        file.write(comma)
        file.write(VortexAhA_2)
        file.write(comma)
        file.write(VortexAhA_3)
        file.write(comma)
        file.write(VortexAhA_4)

        if VortexB == 1:
            file.write(comma)

    if VortexB == 1:
        file.write(VortexAhB_1)
        file.write(comma)
        file.write(VortexAhB_2)
        file.write(comma)
        file.write(VortexAhB_3)
        file.write(comma)
        file.write(VortexAhB_4)

    if TendexC == 1:
        file.write(TendexAhC_1)
        file.write(comma)
        file.write(TendexAhC_2)
        file.write(comma)
        file.write(TendexAhC_3)
        file.write(comma)
        file.write(TendexAhC_4)

        if VortexC == 1:
            file.write(comma)

    if VortexC == 1:
        file.write(VortexAhC_1)
        file.write(comma)
        file.write(VortexAhC_2)
        file.write(comma)
        file.write(VortexAhC_3)
        file.write(comma)
        file.write(VortexAhC_4)


if OrbitalApparentHorizon == 1:

    if (TendexA == 1) or (TendexB == 1) or (VortexA == 1) or (VortexB == 1):
        file.write(topoffile)

    if (TendexC == 1) or (VortexC == 1):
        file.write(topoffileAHC)

    file.write(top_end)

    if TendexA == 1:
        file.write(TendexAhA_O_1)
        file.write(comma)
        file.write(TendexAhA_O_2)
        file.write(comma)
        file.write(TendexAhA_O_3)
        file.write(comma)
        file.write(TendexAhA_O_4)

        if TendexB == 1 or VortexA == 1 or  VortexB == 1:
            file.write(comma)

    if TendexB == 1:
        file.write(TendexAhB_O_1)
        file.write(comma)
        file.write(TendexAhB_O_2)
        file.write(comma)
        file.write(TendexAhB_O_3)
        file.write(comma)
        file.write(TendexAhB_O_4)

        if  VortexA == 1 or  VortexB == 1:
            file.write(comma)


    if VortexA == 1:
        file.write(VortexAhA_O_1)
        file.write(comma)
        file.write(VortexAhA_O_2)
        file.write(comma)
        file.write(VortexAhA_O_3)
        file.write(comma)
        file.write(VortexAhA_O_4)

        if VortexB == 1:
            file.write(comma)

    if VortexB == 1:
        file.write(VortexAhB_O_1)
        file.write(comma)
        file.write(VortexAhB_O_2)
        file.write(comma)
        file.write(VortexAhB_O_3)
        file.write(comma)
        file.write(VortexAhB_O_4)

    if TendexC == 1:
        file.write(TendexAhC_O_1)
        file.write(comma)
        file.write(TendexAhC_O_2)
        file.write(comma)
        file.write(TendexAhC_O_3)
        file.write(comma)
        file.write(TendexAhC_O_4)

        if VortexC == 1:
            file.write(comma)

    if VortexC == 1:
        file.write(VortexAhC_O_1)
        file.write(comma)
        file.write(VortexAhC_O_2)
        file.write(comma)
        file.write(VortexAhC_O_3)
        file.write(comma)
        file.write(VortexAhC_O_4)



if SpecifyPointAndEigenvector == 1:

    if (TendexA == 1) or (TendexB == 1) or (VortexA == 1) or (VortexB == 1):
        file.write(topoffile)

    if (TendexC == 1) or (VortexC == 1):
        file.write(topoffileAHC)

    file.write(top_end)

    if TendexSpecEig == 1:
        file.write(Tendex_eigenvec)

        if VortexSpecEig == 1:
             file.write(comma)

    if VortexSpecEig == 1:
        file.write(Vortex_eigenvec)


if DotProduct ==1:

     if (TendexA == 1) or (TendexB == 1) or (VortexA == 1) or (VortexB == 1):
          file.write(topoffile)

     if (TendexC ==1) or (VortexC == 1):
          file.write(topoffileAHC)

     file.write(top_end)

     if TendexDotEig == 1:
          file.write(Tendex_dot)
          
          if VortexDotEig == 1:
               file.write(comma)
     if VortexDotEig == 1:
          file.write(Vortex_dot)




if DriftVelocity == 1:
    
    if (TendexA == 1) or (TendexB == 1) or (VortexA == 1) or (VortexB == 1):
        file.write(topoffile)
    
    if (TendexC == 1) or (VortexC == 1):
        file.write(topoffileAHC)

    file.write(topoffile_driftvel)
    file.write(top_end)

    if DriftTendex == 1:
        file.write(Tendex_driftvel)
        
        if Vortex==1:
            file.write(comma)

    if DriftVortex == 1:
        file.write(Vortex_driftvel)



file.write(semicolon)

