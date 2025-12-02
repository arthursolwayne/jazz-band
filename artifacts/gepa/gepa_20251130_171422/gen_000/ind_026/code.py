
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.1875),    # Hi-hat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hi-hat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hi-hat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.1875)   # Hi-hat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    (48, 1.5, 0.375),     # F
    (49, 1.875, 0.375),   # Gb
    (50, 2.25, 0.375),    # G
    (51, 2.625, 0.375),   # Ab
    (52, 3.0, 0.375),     # A
    (53, 3.375, 0.375),   # Bb
    (54, 3.75, 0.375),    # B
    (55, 4.125, 0.375),   # C
    (56, 4.5, 0.375),     # C#
    (57, 4.875, 0.375),   # D
    (58, 5.25, 0.375),    # D#
    (59, 5.625, 0.375)    # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 1
    (62, 1.5, 0.375),     # F
    (64, 1.5, 0.375),     # A
    (67, 1.5, 0.375),     # C
    (69, 1.5, 0.375),     # E
    # Bar 2: Bb7 on beat 3
    (67, 2.25, 0.375),    # Bb
    (69, 2.25, 0.375),    # D
    (71, 2.25, 0.375),    # F
    (74, 2.25, 0.375),    # Ab
    # Bar 3: F7 on beat 1
    (62, 3.0, 0.375),     # F
    (64, 3.0, 0.375),     # A
    (67, 3.0, 0.375),     # C
    (69, 3.0, 0.375),     # E
    # Bar 3: Bb7 on beat 3
    (67, 3.75, 0.375),    # Bb
    (69, 3.75, 0.375),    # D
    (71, 3.75, 0.375),    # F
    (74, 3.75, 0.375),    # Ab
    # Bar 4: F7 on beat 1
    (62, 4.5, 0.375),     # F
    (64, 4.5, 0.375),     # A
    (67, 4.5, 0.375),     # C
    (69, 4.5, 0.375),     # E
    # Bar 4: Bb7 on beat 3
    (67, 5.25, 0.375),    # Bb
    (69, 5.25, 0.375),    # D
    (71, 5.25, 0.375),    # F
    (74, 5.25, 0.375)     # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante on sax: short motif, start, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: F (62) on beat 1
    (62, 1.5, 0.375),
    # Bar 2: Ab (65) on beat 2
    (65, 1.875, 0.375),
    # Bar 2: F (62) on beat 3
    (62, 2.25, 0.375),
    # Bar 2: G (66) on beat 4
    (66, 2.625, 0.375),
    # Bar 3: F (62) on beat 1
    (62, 3.0, 0.375),
    # Bar 3: Ab (65) on beat 2
    (65, 3.375, 0.375),
    # Bar 3: Bb (67) on beat 3
    (67, 3.75, 0.375),
    # Bar 3: F (62) on beat 4
    (62, 4.125, 0.375),
    # Bar 4: F (62) on beat 1
    (62, 4.5, 0.375),
    # Bar 4: Ab (65) on beat 2
    (65, 4.875, 0.375),
    # Bar 4: G (66) on beat 3
    (66, 5.25, 0.375),
    # Bar 4: F (62) on beat 4
    (62, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.1875),    # Hi-hat on 1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.875, 0.1875),  # Hi-hat on 2
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.25, 0.1875),   # Hi-hat on 3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.625, 0.1875),  # Hi-hat on 4
    # Bar 3
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.1875),    # Hi-hat on 1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.375, 0.1875),  # Hi-hat on 2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.75, 0.1875),   # Hi-hat on 3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.125, 0.1875),  # Hi-hat on 4
    # Bar 4
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.1875),    # Hi-hat on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.1875),  # Hi-hat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.1875),   # Hi-hat on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.625, 0.1875)   # Hi-hat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("jazz_intro.mid")
