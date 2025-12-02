
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.375, 0.125), # Hihat on &1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.875, 0.125), # Hihat on &2
    (36, 1.125, 0.375), # Kick on 3
    (42, 1.5, 0.125)    # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5, 0.375),   # Fm root (F)
    (40, 1.875, 0.375),  # Bb
    (41, 2.25, 0.375),   # Eb
    (42, 2.625, 0.375),  # Ab
    (43, 3.0, 0.375),    # Db
    (44, 3.375, 0.375),  # G
    (45, 3.75, 0.375),   # C
    (46, 4.125, 0.375),  # F
    (47, 4.5, 0.375),    # Bb
    (48, 4.875, 0.375),  # Eb
    (49, 5.25, 0.375),   # Ab
    (50, 5.625, 0.375)   # Db
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (40, 2.0, 0.375),    # Bb7 (Bb, D, F, Ab)
    (45, 2.0, 0.375),
    (46, 2.0, 0.375),
    (42, 2.0, 0.375),
    # Bar 3
    (40, 3.5, 0.375),    # Bb7
    (45, 3.5, 0.375),
    (46, 3.5, 0.375),
    (42, 3.5, 0.375),
    # Bar 4
    (40, 5.0, 0.375),    # Bb7
    (45, 5.0, 0.375),
    (46, 5.0, 0.375),
    (42, 5.0, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Whisper at first, cry later
# Bar 2: Motif starts
sax_notes = [
    (43, 2.0, 0.375),    # Db
    (45, 2.375, 0.375),  # F
    (42, 2.75, 0.375),   # Ab
    (43, 3.125, 0.375),  # Db
    (45, 3.5, 0.375),    # F
    (42, 3.875, 0.375),  # Ab
    (43, 4.25, 0.375),   # Db
    (46, 4.625, 0.375),  # G (higher)
    (47, 4.625, 0.375),  # Ab (staccato)
    (43, 5.0, 0.375),    # Db
    (45, 5.375, 0.375),  # F
    (47, 5.75, 0.375)    # Ab (higher)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.5, end=start + 1.875))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 2.25, end=start + 2.625))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
