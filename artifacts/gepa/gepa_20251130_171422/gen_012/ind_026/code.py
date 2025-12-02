
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums, with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=3.25, end=3.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.625, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=4.25, end=4.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.375, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.125, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=5.75),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=5.75, end=5.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.875, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=1.625, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),  # C

    # Bar 3: Dm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.875, end=3.0),  # C

    # Bar 4: Dm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.625, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.875, end=4.0),  # C
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    for beat in range(4):
        time = 1.5 + (bar - 2) * 1.5 + beat * 0.375
        if beat % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Sax: Short motif, start it, leave it hanging, come back and finish it
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, Eb, F, G -> leave it hanging on G -> come back to D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
