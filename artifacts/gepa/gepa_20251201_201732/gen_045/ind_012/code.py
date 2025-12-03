
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in D (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 1.5, 1.75),   # D2 on 1
    (40, 1.75, 2.0),   # F2 on 2
    (42, 2.0, 2.25),   # A2 on 3
    (43, 2.25, 2.5),   # Bb2 on 4
    (43, 2.5, 2.75),   # Bb2 on 1
    (42, 2.75, 3.0),   # A2 on 2
    (40, 3.0, 3.25),   # F2 on 3
    (38, 3.25, 3.5),   # D2 on 4
    (38, 3.5, 3.75),   # D2 on 1
    (40, 3.75, 4.0),   # F2 on 2
    (42, 4.0, 4.25),   # A2 on 3
    (43, 4.25, 4.5),   # Bb2 on 4
    (43, 4.5, 4.75),   # Bb2 on 1
    (42, 4.75, 5.0),   # A2 on 2
    (40, 5.0, 5.25),   # F2 on 3
    (38, 5.25, 5.5)    # D2 on 4
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: Open voicings, resolve on last beat of each bar
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    (62, 1.5, 1.75), (65, 1.5, 1.75), (67, 1.5, 1.75), (69, 1.5, 1.75),
    # Bar 3: G7 (G-B-D-F)
    (67, 2.25, 2.5), (71, 2.25, 2.5), (69, 2.25, 2.5), (65, 2.25, 2.5),
    # Bar 4: C#m7 (C#-E-G-C)
    (69, 3.0, 3.25), (71, 3.0, 3.25), (67, 3.0, 3.25), (60, 3.0, 3.25)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: Motif in D, short and singable
sax_notes = [
    (62, 1.5, 1.75),   # D4 on 1
    (65, 1.75, 2.0),   # F#4 on 2
    (67, 2.0, 2.25),   # A4 on 3
    (69, 2.25, 2.5),   # B4 on 4
    (65, 2.5, 2.75),   # F#4 on 1
    (67, 2.75, 3.0),   # A4 on 2
    (69, 3.0, 3.25),   # B4 on 3
    (67, 3.25, 3.5),   # A4 on 4
    (62, 3.5, 3.75),   # D4 on 1
    (65, 3.75, 4.0),   # F#4 on 2
    (67, 4.0, 4.25),   # A4 on 3
    (69, 4.25, 4.5),   # B4 on 4
    (67, 4.5, 4.75),   # A4 on 1
    (65, 4.75, 5.0),   # F#4 on 2
    (69, 5.0, 5.25),   # B4 on 3
    (67, 5.25, 5.5)    # A4 on 4
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.75), (42, 1.5, 1.75), (38, 1.75, 2.0), (42, 1.75, 2.0),
    (36, 2.25, 2.5), (42, 2.25, 2.5), (38, 2.5, 2.75), (42, 2.5, 2.75),
    # Bar 3
    (36, 3.0, 3.25), (42, 3.0, 3.25), (38, 3.25, 3.5), (42, 3.25, 3.5),
    (36, 3.75, 4.0), (42, 3.75, 4.0), (38, 4.0, 4.25), (42, 4.0, 4.25),
    # Bar 4
    (36, 4.5, 4.75), (42, 4.5, 4.75), (38, 4.75, 5.0), (42, 4.75, 5.0),
    (36, 5.25, 5.5), (42, 5.25, 5.5), (38, 5.5, 5.75), (42, 5.5, 5.75)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
