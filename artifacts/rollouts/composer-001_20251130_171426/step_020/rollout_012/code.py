
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2, beat 1
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),
    # Bar 2, beat 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),
    # Bar 2, beat 3
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625),
    # Bar 2, beat 4
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 - F7
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=81, start=1.875, end=2.25), # D
    # Bar 2, beat 4 - F7
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0), # C
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=3.0), # D
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif: F - Bb - G - Ab (first four notes of phrase)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),  # Ab
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass line (Marcus)
bass_notes = [
    # Bar 3, beat 1
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),
    # Bar 3, beat 2
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),
    # Bar 3, beat 3
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),
    # Bar 3, beat 4
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2 - F7
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=81, start=3.375, end=3.75), # D
    # Bar 3, beat 4 - F7
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5), # A
    pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.5), # C
    pretty_midi.Note(velocity=100, pitch=81, start=4.125, end=4.5), # D
]
piano.notes.extend(piano_notes)

# Sax (Dante) - continuation of motif: F - Bb - G - Ab (echoed again)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5),  # Ab
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bass line (Marcus)
bass_notes = [
    # Bar 4, beat 1
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),
    # Bar 4, beat 2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),
    # Bar 4, beat 3
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),
    # Bar 4, beat 4
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2 - F7
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=81, start=4.875, end=5.25), # D
    # Bar 4, beat 4 - F7
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0), # C
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0), # D
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif completion: F - Bb - G - Ab (second echo)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=70, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0),  # Ab
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
