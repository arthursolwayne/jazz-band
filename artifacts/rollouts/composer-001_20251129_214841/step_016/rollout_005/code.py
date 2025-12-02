
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts
sax_note_1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
sax_note_2 = pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0)
sax_note_3 = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25)
sax_note_4 = pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5)
sax.notes.extend([sax_note_1, sax_note_2, sax_note_3, sax_note_4])

# Bass: walking line, chromatic approaches
bass_note_1 = pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75)
bass_note_2 = pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0)
bass_note_3 = pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25)
bass_note_4 = pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5)
bass.notes.extend([bass_note_1, bass_note_2, bass_note_3, bass_note_4])

# Piano: 7th chords, comp on 2 and 4
piano_note_1 = pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0)
piano_note_2 = pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0)
piano_note_3 = pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0)
piano_note_4 = pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0)
piano_note_5 = pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5)
piano_note_6 = pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5)
piano_note_7 = pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5)
piano_note_8 = pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5)
piano.notes.extend([piano_note_1, piano_note_2, piano_note_3, piano_note_4, piano_note_5, piano_note_6, piano_note_7, piano_note_8])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif repeats with variation
sax_note_5 = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25)
sax_note_6 = pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5)
sax_note_7 = pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75)
sax_note_8 = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)
sax.notes.extend([sax_note_5, sax_note_6, sax_note_7, sax_note_8])

# Bass: walking line, chromatic approaches
bass_note_5 = pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25)
bass_note_6 = pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5)
bass_note_7 = pretty_midi.Note(velocity=80, pitch=54, start=3.5, end=3.75)
bass_note_8 = pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.0)
bass.notes.extend([bass_note_5, bass_note_6, bass_note_7, bass_note_8])

# Piano: 7th chords, comp on 2 and 4
piano_note_9 = pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5)
piano_note_10 = pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5)
piano_note_11 = pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5)
piano_note_12 = pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5)
piano_note_13 = pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0)
piano_note_14 = pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0)
piano_note_15 = pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0)
piano_note_16 = pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0)
piano.notes.extend([piano_note_9, piano_note_10, piano_note_11, piano_note_12, piano_note_13, piano_note_14, piano_note_15, piano_note_16])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: motif finishes
sax_note_9 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)
sax_note_10 = pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0)
sax_note_11 = pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25)
sax_note_12 = pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5)
sax.notes.extend([sax_note_9, sax_note_10, sax_note_11, sax_note_12])

# Bass: walking line, chromatic approaches
bass_note_9 = pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.75)
bass_note_10 = pretty_midi.Note(velocity=80, pitch=57, start=4.75, end=5.0)
bass_note_11 = pretty_midi.Note(velocity=80, pitch=58, start=5.0, end=5.25)
bass_note_12 = pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.5)
bass.notes.extend([bass_note_9, bass_note_10, bass_note_11, bass_note_12])

# Piano: 7th chords, comp on 2 and 4
piano_note_17 = pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0)
piano_note_18 = pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0)
piano_note_19 = pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0)
piano_note_20 = pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0)
piano_note_21 = pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5)
piano_note_22 = pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5)
piano_note_23 = pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5)
piano_note_24 = pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5)
piano.notes.extend([piano_note_17, piano_note_18, piano_note_19, piano_note_20, piano_note_21, piano_note_22, piano_note_23, piano_note_24])

# Drum fill in bar 4
drum_notes_2 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes_2)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
