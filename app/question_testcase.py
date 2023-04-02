info = {
    1: {
        "attr" :  "listSum",
        "testcase": [
            [5, [[3,2]]],
            [4, [[2,2]]],
            [0, [[0,0]]],
            [6, [[1,2,3]]],
            [12, [[4,4,4]]]
        ],
        "logic": lambda x,y: x == y
    },
    2:{
        "attr" :  "validParentheses",
        "testcase": [
            [True, ['()[]{}']],
            [False, ['(]']],
            [False, ['([)]']],
            [False, ['[[[[[[[)]]]]]]]']],
            [True, ['(())(())(())(())(())[]()[]({{{{{{{{[]}}}}}}}})']],
            [False, ['[([)]{}']]
        ],
        "logic": lambda x,y: x == y
    },
    3: {
        "attr" : "maxProfit",
        "testcase" : [
            [5, [[7,1,5,3,6,4]]],
            [0, [[7,6,4,3,1]]],
            [0, [[]]],
            [100, [[0,2,3,5,6,7,8,2,3,4,67,7,8,45,2,4,65,1,34,3,75,27,74,100,99,0]]],
            [201, [[0,2,3,5,6,7,8,2,3,4,67,7,8,45,2,4,65,1,34,3,75,27,74,100,0,201]]],
            [404, [[404,0,403,404]]],
            [1, [[9,8,7,6,5,4,3,4,1,0]]]
        ],
        "logic": lambda x,y: x == y
    },
    4: {
        "attr" : "canJump",
        "testcase" : [
            [True, [[2,3,1,1,4]]], 
            [False, [[3,2,1,0,4]]],
            [True, [[5,9,3,2,1,0,2,3,3,1,0,0]]],
            [False, [[4,0,2,2,2,1,0,1,4,2,1,0]]],
            [False, [[1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1]]],
            [True, [[8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]]]
        ],
        "logic": lambda x,y: x == y
    },
    5: {  
        "attr" : "topKFrequent",
        "testcase" : [
            [[1,2], [[1,1,1,2,2,3],2]], 
            [[1], [[1],1]], 
            [[-1,2], [[4,1,-1,2,-1,2,3],2]], 
        ],
        "logic": lambda x,y: set(x) == set(y)
    },
    6: {
        "attr" : "isPalindrome",
        "testcase" : [
            [True, [121]], 
            [False, [-121]], 
            [False, [10]], 
            [True, [1000000001]], 
            [False, [120030221]], 
            [True, [555555]], 
        ],
        "logic": lambda x,y: x == y
    },
    7: {
        "attr" : "lengthOfLastWord",
        "testcase" : [
            [5, ["Hello World"]], 
            [5, ["fly me to the mooon"]], 
            [1, [" ?  "]], 
            [1, ["fly me        m           "]], 
            [4, ["    change my       mind"]], 
            [4, ["This       is four"]], 
        ],
        "logic": lambda x,y: x == y
    },
    8: {  # "__eq__ = "in" 을 사용해야 함" - 순서 상관 x
        "attr" : "subsets",
        "testcase" : [
            [[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]], [[1,2,3]]],
            [[[],[0]], [[0]]], 
            [[[], [9], [9, 0], [9, 0, 3], [9, 0, 3, 5], [9, 0, 3, 5, 7], [9, 0, 3, 7], [9, 0, 5], [9, 0, 5, 7], [9, 0, 7], [9, 3], [9, 3, 5], [9, 3, 5, 7], [9, 3, 7], [9, 5], [9, 5, 7], [9, 7], [0], [0, 3], [0, 3, 5], [0, 3, 5, 7], [0, 3, 7], [0, 5], [0, 5, 7], [0, 7], [3], [3, 5], [3, 5, 7], [3, 7], [5], [5, 7], [7]], [[9,0,3,5,7]]], 
        ],
        "logic": lambda x,y: x == y
    },
    9: { 
        "attr" : "rob",
        "testcase" : [
            [4, [[1,2,3,1]]],
            [12, [[2,7,9,3,1]]],
            [100, [[100,1]]],
            [42, [[1,1,3,6,7,10,7,1,8,5,9,1,4,4,3]]],
            [3365, [[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]]],
            [4173, [[114,117,207,117,235,82,90,67,143,146,53,108,200,91,80,223,58,170,110,236,81,90,222,160,165,195,187,199,114,235,197,187,69,129,64,214,228,78,188,67,205,94,205,169,241,202,144,240]]],
            [7102, [[226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]]],
        ],
        "logic": lambda x,y: x == y
    },
    10: {
        "attr" : "numIslands",
        "testcase" : [
            [1, [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]]],
            [3, [[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]]],
            [2, [[["1","1","1","1","1","0","1","1","1","1"],["1","0","1","0","1","1","1","1","1","1"],["0","1","1","1","0","1","1","1","1","1"],["1","1","0","1","1","0","0","0","0","1"],["1","0","1","0","1","0","0","1","0","1"],["1","0","0","1","1","1","0","1","0","0"],["0","0","1","0","0","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","1"],["1","1","1","1","1","1","1","1","0","1"],["1","0","1","1","1","1","1","1","1","0"]]]],
            [58, [[["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]]]],
        ],
        "logic": lambda x,y: x == y
    },
    11: {
        "attr" : "isAnagram",
        "testcase" : [
            [True, ["anagram","nagaram"]],
            [False, ["rat","car"]],
            [False, ["a","n"]],
            [True, ["anagramaamm","aammnagaram"]],
            [True, ["dgqztusjuu", "dqugjzutsu"]]
        ],
        "logic": lambda x,y: x == y
    },
    12: {
        "attr" : "missingNumber",
        "testcase" : [
            [2, [[3,0,1]]],
            [2, [[0,1]]],
            [8, [[9,6,4,2,3,5,7,0,1]]],
            [10, [[0,1,2,3,4,5,6,7,8,9]]],
            [5, [[0,1,2,4,3]]],
        ],
        "logic": lambda x,y: x == y
    },
    13: {
        "attr" : "eraseOverlapIntervals",
        "testcase" : [
            [1, [[[1,2],[2,3],[3,4],[1,3]]]],
            [2, [[[1,2],[1,2],[1,2]]]],
            [7, [[[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]]],
            [0, [[[1,2],[2,3]]]],
            [9, [[[-3035,30075],[1937,6906],[11834,20971],[44578,45600],[28565,37578],[19621,34415],[32985,36313],[-8144,1080],[-15279,21851],[-27140,-14703],[-12098,16264],[-36057,-16287],[47939,48626],[-15129,-5773],[10508,46685],[-35323,-26257]]]],
            [19, [[[-25322,-4602],[-35630,-28832],[-33802,29009],[13393,24550],[-10655,16361],[-2835,10053],[-2290,17156],[1236,14847],[-45022,-1296],[-34574,-1993],[-14129,15626],[3010,14502],[42403,45946],[-22117,13380],[7337,33635],[-38153,27794],[47640,49108],[40578,46264],[-38497,-13790],[-7530,4977],[-29009,43543],[-49069,32526],[21409,43622],[-28569,16493],[-28301,34058]]]],
            [31, [[[18,42],[-12,-3],[-83,66],[4,32],[0,29],[62,72],[-97,-14],[24,87],[23,56],[67,97],[14,48],[41,48],[-59,74],[-91,50],[35,97],[77,83],[57,68],[-99,86],[-27,16],[84,94],[88,90],[91,93],[92,96],[-78,-24],[32,76],[-90,7],[-78,-38],[-67,30],[4,58],[35,36],[-47,-18],[-17,-7],[39,70],[85,86],[-28,-15],[91,97],[-84,1],[30,71],[2,93],[66,97],[94,97],[-7,74],[-3,26]]]],
        ],
        "logic": lambda x,y: x == y
    },
    14: {
        "attr" : "sortedSquares",
        "testcase" : [
            [[0,1,9,16,100], [[-4,-1,0,3,10]]],
            [[4,9,9,49,121], [[-7,-3,2,3,11]]],
            [[4,4,16,25,36,36,49,49,64,81,100,144,144,196,289,289,324,324,361,400], [[-20,-19,-14,-12,-7,-5,2,2,4,6,6,7,8,9,10,12,17,17,18,18]]],
            [[1,1,4,9,16,64,81,169,196,196,225,225,225,256,256,361,361,400,441,441,441,484,484,529,529], [[-23,-22,-21,-19,-16,-14,-3,-2,-1,1,4,8,9,13,14,15,15,15,16,19,20,21,21,22,23]]],
            [[0,0,9,16,25,36,36,36,49,64,81,121,144,169,169,196,256,256,324,484,484,529,576,625,625,676,729,784,841,841,900,961,961,1024,1024,1089,1089,1225,1225,1225,1521,1849,2025,2025,2025,2025,2025,2401,2401,2500], [[-49,-39,-35,-35,-33,-33,-32,-31,-27,-24,-22,-14,-9,-8,-7,0,0,3,4,5,6,6,6,11,12,13,13,16,16,18,22,23,25,25,26,28,29,29,30,31,32,35,43,45,45,45,45,45,49,50]]],
        ],
        "logic": lambda x,y: x == y
    },
    15: {
        "attr" : "numberOfSteps",
        "testcase" : [
            [6, [14]],
            [4, [8]],
            [12, [123]],
            [27, [83962]],
            [23, [94354]],
            [33 ,[969647]],
        ],
        "logic": lambda x,y: x == y
    },
    16: {
       "attr" : "generate",
        "testcase" : [
            [[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], [5]],
            [[[1]], [1]],
            [[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1],[1,6,15,20,15,6,1],[1,7,21,35,35,21,7,1],[1,8,28,56,70,56,28,8,1],[1,9,36,84,126,126,84,36,9,1],[1,10,45,120,210,252,210,120,45,10,1]], [11]]
        ],
        "logic": lambda x,y: x == y
    },
    17: {
        "attr" : "search",
        "testcase" : [
            [4, [[-1,0,3,5,9,12], 9]],
            [-1, [[-1,0,3,5,9,12], 2]],
            [-1, [[4,5,6,7,0,1,2], 3]],
            [994, [[-998,-997,-995,-994,-991,-986,-984,-982,-981,-980,-978,-975,-973,-972,-970,-968,-967,-966,-962,-961,-960,-959,-958,-954,-953,-952,-950,-947,-946,-945,-944,-943,-942,-941,-939,-937,-936,-934,-931,-929,-928,-925,-924,-923,-922,-921,-918,-917,-916,-914,-912,-910,-909,-908,-905,-900,-897,-896,-895,-894,-893,-892,-891,-886,-882,-881,-880,-879,-878,-876,-873,-872,-871,-870,-864,-863,-860,-859,-857,-856,-853,-852,-851,-846,-844,-843,-841,-840,-835,-831,-829,-825,-822,-820,-819,-817,-815,-814,-812,-810,-808,-807,-804,-801,-800,-798,-797,-794,-793,-792,-790,-787,-786,-785,-782,-781,-778,-777,-776,-773,-772,-770,-767,-766,-763,-762,-759,-757,-751,-750,-748,-744,-743,-741,-740,-738,-737,-736,-733,-729,-727,-726,-725,-724,-723,-720,-718,-716,-715,-714,-710,-709,-703,-702,-701,-699,-698,-695,-694,-693,-690,-688,-686,-685,-682,-681,-680,-678,-674,-673,-672,-670,-668,-667,-666,-661,-657,-656,-655,-653,-651,-650,-646,-645,-644,-643,-642,-636,-635,-634,-633,-632,-631,-630,-629,-627,-626,-625,-624,-623,-622,-621,-618,-617,-616,-615,-614,-608,-606,-605,-603,-602,-597,-596,-595,-594,-590,-589,-581,-576,-574,-572,-568,-566,-565,-562,-557,-555,-554,-552,-551,-549,-547,-545,-544,-543,-537,-536,-533,-532,-530,-529,-526,-524,-517,-516,-515,-514,-513,-511,-509,-508,-502,-500,-498,-497,-493,-492,-491,-490,-487,-486,-485,-483,-479,-477,-476,-474,-472,-471,-469,-468,-465,-464,-463,-458,-457,-455,-453,-449,-444,-443,-442,-437,-433,-430,-429,-427,-426,-421,-419,-416,-415,-414,-413,-411,-409,-408,-406,-405,-404,-403,-402,-400,-398,-397,-393,-392,-389,-388,-387,-379,-376,-372,-370,-369,-367,-366,-364,-363,-361,-360,-359,-358,-357,-356,-351,-349,-348,-343,-339,-338,-334,-332,-330,-326,-323,-322,-321,-318,-315,-314,-313,-305,-304,-303,-302,-296,-295,-294,-293,-292,-291,-290,-289,-287,-286,-284,-282,-281,-279,-276,-274,-273,-272,-270,-268,-267,-266,-265,-264,-263,-261,-258,-257,-256,-255,-253,-252,-249,-245,-244,-241,-240,-239,-238,-237,-236,-235,-234,-233,-231,-230,-228,-224,-222,-221,-220,-219,-218,-217,-215,-212,-210,-209,-206,-204,-202,-201,-200,-199,-190,-184,-181,-178,-175,-174,-173,-171,-164,-163,-162,-159,-158,-157,-156,-150,-147,-145,-144,-141,-140,-138,-137,-136,-133,-131,-130,-128,-127,-125,-124,-122,-119,-118,-117,-116,-114,-113,-112,-111,-110,-107,-106,-103,-102,-99,-98,-94,-91,-88,-86,-85,-84,-80,-79,-78,-77,-76,-71,-70,-69,-67,-63,-62,-61,-59,-58,-57,-56,-53,-49,-48,-44,-43,-40,-35,-34,-32,-31,-30,-25,-21,-19,-17,-15,-11,-10,-9,-8,-5,-2,8,9,10,12,13,15,19,22,23,25,27,28,29,30,34,35,38,42,43,44,45,49,52,53,54,55,56,58,59,61,62,63,68,73,74,76,77,78,84,85,86,87,88,90,91,92,94,95,97,101,104,105,106,113,114,116,118,119,122,124,125,127,129,132,138,140,143,145,146,147,151,153,158,159,160,161,162,163,164,167,168,169,172,176,179,182,184,185,186,188,189,192,193,196,197,198,201,202,204,207,210,219,220,221,222,225,232,234,235,236,237,240,241,243,244,245,246,247,248,250,254,256,257,258,259,260,261,262,263,265,268,270,274,275,276,277,278,282,286,287,292,293,295,296,298,302,303,304,305,306,307,308,312,314,315,316,317,319,320,324,325,326,328,330,331,332,333,334,335,337,338,339,341,342,343,344,345,350,351,353,355,357,360,362,365,367,369,370,371,373,375,376,378,379,380,383,384,385,389,390,391,397,399,400,401,405,407,410,412,414,416,418,420,421,422,427,428,431,433,435,436,438,439,444,445,446,448,449,452,453,455,456,459,461,462,463,464,465,466,469,473,474,476,477,478,479,481,484,486,490,491,494,497,498,500,501,502,503,512,513,519,520,522,523,525,526,528,529,530,532,536,539,540,542,544,546,550,554,559,562,568,569,570,572,573,574,575,576,579,583,587,590,592,593,595,596,598,601,604,606,607,608,613,614,615,618,619,622,624,626,628,632,633,634,635,639,641,642,644,648,649,656,657,659,660,661,664,665,666,667,670,673,674,676,678,682,685,689,692,697,698,700,701,702,704,707,711,714,716,717,718,722,723,725,726,728,729,732,733,734,735,739,745,747,754,755,756,757,758,759,760,761,762,763,764,766,767,769,774,775,778,780,782,783,786,787,790,791,792,793,795,796,797,798,799,800,804,806,807,808,809,813,814,817,819,822,823,824,826,830,831,832,833,836,838,840,841,844,845,846,849,852,854,859,860,862,864,865,866,868,870,871,872,873,876,877,884,890,891,892,894,896,898,899,900,901,903,910,911,912,916,917,919,920,924,925,926,930,934,935,939,940,941,942,943,945,947,948,952,953,954,955,956,957,958,960,961,965,967,969,970,971,972,975,977,978,979,980,981,982,986,987,988,990,992,994,995,997],988]],
            [812, [[-997,-996,-992,-990,-988,-985,-983,-980,-979,-977,-975,-974,-973,-972,-971,-967,-965,-964,-959,-956,-954,-951,-950,-949,-947,-946,-945,-943,-942,-938,-936,-935,-933,-932,-930,-929,-927,-925,-924,-923,-921,-919,-917,-916,-913,-912,-911,-910,-909,-908,-903,-900,-899,-898,-891,-890,-886,-884,-883,-880,-874,-872,-871,-870,-869,-868,-867,-866,-865,-860,-859,-858,-854,-852,-851,-848,-845,-844,-843,-842,-840,-839,-837,-836,-835,-833,-832,-831,-829,-828,-826,-822,-820,-819,-818,-817,-816,-815,-814,-812,-811,-808,-807,-806,-805,-803,-801,-798,-796,-795,-793,-792,-791,-790,-789,-788,-787,-785,-782,-779,-778,-773,-771,-769,-768,-767,-765,-764,-763,-759,-756,-755,-754,-753,-751,-750,-747,-746,-744,-743,-741,-740,-730,-729,-728,-727,-726,-725,-724,-723,-722,-717,-715,-714,-711,-710,-709,-708,-700,-697,-688,-687,-685,-683,-681,-678,-677,-676,-673,-670,-669,-668,-666,-661,-659,-658,-655,-654,-652,-647,-643,-641,-635,-633,-632,-630,-629,-627,-626,-620,-616,-612,-611,-610,-608,-604,-602,-601,-597,-596,-592,-585,-584,-583,-578,-577,-574,-567,-565,-557,-554,-553,-550,-549,-548,-547,-545,-543,-542,-541,-540,-538,-535,-532,-531,-530,-528,-526,-524,-522,-521,-520,-519,-518,-517,-516,-508,-507,-506,-504,-502,-499,-497,-496,-495,-492,-485,-484,-483,-482,-478,-477,-474,-473,-472,-471,-465,-464,-462,-461,-457,-453,-452,-450,-448,-447,-446,-445,-444,-442,-441,-440,-439,-438,-437,-436,-435,-434,-432,-430,-429,-427,-425,-424,-421,-419,-417,-412,-411,-409,-405,-404,-403,-398,-397,-395,-390,-388,-387,-385,-384,-383,-378,-377,-376,-374,-370,-365,-364,-362,-361,-356,-352,-351,-350,-346,-343,-342,-340,-339,-338,-336,-334,-332,-329,-327,-326,-325,-324,-322,-320,-318,-316,-315,-314,-310,-309,-305,-304,-303,-301,-300,-298,-297,-291,-290,-288,-286,-284,-282,-278,-277,-276,-271,-269,-267,-266,-265,-264,-263,-259,-258,-256,-255,-253,-252,-251,-250,-249,-245,-244,-240,-239,-236,-234,-232,-227,-226,-222,-219,-217,-216,-213,-212,-211,-210,-209,-208,-207,-205,-203,-202,-197,-196,-194,-193,-192,-190,-189,-188,-187,-186,-185,-183,-182,-181,-180,-179,-178,-176,-175,-174,-172,-170,-168,-167,-166,-163,-162,-161,-157,-156,-155,-148,-147,-145,-144,-143,-139,-137,-135,-133,-131,-128,-121,-120,-119,-117,-114,-112,-111,-109,-107,-106,-104,-102,-97,-95,-94,-93,-91,-88,-87,-85,-82,-80,-79,-78,-77,-76,-75,-74,-73,-66,-63,-59,-58,-57,-53,-52,-51,-50,-49,-47,-46,-45,-42,-40,-38,-36,-35,-34,-33,-32,-28,-27,-26,-25,-24,-21,-14,-9,-3,-1,0,2,3,7,9,11,13,17,19,20,21,22,23,26,28,31,33,36,37,38,39,41,42,47,48,51,53,54,56,57,58,60,63,65,67,72,73,74,76,78,80,82,85,86,91,92,93,94,99,101,102,103,104,105,107,112,114,115,119,120,122,123,125,126,127,128,130,133,137,139,140,141,142,145,146,148,151,156,157,158,161,163,164,167,172,174,176,177,179,189,191,199,201,202,203,206,210,211,213,214,217,218,220,221,222,223,226,236,237,240,241,244,245,250,251,252,253,254,255,257,258,261,262,265,266,271,272,273,275,276,278,279,281,284,289,291,294,295,296,298,299,300,302,303,306,307,308,309,310,311,313,314,315,316,319,320,328,333,334,339,341,343,344,345,347,349,352,353,356,360,361,362,364,366,367,369,371,373,376,377,378,379,381,383,386,387,388,390,392,393,394,396,397,398,399,400,401,403,406,413,415,416,419,421,426,428,432,435,436,438,439,440,441,444,445,448,450,455,456,457,459,460,463,466,467,471,473,474,475,476,477,478,479,480,484,485,486,487,489,490,492,497,498,500,501,502,504,505,507,508,509,510,511,513,514,515,516,520,521,528,535,538,542,545,546,547,548,553,556,557,558,559,561,562,563,565,566,567,570,572,573,575,576,577,578,579,580,581,583,585,586,591,592,594,595,598,599,601,607,608,610,613,614,617,621,625,628,631,632,633,635,637,639,640,644,648,650,652,656,660,661,662,664,665,666,667,669,670,671,672,676,677,680,681,682,683,684,686,688,689,690,691,692,693,694,695,696,698,700,701,706,707,709,712,713,718,719,724,725,727,728,731,733,734,740,741,742,744,746,749,750,751,753,754,755,756,758,761,763,764,766,771,772,773,774,776,777,778,779,780,781,785,786,787,792,793,796,798,800,801,802,804,808,810,812,813,814,815,817,821,823,825,826,828,829,830,833,834,843,844,845,850,854,856,857,859,860,862,863,864,865,866,867,868,869,872,873,874,876,877,880,881,883,884,886,887,888,889,891,892,893,894,896,897,898,901,905,906,907,908,910,911,912,913,914,917,920,921,923,924,925,926,927,929,931,932,936,939,940,943,944,947,952,954,956,959,960,963,965,969,970,972,973,974,975,981,985,986,987,988,989,991,995,996,997,998], 656]],
        ],
        "logic": lambda x,y: x == y
    }
}