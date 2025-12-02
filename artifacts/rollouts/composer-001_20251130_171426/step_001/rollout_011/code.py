
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Bass enters, piano enters, sax enters
# Bass: Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0),  # A
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7: F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # Eb
    # Bar 3, beat 2 (F7 again)
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # Eb
    # Bar 4, beat 2 (F7 again)
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # Eb
]

# Sax: One short motif, make it sing
# Fm motif: F, Gb, Ab, Bb -> F, Gb, Ab, Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),  # Bb
    # Repeat the motif with a slight delay
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75),  # Bb
    # End with a resolution to C
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.75),  # Bb to C
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_intro.mid")
