
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625]

drums.notes.extend([pretty_midi.Note(velocity=100, pitch=36, start=kt, end=kt+0.125) for kt in kick_times])
drums.notes.extend([pretty_midi.Note(velocity=100, pitch=38, start=st, end=st+0.125) for st in snare_times])
drums.notes.extend([pretty_midi.Note(velocity=100, pitch=42, start=ht, end=ht+0.0625) for ht in hihat_times])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches, no repeated notes
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
# Walking bass line: F, Gb, Ab, Bb, B, Db, Eb, F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25),  # Db
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),  # Db
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=3.625, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),  # Db
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.375),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875),  # Db
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.125, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.75),  # Db
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, Db
# Cm7: C, Eb, F, Ab
# Gm7: G, Bb, C, D
# Dm7: D, F, G, A
# Chromatic passing chords
piano_notes = []

# Bar 2: Fm7 on beat 2, Cm7 on beat 4
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0)])  # F
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0)])  # Ab
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0)])  # Bb
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0)])  # Db

piano_notes.extend([pretty_midi.Note(velocity=100, pitch=72, start=2.375, end=2.5)])  # C
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5)])  # Eb
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=70, start=2.375, end=2.5)])  # F
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5)])  # Ab

# Bar 3: Gm7 on beat 2, Dm7 on beat 4
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=71, start=3.125, end=3.25)])  # G
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.25)])  # Bb
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25)])  # C
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25)])  # D

piano_notes.extend([pretty_midi.Note(velocity=100, pitch=74, start=3.625, end=3.75)])  # D
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=70, start=3.625, end=3.75)])  # F
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.75)])  # G
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=71, start=3.625, end=3.75)])  # A

# Bar 4: Fm7 on beat 2, rest on beat 4
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=70, start=4.375, end=4.5)])  # F
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.5)])  # Ab
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=66, start=4.375, end=4.5)])  # Bb
piano_notes.extend([pretty_midi.Note(velocity=100, pitch=64, start=4.375, end=4.5)])  # Db

piano.notes.extend(piano_notes)

# Dante: Saxophone motif in Fm, short and haunting
# Motif: F, Ab, Bb, F (on beat 2), then Ab, Bb, F (on beat 3), then Bb, F, Ab, Bb (on beat 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=66, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.375),  # F

    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=2.75, end=2.875),  # F

    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.5),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
