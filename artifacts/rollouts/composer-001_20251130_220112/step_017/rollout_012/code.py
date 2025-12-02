
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on & of 1
    (1.0, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on & of 2
    (2.0, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.75, 42, 100)  # Hihat on & of 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    (1.5, 45, 100),  # F
    (1.75, 46, 100), # F#
    (2.0, 44, 100),  # E
    (2.25, 45, 100), # F
    (2.5, 47, 100),  # G
    (2.75, 48, 100), # G#
    (3.0, 47, 100),  # G
    (3.25, 45, 100), # F
    (3.5, 46, 100),  # F#
    (3.75, 48, 100), # G#
    (4.0, 47, 100),  # G
    (4.25, 45, 100), # F
    (4.5, 46, 100),  # F#
    (4.75, 48, 100), # G#
    (5.0, 47, 100),  # G
    (5.25, 45, 100), # F
    (5.5, 46, 100),  # F#
    (5.75, 48, 100)  # G#
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 46, 100),  # F7 - F
    (1.5, 50, 100),  # F7 - Bb
    (1.5, 53, 100),  # F7 - E
    (1.5, 57, 100),  # F7 - A
    (2.0, 46, 100),  # F7 - F
    (2.0, 50, 100),  # F7 - Bb
    (2.0, 53, 100),  # F7 - E
    (2.0, 57, 100),  # F7 - A
    # Bar 3
    (3.0, 46, 100),  # F7 - F
    (3.0, 50, 100),  # F7 - Bb
    (3.0, 53, 100),  # F7 - E
    (3.0, 57, 100),  # F7 - A
    (3.5, 46, 100),  # F7 - F
    (3.5, 50, 100),  # F7 - Bb
    (3.5, 53, 100),  # F7 - E
    (3.5, 57, 100),  # F7 - A
    # Bar 4
    (4.5, 46, 100),  # F7 - F
    (4.5, 50, 100),  # F7 - Bb
    (4.5, 53, 100),  # F7 - E
    (4.5, 57, 100),  # F7 - A
    (5.0, 46, 100),  # F7 - F
    (5.0, 50, 100),  # F7 - Bb
    (5.0, 53, 100),  # F7 - E
    (5.0, 57, 100),  # F7 - A
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 36, 100),  # Kick on 1
    (1.75, 42, 100), # Hihat on &
    (2.0, 38, 100),  # Snare on 2
    (2.25, 42, 100), # Hihat on &
    (2.5, 36, 100),  # Kick on 3
    (2.75, 42, 100), # Hihat on &
    (3.0, 38, 100),  # Snare on 4
    (3.25, 42, 100), # Hihat on &
    # Bar 3 (3.0 - 4.5s)
    (3.5, 36, 100),  # Kick on 1
    (3.75, 42, 100), # Hihat on &
    (4.0, 38, 100),  # Snare on 2
    (4.25, 42, 100), # Hihat on &
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 100), # Hihat on &
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 100), # Hihat on &
    # Bar 4 (4.5 - 6.0s)
    (5.5, 36, 100),  # Kick on 1
    (5.75, 42, 100), # Hihat on &
    (6.0, 38, 100),  # Snare on 2
    (6.25, 42, 100), # Hihat on &
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (G), G (A), A (Bb), F (G) — played in 4 bars
sax_notes = [
    # Bar 2 (1.5s)
    (1.5, 65, 100),  # F (G)
    (1.75, 67, 100), # G (A)
    (2.0, 69, 100),  # A (Bb)
    (2.25, 65, 100), # F (G)
    # Bar 3 (3.0s)
    (3.0, 65, 100),  # F (G)
    (3.25, 67, 100), # G (A)
    (3.5, 69, 100),  # A (Bb)
    (3.75, 65, 100), # F (G)
    # Bar 4 (4.5s)
    (4.5, 65, 100),  # F (G)
    (4.75, 67, 100), # G (A)
    (5.0, 69, 100),  # A (Bb)
    (5.25, 65, 100), # F (G)
    # Final note to wrap it up
    (5.5, 65, 100),  # F (G)
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
