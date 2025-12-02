
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=75, pitch=60, start=1.5, end=1.875),
    # Bar 3 - Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=75, pitch=60, start=3.0, end=3.375),
    # Bar 4 - Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=75, pitch=60, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax - motif in Dm, short and singable
sax_notes = [
    # Bar 2 - motif start
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # D
    # Bar 3 - leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # D
    # Bar 4 - come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.6875),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=110, pitch=64, start=5.0625, end=5.25), # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.4375), # E
    pretty_midi.Note(velocity=110, pitch=64, start=5.4375, end=5.625), # D
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.8125, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
