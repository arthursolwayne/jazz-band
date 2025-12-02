
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Everybody in (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Dm7: D F A C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # C
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=75, pitch=64, start=2.25, end=2.625), # F
    # Dm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=75, pitch=64, start=3.0, end=3.375), # F
]

piano.notes.extend(piano_notes)

# Sax: Motif, short and singable
sax_notes = [
    # Start of motif on beat 1
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875), # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # D
]

sax.notes.extend(sax_notes)

# Bar 3: Continue the quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=75, pitch=64, start=3.75, end=4.125), # F
    # Dm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=75, pitch=64, start=4.5, end=4.875), # F
]

piano.notes.extend(piano_notes)

# Sax: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=73, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # A
]

sax.notes.extend(sax_notes)

# Bar 4: Continue the quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=75, pitch=64, start=5.25, end=5.625), # F
    # Dm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=6.0, end=6.375), # D
    pretty_midi.Note(velocity=85, pitch=67, start=6.0, end=6.375), # A
    pretty_midi.Note(velocity=80, pitch=69, start=6.0, end=6.375), # C
    pretty_midi.Note(velocity=75, pitch=64, start=6.0, end=6.375), # F
]

piano.notes.extend(piano_notes)

# Sax: Finish the motif, return to the start
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # D
]

sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
