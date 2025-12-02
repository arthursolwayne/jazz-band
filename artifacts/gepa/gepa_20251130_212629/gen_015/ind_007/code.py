
from music21 import note, chord, stream, tempo, meter, duration, clef, key, instrument

# Create a new stream
intro = stream.Stream()
intro.append(key.Key('D', 'major'))
intro.append(tempo.MetronomeMark(number=160))
intro.append(meter.TimeSignature('4/4'))
intro.append(clef.TrebleClef())

# Define instruments
dante_sax = instrument.TenorSaxophone()
diane_piano = instrument.Piano()
marcus_bass = instrument.ElectricBass()
little_ray_drums = instrument.Drums()

intro.append(dante_sax)
intro.append(diane_piano)
intro.append(marcus_bass)
intro.append(little_ray_drums)

# Bar 1: Little Ray on drums (quiet, subtle)
hi_hat = note.Note('C5', type='eighth')
hi_hat.duration.type = 'eighth'
hi_hat.duration.dots = 1
intro.append(hi_hat)

kick = note.Note('C3', type='quarter')
kick.duration.type = 'quarter'
kick.offset = 0
intro.append(kick)

snare = note.Note('G4', type='quarter')
snare.duration.type = 'quarter'
snare.offset = 2
intro.append(snare)

# Bar 1: Diane (piano) - comp on 2 and 4
diane_chord_1 = chord.Chord(['D', 'F#', 'A', 'C#'], duration=duration.Duration(0.5))
diane_chord_1.offset = 1
diane_chord_1.quarterLength = 0.5
intro.append(diane_chord_1)

diane_chord_2 = chord.Chord(['G', 'B', 'D', 'F#'], duration=duration.Duration(0.5))
diane_chord_2.offset = 3
diane_chord_2.quarterLength = 0.5
intro.append(diane_chord_2)

# Bar 1: Marcus (bass) - walking line with chromatic approaches
bass_notes = [
    note.Note('D3', type='quarter'),
    note.Note('E3', type='eighth'),
    note.Note('F3', type='eighth'),
    note.Note('G3', type='quarter'),
]
for n in bass_notes:
    intro.append(n)

# Bar 2: Everyone in, Dante's motif starts
# Dante (tenor sax) - motif
dante_motif = [
    note.Note('F#4', type='eighth'),
    note.Note('G4', type='eighth'),
    note.Note('A4', type='quarter'),
    note.Note('D5', type='half'),  # Hang on the D
]
for n in dante_motif:
    intro.append(n)

# Bar 2: Diane (piano) - comp on 2 and 4
diane_chord_3 = chord.Chord(['A', 'C#', 'E', 'G#'], duration=duration.Duration(0.5))
diane_chord_3.offset = 1
diane_chord_3.quarterLength = 0.5
intro.append(diane_chord_3)

diane_chord_4 = chord.Chord(['D', 'F#', 'A', 'C#'], duration=duration.Duration(0.5))
diane_chord_4.offset = 3
diane_chord_4.quarterLength = 0.5
intro.append(diane_chord_4)

# Bar 2: Marcus (bass) - walking line
bass_notes_2 = [
    note.Note('A3', type='quarter'),
    note.Note('B3', type='eighth'),
    note.Note('C#4', type='eighth'),
    note.Note('D4', type='quarter'),
]
for n in bass_notes_2:
    intro.append(n)

# Bar 2: Little Ray (drums) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_2 = note.Note('C3', type='quarter')
kick_2.offset = 0
intro.append(kick_2)

snare_2 = note.Note('G4', type='quarter')
snare_2.offset = 2
intro.append(snare_2)

hi_hat_2 = note.Note('C5', type='eighth')
hi_hat_2.duration.type = 'eighth'
hi_hat_2.duration.dots = 1
hi_hat_2.offset = 0
intro.append(hi_hat_2)

hi_hat_2_2 = note.Note('C5', type='eighth')
hi_hat_2_2.duration.type = 'eighth'
hi_hat_2_2.duration.dots = 1
hi_hat_2_2.offset = 0.5
intro.append(hi_hat_2_2)

hi_hat_2_3 = note.Note('C5', type='eighth')
hi_hat_2_3.duration.type = 'eighth'
hi_hat_2_3.duration.dots = 1
hi_hat_2_3.offset = 1
intro.append(hi_hat_2_3)

hi_hat_2_4 = note.Note('C5', type='eighth')
hi_hat_2_4.duration.type = 'eighth'
hi_hat_2_4.duration.dots = 1
hi_hat_2_4.offset = 1.5
intro.append(hi_hat_2_4)

# Bar 3: Diane (piano) - comp on 2 and 4
diane_chord_5 = chord.Chord(['B', 'D', 'F#', 'A'], duration=duration.Duration(0.5))
diane_chord_5.offset = 1
diane_chord_5.quarterLength = 0.5
intro.append(diane_chord_5)

diane_chord_6 = chord.Chord(['E', 'G#', 'B', 'D'], duration=duration.Duration(0.5))
diane_chord_6.offset = 3
diane_chord_6.quarterLength = 0.5
intro.append(diane_chord_6)

# Bar 3: Marcus (bass) - walking line
bass_notes_3 = [
    note.Note('E3', type='quarter'),
    note.Note('F#3', type='eighth'),
    note.Note('G3', type='eighth'),
    note.Note('A3', type='quarter'),
]
for n in bass_notes_3:
    intro.append(n)

# Bar 3: Little Ray (drums) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_3 = note.Note('C3', type='quarter')
kick_3.offset = 2
intro.append(kick_3)

snare_3 = note.Note('G4', type='quarter')
snare_3.offset = 4
intro.append(snare_3)

hi_hat_3 = note.Note('C5', type='eighth')
hi_hat_3.duration.type = 'eighth'
hi_hat_3.duration.dots = 1
hi_hat_3.offset = 2
intro.append(hi_hat_3)

hi_hat_3_2 = note.Note('C5', type='eighth')
hi_hat_3_2.duration.type = 'eighth'
hi_hat_3_2.duration.dots = 1
hi_hat_3_2.offset = 2.5
intro.append(hi_hat_3_2)

hi_hat_3_3 = note.Note('C5', type='eighth')
hi_hat_3_3.duration.type = 'eighth'
hi_hat_3_3.duration.dots = 1
hi_hat_3_3.offset = 3
intro.append(hi_hat_3_3)

hi_hat_3_4 = note.Note('C5', type='eighth')
hi_hat_3_4.duration.type = 'eighth'
hi_hat_3_4.duration.dots = 1
hi_hat_3_4.offset = 3.5
intro.append(hi_hat_3_4)

# Bar 4: Diane (piano) - comp on 2 and 4
diane_chord_7 = chord.Chord(['F#', 'A', 'C#', 'E'], duration=duration.Duration(0.5))
diane_chord_7.offset = 1
diane_chord_7.quarterLength = 0.5
intro.append(diane_chord_7)

diane_chord_8 = chord.Chord(['B', 'D', 'F#', 'A'], duration=duration.Duration(0.5))
diane_chord_8.offset = 3
diane_chord_8.quarterLength = 0.5
intro.append(diane_chord_8)

# Bar 4: Marcus (bass) - walking line
bass_notes_4 = [
    note.Note('F#3', type='quarter'),
    note.Note('G3', type='eighth'),
    note.Note('A3', type='eighth'),
    note.Note('B3', type='quarter'),
]
for n in bass_notes_4:
    intro.append(n)

# Bar 4: Little Ray (drums) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_4 = note.Note('C3', type='quarter')
kick_4.offset = 4
intro.append(kick_4)

snare_4 = note.Note('G4', type='quarter')
snare_4.offset = 6
intro.append(snare_4)

hi_hat_4 = note.Note('C5', type='eighth')
hi_hat_4.duration.type = 'eighth'
hi_hat_4.duration.dots = 1
hi_hat_4.offset = 4
intro.append(hi_hat_4)

hi_hat_4_2 = note.Note('C5', type='eighth')
hi_hat_4_2.duration.type = 'eighth'
hi_hat_4_2.duration.dots = 1
hi_hat_4_2.offset = 4.5
intro.append(hi_hat_4_2)

hi_hat_4_3 = note.Note('C5', type='eighth')
hi_hat_4_3.duration.type = 'eighth'
hi_hat_4_3.duration.dots = 1
hi_hat_4_3.offset = 5
intro.append(hi_hat_4_3)

hi_hat_4_4 = note.Note('C5', type='eighth')
hi_hat_4_4.duration.type = 'eighth'
hi_hat_4_4.duration.dots = 1
hi_hat_4_4.offset = 5.5
intro.append(hi_hat_4_4)

# Write the score to a MIDI file
intro.show('midi')
