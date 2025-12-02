
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches, never the same note twice
# F bass line: F, G, Ab, A, Bb, B, C, Db
for bar in range(2, 5):
    start = bar * 1.5
    # Walking bass notes (quarter notes)
    notes = [77, 79, 80, 81, 82, 83, 84, 85]
    for i, pitch in enumerate(notes):
        duration = 0.375
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + duration)
        bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# F7 = F, A, C, Eb
for bar in range(2, 5):
    start = bar * 1.5
    # Chord on beat 2 and 4
    for i in [1, 3]:
        chord_start = start + i * 0.375
        # F7
        for pitch in [77, 82, 84, 87]:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=chord_start, end=chord_start + 0.375)
            piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Dante: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F, Bb, Eb, F (bar 2), then repeat (bar 3), then G, Bb, F (bar 4)
note_lengths = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
note_pitches = [77, 82, 87, 77, 77, 82, 87, 84]

for bar in range(2, 5):
    start = bar * 1.5
    for i, pitch in enumerate(note_pitches):
        duration = note_lengths[i]
        note = pretty_midi.Note(velocity=110, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + duration)
        sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
