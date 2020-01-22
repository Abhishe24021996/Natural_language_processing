def gender_features2(name):
  feautres["firstletter"] = name[0].lower()
  feautres["lastletter"] = name[-1].lower()
  for letter in 'abcdefghijklmnopqrstuvwxyz':
    feautres["count(%s)"%letter] = name.lower().count(letter)
    feautres["has(%s)"%letter] = (letter in name.lower())
  return feautres