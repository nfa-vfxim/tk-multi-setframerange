# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import maya.cmds as cmds

import sgtk

HookBaseClass = sgtk.get_hook_baseclass()


class FrameOperation(HookBaseClass):
    """
    Hook called to perform a frame operation with the
    current scene
    """

    def get_frame_range(self, **kwargs):
        """
        get_frame_range will return a tuple of (in_frame, out_frame)

        :returns: Returns the frame range in the form (in_frame, out_frame)
        :rtype: tuple[int, int]
        """
        current_in = cmds.playbackOptions(query=True, minTime=True)
        current_out = cmds.playbackOptions(query=True, maxTime=True)
        return (current_in, current_out)

    def set_frame_range(self, in_frame=None, out_frame=None, **kwargs):
        """
        set_frame_range will set the frame range using `in_frame` and `out_frame`

        :param int in_frame: in_frame for the current context
            (e.g. the current shot, current asset etc)

        :param int out_frame: out_frame for the current context
            (e.g. the current shot, current asset etc)

        """

        # set frame ranges for plackback
        cmds.playbackOptions(
            minTime=in_frame,
            maxTime=out_frame,
            animationStartTime=in_frame,
            animationEndTime=out_frame,
        )

        # set frame ranges for rendering
        cmds.setAttr("defaultRenderGlobals.startFrame", in_frame)
        cmds.setAttr("defaultRenderGlobals.endFrame", out_frame)

        self.set_resolution()  # lol

    def set_resolution(self):
        """Sets the resolution of the Maya project. We need this right now for an animation project
        and I don't feel like making a whole new app thingy for this so I'm putting this here.
        Thanks Chris Devito for figuring out this code. Maya makes this weirdly difficult."""
        resolution = self.parent.get_resolution_from_shotgun()
        device_aspect = float(resolution[0] * 1) / float(resolution[1])
        cmds.setAttr("defaultResolution.lockDeviceAspectRatio", 1)
        cmds.setAttr("defaultResolution.width", resolution[0])
        cmds.setAttr("defaultResolution.height", resolution[1])
        cmds.setAttr("defaultResolution.deviceAspectRatio", device_aspect)
