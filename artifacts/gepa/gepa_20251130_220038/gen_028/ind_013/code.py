
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.125),  # Hihat on 1
    (42, 0.125, 0.125),  # Hihat on &
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.125),  # Hihat on 2
    (42, 0.5, 0.125),   # Hihat on &
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.125),  # Hihat on 3
    (42, 0.875, 0.125), # Hihat on &
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.125), # Hihat on 4
    (42, 1.25, 0.125),  # Hihat on &
    (42, 1.375, 0.125), # Hihat on &
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    (12, 1.5, 0.375),  # F
    (10, 1.875, 0.375), # Eb
    (9, 2.25, 0.375),   # D
    (11, 2.625, 0.375), # E
    # Bar 3
    (12, 3.0, 0.375),   # F
    (10, 3.375, 0.375), # Eb
    (9, 3.75, 0.375),   # D
    (11, 4.125, 0.375), # E
    # Bar 4
    (12, 4.5, 0.375),   # F
    (10, 4.875, 0.375), # Eb
    (9, 5.25, 0.375),   # D
    (11, 5.625, 0.375), # E
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
# Bar 2: Fm7 on 1 and 2
piano_notes = []
# Bar 2
piano_notes.extend([
    (60, 1.5, 0.375),  # F
    (64, 1.5, 0.375),  # A
    (62, 1.5, 0.375),  # G
    (65, 1.5, 0.375),  # Bb
    (60, 1.875, 0.375), # F
    (64, 1.875, 0.375), # A
    (62, 1.875, 0.375), # G
    (65, 1.875, 0.375), # Bb
])
# Bar 3: Eb7 on 3 and 4
piano_notes.extend([
    (61, 2.25, 0.375),  # Eb
    (65, 2.25, 0.375),  # Bb
    (63, 2.25, 0.375),  # G
    (67, 2.25, 0.375),  # D
    (61, 2.625, 0.375), # Eb
    (65, 2.625, 0.375), # Bb
    (63, 2.625, 0.375), # G
    (67, 2.625, 0.375), # D
])
# Bar 4: Fm7 on 1 and 2
piano_notes.extend([
    (60, 3.0, 0.375),  # F
    (64, 3.0, 0.375),  # A
    (62, 3.0, 0.375),  # G
    (65, 3.0, 0.375),  # Bb
    (60, 3.375, 0.375), # F
    (64, 3.375, 0.375), # A
    (62, 3.375, 0.375), # G
    (65, 3.375, 0.375), # Bb
])

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Your motif (start on bar 2)
# Motif: F (60), G (62), Eb (61), D (60)
# Whispered, then cry
sax_notes = [
    (60, 1.5, 0.375),   # F (whisper)
    (62, 1.875, 0.375), # G (build)
    (61, 2.25, 0.375),  # Eb (cry)
    (60, 2.625, 0.375), # D (resolve)
    (60, 3.0, 0.375),   # F (reprise)
    (62, 3.375, 0.375), # G (build)
    (61, 3.75, 0.375),  # Eb (cry)
    (60, 4.125, 0.375), # D (resolve)
    (60, 4.5, 0.375),   # F (reprise)
    (62, 4.875, 0.375), # G (build)
    (61, 5.25, 0.375),  # Eb (cry)
    (60, 5.625, 0.375), # D (resolve)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add drum fills for bar 3 and 4
# Bar 3: Little fill on 3
drum_fill_bar3 = [
    (36, 2.25, 0.375),  # Kick
    (38, 2.625, 0.375), # Snare
    (42, 2.25, 0.125),  # Hihat on 3
    (42, 2.375, 0.125), # Hihat
    (42, 2.5, 0.125),   # Hihat
    (42, 2.625, 0.125), # Hihat
    (42, 2.75, 0.125),  # Hihat
    (42, 2.875, 0.125), # Hihat
]

for note, start, duration in drum_fill_bar3:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Little fill on 4
drum_fill_bar4 = [
    (36, 4.5, 0.375),   # Kick
    (38, 4.875, 0.375), # Snare
    (42, 4.5, 0.125),   # Hihat on 4
    (42, 4.625, 0.125), # Hihat
    (42, 4.75, 0.125),  # Hihat
    (42, 4.875, 0.125), # Hihat
    (42, 5.0, 0.125),   # Hihat
    (42, 5.125, 0.125), # Hihat
]

for note, start, duration in drum_fill_bar4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
