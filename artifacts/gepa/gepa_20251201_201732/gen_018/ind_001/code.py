
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2, Ab2, Bb2, Db3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (F2, Ab2 - chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),
    # Bar 3 (Bb2, Db3 - chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),
    # Bar 4 (F2, Ab2 - chromatic approach)
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),
    # Bar 4: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
