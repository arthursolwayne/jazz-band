
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

# Bar 2: Everyone in. Sax melody
# F7 chord: F A C E
# Start with a motif: F - G - Bb - F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # F
]

# Bass: Walking line in F
# F - G - Ab - A - Bb - B - C - D - E - F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=46, start=2.125, end=2.25),  # B
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=2.625, end=2.75),  # F
]

# Piano: 7th chords on 2 and 4
# F7 on beat 2: F A C E
# F7 on beat 4: F A C E
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.125),  # E
]

# Bar 3: Sax continues the motif
# F - G - Bb - F
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.125, end=3.25),  # F
])

# Bass: Walking line in F
# F - G - Ab - A - Bb - B - C - D - E - F
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=45, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.5),  # B
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=3.875),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=3.875, end=4.0),  # F
])

# Piano: 7th chords on 2 and 4
# F7 on beat 2: F A C E
# F7 on beat 4: F A C E
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.625),  # E
])

# Bar 4: Sax continues the motif
# F - G - Bb - F
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # F
])

# Bass: Walking line in F
# F - G - Ab - A - Bb - B - C - D - E - F
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=47, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=4.0, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=4.125, end=4.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.375),  # A
    pretty_midi.Note(velocity=80, pitch=45, start=4.375, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.625),  # B
    pretty_midi.Note(velocity=80, pitch=47, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.125),  # F
])

# Piano: 7th chords on 2 and 4
# F7 on beat 2: F A C E
# F7 on beat 4: F A C E
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.625),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=5.5, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=5.5, end=5.625),  # E
])

# Add notes to instruments
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
