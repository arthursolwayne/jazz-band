
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F (F2 - C3, MIDI 45-52)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),   # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last bar
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # A (MIDI 74)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # E (MIDI 79)
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Bb (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # D (MIDI 72)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # F (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=3.0),  # Ab (MIDI 70)
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # Eb (MIDI 64)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # G (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # Bb (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # D (MIDI 72)
]
piano.notes.extend(piano_notes)

# Sax: Motif in F (F, G, Ab, Bb), start on 1.5s, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
