
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
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # G (fifth)
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # A (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=3.0),  # F (lowest note)
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=4.5),  # Bb (lowest note)
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=6.0),  # D (lowest note)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# F - G - Ab - F (melody)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # F (end of motif)
    # Repeat the motif an octave higher for the second half of bar 2
    pretty_midi.Note(velocity=110, pitch=77, start=3.0, end=3.375),  # F (octave)
    pretty_midi.Note(velocity=110, pitch=79, start=3.375, end=3.75),  # G (octave)
    pretty_midi.Note(velocity=110, pitch=78, start=3.75, end=4.125),  # Ab (octave)
    pretty_midi.Note(velocity=110, pitch=77, start=4.125, end=4.5),  # F (octave)
    # Hold the last note of the motif through the rest of the piece
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
