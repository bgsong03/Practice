def replaceUnderScore(arr, word):
  chars = list(word)
  counter = 0
  underscore = 0
  for i in range(len(arr)):
    if (arr[i] == '_'):
      underscore += 1
      if (underscore > len(chars)):
        arr[:] = [''.join(arr[:])]
        return(arr[0])
      arr[i] = chars[counter]
      counter += 1
  if (underscore < len(chars)):
    return(False)
  else:
    arr[:] = [''.join(arr[:])]
    return(arr[0])

print (replaceUnderScore(['s'], 'u'))

