
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.25),   # F
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25),   # Ab
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),   # C
    pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.25),   # Db
    # Bar 3: Bb7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0),    # Bb
    pretty_midi.Note(velocity=95, pitch=57, start=2.625, end=3.0),    # D
    pretty_midi.Note(velocity=95, pitch=60, start=2.625, end=3.0),    # F
    pretty_midi.Note(velocity=95, pitch=59, start=2.625, end=3.0),    # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif - start with a whisper, then a cry
sax_notes = [
    # Bar 2: First note - a whisper
    pretty_midi.Note(velocity=70, pitch=71, start=1.5, end=1.6875),   # G
    # Bar 3: Second note - a cry
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),  # C
    # Bar 4: Return to the motif, finish it
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=110, pitch=81, start=3.5625, end=3.75), # E
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 6.0s)
# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.75),   # F
    pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.75),   # Ab
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),   # C
    pretty_midi.Note(velocity=95, pitch=65, start=3.375, end=3.75),   # Db
    # Bar 4: Bb7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.6875, end=5.0),    # Bb
    pretty_midi.Note(velocity=95, pitch=57, start=4.6875, end=5.0),    # D
    pretty_midi.Note(velocity=95, pitch=60, start=4.6875, end=5.0),    # F
    pretty_midi.Note(velocity=95, pitch=59, start=4.6875, end=5.0),    # Eb
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, build to a cry
sax_notes = [
    pretty_midi.Note(velocity=70, pitch=69, start=3.0, end=3.1875),   # F
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=77, start=4.125, end=4.3125), # C#
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=70, pitch=69, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=77, start=5.625, end=5.8125), # C#
    pretty_midi.Note(velocity=110, pitch=76, start=6.0, end=6.1875),  # C
]
sax.notes.extend(sax_notes)

# Bar 4: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.6875, end=4.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
