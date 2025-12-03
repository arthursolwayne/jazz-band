
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
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus bass: D2 (38) to A2 (45) on 1, G2 (43) on 2, C3 (48) on 3, D2 (38) on 4
bass_notes = [
    (38, 1.5), (43, 1.875), (48, 2.25), (38, 2.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane piano: Cmaj7 (C-E-G-B) on 2, D7 (D-F#-A-C) on 4
piano_notes = [
    (60, 1.875), (64, 1.875), (67, 1.875), (71, 1.875),  # Cmaj7
    (62, 2.625), (66, 2.625), (69, 2.625), (72, 2.625)   # D7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante sax: motif - D4 (62) to Bb4 (66), then F#4 (65), then D4 (62)
sax_notes = [
    (62, 1.5), (66, 1.5), (65, 2.25), (62, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 3 (3.0 - 4.5s)
# Marcus bass: G2 (43) to D3 (50) on 1, A2 (45) on 2, B2 (47) on 3, D3 (50) on 4
bass_notes = [
    (43, 3.0), (45, 3.375), (47, 3.75), (50, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane piano: G7 (G-B-D-F) on 2, A7 (A-C#-E-G) on 4
piano_notes = [
    (67, 3.375), (71, 3.375), (74, 3.375), (77, 3.375),  # G7
    (69, 4.125), (73, 4.125), (76, 4.125), (79, 4.125)   # A7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4 (4.5 - 6.0s)
# Marcus bass: B2 (47) to F3 (55) on 1, D3 (50) on 2, G3 (53) on 3, B2 (47) on 4
bass_notes = [
    (47, 4.5), (50, 4.875), (53, 5.25), (47, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane piano: B7 (B-D#-F#-A) on 2, Cmaj7 (C-E-G-B) on 4
piano_notes = [
    (71, 4.875), (74, 4.875), (76, 4.875), (79, 4.875),  # B7
    (60, 5.625), (64, 5.625), (67, 5.625), (71, 5.625)   # Cmaj7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante sax: motif repeats, but ends on D4 (62)
sax_notes = [
    (62, 4.5), (66, 4.5), (65, 5.25), (62, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
