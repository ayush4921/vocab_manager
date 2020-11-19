from PyDictionary import PyDictionary
import pandas as pd
import os
from flask import Flask, flash, request, redirect, url_for, render_template
dictionary=PyDictionary()
word2=['Abate', 'Abstract', 'Abysmal', 'Accordingly', 'Acquisition', 'Adapt', 'Adept', 'Adequate', 'Advent', 'Adversarial', 'Advocate', 'Aesthetic', 'Afford', 'Agitate', 'Allow', 'Allude', 'Altercation', 'Ambiguous', 'Ambitious', 'Ambivalence', 'Analogous', 'Annihilate', 'Anomaly', 'Anticipate', 'Antipathy', 'Apex', 'Apprehension', 'Articulate', 'Artificial', 'Assertion', 'Austere', 'Authenticity', 'Avenue', 'Avid', 'Basic', 'Bear', 'Benevolent', 'Bias', 'Bittersweet', 'Bolster', 'Boost', 'Brawl', 'Brevity', 'Candid', 'Candor', 'Capitalize', 'Capture', 'Civic', 'Clinical', 'Clout', 'Coarse', 'Coincide', 'Commission', 'Comparable', 'Competent', 'Complacent', 'Complement', 'Concede', 'Conceive', 'Condone', 'Conducive', 'Conduct', 'Confide', 'Confine', 'Consensus', 'Constitute', 'Contemplate', 'Contend', 'Contradict', 'Controversial', 'Conventional', 'Convey', 'Conviction', 'Corroborate', 'Counteract', 'Counterargument', 'Counterproductive', 'Culmination', 'Cultivate', 'Decree', 'Deference', 'Deficient', 'Demonstrate', 'Demur', 'Deplete', 'Desolate', 'Devise', 'Dilemma', 'Diligence', 'Diminish', 'Dire', 'Discord', 'Disdain', 'Dismay', 'Disparage', 'Dispatch', 'Diversification', 'Doctrine', 'Dominion', 'Dreary', 'Dubious', 'Eccentric', 'Egregious', 'Eloquent', 'Eminent', 'Emit', 'Emphatic', 'Empirical', 'Endow', 'Endure', 'Entail', 'Entrenched', 'Enumerate', 'Envy', 'Erratic', 'Establish', 'Evoke', 'Exacerbate', 'Excel', 'Exert', 'Exhilarating', 'Expend', 'Exploit', 'Facilitate', 'Feasibility', 'Ferocity', 'Fiscal', 'Flourish', 'Fluctuate', 'Foment', 'Foreseeable', 'Frankly', 'Freewheeling', 'Fundamental', 'Galvanizing', 'Geriatric', 'Hostile', 'Hypothetical', 'Ignominious', 'Impart', 'Impartiality', 'Imposing', 'Imposition', 'Imprudent', 'Incite', 'Indifference', 'Indiscriminately', 'Indulge', 'Infer', 'Innovative', 'Insatiable', 'Inversion', 'Invoke', 'Irreconcilable', 'Lament', 'Locomotion', 'Lucrative', 'Malicious', 'Malleable', 'Materialistic', 'Melodramatic', 'Modest', 'Modify', 'Momentous', 'Novel', 'Nuance', 'Null', 'Objectivity', 'Obsolete', 'Omnipotent', 'Onset', 'Opine', 'Ornate', 'Oust', 'Paramount', 'Peculiar', 'Perish', 'Persecute', 'Petulant', 'Pinnacle', 'Pitiable', 'Plausible', 'Postulate', 'Potent', 'Pragmatic', 'Precedent', 'Predecessor', 'Prescribe', 'Principle', 'Prohibit', 'Prompt', 'Promulgate', 'Prosecute', 'Provocative', 'Qualitative', 'Quantitative', 'Quirk', 'Ramify', 'Rash', 'Raw', 'Readily', 'Reconsideration', 'Reform', 'Refute', 'Reinforce', 'Reluctantly', 'Renounce', 'Reproach', 'Repudiate', 'Retention', 'Satiated', 'Savvy', 'Scandalous', 'Scorn', 'Scrupulous', 'Scrutinize', 'Secrete', 'Sentiment', 'Sheer', 'Simple', 'Sinister', 'Solidarity', 'Sparingly', 'Spawn', 'Spur', 'Squalid', 'Stark', 'Static', 'Subordinate', 'Subsequently', 'Substantial', 'Substantiate', 'Subtle', 'Sufficient', 'Surly', 'Surmount', 'Susceptible', 'Tactful', 'Taut', 'Teeming', 'Temperament', 'Tentative', 'Transparent', 'Treacherous', 'Tremendous', 'Ubiquitous', 'Unadorned', 'Undermine', 'Underscore', 'Undulate', 'Unilateral', 'Unjust', 'Unmitigated', 'Unprecedented', 'Unveil', 'Urge', 'Validate', 'Viability', 'Vital', 'Vow', 'Warrant', 'Yield']
meaning1=[]
synonym1=[]
antonym1=[]
for a in word2:
    try:
        meaning1.append(dictionary.meaning(a))
        synonym1.append(dictionary.synonym(a))
        antonym1.append(dictionary.antonym(a))
    except:
        meaning1.append('not found')
        synonym1.append('not found')
        antonym1.append('not found')

dicti1 = {'word': word2, 'meaning': meaning1, 'synonym': synonym1,'antonym':antonym1}  
df11 = pd.DataFrame(dicti1)
path=os.getcwd()
filename = os.path.join(path, 'output1.csv')
if os.path.isfile(filename):
    mode = 'a'
    header = 0
else:
    mode = 'w'
    header = True


df11.to_csv('output1.csv', mode=mode,index=None,header=header)