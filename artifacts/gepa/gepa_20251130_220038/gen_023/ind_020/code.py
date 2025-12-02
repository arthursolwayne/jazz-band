
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
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
for bar in range(2, 5):
    start = bar * 1.5
    # F7 chord: F, A, C, E, Bb
    # Walking bass line in F
    if bar == 2:
        bass_notes = [pretty_midi.Note(velocity=100, pitch=70, start=start, end=start + 0.375),  # F
                      pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75),  # E
                      pretty_midi.Note(velocity=100, pitch=71, start=start + 0.75, end=start + 1.125),  # G
                      pretty_midi.Note(velocity=100, pitch=68, start=start + 1.125, end=start + 1.5)]  # Eb
    elif bar == 3:
        bass_notes = [pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375),  # G
                      pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75),  # D
                      pretty_midi.Note(velocity=100, pitch=69, start=start + 0.75, end=start + 1.125),  # E
                      pretty_midi.Note(velocity=100, pitch=70, start=start + 1.125, end=start + 1.5)]  # F
    elif bar == 4:
        bass_notes = [pretty_midi.Note(velocity=100, pitch=68, start=start, end=start + 0.375),  # Eb
                      pretty_midi.Note(velocity=100, pitch=70, start=start + 0.375, end=start + 0.75),  # F
                      pretty_midi.Note(velocity=100, pitch=69, start=start + 0.75, end=start + 1.125),  # E
                      pretty_midi.Note(velocity=100, pitch=71, start=start + 1.125, end=start + 1.5)]  # G
    bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # F7 chord: F, A, C, E, Bb
    if bar == 2:
        # Comp on 2 and 4
        piano_notes = [
            pretty_midi.Note(velocity=100, pitch=70, start=start + 0.375, end=start + 0.75),  # F
            pretty_midi.Note(velocity=100, pitch=68, start=start + 0.375, end=start + 0.75),  # Eb
            pretty_midi.Note(velocity=100, pitch=71, start=start + 0.375, end=start + 0.75),  # G
            pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75),  # E
            pretty_midi.Note(velocity=100, pitch=70, start=start + 1.125, end=start + 1.5),  # F
            pretty_midi.Note(velocity=100, pitch=68, start=start + 1.125, end=start + 1.5),  # Eb
            pretty_midi.Note(velocity=100, pitch=71, start=start + 1.125, end=start + 1.5),  # G
            pretty_midi.Note(velocity=100, pitch=69, start=start + 1.125, end=start + 1.5)   # E
        ]
    elif bar == 3:
        # F7 chord with chromatic passing tone
        piano_notes = [
            pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75),  # D
            pretty_midi.Note(velocity=100, pitch=70, start=start + 0.375, end=start + 0.75),  # F
            pretty_midi.Note(velocity=100, pitch=68, start=start + 0.375, end=start + 0.75),  # Eb
            pretty_midi.Note(velocity=100, pitch=71, start=start + 0.375, end=start + 0.75),  # G
            pretty_midi.Note(velocity=100, pitch=67, start=start + 1.125, end=start + 1.5),  # D
            pretty_midi.Note(velocity=100, pitch=70, start=start + 1.125, end=start + 1.5),  # F
            pretty_midi.Note(velocity=100, pitch=68, start=start + 1.125, end=start + 1.5),  # Eb
            pretty_midi.Note(velocity=100, pitch=71, start=start + 1.125, end=start + 1.5)   # G
        ]
    elif bar == 4:
        # F7 chord with passing tone
        piano_notes = [
            pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75),  # E
            pretty_midi.Note(velocity=100, pitch=70, start=start + 0.375, end=start + 0.75),  # F
            pretty_midi.Note(velocity=100, pitch=68, start=start + 0.375, end=start + 0.75),  # Eb
            pretty_midi.Note(velocity=100, pitch=71, start=start + 0.375, end=start + 0.75),  # G
            pretty_midi.Note(velocity=100, pitch=69, start=start + 1.125, end=start + 1.5),  # E
            pretty_midi.Note(velocity=100, pitch=70, start=start + 1.125, end=start + 1.5),  # F
            pretty_midi.Note(velocity=100, pitch=68, start=start + 1.125, end=start + 1.5),  # Eb
            pretty_midi.Note(velocity=100, pitch=71, start=start + 1.125, end=start + 1.5)   # G
        ]
    piano.notes.extend(piano_notes)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
start = 1.5
note1 = pretty_midi.Note(velocity=100, pitch=67, start=start, end=start + 0.375)  # D
note2 = pretty_midi.Note(velocity=100, pitch=70, start=start + 0.75, end=start + 1.125)  # F
note3 = pretty_midi.Note(velocity=100, pitch=67, start=start + 1.5, end=start + 1.875)  # D
note4 = pretty_midi.Note(velocity=100, pitch=70, start=start + 2.25, end=start + 2.625)  # F
note5 = pretty_midi.Note(velocity=100, pitch=68, start=start + 3.0, end=start + 3.375)  # Eb
note6 = pretty_midi.Note(velocity=100, pitch=70, start=start + 3.75, end=start + 4.125)  # F
note7 = pretty_midi.Note(velocity=100, pitch=67, start=start + 4.5, end=start + 4.875)  # D
note8 = pretty_midi.Note(velocity=100, pitch=70, start=start + 5.25, end=start + 5.625)  # F

sax.notes.extend([note1, note2, note3, note4, note5, note6, note7, note8])

# Drums for bars 2-4: Same pattern as bar 1, repeated
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
