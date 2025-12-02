
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),
    # 2nd beat
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625),
]
piano.notes.extend(piano_notes)

# Sax (Dante): Start with a short motif that sings, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375), # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Continue the same pattern but add a slight variation
# Bass line (Marcus): Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),
    # 2nd beat
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.125),
]
piano.notes.extend(piano_notes)

# Sax (Dante): Repeat motif but raise it a bit
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.625, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875), # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.0),  # C
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

# Bass line (Marcus): Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),
    # 2nd beat
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625),  # D7
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Sax (Dante): Finish the motif, let it cry
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.125, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375), # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=5.875), # B
    pretty_midi.Note(velocity=100, pitch=65, start=5.875, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
