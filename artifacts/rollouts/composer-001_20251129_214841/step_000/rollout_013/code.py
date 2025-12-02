
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=80, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=80, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=80, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=80, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, chromatic approaches)
for bar in range(2, 5):
    start = bar * 1.5
    # Walking bass line in C
    if bar == 2:
        # C -> B -> C -> D
        bass_notes = [pretty_midi.Note(velocity=80, pitch=60, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=80, pitch=61, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=80, pitch=60, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=80, pitch=62, start=start + 1.125, end=start + 1.5)]
    elif bar == 3:
        # D -> C -> D -> E
        bass_notes = [pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=80, pitch=60, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=80, pitch=62, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=80, pitch=64, start=start + 1.125, end=start + 1.5)]
    else:
        # E -> D -> E -> F
        bass_notes = [pretty_midi.Note(velocity=80, pitch=64, start=start, end=start + 0.375),
                      pretty_midi.Note(velocity=80, pitch=62, start=start + 0.375, end=start + 0.75),
                      pretty_midi.Note(velocity=80, pitch=64, start=start + 0.75, end=start + 1.125),
                      pretty_midi.Note(velocity=80, pitch=65, start=start + 1.125, end=start + 1.5)]
    bass.notes.extend(bass_notes)

# Diane on piano (7th chords, comp on 2 and 4)
for bar in range(2, 5):
    start = bar * 1.5
    if bar == 2:
        # C7 on 2 and 4
        chord_notes = [pretty_midi.Note(velocity=90, pitch=60, start=start + 0.375, end=start + 0.75),
                       pretty_midi.Note(velocity=90, pitch=64, start=start + 0.375, end=start + 0.75),
                       pretty_midi.Note(velocity=90, pitch=67, start=start + 0.375, end=start + 0.75),
                       pretty_midi.Note(velocity=90, pitch=71, start=start + 0.375, end=start + 0.75)]
    elif bar == 3:
        # D7 on 2 and 4
        chord_notes = [pretty_midi.Note(velocity=90, pitch=62, start=start + 0.375, end=start + 0.75),
                       pretty_midi.Note(velocity=90, pitch=66, start=start + 0.375, end=start + 0.75),
                       pretty_midi.Note(velocity=90, pitch=69, start=start + 0.375, end=start + 0.75),
                       pretty_midi.Note(velocity=90, pitch=73, start=start + 0.375, end=start + 0.75)]
    else:
        # E7 on 2 and 4
        chord_notes = [pretty_midi.Note(velocity=90, pitch=64, start=start + 0.375, end=start + 0.75),
                       pretty_midi.Note(velocity=90, pitch=68, start=start + 0.375, end=start + 0.75),
                       pretty_midi.Note(velocity=90, pitch=71, start=start + 0.375, end=start + 0.75),
                       pretty_midi.Note(velocity=90, pitch=76, start=start + 0.375, end=start + 0.75)]
    piano.notes.extend(chord_notes)

# Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=80, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=80, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=80, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=80, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Dante on sax (short motif, make it sing)
# Bar 2: Start the motif
start = 1.5
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=start, end=start + 0.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=start + 0.25, end=start + 0.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=start + 0.5, end=start + 0.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=start + 0.75, end=start + 1.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=start + 1.0, end=start + 1.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=start + 1.25, end=start + 1.5),  # G
]
sax.notes.extend(sax_notes)

# Bar 3-4: Rest, let the motif hang
# No sax notes on bars 3-4, just let it echo

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
