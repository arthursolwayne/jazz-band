
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0), # Ab
]

bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=90, pitch=78, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=82, start=1.875, end=2.25), # E
    # Bar 3: Ab7 on beat 4
    pretty_midi.Note(velocity=95, pitch=68, start=2.625, end=3.0), # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0), # Db
    pretty_midi.Note(velocity=90, pitch=73, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0), # Eb
    pretty_midi.Note(velocity=90, pitch=78, start=2.625, end=3.0), # G
]

piano.notes.extend(piano_notes)

# Dante: Tenor sax melody
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875), # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0), # E
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in F minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # C#
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5), # D#
]

bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=82, start=3.375, end=3.75), # E
    # Bar 4: Ab7 on beat 4
    pretty_midi.Note(velocity=95, pitch=68, start=4.125, end=4.5), # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5), # Db
    pretty_midi.Note(velocity=90, pitch=73, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5), # Eb
    pretty_midi.Note(velocity=90, pitch=78, start=4.125, end=4.5), # G
]

piano.notes.extend(piano_notes)

# Dante: Tenor sax melody
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5), # E
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in F minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0), # E
]

bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=82, start=4.875, end=5.25), # E
    # Bar 4: Ab7 on beat 4
    pretty_midi.Note(velocity=95, pitch=68, start=5.625, end=6.0), # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0), # Db
    pretty_midi.Note(velocity=90, pitch=73, start=5.625, end=6.0), # D
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0), # Eb
    pretty_midi.Note(velocity=90, pitch=78, start=5.625, end=6.0), # G
]

piano.notes.extend(piano_notes)

# Dante: Tenor sax melody
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0), # E
]

sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
for bar in [2, 3]:
    start = bar * 1.5
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
        # Hihat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875),
        pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
