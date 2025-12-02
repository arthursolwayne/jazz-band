
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    # Fm7 chord: F, Ab, Bb, D
    # Walking bass line in Fm
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.0625), # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.0625, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.4375), # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.4375, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.8125), # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.8125, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # D
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.875, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.875, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.0625, end=2.25), # C
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=2.4375, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.8125, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.5625, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=3.9375), # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.9375, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.3125), # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.3125, end=4.5),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.875, end=4.0),  # F
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.5625, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.9375), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=3.9375, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.3125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.1875), # C
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.0625, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.4375), # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.4375, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=5.8125), # D
    pretty_midi.Note(velocity=90, pitch=63, start=5.8125, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=5.4375, end=5.625), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.8125, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
