import hou
hou.hipFile.load('./pigen.hipnc')
rnode = hou.node("/out/mantra1")
rnode.render()