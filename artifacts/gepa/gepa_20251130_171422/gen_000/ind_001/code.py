
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - begin motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),   # Fm7: F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),   # F
]
sax.notes.extend(sax_notes)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.75),    # F
    pretty_midi.Note(velocity=80, pitch=38, start=1.75, end=2.0),    # Gb
    pretty_midi.Note(velocity=80, pitch=36, start=2.0, end=2.25),    # E
    pretty_midi.Note(velocity=80, pitch=35, start=2.25, end=2.5),    # D
]
bass.notes.extend(bass_notes)

# Piano - comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),    # F7: F
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),    # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),    # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),    # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),    # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),    # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),    # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),    # D
]
piano.notes.extend(piano_notes)

# Drums - continuation
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),   # Ab (continue motif)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),   # F#
]
sax.notes.extend(sax_notes)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=34, start=3.0, end=3.25),    # C
    pretty_midi.Note(velocity=80, pitch=35, start=3.25, end=3.5),    # D
    pretty_midi.Note(velocity=80, pitch=37, start=3.5, end=3.75),    # F
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.0),    # Gb
]
bass.notes.extend(bass_notes)

# Piano - comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),    # F7: F
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),    # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),    # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),    # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),    # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),    # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),    # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),    # D
]
piano.notes.extend(piano_notes)

# Drums - continuation
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - complete motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),   # F (ending on the beat)
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),   # F (sustained)
]
sax.notes.extend(sax_notes)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.75),    # Gb
    pretty_midi.Note(velocity=80, pitch=36, start=4.75, end=5.0),    # E
    pretty_midi.Note(velocity=80, pitch=35, start=5.0, end=5.25),    # D
    pretty_midi.Note(velocity=80, pitch=37, start=5.25, end=5.5),    # F
    pretty_midi.Note(velocity=80, pitch=37, start=5.5, end=5.75),    # F
    pretty_midi.Note(velocity=80, pitch=37, start=5.75, end=6.0),    # F
]
bass.notes.extend(bass_notes)

# Piano - comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),    # F7: F
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),    # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),    # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),    # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.75),    # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75),    # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),    # C
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),    # D
]
piano.notes.extend(piano_notes)

# Drums - continuation
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
