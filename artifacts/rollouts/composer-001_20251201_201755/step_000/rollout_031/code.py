
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # E
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # Ab
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: short motif, sing, leave it hanging
# Motif: F, G, Bb, F (1.5 - 2.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# Fill in the rest of the sax line with space and tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Add final resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_russo_intro.mid')
