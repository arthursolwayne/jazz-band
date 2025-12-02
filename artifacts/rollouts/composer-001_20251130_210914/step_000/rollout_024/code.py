
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7 chord: D F A C
        # Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
        bass_notes = [50, 51, 52, 53, 55, 56, 57, 58, 50]
        for note in bass_notes:
            duration = 0.375
            bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))
            start += duration
    elif bar == 3:
        # Chromatic descent through Dm7
        bass_notes = [50, 49, 48, 47, 50, 51, 52, 51, 50]
        for note in bass_notes:
            duration = 0.375
            bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))
            start += duration
    else:
        # Return to walking line
        bass_notes = [50, 51, 52, 53, 55, 56, 57, 58, 50]
        for note in bass_notes:
            duration = 0.375
            bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))
            start += duration

# Diane: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # Dm7 (D F A C)
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start + 0.75, end=start + 1.125))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=52, start=start + 0.75, end=start + 1.125))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=start + 0.75, end=start + 1.125))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=start + 0.75, end=start + 1.125))
    elif bar == 3:
        # Dm7 with variation
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start + 0.75, end=start + 1.125))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=52, start=start + 0.75, end=start + 1.125))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=start + 0.75, end=start + 1.125))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=start + 0.75, end=start + 1.125))
    else:
        # Dm7 again
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=start + 0.75, end=start + 1.125))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=52, start=start + 0.75, end=start + 1.125))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=start + 0.75, end=start + 1.125))
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=start + 0.75, end=start + 1.125))

# Dante: saxophone motif
# Bar 2: Start the motif
# Bar 3: Leave it hanging
# Bar 4: Finish it
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Motif: Dm7 in D, with a twist
# D - F - A - C
# Add a chromatic passing tone on the way up
# D - Eb - F - A - C

# Bar 2: Start the motif
note1 = pretty_midi.Note(velocity=110, pitch=50, start=bar2_start, end=bar2_start + 0.375)
note2 = pretty_midi.Note(velocity=110, pitch=51, start=bar2_start + 0.375, end=bar2_start + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=52, start=bar2_start + 0.75, end=bar2_start + 1.125)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)

# Bar 3: Leave it hanging on A
note4 = pretty_midi.Note(velocity=110, pitch=55, start=bar3_start, end=bar3_start + 0.375)
sax.notes.append(note4)

# Bar 4: Finish the motif with a chromatic approach to C
note5 = pretty_midi.Note(velocity=110, pitch=57, start=bar4_start, end=bar4_start + 0.375)
note6 = pretty_midi.Note(velocity=110, pitch=58, start=bar4_start + 0.375, end=bar4_start + 0.75)
sax.notes.append(note5)
sax.notes.append(note6)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
