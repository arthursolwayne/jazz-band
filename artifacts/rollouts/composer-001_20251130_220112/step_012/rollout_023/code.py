
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
    (0.0, 36, 100),   # Kick on 1
    (0.75, 42, 100),  # Hihat on 2
    (1.125, 42, 100), # Hihat on 3
    (1.5, 38, 100)    # Snare on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 48, 100),   # F (1)
    (1.875, 49, 100),  # Gb (2)
    (2.25, 50, 100),   # G (3)
    (2.625, 51, 100),  # Ab (4)
    (3.0, 53, 100),    # Bb (1)
    (3.375, 55, 100),  # B (2)
    (3.75, 57, 100),   # C (3)
    (4.125, 59, 100),  # C# (4)
    (4.5, 60, 100),    # D (1)
    (4.875, 62, 100),  # Eb (2)
    (5.25, 64, 100),   # E (3)
    (5.625, 65, 100)   # F (4)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 64, 100),  # D7: D (64)
    (1.875, 71, 100),  # B (71)
    (1.875, 76, 100),  # F (76)
    (1.875, 79, 100),  # A (79)
    # Bar 3
    (3.375, 65, 100),  # E7: E (65)
    (3.375, 72, 100),  # C (72)
    (3.375, 76, 100),  # F (76)
    (3.375, 81, 100),  # G (81)
    # Bar 4
    (4.875, 67, 100),  # G7: G (67)
    (4.875, 74, 100),  # D (74)
    (4.875, 76, 100),  # F (76)
    (4.875, 81, 100),  # B (81)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Drums: Bars 2-4
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(100, 36, start_time, start_time + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(100, 38, start_time + 1.125, start_time + 1.5))
    # Hihat on every eighth
    for i in range(0, 4):
        time = start_time + i * 0.375
        drums.notes.append(pretty_midi.Note(100, 42, time, time + 0.1875))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F, Bb, G, Ab (bars 2-3), then resolve on F (bar 4)
sax_notes = [
    (1.5, 84, 100),   # F (bar 2, beat 1)
    (1.875, 88, 100),  # Bb (bar 2, beat 2)
    (2.25, 87, 100),   # G (bar 2, beat 3)
    (2.625, 89, 100),  # Ab (bar 2, beat 4)
    (3.0, 84, 100),    # F (bar 3, beat 1)
    (3.375, 88, 100),  # Bb (bar 3, beat 2)
    (3.75, 87, 100),   # G (bar 3, beat 3)
    (4.125, 89, 100),  # Ab (bar 3, beat 4)
    (4.5, 84, 100),    # F (bar 4, beat 1)
    (4.875, 88, 100),  # Bb (bar 4, beat 2)
    (5.25, 87, 100),   # G (bar 4, beat 3)
    (5.625, 84, 100)   # F (bar 4, beat 4)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
