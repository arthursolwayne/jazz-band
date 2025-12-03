
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 1.0),   # Kick on 1
    (38, 0.5, 1.0),   # Snare on 2
    (36, 1.0, 1.0),   # Kick on 3
    (38, 1.5, 1.0),   # Snare on 4
    (42, 0.0, 1.0),   # Hihat on 1
    (42, 0.25, 1.0),  # Hihat on 2
    (42, 0.5, 1.0),   # Hihat on 3
    (42, 0.75, 1.0),  # Hihat on 4
    (42, 1.0, 1.0),   # Hihat on 5
    (42, 1.25, 1.0),  # Hihat on 6
    (42, 1.5, 1.0),   # Hihat on 7
    (42, 1.75, 1.0)   # Hihat on 8
]

for note, start, duration in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - roots and fifths with chromatic approaches (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 1.5, 0.5),   # D2
    (39, 2.0, 0.5),   # Eb2 (chromatic approach)
    (40, 2.5, 0.5),   # E2
    (43, 3.0, 0.5),   # G2
    (43, 3.5, 0.5),   # G2
    (42, 4.0, 0.5),   # F2 (chromatic approach)
    (43, 4.5, 0.5),   # G2
    (38, 5.0, 0.5),   # D2
]

for note, start, duration in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano - open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (50, 1.5, 0.5),   # D
    (53, 1.5, 0.5),   # F
    (57, 1.5, 0.5),   # A
    (60, 1.5, 0.5),   # C

    # Bar 3: G7 (G, B, D, F)
    (55, 2.5, 0.5),   # G
    (59, 2.5, 0.5),   # B
    (62, 2.5, 0.5),   # D
    (65, 2.5, 0.5),   # F

    # Bar 4: Bm7 (B, D, F#, A)
    (59, 3.5, 0.5),   # B
    (62, 3.5, 0.5),   # D
    (67, 3.5, 0.5),   # F#
    (67, 4.5, 0.5),   # A (resolve on last beat)
]

for note, start, duration in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax - one short motif, haunting and incomplete
# Start at 1.5s, introduce a short, unresolved melody
sax_notes = [
    (62, 1.5, 0.375),  # E4 (start of motif)
    (65, 2.0, 0.375),  # G4
    (62, 2.5, 0.375),  # E4
    (60, 3.0, 0.375),  # D4
    (58, 3.5, 0.375),  # B3
    (57, 4.0, 0.375),  # A3
    (60, 4.5, 0.375),  # D4
    (62, 5.0, 0.375),  # E4 (end of motif)
]

for note, start, duration in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Add drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 1.0),   # Kick on 1
    (38, 2.0, 1.0),   # Snare on 2
    (36, 2.5, 1.0),   # Kick on 3
    (38, 3.0, 1.0),   # Snare on 4
    (42, 1.5, 1.0),   # Hihat on 1
    (42, 1.75, 1.0),  # Hihat on 2
    (42, 2.0, 1.0),   # Hihat on 3
    (42, 2.25, 1.0),  # Hihat on 4
    (42, 2.5, 1.0),   # Hihat on 5
    (42, 2.75, 1.0),  # Hihat on 6
    (42, 3.0, 1.0),   # Hihat on 7
    (42, 3.25, 1.0),  # Hihat on 8

    # Bar 3
    (36, 3.5, 1.0),   # Kick on 1
    (38, 4.0, 1.0),   # Snare on 2
    (36, 4.5, 1.0),   # Kick on 3
    (38, 5.0, 1.0),   # Snare on 4
    (42, 3.5, 1.0),   # Hihat on 1
    (42, 3.75, 1.0),  # Hihat on 2
    (42, 4.0, 1.0),   # Hihat on 3
    (42, 4.25, 1.0),  # Hihat on 4
    (42, 4.5, 1.0),   # Hihat on 5
    (42, 4.75, 1.0),  # Hihat on 6
    (42, 5.0, 1.0),   # Hihat on 7
    (42, 5.25, 1.0),  # Hihat on 8

    # Bar 4
    (36, 5.5, 1.0),   # Kick on 1
    (38, 6.0, 1.0),   # Snare on 2
    (36, 6.5, 1.0),   # Kick on 3
    (38, 7.0, 1.0),   # Snare on 4
    (42, 5.5, 1.0),   # Hihat on 1
    (42, 5.75, 1.0),  # Hihat on 2
    (42, 6.0, 1.0),   # Hihat on 3
    (42, 6.25, 1.0),  # Hihat on 4
    (42, 6.5, 1.0),   # Hihat on 5
    (42, 6.75, 1.0),  # Hihat on 6
    (42, 7.0, 1.0),   # Hihat on 7
    (42, 7.25, 1.0)   # Hihat on 8
]

for note, start, duration in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
