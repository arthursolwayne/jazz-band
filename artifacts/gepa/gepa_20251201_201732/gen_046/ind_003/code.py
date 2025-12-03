
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

# Bass: Walking line in Fm (F2, Ab2, D2, Eb2, etc.)
bass_notes = [
    (71, 1.5),    # F2
    (70, 1.875),  # Eb2
    (67, 2.25),   # D2
    (72, 2.625)   # G2
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicing, Fm7, Bb7, Eb7, Am7
piano_notes = [
    (64, 1.5), (67, 1.5), (69, 1.5), (72, 1.5),  # Fm7
    (62, 1.875), (66, 1.875), (69, 1.875), (72, 1.875),  # Bb7
    (64, 2.25), (69, 2.25), (72, 2.25), (76, 2.25),  # Eb7
    (64, 2.625), (67, 2.625), (70, 2.625), (72, 2.625)   # Am7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: Motif
sax_notes = [
    (62, 1.5),    # G
    (65, 1.875),  # Bb
    (62, 2.25),   # G
    (60, 2.625)   # F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
bass_notes = [
    (72, 3.0),    # G2
    (70, 3.375),  # Eb2
    (67, 3.75),   # D2
    (71, 4.125)   # F2
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicing, Fm7, Bb7, Eb7, Am7
piano_notes = [
    (64, 3.0), (67, 3.0), (69, 3.0), (72, 3.0),  # Fm7
    (62, 3.375), (66, 3.375), (69, 3.375), (72, 3.375),  # Bb7
    (64, 3.75), (69, 3.75), (72, 3.75), (76, 3.75),  # Eb7
    (64, 4.125), (67, 4.125), (70, 4.125), (72, 4.125)   # Am7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: Motif (repeat)
sax_notes = [
    (62, 3.0),    # G
    (65, 3.375),  # Bb
    (62, 3.75),   # G
    (60, 4.125)   # F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line
bass_notes = [
    (71, 4.5),    # F2
    (70, 4.875),  # Eb2
    (67, 5.25),   # D2
    (72, 5.625)   # G2
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: Open voicing, Fm7, Bb7, Eb7, Am7
piano_notes = [
    (64, 4.5), (67, 4.5), (69, 4.5), (72, 4.5),  # Fm7
    (62, 4.875), (66, 4.875), (69, 4.875), (72, 4.875),  # Bb7
    (64, 5.25), (69, 5.25), (72, 5.25), (76, 5.25),  # Eb7
    (64, 5.625), (67, 5.625), (70, 5.625), (72, 5.625)   # Am7
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: Motif (variation)
sax_notes = [
    (62, 4.5),    # G
    (65, 4.875),  # Bb
    (62, 5.25),   # G
    (60, 5.625)   # F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
