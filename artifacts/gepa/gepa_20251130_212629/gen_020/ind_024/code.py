
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
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax plays a short motif, starting on D (note 62)
# Motif: D (62) on beat 1, E (64) on & of 1, B (67) on beat 2, rest on & of 2
sax.notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D on beat 1
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # E on & of 1
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # B on beat 2
])

# Marcus: Walking line - chromatic approach to D
# D (62) -> C# (61) -> D (62) -> E (64)
bass.notes.extend([
    pretty_midi.Note(velocity=80, pitch=61, start=1.5, end=1.875),  # C# on beat 1
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25), # D on & of 1
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625), # E on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # D on & of 2
])

# Diane: 7th chords on 2 and 4, comp on 2 and 4
# Bar 2: D7 on beat 2 (D, F#, A, C)
piano.notes.extend([
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=85, pitch=60, start=2.25, end=2.625),  # C
])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
])

# Bar 3: Full quartet (3.0 - 4.5s)
# sax: rest on beat 1, play B (67) on & of 1, D (62) on beat 2, E (64) on & of 2
sax.notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # B on & of 1
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # D on beat 2
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),  # E on & of 2
])

# Marcus: Walking line - chromatic approach to B
# B (67) -> A# (66) -> B (67) -> C (60)
bass.notes.extend([
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.375),  # A# on beat 1
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # B on & of 1
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # C on beat 2
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # B on & of 2
])

# Diane: 7th chords on 2 and 4
# Bar 3: B7 on beat 2 (B, D#, F#, A)
piano.notes.extend([
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=4.125),  # D#
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=85, pitch=65, start=3.75, end=4.125),  # A
])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
])

# Bar 4: Full quartet (4.5 - 6.0s)
# sax: rest on beat 1, rest on & of 1, rest on beat 2, play B (67) on & of 2
sax.notes.extend([
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # B on & of 2
])

# Marcus: Walking line - chromatic approach to D
# D (62) -> C# (61) -> D (62) -> E (64)
bass.notes.extend([
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875),  # C# on beat 1
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25), # D on & of 1
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625), # E on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D on & of 2
])

# Diane: 7th chords on 2 and 4
# Bar 4: D7 on beat 2 (D, F#, A, C)
piano.notes.extend([
    pretty_midi.Note(velocity=85, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=85, pitch=64, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=85, pitch=60, start=5.25, end=5.625),  # C
])

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
