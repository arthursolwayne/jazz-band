
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (24, 0.0),  # F
    (26, 0.375), # Gb
    (25, 0.75),  # E
    (24, 1.125), # F
    (26, 1.5),   # Gb
    (28, 1.875), # Ab
    (27, 2.25),  # G
    (26, 2.625), # Gb
    (24, 3.0),   # F
    (26, 3.375), # Gb
    (28, 3.75),  # Ab
    (30, 4.125), # Bb
    (29, 4.5),   # A
    (28, 4.875), # Ab
    (26, 5.25),  # Gb
    (24, 5.625), # F
]

for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time + 1.5, end=time + 1.5 + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (36, 2.0), (39, 2.0), (41, 2.0), (43, 2.0),  # F7 on beat 2
    (36, 4.0), (39, 4.0), (41, 4.0), (43, 4.0),  # F7 on beat 4
]

for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + 1.5, end=time + 1.5 + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - F (sax in Fm)
sax_notes = [
    (24, 1.5),  # F
    (26, 1.75), # Ab
    (28, 2.0),  # Bb
    (24, 2.5),  # F
    (24, 3.5),  # F
    (26, 3.75), # Ab
    (28, 4.0),  # Bb
    (24, 4.5),  # F
]

for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
