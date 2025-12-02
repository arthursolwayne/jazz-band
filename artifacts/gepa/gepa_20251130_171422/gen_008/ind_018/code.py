
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
    # Kick on 1
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    # Snare on 2
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    # Kick on 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375)
    drums.notes.append(kick)
    # Snare on 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.5, end=start + 1.5 + 0.375)
    drums.notes.append(snare)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
# Bar 2: D - Eb - F - G
# Bar 3: A - Bb - B - C
# Bar 4: D - Eb - F - G
for bar in range(2, 5):
    start = bar * 1.5
    # D - Eb - F - G
    if bar == 2:
        notes = [62, 63, 65, 67]
    elif bar == 3:
        notes = [67, 68, 70, 72]
    else:
        notes = [62, 63, 65, 67]
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 (F# - C#), comp on beat 2 and 4
# Bar 3: Bm7b5 (D - F# - A - C), comp on beat 2 and 4
# Bar 4: D7 (F# - C#), comp on beat 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # D7 - F#, C#
        chord_notes = [62, 67, 70, 72]
    elif bar == 3:
        # Bm7b5 - D, F#, A, C
        chord_notes = [67, 70, 72, 74]
    else:
        # D7 - F#, C#
        chord_notes = [62, 67, 70, 72]
    # Play the chord on beat 1 and 3
    for i in [0, 2]:
        for pitch in chord_notes:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
            piano.notes.append(note)
    # Comp on beat 2 and 4
    for i in [1, 3]:
        for pitch in chord_notes:
            note = pretty_midi.Note(velocity=60, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
            piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F - G - D
# Bar 2: Start the motif
# Bar 3: Leave it hanging
# Bar 4: Finish it

# Bar 2: Start the motif
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375)
sax.notes.append(note1)
note2 = pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 0.75, end=1.5 + 0.75 + 0.375)
sax.notes.append(note2)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.125, end=1.5 + 1.125 + 0.375)
sax.notes.append(note3)

# Bar 3: Leave it hanging
note4 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.375)
sax.notes.append(note4)

# Bar 4: Finish it
note5 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.5 + 0.375)
sax.notes.append(note5)
note6 = pretty_midi.Note(velocity=100, pitch=67, start=4.5 + 0.75, end=4.5 + 0.75 + 0.375)
sax.notes.append(note6)
note7 = pretty_midi.Note(velocity=100, pitch=62, start=4.5 + 1.125, end=4.5 + 1.125 + 0.375)
sax.notes.append(note7)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
