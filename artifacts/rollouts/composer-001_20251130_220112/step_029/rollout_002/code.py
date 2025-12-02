
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # F (1st beat)
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),
    # Bb (2nd beat)
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    # Ab (chromatic approach to A)
    pretty_midi.Note(velocity=75, pitch=68, start=2.25, end=2.625),
    # A (3rd beat)
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    # D (4th beat)
    pretty_midi.Note(velocity=80, pitch=73, start=3.0, end=3.375)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on 2nd beat (Bb, F, A, C)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),
    # F7 on 4th beat (Bb, F, A, C)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375)
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    # F (first beat)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # Bb (second beat)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    # Ab (chromatic approach to A)
    pretty_midi.Note(velocity=95, pitch=68, start=2.25, end=2.625),
    # Rest on third beat
    pretty_midi.Note(velocity=0, pitch=71, start=2.625, end=3.0),
    # A (fourth beat)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # A (1st beat)
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),
    # D (2nd beat)
    pretty_midi.Note(velocity=80, pitch=73, start=3.375, end=3.75),
    # C# (chromatic approach to C)
    pretty_midi.Note(velocity=75, pitch=72, start=3.75, end=4.125),
    # C (3rd beat)
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),
    # F (4th beat)
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # A7 on 2nd beat (C, E, G, A)
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=85, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),
    # A7 on 4th beat (C, E, G, A)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation
sax_notes = [
    # A (first beat)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    # D (second beat)
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75),
    # C# (chromatic approach to C)
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=4.125),
    # Rest on third beat
    pretty_midi.Note(velocity=0, pitch=69, start=4.125, end=4.5),
    # C (fourth beat)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # C (1st beat)
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),
    # F (2nd beat)
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),
    # E (chromatic approach to Eb)
    pretty_midi.Note(velocity=75, pitch=70, start=5.25, end=5.625),
    # Eb (3rd beat)
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0),
    # A (4th beat - rest)
    pretty_midi.Note(velocity=0, pitch=69, start=6.0, end=6.375)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 on 2nd beat (E, G, B, C)
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=85, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),
    # C7 on 4th beat (E, G, B, C)
    pretty_midi.Note(velocity=90, pitch=72, start=6.0, end=6.375),
    pretty_midi.Note(velocity=85, pitch=74, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=77, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=72, start=6.0, end=6.375)
]
piano.notes.extend(piano_notes)

# Sax: Motif completion
sax_notes = [
    # C (first beat)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    # F (second beat)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    # E (chromatic approach to Eb)
    pretty_midi.Note(velocity=95, pitch=70, start=5.25, end=5.625),
    # Rest on third beat
    pretty_midi.Note(velocity=0, pitch=72, start=5.625, end=6.0),
    # Eb (fourth beat)
    pretty_midi.Note(velocity=100, pitch=70, start=6.0, end=6.375)
]
sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
