
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=61, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # Eb
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=61, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875), # Dm7 (F)
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875), # Dm7 (Ab)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # Dm7 (D)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875), # Dm7 (Bb)
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375), # Dm7 (F)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375), # Dm7 (Ab)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375), # Dm7 (D)
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375), # Dm7 (Bb)
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.875), # Dm7 (F)
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875), # Dm7 (Ab)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875), # Dm7 (D)
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875), # Dm7 (Bb)
]
piano.notes.extend(piano_notes)

# Sax: Melody, one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2, 4):
    for beat in [0.0, 1.125]:
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=36, start=1.5 + i * 1.5 + beat, end=1.5 + i * 1.5 + beat + 0.375))
    for beat in [0.75, 1.875]:
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5 + i * 1.5 + beat, end=1.5 + i * 1.5 + beat + 0.125))
    for beat in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:
        drum_notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.5 + i * 1.5 + beat, end=1.5 + i * 1.5 + beat + 0.1875))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
