
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
    # Hi-hat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, Dm7 (D F A C)
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # C
    # Bar 3: Dm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Dante: Sax melody in Dm, short motif - whisper then cry
sax_notes = [
    # Bar 2: Whispering start on D
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),
    # Bar 2: Move to F
    pretty_midi.Note(velocity=95, pitch=64, start=1.625, end=1.75),
    # Bar 3: Lean into A
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    # Bar 3: Bb - tension
    pretty_midi.Note(velocity=95, pitch=66, start=1.875, end=2.0),
    # Bar 4: Resolve to D
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),
    # Bar 4: Close with F
    pretty_midi.Note(velocity=95, pitch=64, start=2.125, end=2.25),
    # Bar 4: Prolong with A
    pretty_midi.Note(velocity=105, pitch=67, start=2.25, end=2.625),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, Dm7
piano_notes = [
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # C
    # Bar 4: Dm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Dante: Sax melody continues, building tension
sax_notes = [
    # Bar 3: Continue with Bb
    pretty_midi.Note(velocity=95, pitch=66, start=3.0, end=3.125),
    # Bar 3: Move to C
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),
    # Bar 3: F
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.375),
    # Bar 4: Building toward resolution
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5),
    pretty_midi.Note(velocity=95, pitch=64, start=3.5, end=3.625),
    pretty_midi.Note(velocity=105, pitch=67, start=3.625, end=3.75),
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.875),
    pretty_midi.Note(velocity=115, pitch=62, start=3.875, end=4.0),
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.125),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, Dm7
piano_notes = [
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # C
    # Bar 4: Dm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Dante: Sax melody resolution
sax_notes = [
    # Bar 4: Full resolution
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=115, pitch=64, start=4.625, end=4.75),
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=105, pitch=62, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.125),
    pretty_midi.Note(velocity=95, pitch=67, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.375),
    pretty_midi.Note(velocity=95, pitch=64, start=5.375, end=5.5),
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.625),
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.75),
    pretty_midi.Note(velocity=115, pitch=64, start=5.75, end=5.875),
    pretty_midi.Note(velocity=110, pitch=67, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    # Bar 4 continuation
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 4 final beats
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
