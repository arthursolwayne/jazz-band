
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.125, 0.25),   # Hihat on &1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.5, 0.25),     # Hihat on &2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.875, 0.25),   # Hihat on &3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.25, 0.25),    # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm
bass_notes = [
    (43, 1.5, 0.375),    # D
    (41, 1.875, 0.375),  # Bb
    (44, 2.25, 0.375),   # Eb
    (45, 2.625, 0.375),  # F
    (43, 3.0, 0.375),    # D
    (41, 3.375, 0.375),  # Bb
    (44, 3.75, 0.375),   # Eb
    (45, 4.125, 0.375),  # F
    (43, 4.5, 0.375),    # D
    (41, 4.875, 0.375),  # Bb
    (44, 5.25, 0.375),   # Eb
    (45, 5.625, 0.375)   # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (42, 1.5, 0.25),  # Ab7 (Ab, C, Db, F)
    (45, 1.5, 0.25),
    (44, 1.5, 0.25),
    (47, 1.5, 0.25),
    (42, 1.875, 0.25),  # Ab7 again on 2
    (45, 1.875, 0.25),
    (44, 1.875, 0.25),
    (47, 1.875, 0.25),
    # Bar 3
    (42, 2.25, 0.25),  # Ab7
    (45, 2.25, 0.25),
    (44, 2.25, 0.25),
    (47, 2.25, 0.25),
    (42, 2.625, 0.25),  # Ab7 on 2
    (45, 2.625, 0.25),
    (44, 2.625, 0.25),
    (47, 2.625, 0.25),
    # Bar 4
    (42, 3.0, 0.25),   # Ab7
    (45, 3.0, 0.25),
    (44, 3.0, 0.25),
    (47, 3.0, 0.25),
    (42, 3.375, 0.25),  # Ab7 on 2
    (45, 3.375, 0.25),
    (44, 3.375, 0.25),
    (47, 3.375, 0.25),
    (42, 3.75, 0.25),  # Ab7
    (45, 3.75, 0.25),
    (44, 3.75, 0.25),
    (47, 3.75, 0.25),
    (42, 4.125, 0.25),  # Ab7 on 2
    (45, 4.125, 0.25),
    (44, 4.125, 0.25),
    (47, 4.125, 0.25),
    (42, 4.5, 0.25),   # Ab7
    (45, 4.5, 0.25),
    (44, 4.5, 0.25),
    (47, 4.5, 0.25),
    (42, 4.875, 0.25),  # Ab7 on 2
    (45, 4.875, 0.25),
    (44, 4.875, 0.25),
    (47, 4.875, 0.25)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Motif in Fm
# Start on F, then Ab, then Eb, then F again — a question in the air
sax_notes = [
    (45, 1.5, 0.375),  # F
    (42, 1.875, 0.375), # Ab
    (44, 2.25, 0.375),  # Eb
    (45, 2.625, 0.375), # F
    (45, 3.0, 0.375),   # F (return)
    (42, 3.375, 0.375), # Ab
    (44, 3.75, 0.375),  # Eb
    (45, 4.125, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),    # Kick on 1
    (38, 1.875, 0.375),  # Snare on 2
    (36, 2.25, 0.375),   # Kick on 3
    (38, 2.625, 0.375),  # Snare on 4
    # Bar 3
    (36, 3.0, 0.375),    # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (36, 3.75, 0.375),   # Kick on 3
    (38, 4.125, 0.375),  # Snare on 4
    # Bar 4
    (36, 4.5, 0.375),    # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (36, 5.25, 0.375),   # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add hi-hats on every eighth note for all bars 2-4
for bar in range(2, 5):
    for eighth in range(0, 8):
        start = 1.5 + (bar - 2) * 1.5 + eighth * 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
