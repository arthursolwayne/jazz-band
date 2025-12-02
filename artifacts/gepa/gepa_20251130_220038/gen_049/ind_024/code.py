
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.125),    # Hihat on 1
    (38, 0.375, 0.125),  # Snare on 2
    (42, 0.375, 0.125),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.125),   # Hihat on 3
    (38, 1.125, 0.125),  # Snare on 4
    (42, 1.125, 0.125),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    (39, 1.5, 0.375),    # Fm7 - root
    (40, 1.875, 0.375),  # Bb (chromatic approach)
    (41, 2.25, 0.375),   # Ab
    (37, 2.625, 0.375),  # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 2
    (39, 1.875, 0.375),  # F
    (44, 1.875, 0.375),  # Ab
    (42, 1.875, 0.375),  # C
    (45, 1.875, 0.375),  # D
    # Bar 3: Fm7 on 2
    (39, 2.625, 0.375),  # F
    (44, 2.625, 0.375),  # Ab
    (42, 2.625, 0.375),  # C
    (45, 2.625, 0.375),  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Whisper at first, then a cry
# Bar 2: Start the motif
sax_notes = [
    (40, 1.5, 0.375),    # Bb
    (42, 1.875, 0.375),  # C (leaning into the 3rd)
    (40, 2.25, 0.375),   # Bb (space)
    (44, 2.625, 0.375),  # Ab (climactic cry)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Drums continue with same pattern
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.125),    # Hihat on 1
    (38, 3.375, 0.125),  # Snare on 2
    (42, 3.375, 0.125),  # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.125),   # Hihat on 3
    (38, 4.125, 0.125),  # Snare on 4
    (42, 4.125, 0.125),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Bass continues walking line
bass_notes = [
    (41, 3.0, 0.375),    # Ab
    (42, 3.375, 0.375),  # Bb
    (39, 3.75, 0.375),   # F
    (40, 4.125, 0.375),  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Piano continues with 7th chords
piano_notes = [
    # Bar 3: Fm7 on 2
    (39, 3.375, 0.375),  # F
    (44, 3.375, 0.375),  # Ab
    (42, 3.375, 0.375),  # C
    (45, 3.375, 0.375),  # D
    # Bar 4: Fm7 on 2
    (39, 4.125, 0.375),  # F
    (44, 4.125, 0.375),  # Ab
    (42, 4.125, 0.375),  # C
    (45, 4.125, 0.375),  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 3: Sax continues motif
sax_notes = [
    (44, 3.0, 0.375),    # Ab
    (42, 3.375, 0.375),  # C
    (44, 3.75, 0.375),   # Ab
    (41, 4.125, 0.375),  # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 4: Drums continue with same pattern
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.125),    # Hihat on 1
    (38, 4.875, 0.125),  # Snare on 2
    (42, 4.875, 0.125),  # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.125),   # Hihat on 3
    (38, 5.625, 0.125),  # Snare on 4
    (42, 5.625, 0.125),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Bass continues walking line
bass_notes = [
    (40, 4.5, 0.375),    # G
    (41, 4.875, 0.375),  # Ab
    (39, 5.25, 0.375),   # F
    (40, 5.625, 0.375),  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Piano continues with 7th chords
piano_notes = [
    # Bar 4: Fm7 on 2
    (39, 4.875, 0.375),  # F
    (44, 4.875, 0.375),  # Ab
    (42, 4.875, 0.375),  # C
    (45, 4.875, 0.375),  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 4: Sax resolves motif
sax_notes = [
    (40, 4.5, 0.375),    # G
    (42, 4.875, 0.375),  # C
    (40, 5.25, 0.375),   # G
    (39, 5.625, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
