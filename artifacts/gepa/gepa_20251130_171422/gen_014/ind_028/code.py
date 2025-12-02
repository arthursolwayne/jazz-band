
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
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice. He's the anchor.
bass_notes = [
    # Bar 2
    (1.5, 62, 100), # D
    (1.875, 61, 100), # C#
    (2.25, 63, 100), # D#
    (2.625, 62, 100), # D
    # Bar 3
    (3.0, 65, 100), # F#
    (3.375, 64, 100), # F
    (3.75, 66, 100), # G
    (4.125, 65, 100), # F#
    # Bar 4
    (4.5, 62, 100), # D
    (4.875, 61, 100), # C#
    (5.25, 63, 100), # D#
    (5.625, 62, 100)  # D
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Diane: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    # Bar 2
    (1.5, 62, 100), # D7: D, F#, A, C
    (1.5, 67, 100),
    (1.5, 71, 100),
    (1.5, 64, 100),
    (1.875, 62, 100),
    (1.875, 67, 100),
    (1.875, 71, 100),
    (1.875, 64, 100),
    # Bar 3
    (3.0, 62, 100), # D7 again
    (3.0, 67, 100),
    (3.0, 71, 100),
    (3.0, 64, 100),
    (3.375, 62, 100),
    (3.375, 67, 100),
    (3.375, 71, 100),
    (3.375, 64, 100),
    # Bar 4
    (4.5, 62, 100), # D7 again
    (4.5, 67, 100),
    (4.5, 71, 100),
    (4.5, 64, 100),
    (4.875, 62, 100),
    (4.875, 67, 100),
    (4.875, 71, 100),
    (4.875, 64, 100)
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# You: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs — that's student shit.
sax_notes = [
    (1.5, 67, 100), # E
    (1.875, 69, 100), # G
    (2.25, 67, 100), # E
    (2.625, 69, 100), # G
    (3.0, 67, 100), # E
    (3.375, 69, 100), # G
    (3.75, 67, 100), # E
    (4.125, 69, 100), # G
    (4.5, 67, 100), # E
    (4.875, 69, 100), # G
    (5.25, 67, 100), # E
    (5.625, 69, 100)  # G
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (1.5, 36, 100),  # Kick on beat 1
    (2.0, 38, 100),  # Snare on beat 2
    (2.5, 36, 100),  # Kick on beat 3
    (3.0, 38, 100),  # Snare on beat 4
    # Bar 3
    (3.5, 36, 100),  # Kick on beat 1
    (4.0, 38, 100),  # Snare on beat 2
    (4.5, 36, 100),  # Kick on beat 3
    (5.0, 38, 100),  # Snare on beat 4
    # Bar 4
    (5.5, 36, 100),  # Kick on beat 1
    (6.0, 38, 100),  # Snare on beat 2
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.375))

# Add hihat every eighth note
for start in [1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75, 6.0]:
    if start < 6.0:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
