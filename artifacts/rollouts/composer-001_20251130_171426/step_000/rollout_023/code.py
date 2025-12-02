
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
drum_notes = [
    (36, 0.0, 1.0),     # kick on beat 1
    (38, 0.5, 1.0),     # snare on beat 2
    (42, 0.0, 1.0),     # hihat on beat 1
    (42, 0.5, 1.0),     # hihat on beat 2
    (42, 1.0, 1.0),     # hihat on beat 3
    (42, 1.5, 1.0),     # hihat on beat 4
    (36, 1.0, 1.0),     # kick on beat 3
    (38, 1.5, 1.0)      # snare on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approaches
bass_notes = [
    (44, 1.5, 0.375),  # F
    (45, 1.875, 0.375), # F#
    (46, 2.25, 0.375),  # G
    (47, 2.625, 0.375), # G#
    (48, 3.0, 0.375),   # A
    (49, 3.375, 0.375), # A#
    (50, 3.75, 0.375),  # Bb
    (51, 4.125, 0.375), # B
    (52, 4.5, 0.375),   # B
    (53, 4.875, 0.375), # C
    (54, 5.25, 0.375),  # C#
    (55, 5.625, 0.375)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    (50, 1.875, 0.375),  # Bb7
    (53, 1.875, 0.375),
    (55, 1.875, 0.375),
    (60, 1.875, 0.375),
    (50, 3.375, 0.375),  # Bb7
    (53, 3.375, 0.375),
    (55, 3.375, 0.375),
    (60, 3.375, 0.375),
    (52, 4.875, 0.375),  # D7
    (55, 4.875, 0.375),
    (57, 4.875, 0.375),
    (62, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375),    # kick on 1
    (38, 2.0, 0.375),    # snare on 2
    (42, 1.5, 0.375),    # hihat on 1
    (42, 2.0, 0.375),    # hihat on 2
    (42, 2.5, 0.375),    # hihat on 3
    (42, 3.0, 0.375),    # hihat on 4
    (36, 2.5, 0.375),    # kick on 3
    (38, 3.0, 0.375),    # snare on 4
    (36, 3.5, 0.375),    # kick on 1
    (38, 4.0, 0.375),    # snare on 2
    (42, 3.5, 0.375),    # hihat on 1
    (42, 4.0, 0.375),    # hihat on 2
    (42, 4.5, 0.375),    # hihat on 3
    (42, 5.0, 0.375),    # hihat on 4
    (36, 4.5, 0.375),    # kick on 3
    (38, 5.0, 0.375)     # snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax melody - one short motif, make it sing
sax_notes = [
    (62, 1.5, 0.4),     # F
    (65, 1.9, 0.4),     # A
    (66, 2.3, 0.4),     # Bb
    (62, 2.7, 0.4),     # F
    (65, 3.1, 0.4),     # A
    (66, 3.5, 0.4),     # Bb
    (69, 3.9, 0.4),     # D
    (66, 4.3, 0.4),     # Bb
    (62, 4.7, 0.4),     # F
    (65, 5.1, 0.4),     # A
    (66, 5.5, 0.4),     # Bb
    (69, 5.9, 0.4)      # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_russo_intro.mid')
