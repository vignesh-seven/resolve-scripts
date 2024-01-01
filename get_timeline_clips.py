#!/usr/bin/env python

from python_get_resolve import GetResolve

def main( project , mediaPool ):

  print("Project : " + project.GetName())

  currentTimeline = project.GetCurrentTimeline()

  print("Timeline: " + currentTimeline.GetName())

  clips = currentTimeline.GetItemListInTrack("video", 1)


  #
  totalLength = currentTimeline.GetEndFrame()
  myEnd = clips[0].GetEnd()
  print(" --- --- ")
  return

# Get currently open project
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()


main(project, mediaPool)


