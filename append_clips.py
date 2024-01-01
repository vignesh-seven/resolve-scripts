#!/usr/bin/env python

from python_get_resolve import GetResolve

def main( project , mediaPool ):

  print("Project : " + project.GetName())

  currentTimeline = project.GetCurrentTimeline()

  print("Timeline: " + currentTimeline.GetName())

  folder = mediaPool.GetCurrentFolder()

  clipList = folder.GetClipList()

  print(" ---  ")

  testClip = clipList[0]
  
  # mediaPool.AppendToTimeline({ 'mediaPoolItem': testClip, 'startFrame': 10, 'endFrame': 35})
  # mediaPool.AppendToTimeline({ "mediaPoolItem": testClip, "startFrame": 10, "endFrame": 35})
  # mediaPool.AppendToTimeline([{ 'mediaPoolItem': testClip, 'startFrame': 10, 'endFrame': 35, 'mediatype': 1}])
  # mediaPool.AppendToTimeline(testClip)

  print(" --- --- ")
  return

# Get currently open project
resolve = GetResolve()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()


main(project, mediaPool)


