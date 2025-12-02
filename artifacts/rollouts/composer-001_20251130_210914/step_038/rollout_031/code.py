
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

# Bar 2: Everyone in
# Sax: Fm7 - Bb7 - Eb7 - Ab7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.1875), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.1875, end=2.375), # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.5625, end=2.75), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0), # Ab
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.0), # A
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.1875), # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=2.1875, end=2.375), # C
    pretty_midi.Note(velocity=90, pitch=59, start=2.375, end=2.5625), # Db
    pretty_midi.Note(velocity=90, pitch=61, start=2.5625, end=2.75), # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s) - Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.0), # A
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.0), # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.0), # C
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0), # D
    # Bar 3 (2.0 - 2.5s) - Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.375, end=2.5625), # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.375, end=2.5625), # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.375, end=2.5625), # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.375, end=2.5625), # Bb
    # Bar 4 (2.5 - 3.0s) - Eb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=66, start=2.875, end=3.0), # G
    pretty_midi.Note(velocity=90, pitch=68, start=2.875, end=3.0), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=2.875, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.875, end=3.0), # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Everyone in
# Sax: Fm7 - Bb7 - Eb7 - Ab7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=3.5625, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.9375), # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.9375, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.3125, end=4.625), # Ab
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.5625), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.5625, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.9375), # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.9375, end=4.125), # Db
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.3125), # D
    pretty_midi.Note(velocity=90, pitch=79, start=4.3125, end=4.625), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 3.5s) - Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5625), # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5625), # Bb
    # Bar 4 (3.5 - 4.0s) - Eb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=66, start=3.875, end=4.0), # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.875, end=4.0), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.0), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.875, end=4.0), # Db
    # Bar 4 (4.0 - 4.5s) - Ab7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.375, end=4.5625), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.375, end=4.5625), # Db
    pretty_midi.Note(velocity=90, pitch=76, start=4.375, end=4.5625), # D
    pretty_midi.Note(velocity=90, pitch=79, start=4.375, end=4.5625), # F
]
piano.notes.extend(piano_notes)

# Bar 4: Everyone in
# Sax: Fm7 - Bb7 - Eb7 - Ab7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.8125), # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.8125, end=5.0), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.1875), # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=5.1875, end=5.5), # Ab
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=79, start=4.625, end=4.8125), # F
    pretty_midi.Note(velocity=90, pitch=81, start=4.8125, end=5.0), # G
    pretty_midi.Note(velocity=90, pitch=83, start=5.0, end=5.1875), # Ab
    pretty_midi.Note(velocity=90, pitch=86, start=5.1875, end=5.5), # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 (4.625 - 5.125s) - Eb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=66, start=4.8125, end=5.0), # G
    pretty_midi.Note(velocity=90, pitch=68, start=4.8125, end=5.0), # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.8125, end=5.0), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.8125, end=5.0), # Db
    # Bar 4 (5.125 - 5.5s) - Ab7 on beat 4
    pretty_midi.Note(velocity=90, pitch=71, start=5.375, end=5.5), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=5.375, end=5.5), # Db
    pretty_midi.Note(velocity=90, pitch=76, start=5.375, end=5.5), # D
    pretty_midi.Note(velocity=90, pitch=79, start=5.375, end=5.5), # F
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
