# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named SSAOExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from SSAOExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.SSAO"

def getLabel():
    return "SSAO"

def getVersion():
    return 2

def getIconPath():
    return "SSAO.png"

def getGrouping():
    return "Draw/Relight"

def getPluginDescription():
    return "Generate a Screen Space Ambiant Occlusion pass from a Z pass. \nMay need a bit of time tweaking the parameters to get good results as it changes a lot depending on the original Z values.\nTo use it : \nSet Near and Far plane (minimum and maximum Z Value) to map the Z pass roughly bettween 0 and 1 value.\nSet Radius and Falloff to get good shadows\nSet the sample value (may need up to 1000 iterations for a very smooth result)\nas you increase the samples, you\'ll need to lower the sample noise value to something like 0.05\nFinally you can blur the AO a little bit to get rid of the final noise/artifacts... \nIf you have high samples and high noise sample value, the result is still noisy. \nIf you have low samples and low noise Value , the result as artifacts. \nCredits : \nThe original code by Daniel Holden is taken from here : http://theorangeduck.com/page/pure-depth-ssao \nthe sampling sphere fonction by John Chapman is taken from here : http://john-chapman-graphics.blogspot.fr/2013/01/ssao-tutorial.html "

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("laba", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("Modify Z values :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.laba = param
    del param

    param = lastNode.createChoiceParam("Shuffle1outputR", "Z Channel")
    entries = [ ("A.r", "Red channel from input A"),
    ("A.g", "Green channel from input A"),
    ("A.b", "Blue channel from input A"),
    ("A.a", "Alpha channel from input A"),
    ("0", "0 constant channel"),
    ("1", "1 constant channel"),
    ("B.r", "Red channel from input B"),
    ("B.g", "Green channel from input B"),
    ("B.b", "Blue channel from input B"),
    ("B.a", "Alpha channel from input B"),
    ("B.Backward.Motion.U", "U channel from layer/view Backward.Motion of input A"),
    ("B.Backward.Motion.V", "V channel from layer/view Backward.Motion of input A"),
    ("A.Composite.Combined.R", "R channel from layer/view Composite.Combined of input A"),
    ("A.Composite.Combined.G", "G channel from layer/view Composite.Combined of input A"),
    ("A.Composite.Combined.B", "B channel from layer/view Composite.Combined of input A"),
    ("A.Composite.Combined.A", "A channel from layer/view Composite.Combined of input A"),
    ("B.DisparityLeft.Disparity.X", "X channel from layer/view DisparityLeft.Disparity of input A"),
    ("B.DisparityLeft.Disparity.Y", "Y channel from layer/view DisparityLeft.Disparity of input A"),
    ("B.DisparityRight.Disparity.X", "X channel from layer/view DisparityRight.Disparity of input A"),
    ("B.DisparityRight.Disparity.Y", "Y channel from layer/view DisparityRight.Disparity of input A"),
    ("B.Forward.Motion.U", "U channel from layer/view Forward.Motion of input A"),
    ("B.Forward.Motion.V", "V channel from layer/view Forward.Motion of input A"),
    ("A.RenderLayer.Combined.R", "R channel from layer/view RenderLayer.Combined of input A"),
    ("A.RenderLayer.Combined.G", "G channel from layer/view RenderLayer.Combined of input A"),
    ("A.RenderLayer.Combined.B", "B channel from layer/view RenderLayer.Combined of input A"),
    ("A.RenderLayer.Combined.A", "A channel from layer/view RenderLayer.Combined of input A"),
    ("A.RenderLayer.Depth.Z", "Z channel from layer/view RenderLayer.Depth of input A"),
    ("A.RenderLayer.Normal.Z", "Z channel from layer/view RenderLayer.Normal of input A"),
    ("A.RenderLayer.Normal.X", "X channel from layer/view RenderLayer.Normal of input A"),
    ("A.RenderLayer.Normal.Y", "Y channel from layer/view RenderLayer.Normal of input A"),
    ("B.Backward.Motion.U", "U channel from layer/view Backward.Motion of input B"),
    ("B.Backward.Motion.V", "V channel from layer/view Backward.Motion of input B"),
    ("B.Composite.Combined.R", "R channel from layer/view Composite.Combined of input B"),
    ("B.Composite.Combined.G", "G channel from layer/view Composite.Combined of input B"),
    ("B.Composite.Combined.B", "B channel from layer/view Composite.Combined of input B"),
    ("B.Composite.Combined.A", "A channel from layer/view Composite.Combined of input B"),
    ("B.DisparityLeft.Disparity.X", "X channel from layer/view DisparityLeft.Disparity of input B"),
    ("B.DisparityLeft.Disparity.Y", "Y channel from layer/view DisparityLeft.Disparity of input B"),
    ("B.DisparityRight.Disparity.X", "X channel from layer/view DisparityRight.Disparity of input B"),
    ("B.DisparityRight.Disparity.Y", "Y channel from layer/view DisparityRight.Disparity of input B"),
    ("B.Forward.Motion.U", "U channel from layer/view Forward.Motion of input B"),
    ("B.Forward.Motion.V", "V channel from layer/view Forward.Motion of input B"),
    ("B.RenderLayer.Combined.R", "R channel from layer/view RenderLayer.Combined of input B"),
    ("B.RenderLayer.Combined.G", "G channel from layer/view RenderLayer.Combined of input B"),
    ("B.RenderLayer.Combined.B", "B channel from layer/view RenderLayer.Combined of input B"),
    ("B.RenderLayer.Combined.A", "A channel from layer/view RenderLayer.Combined of input B"),
    ("B.RenderLayer.Depth.Z", "Z channel from layer/view RenderLayer.Depth of input B"),
    ("B.RenderLayer.Normal.Z", "Z channel from layer/view RenderLayer.Normal of input B"),
    ("B.RenderLayer.Normal.X", "X channel from layer/view RenderLayer.Normal of input B"),
    ("B.RenderLayer.Normal.Y", "Y channel from layer/view RenderLayer.Normal of input B")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Input channel for the output red channel")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.Shuffle1outputR = param
    del param

    param = lastNode.createIntParam("np", "Near Plane")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("the closest Z value")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.np = param
    del param

    param = lastNode.createIntParam("fp", "Far Plane")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1000, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.fp = param
    del param

    param = lastNode.createBooleanParam("showZ", "Show modified Z pass")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Show the modified Z pass , ideally your scene needs to fit roughly between 0 and 1 value")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.showZ = param
    del param

    param = lastNode.createSeparatorParam("sepa", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sepa = param
    del param

    param = lastNode.createStringParam("labc", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("AO settings :")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.labc = param
    del param

    param = lastNode.createDoubleParam("radius", "Radius")
    param.setMinimum(0, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(2, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(0.5, 0)
    lastNode.radius = param
    del param

    param = lastNode.createDoubleParam("falloff", "Falloff")
    param.setMinimum(-51315, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0.002, 0)
    param.setDisplayMaximum(2, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Increase this Value soften the shadows")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1, 0)
    lastNode.falloff = param
    del param

    param = lastNode.createIntParam("samples", "Samples")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(0, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Number of iteration to get the AO\n\nfor a very smooth AO you may need to increase this value to 1000  and lower the Sample noise value to 0.02")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(10, 0)
    lastNode.samples = param
    del param

    param = lastNode.createDoubleParam("sample_noise", "Samples_Noise")
    param.setMinimum(0, 0)
    param.setMaximum(2, 0)
    param.setDisplayMinimum(0.001, 0)
    param.setDisplayMaximum(1, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("To calculate AO some noise is needed to get the samples correctly .\nIf the samples number is very high , then lower this value to something like 0.05 . ")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(1, 0)
    lastNode.sample_noise = param
    del param

    param = lastNode.createSeparatorParam("sepd", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sepd = param
    del param

    param = lastNode.createDoubleParam("strength", "Strength")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(2, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.strength = param
    del param

    param = lastNode.createBooleanParam("filter", "Filter_Output")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Blur slightly the image to get rid of the remaining noise/artifacts")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.filter = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Node'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(907, 349)
    lastNode.setSize(104, 30)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "SSAO_Shader"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("SSAO_Shader")
    lastNode.setLabel("SSAO_Shader")
    lastNode.setPosition(720, 100)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSSAO_Shader = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(1e-05, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(0.01, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueInt3")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramValueFloat3")
    if param is not None:
        param.setValue(0.005, 0)
        del param

    param = lastNode.getParam("paramValueInt4")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramValueFloat5")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("uniform float total_strength = 1.0;\nuniform float base = 0.2;\nuniform float area = 0.01 ;\nuniform float falloff = 0.1;\nuniform float radius = 4.0;\nuniform int samples = 10;\nuniform float noise_amt = 1.0;\n\nfloat nrand( vec2 n )\n{\n  float rnd = fract(sin(dot(n.xy, vec2(12.9898, 78.233)))* 43758.5453);\n  rnd=(rnd*2)-1;\n\treturn rnd ;\n}\n\nvec3 gen_rnd_vec(vec2 co){\n  float x = nrand( co ) ;\n  float y = nrand( co+0.25464853 ) ;\n  float z = nrand( co-0.16498 ) ;\n  return vec3 (x,y,z)*noise_amt ;\n}\n\nvec3 normal_from_depth(vec3 depth, vec2 Coord) {\n  const vec2 offset1 = vec2(0.0,0.001);\n  const vec2 offset2 = vec2(0.001,0.0);\n  float depth1 = texture2D(iChannel0, Coord.xy / iResolution.xy + offset1).r;\n  float depth2 = texture2D(iChannel0, Coord.xy / iResolution.xy + offset2).r;\n  vec3 p1 = vec3(offset1, depth1 - depth.r);\n  vec3 p2 = vec3(offset2, depth2 - depth.r);\n  vec3 normal = cross(p1, p2);\n  normal.z = -normal.z;\n  return normalize(normal);\n}\n\nvec3 sample_sphere_trash(int id, vec2 fragCoord){\n  vec2 coord= vec2(fragCoord.x+(id),fragCoord.y+(id));\n  vec3 vector = gen_rnd_vec(coord) ;\n  float scale = float(id) / radius ;\n  scale = mix(0.1, 1.0, scale * scale);\n  vector *=scale ;\n  vector = normalize(vector);\n  return(vector) ;\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n  vec2 uv = fragCoord.xy / iResolution.xy;\n  vec3 random = gen_rnd_vec(uv);\n  vec3 depth    = texture2D(iChannel0, uv).rgb ;\n  vec3 position = vec3(uv,depth);\n  vec3 normal   = normal_from_depth(depth, fragCoord);\n  float radius_depth = radius/depth.r;\n  float occlusion = 0.0;\n  for(int i=0; i < samples; i++) {\n    vec3 ray         = radius_depth * reflect(sample_sphere_trash(i,fragCoord/iRenderScale) , random);\n    vec3 hemi_ray    = position + sign(dot(ray,normal)) * ray;\n    vec2 hrl=clamp(hemi_ray.xy,vec2(0.,0.),vec2(1.,1.));\n    float occ_depth  = texture2D(iChannel0, hrl).r;\n    float difference = depth.r - occ_depth;\n    occlusion += (1.0-smoothstep(falloff, area, difference));\n  }\n\n  float ao = 1.0 - total_strength * occlusion * (1.0 / samples);\n  fragColor = vec4(ao,ao,ao,1.0);\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("Nearest")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("square_2K 2048x2048")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(6, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("area")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("area")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(0.009999999776482582, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("falloff")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("falloff")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(0.1000000014901161, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("noise_amt")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("noise_amt")
        del param

    param = lastNode.getParam("paramDefaultFloat2")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("radius")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("radius")
        del param

    param = lastNode.getParam("paramDefaultFloat3")
    if param is not None:
        param.setValue(4, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("samples")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("samples")
        del param

    param = lastNode.getParam("paramDefaultInt4")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("total_strength")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("total_strength")
        del param

    param = lastNode.getParam("paramDefaultFloat5")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "SSAO_Shader"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(708, -155)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputChannelsChoice")
    if param is not None:
        param.setValue("Color.RGBA")
        del param

    param = lastNode.getParam("outputRChoice")
    if param is not None:
        param.setValue("A.r")
        del param

    param = lastNode.getParam("outputGChoice")
    if param is not None:
        param.setValue(".g")
        del param

    param = lastNode.getParam("outputBChoice")
    if param is not None:
        param.setValue(".b")
        del param

    param = lastNode.getParam("outputAChoice")
    if param is not None:
        param.setValue(".a")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "ZRemap"
    lastNode = app.createNode("net.sf.openfx.GradePlugin", 2, group)
    lastNode.setScriptName("ZRemap")
    lastNode.setLabel("ZRemap")
    lastNode.setPosition(708, -50)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.48, 0.66, 1)
    groupZRemap = lastNode

    param = lastNode.getParam("blackPoint")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("whitePoint")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        param.setValue(0, 3)
        del param

    del lastNode
    # End of node "ZRemap"

    # Start of node "Switch1"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch1")
    lastNode.setLabel("Switch1")
    lastNode.setPosition(907, 172)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(952, -36)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Z"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Z")
    lastNode.setLabel("Z")
    lastNode.setPosition(709, -286)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupZ = lastNode

    del lastNode
    # End of node "Z"

    # Start of node "Blur1"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 3, group)
    lastNode.setScriptName("Blur1")
    lastNode.setLabel("Blur1")
    lastNode.setPosition(708, 172)
    lastNode.setSize(104, 43)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(3, 0)
        param.setValue(3, 1)
        del param

    param = lastNode.getParam("filter")
    if param is not None:
        param.set("Quasi-Gaussian")
        del param

    param = lastNode.getParam("expandRoD")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Blur1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupSwitch1)
    groupSSAO_Shader.connectInput(0, groupZRemap)
    groupShuffle1.connectInput(0, groupZ)
    groupShuffle1.connectInput(1, groupZ)
    groupZRemap.connectInput(0, groupShuffle1)
    groupSwitch1.connectInput(0, groupBlur1)
    groupSwitch1.connectInput(1, groupDot1)
    groupDot1.connectInput(0, groupZRemap)
    groupBlur1.connectInput(0, groupSSAO_Shader)

    param = groupSSAO_Shader.getParam("paramValueFloat1")
    param.setExpression("thisGroup.falloff.get()/100.0", False, 0)
    del param
    param = groupSSAO_Shader.getParam("paramValueFloat2")
    param.setExpression("thisGroup.sample_noise.get()", False, 0)
    del param
    param = groupSSAO_Shader.getParam("paramValueFloat3")
    param.setExpression("thisGroup.radius.get()/100.0", False, 0)
    del param
    param = groupSSAO_Shader.getParam("paramValueInt4")
    param.setExpression("thisGroup.samples.get()", False, 0)
    del param
    param = groupSSAO_Shader.getParam("paramValueFloat5")
    param.setExpression("thisGroup.strength.get()", False, 0)
    del param
    param = groupZRemap.getParam("blackPoint")
    param.setExpression("thisGroup.np.get()", False, 0)
    del param
    param = groupZRemap.getParam("whitePoint")
    param.setExpression("thisGroup.fp.get()", False, 0)
    del param
    param = groupSwitch1.getParam("which")
    param.setExpression("thisGroup.showZ.get()", False, 0)
    del param
    param = groupBlur1.getParam("disableNode")
    param.setExpression("1-(thisGroup.filter.get())", False, 0)
    del param

    try:
        extModule = sys.modules["SSAOExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)

