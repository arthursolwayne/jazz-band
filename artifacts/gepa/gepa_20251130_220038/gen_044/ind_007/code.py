
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375), (42, 0.75),
    (36, 1.125), (38, 1.5), (42, 1.5), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    (44, 1.5), (45, 1.75), (43, 2.0), (41, 2.25),
    (40, 2.5), (41, 2.75), (39, 3.0), (37, 3.25),
    (36, 3.5), (37, 3.75), (35, 4.0), (33, 4.25),
    (32, 4.5), (33, 4.75), (31, 5.0), (29, 5.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (40, 2.0), (43, 2.0), (45, 2.0), (47, 2.0),  # Fm7
    (43, 2.5), (46, 2.5), (48, 2.5), (50, 2.5),  # Bbm7
    (47, 3.0), (50, 3.0), (52, 3.0), (53, 3.0),  # Dm7
    (43, 3.5), (46, 3.5), (48, 3.5), (50, 3.5)   # Bbm7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Melody
sax_notes = [
    (41, 1.5), (43, 1.75), (41, 2.0), (43, 2.25),
    (44, 2.5), (43, 2.75), (41, 3.0), (43, 3.25),
    (44, 3.5), (43, 3.75), (41, 4.0), (43, 4.25),
    (44, 4.5), (43, 4.75), (41, 5.0), (43, 5.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
