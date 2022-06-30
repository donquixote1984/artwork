import hou
hou.hipFile.load('./pigen2.hipnc')
param = hou.node("/obj/geo1/param");
param.parm("seed").set(500)
rnode = hou.node("/out/mantra1")
rnode.render()