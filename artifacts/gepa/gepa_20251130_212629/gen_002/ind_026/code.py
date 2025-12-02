
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
    (36, 1.125), (38, 1.5), (42, 1.5)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: Fm7 to Bb7 to Eb7 to Ab7 (motif)
# Fm7: F, Ab, Bb, Db
# Bb7: Bb, D, F, Ab
# Eb7: Eb, G, Bb, Db
# Ab7: Ab, C, Eb, Gb

# Bar 2 - 1.5s to 3.0s
sax_notes = [
    (84, 1.5), (81, 1.5), (82, 1.5), (80, 1.5),  # F, Ab, Bb, Db
    (82, 1.75), (80, 1.75), (84, 1.75), (81, 1.75),  # Bb, D, F, Ab
    (80, 2.0), (83, 2.0), (82, 2.0), (80, 2.0),  # Eb, G, Bb, Db
    (81, 2.25), (85, 2.25), (80, 2.25), (83, 2.25)   # Ab, C, Eb, Gb
]
for pitch, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125))

# Bass: Walking line in Fm
# F, Gb, G, Ab, A, Bb, B, C, C#, D, Eb, E, F, Gb, G, Ab (chromatic line)
bass_notes = [
    (84, 1.5), (83, 1.625), (85, 1.75), (81, 1.875),
    (86, 2.0), (82, 2.125), (87, 2.25), (88, 2.375),
    (89, 2.5), (84, 2.625), (85, 2.75), (81, 2.875)
]
for pitch, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
# Bar 2: Bb7 on 2 (1.875), Eb7 on 4 (2.375)
piano_notes = [
    (82, 1.875), (80, 1.875), (84, 1.875), (81, 1.875),  # Bb7
    (80, 2.375), (83, 2.375), (82, 2.375), (80, 2.375)   # Eb7
]
for pitch, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with variation
sax_notes = [
    (84, 3.0), (81, 3.0), (82, 3.0), (80, 3.0),  # F, Ab, Bb, Db
    (82, 3.25), (80, 3.25), (84, 3.25), (81, 3.25),  # Bb, D, F, Ab
    (80, 3.5), (83, 3.5), (82, 3.5), (80, 3.5),  # Eb, G, Bb, Db
    (81, 3.75), (85, 3.75), (80, 3.75), (83, 3.75)   # Ab, C, Eb, Gb
]
for pitch, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125))

# Bass: Walking line in Fm
bass_notes = [
    (84, 3.0), (83, 3.125), (85, 3.25), (81, 3.375),
    (86, 3.5), (82, 3.625), (87, 3.75), (88, 3.875),
    (89, 4.0), (84, 4.125), (85, 4.25), (81, 4.375)
]
for pitch, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (82, 3.375), (80, 3.375), (84, 3.375), (81, 3.375),  # Bb7
    (80, 3.875), (83, 3.875), (82, 3.875), (80, 3.875)   # Eb7
]
for pitch, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End motif with resolution
sax_notes = [
    (84, 4.5), (81, 4.5), (82, 4.5), (80, 4.5),  # F, Ab, Bb, Db
    (82, 4.75), (80, 4.75), (84, 4.75), (81, 4.75),  # Bb, D, F, Ab
    (80, 5.0), (83, 5.0), (82, 5.0), (80, 5.0),  # Eb, G, Bb, Db
    (84, 5.25), (81, 5.25), (82, 5.25), (80, 5.25)   # F, Ab, Bb, Db
]
for pitch, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125))

# Bass: Walking line in Fm
bass_notes = [
    (84, 4.5), (83, 4.625), (85, 4.75), (81, 4.875),
    (86, 5.0), (82, 5.125), (87, 5.25), (88, 5.375),
    (89, 5.5), (84, 5.625), (85, 5.75), (81, 5.875)
]
for pitch, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (82, 4.875), (80, 4.875), (84, 4.875), (81, 4.875),  # Bb7
    (84, 5.375), (81, 5.375), (82, 5.375), (80, 5.375)   # Fm7
]
for pitch, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 4.125), (38, 4.5), (42, 4.5),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
