#!/usr/bin/env python
# Copyright (c) 2019 CNRS
# Author: Pierre Fernbach
#
# This file is part of hpp-rbprm-robot-data.
# hpp_tutorial is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp_tutorial is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp_tutorial.  If not, see
# <http://www.gnu.org/licenses/>.

from hpp.corbaserver.rbprm.rbprmbuilder import Builder as Parent

class Robot (Parent):
    ##
    #  Information to retrieve urdf and srdf files.
    rootJointType = 'freeflyer'
    packageName = 'anymal-rbprm'
    meshPackageName = 'anymal-rbprm'
    # URDF file describing the trunk of the robot HyQ
    urdfName = 'anymal_trunk'
    # URDF files describing the reachable workspace of each limb of HyQ
    urdfNameRom = ['anymal_RFleg_rom','anymal_LHleg_rom','anymal_LFleg_rom','anymal_RHleg_rom']
    urdfSuffix = ""
    srdfSuffix = ""
    name = urdfName

    ref_height = 0.465

    # TODO
    
    
    rLegId = 'anymal_RFleg_rom'
    lLegId = 'anymal_LFleg_rom'
    rArmId = 'anymal_RHleg_rom'
    lArmId = 'anymal_LHleg_rom'
    
    ref_EE_lLeg =[0.373, 0.264, -0.448]
    ref_EE_rLeg = [0.373, -0.264, -0.448]
    ref_EE_lArm = [-0.373, 0.264, -0.448]
    ref_EE_rArm = [-0.373, -0.264, -0.448]
    #ref_EE_lLeg = [0.3, 0.165 , -0.44]
    #ref_EE_rLeg = [0.3, -0.165 , -0.44]
    #ref_EE_lArm = [-0.3, 0.165 , -0.44]
    #ref_EE_rArm = [-0.3, -0.165 , -0.44]
    
    dict_ref_effector_from_root = {rLegId:ref_EE_rLeg, 
                                   lLegId:ref_EE_lLeg,
                                   rArmId:ref_EE_rArm,
                                   lArmId:ref_EE_lArm}

    def __init__(self, name=None, load=True, client=None, clientRbprm=None):
        if name is not None:
            self.name = name
        Parent.__init__(self, self.name, self.rootJointType, load, client, None, clientRbprm)
        self.setReferenceEndEffector('anymal_LFleg_rom',self.ref_EE_lLeg)
        self.setReferenceEndEffector('anymal_RFleg_rom',self.ref_EE_rLeg)
        self.setReferenceEndEffector('anymal_LHleg_rom',self.ref_EE_lArm)
        self.setReferenceEndEffector('anymal_RHleg_rom',self.ref_EE_rArm)
