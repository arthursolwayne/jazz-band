
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX: Motif starting on F (65), Bb (62), Ab (60), F (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# BASS: Walking line - F, Gb, Ab, A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # A
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 & 4
# F7 on beat 2 (1.75 - 2.0), Ab7 on beat 4 (2.25 - 2.5)
piano_notes = [
    # F7 (F, A, Bb, D)
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # D
    # Ab7 (Ab, C, Db, F)
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # Db
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Repeat motif starting on F (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# BASS: Walking line - Bb, B, Db, D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=63, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # Db
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # D
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 & 4
# Bb7 on beat 2 (3.25 - 3.5), Db7 on beat 4 (3.75 - 4.0)
piano_notes = [
    # Bb7 (Bb, D, Eb, F)
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),  # F
    # Db7 (Db, F, Gb, A)
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # Db
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # A
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: Repeat motif starting on F (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# BASS: Walking line - F, Gb, Ab, A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=68, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),  # A
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 & 4
# F7 on beat 2 (4.75 - 5.0), Ab7 on beat 4 (5.25 - 5.5)
piano_notes = [
    # F7 (F, A, Bb, D)
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # D
    # Ab7 (Ab, C, Db, F)
    pretty_midi.Note(velocity=80, pitch=68, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # Db
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),  # F
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
for bar in range(3, 6):
    for i in range(4):
        start = bar * 1.5 + i * 0.375
        if i == 0:
            # kick on 1
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
            # hihat on 1
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
        elif i == 1:
            # snare on 2
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
            # hihat on 2
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
        elif i == 2:
            # kick on 3
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
            # hihat on 3
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
        elif i == 3:
            # snare on 4
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start, end=start + 0.375))
            # hihat on 4
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
