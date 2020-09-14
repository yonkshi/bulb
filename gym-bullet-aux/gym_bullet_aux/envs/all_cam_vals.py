"""
The following camera values were obtained with getDebugVisualizerCamera()
with the above yaw,pitch,cam dist and tgt pos values and GUI on.
and GUI on. We cache them here, because we can't make this call when
we are using headless DIRECT backend.
"""
ALL_CAM_VALS = {

'CartPole' : [

# CAM_VALS for yaw -30 pitch -70
#[ (0.8660253882408142, 0.46984636783599854, -0.1710100620985031, 0.0, -0.5000000596046448, 0.813797652721405, -0.2961980700492859, 0.0, 0.0, 0.34202009439468384, 0.9396926164627075, 0.0, -0.0, -0.0, -1.9999998807907104, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (0.1710100620985031, 0.2961980700492859, -0.9396926164627075) , (23094.009765625, -13333.3349609375, 0.0) , (9396.927734375, 16275.953125, 6840.40185546875) , 2.0 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 10 pitch -10
[ (0.9848077893257141, -0.030153676867485046, 0.17101003229618073, 0.0, 0.1736481487751007, 0.17101003229618073, -0.969846248626709, 0.0, -0.0, 0.9848077297210693, 0.17364813387393951, 0.0, -2.9802322387695312e-08, -0.0, -1.9999998807907104, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.17101003229618073, 0.969846248626709, -0.17364813387393951) , (26261.541015625, 4630.61767578125, -0.0) , (-603.0736083984375, 3420.200927734375, 19696.154296875) , 2.0 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 50 pitch -65
#[ (0.642787754535675, -0.6942718029022217, 0.3237442672252655, 0.0, 0.7660441994667053, 0.5825635194778442, -0.27165383100509644, 0.0, -0.0, 0.42261818051338196, 0.9063077569007874, 0.0, -0.0, -0.0, -1.999999761581421, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.3237442672252655, 0.27165383100509644, -0.9063077569007874) , (17141.0078125, 20427.84765625, -0.0) , (-13885.4384765625, 11651.271484375, 8452.3642578125) , 2.0 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 90 pitch -40
[ (0.0, -0.642787516117096, 0.7660443782806396, 0.0, 0.9999999403953552, 0.0, -0.0, 0.0, -0.0, 0.7660443186759949, 0.6427875757217407, 0.0, -0.0, -0.0, -2.0, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.7660443782806396, 0.0, -0.6427875757217407) , (0.0, 26666.66796875, -0.0) , (-12855.7529296875, 0.0, 15320.888671875) , 2.0 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 130 pitch -10
#[ (-0.6427876949310303, -0.13302220404148102, 0.7544064521789551, 0.0, 0.7660444378852844, -0.11161889135837555, 0.6330222487449646, 0.0, 0.0, 0.9848077893257141, 0.1736481487751007, 0.0, -0.0, -0.0, -2.0, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.7544064521789551, -0.6330222487449646, -0.1736481487751007) , (-17141.00390625, 20427.8515625, 0.0) , (-2660.44384765625, -2232.377685546875, 19696.154296875) , 2.0 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 170 pitch -25
[ (-0.9848077893257141, -0.07338694483041763, 0.15737879276275635, 0.0, 0.17364828288555145, -0.416197806596756, 0.8925389051437378, 0.0, 0.0, 0.9063078165054321, 0.4226182997226715, 0.0, 2.9802322387695312e-08, 5.960464477539063e-08, -1.9999998807907104, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.15737879276275635, -0.8925389051437378, -0.4226182997226715) , (-26261.541015625, 4630.62109375, 0.0) , (-1467.7388916015625, -8323.955078125, 18126.15625) , 2.0 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 210 pitch -60
#[ (-0.8660253286361694, 0.4330127537250519, -0.25, 0.0, -0.5000000596046448, -0.7499999403953552, 0.43301260471343994, 0.0, 0.0, 0.49999988079071045, 0.8660253882408142, 0.0, -0.0, -0.0, -1.999999761581421, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (0.25, -0.43301260471343994, -0.8660253882408142) , (-23094.009765625, -13333.3359375, 0.0) , (8660.255859375, -15000.0, 9999.9990234375) , 2.0 , (0.0, 0.0, 0.0) ],

],

'BlockOnIncline' : [

# CAM_VALS for yaw -30 pitch -70
#[ (0.8660253882408142, 0.46984630823135376, -0.17101004719734192, 0.0, -0.5, 0.813797652721405, -0.2961980700492859, 0.0, 0.0, 0.34202009439468384, 0.9396926164627075, 0.0, -0.3330127000808716, -0.4318847060203552, -0.7492246627807617, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (0.17101004719734192, 0.2961980700492859, -0.9396926164627075) , (23094.01171875, -13333.333984375, 0.0) , (9396.9267578125, 16275.9541015625, 6840.4013671875) , 0.800000011920929 , (0.5, 0.20000000298023224, 0.10000000149011612) ],
# CAM_VALS for yaw 10 pitch -10
[ (0.9848077893257141, -0.030153676867485046, 0.17101003229618073, 0.0, 0.1736481487751007, 0.17101003229618073, -0.969846248626709, 0.0, -0.0, 0.9848077297210693, 0.17364813387393951, 0.0, -0.5271335244178772, -0.11760593950748444, -0.708900511264801, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.17101003229618073, 0.969846248626709, -0.17364813387393951) , (26261.541015625, 4630.6171875, -0.0) , (-603.0735473632812, 3420.20068359375, 19696.154296875) , 0.800000011920929 , (0.5, 0.20000000298023224, 0.10000000149011612) ],
# CAM_VALS for yaw 50 pitch -65
#[ (0.642787754535675, -0.6942718029022217, 0.3237442672252655, 0.0, 0.7660441994667053, 0.5825635194778442, -0.27165383100509644, 0.0, -0.0, 0.42261818051338196, 0.9063077569007874, 0.0, -0.47460272908210754, 0.18836134672164917, -0.9981721043586731, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.3237442672252655, 0.27165383100509644, -0.9063077569007874) , (17141.0078125, 20427.84765625, -0.0) , (-13885.4384765625, 11651.2724609375, 8452.3642578125) , 0.800000011920929 , (0.5, 0.20000000298023224, 0.10000000149011612) ],
# CAM_VALS for yaw 90 pitch -40
[ (0.0, -0.6427875757217407, 0.7660444974899292, 0.0, 1.0, 0.0, -0.0, 0.0, -0.0, 0.7660444974899292, 0.6427875757217407, 0.0, -0.20000000298023224, 0.24478933215141296, -1.2473011016845703, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.7660444974899292, 0.0, -0.6427875757217407) , (0.0, 26666.66796875, -0.0) , (-12855.751953125, 0.0, 15320.888671875) , 0.800000011920929 , (0.5, 0.20000000298023224, 0.10000000149011612) ],
# CAM_VALS for yaw 130 pitch -10
#[ (-0.6427876949310303, -0.13302220404148102, 0.7544063925743103, 0.0, 0.7660443782806396, -0.11161890625953674, 0.6330222487449646, 0.0, 0.0, 0.9848076701164246, 0.1736481636762619, 0.0, 0.16818499565124512, -0.009645864367485046, -1.3211724758148193, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.7544063925743103, -0.6330222487449646, -0.1736481636762619) , (-17141.005859375, 20427.849609375, 0.0) , (-2660.444091796875, -2232.378173828125, 19696.154296875) , 0.800000011920929 , (0.5, 0.20000000298023224, 0.10000000149011612) ],
# CAM_VALS for yaw 170 pitch -25
[ (-0.9848077297210693, -0.07338691502809525, 0.15737874805927277, 0.0, 0.17364823818206787, -0.4161977469921112, 0.892538845539093, 0.0, 0.0, 0.9063076972961426, 0.4226182699203491, 0.0, 0.45767420530319214, 0.029302239418029785, -1.099458932876587, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.15737874805927277, -0.892538845539093, -0.4226182699203491) , (-26261.541015625, 4630.6201171875, 0.0) , (-1467.738525390625, -8323.955078125, 18126.15625) , 0.800000011920929 , (0.5, 0.20000000298023224, 0.10000000149011612) ],
# CAM_VALS for yaw 210 pitch -60
#[ (-0.8660253286361694, 0.4330127537250519, -0.2499999850988388, 0.0, -0.5000000596046448, -0.7499999403953552, 0.43301260471343994, 0.0, 0.0, 0.49999988079071045, 0.8660253882408142, 0.0, 0.5330126881599426, -0.11650636792182922, -0.8482049703598022, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (0.2499999850988388, -0.43301260471343994, -0.8660253882408142) , (-23094.009765625, -13333.3359375, 0.0) , (8660.255859375, -15000.0, 9999.998046875) , 0.800000011920929 , (0.5, 0.20000000298023224, 0.10000000149011612) ],

],

'Rearrange' : [

# CAM_VALS for yaw -30 pitch -70
#[ (0.8660253882408142, 0.46984636783599854, -0.1710100620985031, 0.0, -0.5000000596046448, 0.813797652721405, -0.2961980700492859, 0.0, 0.0, 0.34202009439468384, 0.9396926164627075, 0.0, -0.0, -0.0, -0.4000000059604645, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (0.1710100620985031, 0.2961980700492859, -0.9396926164627075) , (23094.009765625, -13333.3349609375, 0.0) , (9396.927734375, 16275.953125, 6840.40185546875) , 0.4000000059604645 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 10 pitch -10
[ (0.9848077893257141, -0.030153676867485046, 0.17101003229618073, 0.0, 0.1736481487751007, 0.17101003229618073, -0.969846248626709, 0.0, -0.0, 0.9848077297210693, 0.17364813387393951, 0.0, -7.450580596923828e-09, -7.450580596923828e-09, -0.3999999761581421, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.17101003229618073, 0.969846248626709, -0.17364813387393951) , (26261.541015625, 4630.61767578125, -0.0) , (-603.0736083984375, 3420.200927734375, 19696.154296875) , 0.4000000059604645 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 50 pitch -65
#[ (0.642787754535675, -0.6942718029022217, 0.3237442672252655, 0.0, 0.7660441994667053, 0.5825635194778442, -0.27165383100509644, 0.0, -0.0, 0.42261818051338196, 0.9063077569007874, 0.0, -7.450580596923828e-09, -0.0, -0.3999999463558197, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.3237442672252655, 0.27165383100509644, -0.9063077569007874) , (17141.0078125, 20427.84765625, -0.0) , (-13885.4384765625, 11651.271484375, 8452.3642578125) , 0.4000000059604645 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 90 pitch -40
[ (0.0, -0.642787516117096, 0.7660444378852844, 0.0, 0.9999999403953552, 0.0, -0.0, 0.0, -0.0, 0.7660443782806396, 0.6427875757217407, 0.0, -0.0, -1.4901161193847656e-08, -0.40000003576278687, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.7660444378852844, 0.0, -0.6427875757217407) , (0.0, 26666.66796875, -0.0) , (-12855.7529296875, 0.0, 15320.888671875) , 0.4000000059604645 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 130 pitch -10
#[ (-0.6427876949310303, -0.13302220404148102, 0.7544064521789551, 0.0, 0.7660444378852844, -0.11161889135837555, 0.6330222487449646, 0.0, 0.0, 0.9848077893257141, 0.1736481487751007, 0.0, -0.0, -0.0, -0.40000003576278687, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.7544064521789551, -0.6330222487449646, -0.1736481487751007) , (-17141.005859375, 20427.8515625, 0.0) , (-2660.44384765625, -2232.3779296875, 19696.154296875) , 0.4000000059604645 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 170 pitch -25
[ (-0.9848077297210693, -0.07338692992925644, 0.15737877786159515, 0.0, 0.17364826798439026, -0.4161977469921112, 0.892538845539093, 0.0, 0.0, 0.9063076972961426, 0.4226182699203491, 0.0, 7.450580596923828e-09, -0.0, -0.4000000059604645, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (-0.15737877786159515, -0.892538845539093, -0.4226182699203491) , (-26261.541015625, 4630.62109375, 0.0) , (-1467.7388916015625, -8323.955078125, 18126.15625) , 0.4000000059604645 , (0.0, 0.0, 0.0) ],
# CAM_VALS for yaw 210 pitch -60
#[ (-0.8660253286361694, 0.4330127537250519, -0.25, 0.0, -0.5000000596046448, -0.7499999403953552, 0.43301260471343994, 0.0, 0.0, 0.49999988079071045, 0.8660253882408142, 0.0, -0.0, 1.4901161193847656e-08, -0.3999999463558197, 1.0) , (0.7499999403953552, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, -1.0000200271606445, -1.0, 0.0, 0.0, -0.02000020071864128, 0.0) , (0.25, -0.43301260471343994, -0.8660253882408142) , (-23094.009765625, -13333.3359375, 0.0) , (8660.255859375, -15000.0, 9999.9990234375) , 0.4000000059604645 , (0.0, 0.0, 0.0) ],
]


}
