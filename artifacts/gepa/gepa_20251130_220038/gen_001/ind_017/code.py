
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
    (1.25, 42, 100),  # Hihat on 4
    (1.5, 38, 100)    # Snare on 3
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice. He's the anchor.
# Fm bass line: F, Eb, D, C, Bb, A, G, Ab, F
bass_notes = [
    (1.5, 70, 100),   # F
    (1.875, 69, 100), # Eb
    (2.25, 68, 100),  # D
    (2.625, 67, 100), # C
    (3.0, 65, 100),   # Bb
    (3.375, 66, 100), # A
    (3.75, 67, 100),  # G
    (4.125, 68, 100), # Ab
    (4.5, 70, 100),   # F
    (4.875, 69, 100), # Eb
    (5.25, 68, 100),  # D
    (5.625, 67, 100)  # C
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Diane: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
# Fm7, Bbm7, Eb7, Ab7
piano_notes = [
    # Bar 2 (1.5 - 2.25)
    (1.5, 64, 100),   # F
    (1.5, 62, 100),   # Ab
    (1.5, 60, 100),   # C
    (1.5, 59, 100),   # Eb
    # Bar 3 (2.25 - 3.0)
    (2.25, 57, 100),  # Bb
    (2.25, 55, 100),  # Db
    (2.25, 53, 100),  # F
    (2.25, 52, 100),  # Ab
    # Bar 4 (3.0 - 3.75)
    (3.0, 60, 100),   # Eb
    (3.0, 58, 100),   # B
    (3.0, 56, 100),   # D
    (3.0, 55, 100),   # F
    # Bar 4 (4.125 - 4.875)
    (4.125, 64, 100), # F
    (4.125, 62, 100), # Ab
    (4.125, 60, 100), # C
    (4.125, 59, 100)  # Eb
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
drum_notes = [
    # Bar 2 (1.5 - 2.25)
    (1.5, 36, 100),   # Kick on 1
    (1.875, 42, 100), # Hihat on 2
    (2.25, 38, 100),  # Snare on 3
    (2.625, 42, 100), # Hihat on 4
    # Bar 3 (2.25 - 3.0)
    (2.25, 36, 100),  # Kick on 1
    (2.625, 42, 100), # Hihat on 2
    (3.0, 38, 100),   # Snare on 3
    (3.375, 42, 100), # Hihat on 4
    # Bar 4 (3.0 - 3.75)
    (3.0, 36, 100),   # Kick on 1
    (3.375, 42, 100), # Hihat on 2
    (3.75, 38, 100),  # Snare on 3
    (4.125, 42, 100), # Hihat on 4
    # Bar 4 (4.5 - 5.25)
    (4.5, 36, 100),   # Kick on 1
    (4.875, 42, 100), # Hihat on 2
    (5.25, 38, 100),  # Snare on 3
    (5.625, 42, 100)  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

# Dante: This is your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs — that's student shit.

sax_notes = [
    (1.5, 67, 100),   # G (Fm7)
    (1.875, 65, 100), # Bb
    (2.25, 67, 100),  # G (Eb7)
    (2.625, 69, 100), # B
    (3.0, 67, 100),   # G (Ab7)
    (3.375, 71, 100), # D
    (3.75, 69, 100),  # B (Fm7)
    (4.125, 67, 100), # G (Bbm7)
    (4.5, 65, 100),   # Bb (Eb7)
    (4.875, 67, 100), # G (Ab7)
    (5.25, 69, 100),  # B (Fm7)
    (5.625, 67, 100)  # G (ending on G)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.save('jazz_intro.mid')
