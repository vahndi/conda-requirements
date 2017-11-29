from os import listdir
from os.path import isdir, join
import subprocess

envs_dir = r'C:\Users\Vahndi\.conda\envs'
files_dir = r'C:\Users\Vahndi\Desktop\gitcode\conda-requirements'


def export_envs():

    env_names = [d for d in listdir(envs_dir) 
                 if isdir(join(envs_dir, d))
                 and not d.startswith('.')]
    for env_name in env_names:
        env_file_name = join(files_dir, env_name + '_win.yml')
        f = open(env_file_name, 'w')
        command = ['conda', 'env', 'export', '-n', env_name]
        subprocess.run(command, stdout=f)
        f.close()


if __name__ == '__main__':

    export_envs()
