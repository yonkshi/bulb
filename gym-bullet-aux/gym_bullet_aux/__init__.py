import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

# Register standard gym envs and add Aux prefix.
# Note: not using 'Pusher', 'Striker', 'Thrower': they seem broken
gym_envs = ['CartPole', 'InvertedPendulum', 'InvertedDoublePendulum',
            'InvertedPendulumSwingup',
            'Hopper', 'Walker2D', 'HalfCheetah', 'Ant', 'Humanoid',
            'HumanoidFlagrun', 'HumanoidFlagrunHarder',
            'Reacher', 'Kuka']
v1_envs = ['CartPole']
resolution = 64
for base_env_name in gym_envs:
    for debug_level in [0, 1, 2]:
        sfx = '' if debug_level<=0 else 'Debug' if debug_level<=1 else 'Viz'
        for env_v in [0,1]:
            if env_v==0 and base_env_name=='CartPole': continue  # v1 only
            if env_v==1 and base_env_name not in v1_envs: continue
            env_id = 'Aux'+base_env_name+'BulletEnv'+sfx+'-v'+str(env_v)
            kwargs={'base_env_name':base_env_name, 'env_v':env_v,
                    'obs_resolution':resolution, 'random_colors':False,
                    'visualize':(debug_level>=2), 'debug_level':debug_level}
            register(id=env_id, entry_point='gym_bullet_aux.envs:AuxBulletEnv',
                     kwargs=kwargs)
            if base_env_name.startswith(('CartPole', 'Inverted', 'Walker2D',
                                         'HalfCheetah', 'Ant')):
                env_id = 'Aux'+base_env_name+'ClrBulletEnv'+sfx+'-v'+str(env_v)
                kwargs={'base_env_name':base_env_name, 'env_v':env_v,
                        'obs_resolution':resolution, 'random_colors':True,
                        'visualize':(debug_level>=2), 'debug_level':debug_level}
                register(id=env_id, entry_point='gym_bullet_aux.envs:AuxBulletEnv',
                         kwargs=kwargs)


# Register rearrangement envs.
num_versions = 6*2  # 6 versions and their black-background variants
for robot in ['Reacher', 'Franka']:
    max_episode_len = 50  # don't use max_episode_steps to avoid TimeLimit wrap
    for variant in ['Ycb', 'OneYcb', 'Geom', 'OneGeom']:
        for rnd_init_pos in [False, True]:
            for resolution in [None, 64, 128]:
                for version in range(num_versions):
                    for debug_level in [0, 1, 2]:
                        suffix = '' if rnd_init_pos else 'Nornd'
                        suffix += 'LD' if resolution is None else str(resolution)
                        suffix += '' if debug_level<=0 else 'Debug' if debug_level<=1 else 'Viz'
                        register(
                            id=robot+'Rearrange'+variant+suffix+'-v'+str(version),
                            entry_point='gym_bullet_aux.envs:'+robot+'RearrangeEnv',
                            reward_threshold=1.0,
                            nondeterministic=True,
                            kwargs={'version':version,
                                    'max_episode_len':max_episode_len,
                                    'obs_resolution':resolution,
                                    'variant':variant,
                                    'rnd_init_pos':rnd_init_pos,
                                    'statics_in_lowdim':False,
                                    'visualize':(debug_level>=2),
                                    'debug_level':debug_level},
                        )

# Register BlockOnIncline
scale_dict = {'': 2.5, 'Md': 1.5, 'Sm': 1.0}
for variant in ['Ycb', 'Geom', 'YcbFric', 'GeomFric',
                'YcbLD', 'GeomLD', 'YcbFricLD', 'GeomFricLD',
                'YcbNorndLD', 'GeomNorndLD']:
    obs_resolution=64; randomize=True; report_fric=False; variant_arg=variant
    if variant_arg.endswith('LD'):
        obs_resolution = None; variant_arg = variant[:-2]
    if variant_arg.endswith('Fric'):
        report_fric = True; variant_arg = variant_arg[:-4]
    if variant_arg.endswith('Nornd'):
        randomize = False; variant_arg = variant_arg[:-5]
    for version in range(6):
        for scale_str, scale in scale_dict.items():
            for debug_level in [0, 1, 2]:
                suffix = scale_str
                suffix += '' if debug_level<=0 else 'Debug' if debug_level<=1 else 'Viz'
                rid = 'BlockOnIncline'+variant+suffix+'-v'+str(version)
                register(id=rid, entry_point='gym_bullet_aux.envs:BlockOnInclineEnv',
                         nondeterministic=True,
                         kwargs={'version': version, 'variant': variant_arg,
                                 'scale': scale, 'randomize': randomize,
                                 'report_fric': report_fric,
                                 'obs_resolution': obs_resolution,
                                 'visualize':(debug_level>=2),
                                 'debug_level':debug_level})
            #print('register', rid)