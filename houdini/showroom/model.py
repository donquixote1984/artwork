import hou


def render1(): 
	hou.hipFile.load('./static/pigen/pigen.hipnc')
	rnode = hou.node('/out/mantra1')
	print("start render")
	rnode.render()

def render2():
	hou.hipFile.load('./static/pigen2/pigen2.hipnc')
	param = hou.node("/obj/geo1/param");
	param.parm("seed").set(500)
	rnode = hou.node("/out/mantra1")
	print("start render")
	rnode.render()
