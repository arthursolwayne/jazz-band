
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
    time = bar * 1.5
    # Kick on beat 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    drums.notes.append(kick)
    # Snare on beat 2
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.75, end=time + 0.75 + 0.375)
    drums.notes.append(snare)
    # Kick on beat 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time + 1.125, end=time + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on beat 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=time + 1.5, end=time + 1.5 + 0.375)
    drums.notes.append(snare)

    # Hi-hats on every eighth note
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=time + (i * 0.375), end=time + (i * 0.375) + 0.1875)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
for bar in range(2, 5):
    time = bar * 1.5
    # Dm7 walking bass line: D - F - G - Bb - D - F - G - Bb
    notes = [62, 64, 67, 69, 62, 64, 67, 69]
    for i, pitch in enumerate(notes):
        start = time + (i * 0.375)
        end = start + 0.375
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    time = bar * 1.5
    # Dm7 = D - F - A - C
    # Comp on 2 and 4
    for i in [1, 3]:
        chord_start = time + (i * 0.375)
        # Dm7
        for pitch in [62, 64, 67, 71]:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=chord_start, end=chord_start + 0.375)
            piano.notes.append(note)

# Sax: your motif. Start it, leave it hanging, come back and finish it.
# Dm scale: D - Eb - F - G - A - Bb - C - D
# Motif: D - F - Eb - G (sings)
# Repeat with variation: D - Eb - G - C (finishes)

# Bar 2: Start the motif
time = 2 * 1.5
notes = [62, 67, 64, 67]  # D - F - Eb - G
for i, pitch in enumerate(notes):
    start = time + (i * 0.375)
    end = start + 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bar 3: D - Eb - G - C (variation)
time = 3 * 1.5
notes = [62, 64, 67, 71]  # D - Eb - G - C
for i, pitch in enumerate(notes):
    start = time + (i * 0.375)
    end = start + 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bar 4: Repeat the motif, but finish it
time = 4 * 1.5
notes = [62, 67, 64, 67]  # D - F - Eb - G
for i, pitch in enumerate(notes):
    start = time + (i * 0.375)
    end = start + 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Add the final note to close the motif
final_note = pretty_midi.Note(velocity=100, pitch=62, start=4 * 1.5 + 1.5, end=4 * 1.5 + 1.5 + 0.1875)
sax.notes.append(final_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
