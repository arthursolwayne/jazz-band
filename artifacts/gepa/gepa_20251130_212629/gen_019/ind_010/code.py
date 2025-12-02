
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
    (42, 0.125, 0.125),  # Hihat on 2
    (38, 0.125, 0.375),  # Snare on 2
    (42, 0.25, 0.125),  # Hihat on 3
    (36, 0.375, 0.375),  # Kick on 3
    (42, 0.375, 0.125),  # Hihat on 3
    (42, 0.5, 0.125),  # Hihat on 4
    (38, 0.5, 0.375),  # Snare on 4
    (42, 0.625, 0.125),  # Hihat on 4
    (42, 0.75, 0.125)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full ensemble enters
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5, 0.375),  # Fm root
    (41, 1.875, 0.375),  # Bb
    (40, 2.25, 0.375),  # Ab
    (38, 2.625, 0.375),  # G
    (39, 3.0, 0.375),  # F
    (41, 3.375, 0.375),  # Bb
    (40, 3.75, 0.375),  # Ab
    (38, 4.125, 0.375)   # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, D)
    (53, 1.5, 0.125),  # F
    (60, 1.5, 0.125),  # Ab
    (62, 1.5, 0.125),  # Bb
    (58, 1.5, 0.125),  # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (62, 3.0, 0.125),  # Bb
    (65, 3.0, 0.125),  # D
    (53, 3.0, 0.125),  # F
    (60, 3.0, 0.125),  # Ab
    # Bar 4: Fm7 (F, Ab, Bb, D)
    (53, 4.5, 0.125),  # F
    (60, 4.5, 0.125),  # Ab
    (62, 4.5, 0.125),  # Bb
    (58, 4.5, 0.125)   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Simple motif starting on F
# F -> G -> Ab -> rest
sax_notes = [
    (53, 1.5, 0.125),  # F
    (55, 1.625, 0.125),  # G
    (60, 1.75, 0.125),  # Ab
    (53, 1.875, 0.125)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Drums continue
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.125),  # Hihat on 1
    (42, 3.125, 0.125),  # Hihat on 2
    (38, 3.125, 0.375),  # Snare on 2
    (42, 3.25, 0.125),  # Hihat on 3
    (36, 3.375, 0.375),  # Kick on 3
    (42, 3.375, 0.125),  # Hihat on 3
    (42, 3.5, 0.125),  # Hihat on 4
    (38, 3.5, 0.375),  # Snare on 4
    (42, 3.625, 0.125),  # Hihat on 4
    (42, 3.75, 0.125)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Drums continue
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.125),  # Hihat on 1
    (42, 4.625, 0.125),  # Hihat on 2
    (38, 4.625, 0.375),  # Snare on 2
    (42, 4.75, 0.125),  # Hihat on 3
    (36, 4.875, 0.375),  # Kick on 3
    (42, 4.875, 0.125),  # Hihat on 3
    (42, 5.0, 0.125),  # Hihat on 4
    (38, 5.0, 0.375),  # Snare on 4
    (42, 5.125, 0.125),  # Hihat on 4
    (42, 5.25, 0.125)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
