#!/usr/bin/env python
# from python_get_resolve import GetResolve

import random
import DaVinciResolveScript as dvr_script

TIMECODE = 9000

def get_timecode( frameNumber ):
    return TIMECODE + frameNumber

def add_transitions(ends, mediaPool):
    transitions_folder = mediaPool.GetCurrentFolder()
    blank_folder = mediaPool.GetCurrentFolder().GetSubFolderList()[0]

    transitions = transitions_folder.GetClipList()
    blank_clip = blank_folder.GetClipList()[0]

    transitionsTimeline = project.GetCurrentTimeline()
    print("-----\nTransitions Timeline: " + transitionsTimeline.GetName())
    timelineLength = transitionsTimeline.GetEndFrame()

    for index in range(len(ends)):
        if ends[index] - 25 >= transitionsTimeline.GetEndFrame():
            transitionStartFrame = ends[index] - 25

            ## ADD BLANK CLIP
            mediaPool.AppendToTimeline(
                [
                    {
                        "mediaPoolItem": blank_clip,
                        "startFrame": transitionsTimeline.GetEndFrame(),
                        "endFrame": transitionStartFrame,
                        "mediatype": 1,
                    }
                ]
            )

            print(
                f"added blank clip from {transitionsTimeline.GetEndFrame()} to {transitionStartFrame}"
            )

            ## ADD TRANSITION
            randomTransition = transitions[random.randint(0, len(transitions) - 1)]
            print(randomTransition.GetName())
            # print(f"add transition at {ends[index] - 25}")

            mediaPool.AppendToTimeline(randomTransition)

            print(f"added transition at {transitionStartFrame}")

    # testClip = clipList[0]

    # mediaPool.AppendToTimeline({ 'mediaPoolItem': testClip, 'startFrame': 10, 'endFrame': 35})
    # mediaPool.AppendToTimeline({ "mediaPoolItem": testClip, "startFrame": 10, "endFrame": 35})
    # mediaPool.AppendToTimeline([{ 'mediaPoolItem': testClip, 'startFrame': 10, 'endFrame': 35, 'mediatype': 1}])
    # mediaPool.AppendToTimeline(testClip)


def main(project, mediaPool):
    print("Project : " + project.GetName())

    originalTimeline = project.GetCurrentTimeline()

    print("Orignal Timeline: " + originalTimeline.GetName())

    clips = originalTimeline.GetItemListInTrack("video", 1)

    # silenceClip = 0

    timelineLength = originalTimeline.GetEndFrame()

    ends = [0]

    for clip in clips:
        ends.append(clip.GetEnd())

    ######  PAUSE HERE   #####
    input("Press Enter to continue...")

    # for end in ends:
    # add_transition()
    add_transitions(ends, mediaPool)

    #
    print(" --- --- ")
    return


# Get currently open project
# resolve = GetResolve()

resolve = dvr_script.scriptapp('Resolve')

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()


main(project, mediaPool)
