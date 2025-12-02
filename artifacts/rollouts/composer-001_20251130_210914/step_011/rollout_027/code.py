
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane: 7th chords on 2 and 4 (F7, Bb7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F7
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # Bb7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=3.0),
]
piano.notes.extend(piano_notes)

# Marcus: Walking bass line in F (F, G, Ab, A, Bb, B, C, Db, etc.)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=75, start=4.125, end=4.5), # Db
]
bass.notes.extend(bass_notes)

# Dante: Sax melody - short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5), # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane: 7th chords on 2 and 4 (F7, Bb7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # F7
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),  # Bb7
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.5),
]
piano.notes.extend(piano_notes)

# Marcus: Walking bass line in F (F, G, Ab, A, Bb, B, C, Db, etc.)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5), # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=75, start=5.625, end=6.0), # Db
]
bass.notes.extend(bass_notes)

# Dante: Sax melody - continuation, resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane: 7th chords on 2 and 4 (F7, Bb7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),  # F7
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=6.0),  # Bb7
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=73, start=5.25, end=6.0),
]
piano.notes.extend(piano_notes)

# Marcus: Walking bass line in F (F, G, Ab, A, Bb, B, C, Db, etc.)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0), # A
]
bass.notes.extend(bass_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
