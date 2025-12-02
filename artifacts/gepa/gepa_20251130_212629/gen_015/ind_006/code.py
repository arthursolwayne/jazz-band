
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.75),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.5),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=2.0),    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=34, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=80, pitch=35, start=1.75, end=2.0),   # Gb
    pretty_midi.Note(velocity=80, pitch=33, start=2.0, end=2.25),   # E
    pretty_midi.Note(velocity=80, pitch=31, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=80, pitch=32, start=2.5, end=2.75),   # Eb
    pretty_midi.Note(velocity=80, pitch=30, start=2.75, end=3.0),   # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),   # F7 (again)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Dante: Sax motif (One short motif, make it sing — start it, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625), # Gm (Fm key)
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75), # A
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0), # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.125), # C
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25), # B
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.375), # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5), # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=34, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=80, pitch=35, start=3.25, end=3.5),   # Gb
    pretty_midi.Note(velocity=80, pitch=33, start=3.5, end=3.75),   # E
    pretty_midi.Note(velocity=80, pitch=31, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=80, pitch=32, start=4.0, end=4.25),   # Eb
    pretty_midi.Note(velocity=80, pitch=30, start=4.25, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),   # F7
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),   # F7 (again)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Dante: Sax continues motif, ends on a question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125), # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25), # A
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.375), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5), # B
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625), # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75), # B
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.875), # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0), # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=34, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=80, pitch=35, start=4.75, end=5.0),   # Gb
    pretty_midi.Note(velocity=80, pitch=33, start=5.0, end=5.25),   # E
    pretty_midi.Note(velocity=80, pitch=31, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=80, pitch=32, start=5.5, end=5.75),   # Eb
    pretty_midi.Note(velocity=80, pitch=30, start=5.75, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),   # F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),   # F7 (again)
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Dante: Ends on a question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625), # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75), # A
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0), # B
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.125), # C
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.25), # B
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.375), # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5), # G
]
sax.notes.extend(sax_notes)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=5.0),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.5),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.375, end=5.75),# Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
