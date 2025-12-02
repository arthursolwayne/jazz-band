
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

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=39, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=37, start=2.625, end=3.0),  # E
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # Ab
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=39, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords comp on 2 and 4
# F7 (F, A, C, Eb) on bar 2 (beat 2)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=95, pitch=76, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=95, pitch=77, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=95, pitch=74, start=2.25, end=2.625),  # C
    # F7 on bar 4 (beat 2)
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=95, pitch=76, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=95, pitch=77, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=95, pitch=74, start=5.25, end=5.625),  # C
]
piano.notes.extend(piano_notes)

# Sax: Melody (bars 2-4)
# Bar 2: Start with motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),   # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # B
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),   # A
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # C
    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),   # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # B
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
