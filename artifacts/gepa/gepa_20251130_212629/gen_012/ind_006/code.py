
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
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
for bar in range(2, 5):
    start = bar * 1.5
    # Dm7 walking bass line
    if bar == 2:
        bass_notes = [pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.375),  # F
                      pretty_midi.Note(velocity=100, pitch=60, start=start + 0.375, end=start + 0.75),  # E
                      pretty_midi.Note(velocity=100, pitch=59, start=start + 0.75, end=start + 1.125),  # D
                      pretty_midi.Note(velocity=100, pitch=64, start=start + 1.125, end=start + 1.5)]  # G
    elif bar == 3:
        bass_notes = [pretty_midi.Note(velocity=100, pitch=64, start=start, end=start + 0.375),  # G
                      pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75),  # F
                      pretty_midi.Note(velocity=100, pitch=60, start=start + 0.75, end=start + 1.125),  # E
                      pretty_midi.Note(velocity=100, pitch=59, start=start + 1.125, end=start + 1.5)]  # D
    else:
        bass_notes = [pretty_midi.Note(velocity=100, pitch=59, start=start, end=start + 0.375),  # D
                      pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75),  # F
                      pretty_midi.Note(velocity=100, pitch=64, start=start + 0.75, end=start + 1.125),  # G
                      pretty_midi.Note(velocity=100, pitch=60, start=start + 1.125, end=start + 1.5)]  # E
    bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # Dm7: D, F, A, C
    if bar == 2:
        # Comp on 2 and 4
        piano_notes = [pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75),  # F
                       pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75),  # G
                       pretty_midi.Note(velocity=100, pitch=60, start=start + 1.125, end=start + 1.5),  # E
                       pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)]  # F
    elif bar == 3:
        # Dm7: D, F, A, C
        piano_notes = [pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75),  # F
                       pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75),  # G
                       pretty_midi.Note(velocity=100, pitch=60, start=start + 1.125, end=start + 1.5),  # E
                       pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)]  # F
    else:
        # Dm7: D, F, A, C
        piano_notes = [pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75),  # F
                       pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75),  # G
                       pretty_midi.Note(velocity=100, pitch=60, start=start + 1.125, end=start + 1.5),  # E
                       pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)]  # F
    piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, E, F, G, A, Bb, C
# Motif: D, F, Bb, C (saxophone)
# Bar 2: Start motif
start = 1.5
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=start + 0.75, end=start + 1.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=start + 1.125, end=start + 1.5)   # C
]
sax.notes.extend(sax_notes)

# Bar 3: Leave it hanging (no notes)
# Bar 4: Return and finish it
start = 4.5
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=start + 0.75, end=start + 1.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=start + 1.125, end=start + 1.5)   # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    drums.notes.append(hihat)
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
