import xml.etree.ElementTree as et
from xml.dom import minidom
from os import listdir
from os.path import isfile, join


def add_mesh(p_asset, p_name, p_filename):
    d = {'name': p_name,
         'file': p_filename,
         'scale': '0.001 0.001 0.001'}
    et.SubElement(p_asset, 'mesh', d)


def add_geom(p_body, p_name, p_mesh):
    d = {'name': p_name,
         'type': 'mesh',
         'mesh': p_mesh,
         'rgba': '1 1 1 1'}
    et.SubElement(p_body, 'geom', d)
    
def create_particles(p_worldbody):
    n = 200
    for i in range(n):
        body_attr = {'name': 'ball' + str(i),
                     'pos': '0.59 0.075 ' + str(0.8 + i * 0.01)}
        body = et.SubElement(p_worldbody, 'body', body_attr)
        et.SubElement(body, 'freejoint')
        geom_attr = {'type': 'sphere',
                     'size': '0.005',
                     'rgba': '1 0 0 1'}
        et.SubElement(body, 'geom', geom_attr)



DIR_PATH = 'cup_decomposed'
OUT_NAME = 'particles.xml'

root = et.Element('mujoco')
asset = et.SubElement(root, 'asset')
worldbody = et.SubElement(root, 'worldbody')
# body = et.SubElement(worldbody, 'body')


# onlyfiles = [f for f in listdir(DIR_PATH) if isfile(join(DIR_PATH, f))]
# onlyfiles.sort()

# for name in onlyfiles:
#     mesh_name = name.partition('.')[0]
#     add_mesh(asset, mesh_name, DIR_PATH + '/' + name)
#     add_geom(body, mesh_name + '_geom', mesh_name)

create_particles(worldbody)

xmlstr = minidom.parseString(et.tostring(root)).toprettyxml(indent='\t')
with open(OUT_NAME, "w") as f:
    f.write(xmlstr)

