
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
    # Kick on 1 and 3
    (0.0, 36, 100),
    (0.75, 38, 100),
    (1.5, 36, 100),
    (2.25, 38, 100),
    # Hi-hat on every eighth
    (0.0, 42, 80),
    (0.375, 42, 80),
    (0.75, 42, 80),
    (1.125, 42, 80),
    (1.5, 42, 80),
    (1.875, 42, 80),
    (2.25, 42, 80),
    (2.625, 42, 80)
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Dm7 chord: D F A C
# Walking bass line in Dm
bass_notes = [
    (1.5, 50, 100),  # D
    (1.875, 48, 100), # Eb (chromatic)
    (2.25, 52, 100),  # F
    (2.625, 50, 100), # D
    (3.0, 48, 100),   # Eb
    (3.375, 52, 100), # F
    (3.75, 55, 100),  # G (chromatic)
    (4.125, 52, 100), # F
    (4.5, 50, 100),   # D
    (4.875, 48, 100), # Eb
    (5.25, 52, 100),  # F
    (5.625, 50, 100)  # D
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Diane: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Comp on 2 and 4 of each bar
piano_notes = [
    (2.25, 50, 100),  # D
    (2.25, 57, 100),  # F
    (2.25, 65, 100),  # A
    (2.25, 69, 100),  # C
    (3.75, 50, 100),  # D
    (3.75, 57, 100),  # F
    (3.75, 65, 100),  # A
    (3.75, 69, 100),  # C
    (5.25, 50, 100),  # D
    (5.25, 57, 100),  # F
    (5.25, 65, 100),  # A
    (5.25, 69, 100)   # C
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2-4 (1.5-6.0s)
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick_start = bar_start
    snare_start = bar_start + 0.75
    # Hi-hat on every eighth
    for i in range(0, 4):
        hihat_start = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(80, 42, hihat_start, hihat_start + 0.375))
    drums.notes.append(pretty_midi.Note(100, 36, kick_start, kick_start + 0.375))
    drums.notes.append(pretty_midi.Note(100, 38, snare_start, snare_start + 0.375))

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm melody: D F A C
sax_notes = [
    (1.5, 50, 100),    # D
    (1.75, 57, 100),   # F
    (2.0, 59, 100),    # A
    (2.25, 62, 100),   # C
    (2.625, 50, 100),  # D
    (2.875, 57, 100),  # F
    (3.125, 59, 100),  # A
    (3.375, 62, 100),  # C
    (3.75, 55, 100),   # G (chromatic)
    (4.125, 50, 100),  # D
    (4.5, 57, 100),    # F
    (4.875, 59, 100),  # A
    (5.25, 62, 100)    # C
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.dump()
