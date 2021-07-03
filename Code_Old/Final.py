from os import path
import numpy as np
import heapq




##Data values used
nsqr = np.array([1.4142135623730951, 1.7320508075688772, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.1622776601683795, 3.3166247903554, 3.605551275463989, 3.7416573867739413, 3.872983346207417, 4.123105625617661, 4.358898943540674, 4.58257569495584, 4.69041575982343, 4.795831523312719, 4.898979485566356, 5.0990195135927845, 5.196152422706632, 5.385164807134504, 5.477225575051661, 5.5677643628300215, 5.656854249492381, 5.744562646538029, 5.830951894845301, 5.916079783099616, 6.082762530298219, 6.164414002968976, 6.244997998398398, 6.324555320336759, 6.4031242374328485, 6.48074069840786, 6.557438524302, 6.782329983125268, 6.855654600401044, 7.14142842854285, 7.280109889280518, 7.3484692283495345, 7.416198487095663, 7.483314773547883, 7.54983443527075, 7.615773105863909, 7.681145747868608, 7.810249675906654, 7.874007874011811, 8.06225774829855, 8.12403840463596, 8.18535277187245, 8.306623862918075, 8.366600265340756, 8.426149773176359, 8.54400374531753, 8.602325267042627, 8.774964387392123, 8.831760866327848, 8.888194417315589, 9.055385138137417, 9.1104335791443, 9.219544457292887, 9.273618495495704, 9.327379053088816, 9.38083151964686, 9.433981132056603, 9.539392014169456, 9.643650760992955, 9.695359714832659, 9.746794344808963, 9.797958971132712, 9.848857801796104, 10.04987562112089, 10.099504938362077, 10.14889156509222, 10.198039027185569, 10.246950765959598, 10.295630140987, 10.344080432788601, 10.44030650891055, 10.488088481701515, 10.535653752852738, 10.63014581273465, 10.677078252031311, 10.723805294763608, 10.862780491200215, 10.908712114635714, 10.954451150103322, 11.045361017187261, 11.090536506409418, 11.180339887498949, 11.269427669584644, 11.313708498984761, 11.357816691600547, 11.40175425099138, 11.445523142259598, 11.532562594670797, 11.575836902790225, 11.61895003862225, 11.661903789690601, 11.704699910719626, 11.74734012447073, 11.789826122551595, 11.874342087037917, 11.916375287812984, 11.958260743101398, 12.041594578792296, 12.083045973594572, 12.206555615733702, 12.288205727444508, 12.328828005937952, 12.409673645990857, 12.449899597988733, 12.529964086141668, 12.569805089976535, 12.609520212918492, 12.649110640673518, 12.68857754044952, 12.767145334803704, 12.84523257866513, 12.884098726725126, 12.922847983320086, 12.96148139681572, 13.038404810405298, 13.152946437965905, 13.19090595827292, 13.30413469565007, 13.341664064126334, 13.379088160259652, 13.45362404707371, 13.490737563232042, 13.527749258468683, 13.564659966250536, 13.601470508735444, 13.638181696985855, 13.674794331177344, 13.74772708486752, 13.784048752090222, 13.820274961085254, 13.892443989449804, 13.92838827718412, 13.96424004376894, 14.035668847618199, 14.106735979665885, 14.177446878757825, 14.212670403551895, 14.247806848775006, 14.317821063276353, 14.352700094407323, 14.45683229480096, 14.491376746189438, 14.52583904633395, 14.594519519326424, 14.628738838327793, 14.66287829861518, 14.696938456699069, 14.730919862656235, 14.7648230602334, 14.798648586948742, 14.866068747318506, 14.89966442575134, 14.933184523068078, 14.966629547095765, 15.033296378372908, 15.066519173319364, 15.132745950421556, 15.165750888103101, 15.198684153570664, 15.231546211727817, 15.264337522473747, 15.329709716755891, 15.394804318340652, 15.427248620541512, 15.459624833740307, 15.524174696260024, 15.588457268119896, 15.684387141358123, 15.716233645501712, 15.748015748023622, 15.7797338380595, 15.811388300841896, 15.84297951775486, 15.905973720586866, 15.937377450509228, 15.968719422671311, 16.0312195418814, 16.06237840420901, 16.09347693943108, 16.186414056238647, 16.217274740226856, 16.24807680927192, 16.278820596099706, 16.30950643030009, 16.34013463836819, 16.401219466856727, 16.431676725154983, 16.46207763315433, 16.522711641858304, 16.55294535724685, 16.64331697709324, 16.673332000533065, 16.73320053068151, 16.76305461424021, 16.792855623746664, 16.822603841260722, 16.881943016134134, 16.911534525287763, 16.941074346097416, 17.029386365926403, 17.05872210923198, 17.11724276862369, 17.175564037317667, 17.204650534085253, 17.233687939614086, 17.26267650163207, 17.291616465790582, 17.349351572897472, 17.378147196982766, 17.406895185529212, 17.46424919657298, 17.52141546793523, 17.578395831246947, 17.60681686165901, 17.635192088548397, 17.663521732655695, 17.69180601295413, 17.72004514666935, 17.804493814764857, 17.832554500127006, 17.86057109949175, 17.916472867168917, 17.944358444926362, 17.97220075561143, 18.05547008526779, 18.083141320025124, 18.110770276274835, 18.138357147217054, 18.16590212458495, 18.193405398660254, 18.275666882497067, 18.303005217723125, 18.35755975068582, 18.411952639521967, 18.466185312619388, 18.520259177452136, 18.547236990991408, 18.57417562100671, 18.601075237738275, 18.627936010197157, 18.681541692269406, 18.734993995195193, 18.76166303929372, 18.788294228055936, 18.81488772222678, 18.841443681416774, 18.894443627691185, 18.920887928424502, 18.947295321496416, 19.026297590440446, 19.1049731745428, 19.131126469708992, 19.157244060668017, 19.235384061671343, 19.261360284258224, 19.313207915827967, 19.339079605813716, 19.364916731037084, 19.390719429665317, 19.4164878389476, 19.44222209522358, 19.467922333931785, 19.519221295943137, 19.544820285692065, 19.570385790780925, 19.595917942265423, 19.621416870348583, 19.6468827043885, 19.72308292331602, 19.748417658131498, 19.77371993328519, 19.82422760159901, 19.849433241279208, 19.87460691435179, 19.924858845171276, 19.949937343260004, 19.974984355438178, 20.024984394500787, 20.049937655763422, 20.074859899884732, 20.149441679609886, 20.174241001832016, 20.199009876724155, 20.223748416156685, 20.248456731316587, 20.273134932713294, 20.322401432901575, 20.37154878746336, 20.396078054371138, 20.42057785666214, 20.445048300260872, 20.46948949045872, 20.518284528683193, 20.54263858417414, 20.591260281974, 20.639767440550294, 20.663978319771825, 20.71231517720798, 20.73644135332772, 20.760539492026695, 20.808652046684813, 20.83266665599966, 20.85665361461421, 20.904544960366874, 20.92844953645635, 20.952326839756964, 20.97617696340303, 21.02379604162864, 21.047565179849187, 21.095023109728988, 21.118712081942874, 21.142374511865974, 21.18962010041709, 21.236760581595302, 21.283796653792763, 21.307275752662516, 21.330729007701542, 21.354156504062622, 21.37755832643195, 21.400934559032695, 21.42428528562855, 21.470910553583888, 21.494185260204677, 21.517434791350013, 21.563858652847824, 21.587033144922902, 21.61018278497431, 21.656407827707714, 21.6794833886788, 21.702534414210707, 21.72556098240043, 21.748563170931547, 21.77154105707724, 21.863211109075447, 21.88606862823929, 21.908902300206645, 21.93171219946131, 21.95449840010015, 21.97726097583591, 22.02271554554524, 22.045407685048602, 22.06807649071391, 22.090722034374522, 22.11334438749598, 22.15851980616034, 22.20360331117452, 22.22611077089287, 22.293496809607955, 22.315913604421397, 22.338307903688676, 22.38302928559939, 22.40535650240808, 22.427661492005804, 22.47220505424423, 22.494443758403985, 22.561028345356956, 22.58317958127243, 22.60530911091463, 22.627416997969522, 22.64950330581225, 22.67156809750927, 22.693611435820433, 22.737634001804146, 22.759613353482084, 22.781571499789035, 22.80350850198276, 22.825424421026653, 22.869193252058544, 22.93468988235943, 22.956480566497994, 23.021728866442675, 23.08679276123039, 23.108440016582687, 23.130067012440755, 23.15167380558045, 23.173260452512935, 23.194827009486403, 23.259406699226016, 23.280893453645632, 23.302360395462088, 23.323807579381203, 23.345235059857504, 23.366642891095847, 23.388031127053, 23.473389188611005, 23.49468024894146, 23.515952032609693, 23.53720459187964, 23.558437978779494, 23.600847442411894, 23.643180835073778, 23.68543856465402, 23.706539182259394, 23.727621035409346, 23.769728648009426, 23.790754506740637, 23.83275057562597, 23.853720883753127, 23.874672772626646, 23.895606290697042, 23.93741840717165, 23.958297101421877, 24.020824298928627, 24.06241883103193, 24.1039415863879, 24.124676163629637, 24.145392935299274, 24.166091947189145, 24.20743687382041, 24.228082879171435, 24.269322199023193, 24.289915602982237, 24.310491562286437, 24.351591323771842, 24.372115213907882, 24.392621835300936, 24.43358344574123, 24.454038521274967, 24.474476501040833, 24.515301344262525, 24.535688292770594, 24.61706725018234, 24.63736998950984, 24.657656011875904, 24.677925358506133, 24.698178070456937, 24.71841418861655, 24.758836806279895, 24.779023386727733, 24.79919353527449, 24.819347291981714, 24.839484696748443, 24.859605789312106, 24.879710609249457, 24.919871588754223, 24.939927826679853, 24.95996794869737, 25.019992006393608, 25.03996805109783, 25.079872407968907, 25.11971337416094, 25.13961017995307, 25.15949125081825, 25.179356624028344, 25.199206336708304, 25.25866188063018, 25.298221281347036, 25.317977802344327, 25.337718918639855, 25.357444666211933, 25.39685019840059, 25.41653005427767, 25.436194683953808, 25.475478405713993, 25.514701644346147, 25.553864678361276, 25.573423705088842, 25.592967784139454, 25.65151067676132, 25.67099530598687, 25.709920264364882, 25.729360660537214, 25.748786379167466, 25.768197453450252, 25.787593916455254, 25.826343140289914, 25.865034312755125, 25.88435821108957, 25.903667693977237, 25.92296279363144, 25.942243542145693, 25.96150997149434, 26.019223662515376, 26.038433132583073, 26.057628441590765, 26.076809620810597, 26.095976701399778, 26.115129714401192, 26.13426869074396, 26.1725046566048, 26.19160170741759, 26.210684844162312, 26.248809496813376, 26.267851073127396, 26.28687885618983, 26.343879744638983, 26.362852652928137, 26.38181191654584, 26.40075756488817, 26.419689627245813, 26.43860813280457, 26.476404589747453, 26.49528259898354, 26.514147167125703, 26.551836094703507, 26.570660511172846, 26.589471600616662, 26.627053911388696, 26.645825188948457, 26.68332812825267, 26.70205984563738, 26.720778431774775, 26.739483914241877, 26.77685567799177, 26.795522013948524, 26.814175355583846, 26.851443164195103, 26.888659319497503, 26.962937525425527, 26.981475126464083, 27.018512172212592, 27.03701166919155, 27.073972741361768, 27.09243436828813, 27.129319932501073, 27.147743920996454, 27.184554438136374, 27.2213151776324, 27.23967694375247, 27.258026340878022, 27.27636339397171, 27.294688127912362, 27.313000567495326, 27.367864366808018, 27.386127875258307, 27.40437921208944, 27.440845468024488, 
27.459060435491963, 27.477263328068172, 27.51363298439521, 27.53179979587241, 27.54995462791182, 27.568097504180443, 27.586228448267445, 27.60434748368452, 27.622454633866266, 27.676705006196094, 27.694764848252458, 27.730849247724095, 27.748873851023216, 27.76688675382964, 27.80287754891569, 27.85677655436824, 27.874719729532707, 27.892651361962706, 27.910571473905726, 27.94637722496424, 27.964262908219126, 27.982137159266443, 28.0178514522438, 28.035691537752374, 28.053520278211074, 28.089143810376278, 28.106938645110393, 28.124722220850465, 28.160255680657446, 28.178005607210743, 28.19574435974337, 28.231188426986208, 28.24889378365107, 28.26658805020514, 28.319604517012593, 28.337254630609507, 28.372521918222215, 28.39013913315678, 28.407745422683583, 28.42534080710379, 28.442925306655784, 28.478061731796284, 28.513154858766505, 28.53068523537421, 28.548204847240395, 28.583211855912904, 28.600699292150182, 28.653097563788805, 28.6705423736629, 28.687976575562104, 28.705400188814647, 28.74021572639983, 28.75760768909681, 28.792360097775937, 28.809720581775867, 28.827070610799147, 28.879058156387302, 28.89636655359978, 28.930952282978865, 28.948229652260256, 28.965496715920477, 28.982753492378876, 29.017236257093817, 29.03446228191595, 29.13760456866693, 29.171904291629644, 29.206163733020468, 29.223278392404914, 29.257477676655586, 29.274562336608895, 29.29163703175362, 29.30870177950569, 29.34280150224242, 29.359836511806396, 29.376861643136763, 29.393876913398138, 29.410882339705484, 29.427877939124322, 29.478805945967352, 29.49576240750525, 29.512709126747414, 29.5296461204668, 29.563490998188964, 29.58039891549808, 29.614185789921695, 29.631064780058107, 29.647934160747187, 29.68164415931166, 29.715315916207253, 29.748949561287034, 29.765752132274432, 29.782545223670862, 29.79932885150268, 29.816103031751148, 29.832867780352597, 29.88310559496787, 29.899832775452108, 29.916550603303182, 29.93325909419153, 
29.949958263743873, 29.966648127543394, 29.9833287011299, 30.01666203960727, 30.033314835362415, 30.04995840263344, 30.066592756745816, 30.083217912982647, 30.099833886584822, 30.116440692751194, 30.166206257996713, 30.18277654557314, 30.215889859476256, 30.23243291566195, 30.24896692450835, 30.28200785945344, 30.298514815086232, 30.315012782448235, 30.331501776206203, 30.347981810987037, 30.364452901377952, 30.380915061926625, 30.430248109405877, 30.463092423455635, 30.479501308256342, 30.495901363953813, 30.54504869860253, 30.56141357987225, 30.577769702841312, 30.610455730027933, 30.62678566222711, 30.643106892089126, 30.675723300355934, 30.692018506445613, 30.708305065568176, 30.740852297878796, 30.757112998459398, 30.773365106858236, 30.805843601498726, 30.83828789021855, 30.854497241083024, 30.870698080866262, 30.903074280724887, 30.93541659651604, 30.95157508108432, 30.967725134404045, 31.016124838541646, 31.064449134018133, 31.080540535840107, 31.096623610932426, 31.12876483254676, 31.144823004794873, 31.160872901765767, 31.192947920964443, 31.20897306865447, 31.25699921617557, 31.272991542223778, 31.28897569432403, 31.336879231984796, 31.352830813181765, 31.368774282716245, 31.38470965295043, 31.400636936215164, 31.416556144810016, 31.448370387032774, 31.480152477394387, 31.496031496047245, 31.51190251317746, 31.52776554086889, 31.54362059117501, 31.575306807693888, 31.591137997862628, 31.606961258558215])

def func(inp):
    arr = np.empty(2**inp)
    
    print("Presently at " + str(inp))
    
    outputfile = open("out.txt",'a')
    data = [] 
    initial_dict = {}
    data_dict = {}

    def converter(data,size):
        sums = np.zeros(size)
        values = data_dict[data]
        for i in range (size):
            if (values[1] & 1 << i) > 0 and  (values[0] & 1 << i) == 0:
                sums[i] = 1
            elif (values[0] & 1 << i) > 0 and  (values[1] & 1 << i) == 0:
                sums[i] = -1
            elif (values[1] & 1 << i) > 0 and  (values[0] & 1 << i) == 0:
                sums[i] = 0
        outputfile.write(str(sums))


    ## Initialise heap with values -ve enough to not cause problem
    for i in range(2*inp):
        data.append(-100 + i)
        data_dict[100-i] = (0,i)


    ##Calculates Sum
    for i in range(2**inp):
        sum = 0
        for k in range(inp):
            if i & 1<<k:
                sum += nsqr[k]
        arr[i] = sum
        initial_dict[arr[i]] = i
    
    print("Made sum ")
    
    arr.sort(kind='heapsort',axis=-1)

    print("Sorted sum ")

    heapq.heapify(data)


    ##Iterates over the data to calculate difference and insert in heap
    
    for i in range(2**inp - 1):
        for j in range(1,inp + 1):
            
            # doing & and check for 0 is important so that values dont repeat
            if i+j < 2**inp and initial_dict[arr[i]] & initial_dict[arr[i+j]] == 0:

                diff = arr[i] - arr[i+j]
                if diff >heapq.nsmallest(1,data):
                    removed_element = heapq.heapreplace(data, diff)
                    
                    #Use -ve here as it makes easier to sort with dictionary
                    data_dict[-diff] = (initial_dict[arr[i]],initial_dict[arr[i+j]])
                    data_dict.pop(-removed_element,100)
                
    outputfile.write(str(inp) + ' : \n')

    l=0             
    for i in sorted(data_dict.keys()):
        if l > inp:
            break
        outputfile.write(str(i) + " ") 
        converter(i,inp)
        outputfile.write('\n')  
        l+=1               

    outputfile.write('\n')  
    outputfile.write('\n')   
    
        
    print("Done with " + str(inp))



for i in range(26):
    func(i)