
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (36, 1.5, 0.375),  # F (root)
    (37, 1.875, 0.375), # F#
    (38, 2.25, 0.375),  # G
    (39, 2.625, 0.375), # G#
    (40, 3.0, 0.375),   # A
    (41, 3.375, 0.375), # A#
    (42, 3.75, 0.375),  # B
    (43, 4.125, 0.375), # C
    (45, 4.5, 0.375),   # D
    (46, 4.875, 0.375), # D#
    (48, 5.25, 0.375),  # E
    (49, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E♭)
    (53, 1.5, 0.375),  # F
    (58, 1.5, 0.375),  # A
    (60, 1.5, 0.375),  # C
    (62, 1.5, 0.375),  # E♭
    # Bar 3: B♭7 (B♭, D, F, A♭)
    (57, 2.625, 0.375), # B♭
    (62, 2.625, 0.375), # D
    (60, 2.625, 0.375), # F
    (65, 2.625, 0.375), # A♭
    # Bar 4: E7 (E, G#, B, D)
    (64, 3.75, 0.375),  # E
    (69, 3.75, 0.375),  # G#
    (71, 3.75, 0.375),  # B
    (67, 3.75, 0.375)   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4
    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375), # Hihat on 4
    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# You: Tenor sax - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),  # E (bar 2, beat 1)
    (64, 1.875, 0.375), # G (bar 2, beat 2)
    (66, 2.25, 0.375),  # A (bar 2, beat 3)
    (67, 2.625, 0.375), # B♭ (bar 2, beat 4)
    (66, 3.0, 0.375),   # A (bar 3, beat 1)
    (64, 3.375, 0.375), # G (bar 3, beat 2)
    (62, 3.75, 0.375),  # E (bar 3, beat 3)
    (60, 4.125, 0.375), # D (bar 3, beat 4)
    (62, 4.5, 0.375),   # E (bar 4, beat 1)
    (64, 4.875, 0.375), # G (bar 4, beat 2)
    (66, 5.25, 0.375),  # A (bar 4, beat 3)
    (67, 5.625, 0.375)  # B♭ (bar 4, beat 4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
