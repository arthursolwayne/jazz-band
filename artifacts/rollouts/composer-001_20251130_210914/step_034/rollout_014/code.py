
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

# Bass line - walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
# Bar 2 (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # A
]
# Bar 3 (3.0 - 4.5s)
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # Db
])
# Bar 4 (4.5 - 6.0s)
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # A
])
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, Fm7 on beat 2, Bbm7 on beat 4
# Bar 2 (1.5 - 3.0s)
piano_notes = [
    # Fm7 on beat 2 (1.875 - 2.0)
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=68, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=1.875, end=2.0),  # Gb
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.0),  # D
    # Bbm7 on beat 4 (2.625 - 2.75)
    pretty_midi.Note(velocity=95, pitch=73, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=70, start=2.625, end=2.75),  # Gb
    pretty_midi.Note(velocity=95, pitch=68, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=2.75),  # F
]
# Bar 3 (3.0 - 4.5s)
piano_notes.extend([
    # Fm7 on beat 2 (3.875 - 4.0)
    pretty_midi.Note(velocity=95, pitch=71, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=95, pitch=68, start=3.875, end=4.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=3.875, end=4.0),  # Gb
    pretty_midi.Note(velocity=95, pitch=67, start=3.875, end=4.0),  # D
    # Bbm7 on beat 4 (4.625 - 4.75)
    pretty_midi.Note(velocity=95, pitch=73, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=70, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=95, pitch=68, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=95, pitch=64, start=4.625, end=4.75),  # F
])
# Bar 4 (4.5 - 6.0s)
piano_notes.extend([
    # Fm7 on beat 2 (5.875 - 6.0)
    pretty_midi.Note(velocity=95, pitch=71, start=5.875, end=6.0),  # F
    pretty_midi.Note(velocity=95, pitch=68, start=5.875, end=6.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=70, start=5.875, end=6.0),  # Gb
    pretty_midi.Note(velocity=95, pitch=67, start=5.875, end=6.0),  # D
])
piano.notes.extend(piano_notes)

# Saxophone - motif: F, Ab, Gb, F (start on beat 2 of bar 2)
# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=71, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=105, pitch=68, start=2.0, end=2.125),  # Ab
    pretty_midi.Note(velocity=105, pitch=70, start=2.125, end=2.25), # Gb
    pretty_midi.Note(velocity=105, pitch=71, start=2.25, end=2.5),   # F (held)
]
# Bar 3 (3.0 - 4.5s)
# Leave it hanging, then come back with variation
sax_notes.extend([
    pretty_midi.Note(velocity=105, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=105, pitch=68, start=3.375, end=3.5),  # Ab
    pretty_midi.Note(velocity=105, pitch=70, start=3.5, end=3.625), # Gb
    pretty_midi.Note(velocity=105, pitch=71, start=3.625, end=4.0),  # F
])
# Bar 4 (4.5 - 6.0s)
sax_notes.extend([
    pretty_midi.Note(velocity=105, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=105, pitch=68, start=4.875, end=5.0),  # Ab
    pretty_midi.Note(velocity=105, pitch=70, start=5.0, end=5.125), # Gb
    pretty_midi.Note(velocity=105, pitch=71, start=5.125, end=6.0),  # F (long hold)
])
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
